import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import http from "node:http";

import register from "../index.js";

function createFakeApi(config) {
  const handlers = new Map();
  return {
    config,
    logger: {
      info() {},
      warn() {},
      error() {},
    },
    on(name, handler) {
      handlers.set(name, handler);
    },
    handlers,
  };
}

function pluginConfigFor({
  bridgeMode = "dry-run",
  spoolDir,
  startupBundleDir,
  cortexApiBaseUrl = "",
  enablePromptInjection = true,
  enableEventCapture = true,
} = {}) {
  return {
    plugins: {
      entries: {
        "cortex-phase1-bridge": {
          config: {
            bridgeMode,
            spoolDir,
            startupBundleDir,
            cortexApiBaseUrl,
            enablePromptInjection,
            enableEventCapture,
          },
        },
      },
    },
  };
}

async function startJsonServer(routes) {
  const requests = [];
  const server = http.createServer(async (req, res) => {
    const chunks = [];
    for await (const chunk of req) {
      chunks.push(chunk);
    }
    const rawBody = Buffer.concat(chunks).toString("utf8");
    const key = `${req.method} ${req.url}`;
    requests.push({
      method: req.method,
      url: req.url,
      body: rawBody ? JSON.parse(rawBody) : null,
    });
    const route = routes[key];
    if (!route) {
      res.writeHead(404, { "content-type": "application/json" });
      res.end(JSON.stringify({ error: "not_found" }));
      return;
    }
    res.writeHead(route.status ?? 200, { "content-type": "application/json" });
    res.end(JSON.stringify(route.body ?? {}));
  });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  const address = server.address();
  return {
    baseUrl: `http://${address.address}:${address.port}`,
    requests,
    async close() {
      await new Promise((resolve, reject) => server.close((error) => (error ? reject(error) : resolve())));
    },
  };
}

test("service mode fetches startup bundle from the Cortex bridge service", async () => {
  const server = await startJsonServer({
    "GET /v1/sessions/session-001/startup-bundle/latest": {
      status: 200,
      body: {
        bundle_id: "startup-test",
        blocks: [
          { kind: "policy", payload: { bundle_id: "policy-123" } },
          { kind: "hot_continuity", payload: ["summary one", "summary two"] },
          { kind: "durable_orientation", payload: ["concept a"] },
          { kind: "knowledge_pointers", payload: ["pointer-1"] },
        ],
      },
    },
  });
  try {
    const tempRoot = await fs.mkdtemp(path.join(os.tmpdir(), "cortex-bridge-"));
    const api = createFakeApi(
      pluginConfigFor({
        bridgeMode: "service",
        spoolDir: tempRoot,
        startupBundleDir: path.join(tempRoot, "startup-bundles"),
        cortexApiBaseUrl: server.baseUrl,
      })
    );
    register(api);
    const beforePromptBuild = api.handlers.get("before_prompt_build");
    assert.ok(beforePromptBuild);

    const result = await beforePromptBuild(
      { prompt: "Hello", messages: [] },
      { sessionId: "session-001", sessionKey: "chat:1", trigger: "reply" }
    );

    assert.ok(result);
    assert.match(result.prependSystemContext, /Policy bundle: policy-123/);
    assert.match(result.prependSystemContext, /Hot continuity: summary one \| summary two/);
  } finally {
    await server.close();
  }
});

test("service mode posts hook envelopes to the Cortex bridge service", async () => {
  const server = await startJsonServer({
    "POST /v1/openclaw/hooks": {
      status: 202,
      body: {
        status: "accepted",
      },
    },
  });
  try {
    const tempRoot = await fs.mkdtemp(path.join(os.tmpdir(), "cortex-bridge-"));
    const api = createFakeApi(
      pluginConfigFor({
        bridgeMode: "service",
        spoolDir: tempRoot,
        startupBundleDir: path.join(tempRoot, "startup-bundles"),
        cortexApiBaseUrl: server.baseUrl,
      })
    );
    register(api);
    const agentEnd = api.handlers.get("agent_end");
    assert.ok(agentEnd);

    await agentEnd(
      { durationMs: 14 },
      { sessionId: "session-001", sessionKey: "chat:1", trigger: "reply" }
    );

    assert.equal(server.requests.length, 1);
    assert.equal(server.requests[0].url, "/v1/openclaw/hooks");
    assert.equal(server.requests[0].body.event, "agent_end");
    assert.equal(server.requests[0].body.session_id, "session-001");
  } finally {
    await server.close();
  }
});

test("falls back to local spool capture if the service is unavailable", async () => {
  const tempRoot = await fs.mkdtemp(path.join(os.tmpdir(), "cortex-bridge-"));
  const api = createFakeApi(
    pluginConfigFor({
      bridgeMode: "service",
      spoolDir: tempRoot,
      startupBundleDir: path.join(tempRoot, "startup-bundles"),
      cortexApiBaseUrl: "http://127.0.0.1:1",
    })
  );
  register(api);
  const agentEnd = api.handlers.get("agent_end");
  assert.ok(agentEnd);

  await agentEnd(
    { durationMs: 14 },
    { sessionId: "session-001", sessionKey: "chat:1", trigger: "reply" }
  );

  const eventDir = path.join(tempRoot, "events", "session-001");
  const files = await fs.readdir(eventDir);
  assert.equal(files.length, 1);
  const payload = JSON.parse(await fs.readFile(path.join(eventDir, files[0]), "utf8"));
  assert.equal(payload.event, "agent_end");
  assert.equal(payload.bridge_mode, "service");
});
