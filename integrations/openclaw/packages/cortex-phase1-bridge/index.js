import fs from "node:fs/promises";
import path from "node:path";

function safeString(value, fallback = "") {
  return typeof value === "string" ? value : fallback;
}

function safeBoolean(value, fallback = false) {
  return typeof value === "boolean" ? value : fallback;
}

function sanitizeSegment(value) {
  return String(value || "unknown").replace(/[^a-zA-Z0-9._-]+/g, "_");
}

function resolveConfig(api) {
  const entry =
    api?.config?.plugins?.entries?.["cortex-phase1-bridge"]?.config ?? {};
  const homeDir =
    process.env.HOME ||
    process.env.USERPROFILE ||
    process.cwd();
  const expandHome = (input, fallback) => {
    const raw = safeString(input, fallback);
    if (raw.startsWith("~/")) {
      return path.join(homeDir, raw.slice(2));
    }
    return raw;
  };
  const spoolDir = expandHome(
    entry.spoolDir,
    path.join(homeDir, ".openclaw", "cortex-phase1")
  );
  return {
    bridgeMode: safeString(entry.bridgeMode, "dry-run"),
    spoolDir,
    startupBundleDir: expandHome(
      entry.startupBundleDir,
      path.join(spoolDir, "startup-bundles")
    ),
    cortexApiBaseUrl: safeString(entry.cortexApiBaseUrl, ""),
    enablePromptInjection: safeBoolean(entry.enablePromptInjection, true),
    enableEventCapture: safeBoolean(entry.enableEventCapture, true),
  };
}

async function ensureDir(dirPath) {
  await fs.mkdir(dirPath, { recursive: true });
}

async function loadLatestSessionBundle(bundleRoot, sessionId) {
  const sessionDir = path.join(bundleRoot, sanitizeSegment(sessionId));
  try {
    const entries = await fs.readdir(sessionDir, { withFileTypes: true });
    const jsonFiles = entries
      .filter((entry) => entry.isFile() && entry.name.endsWith(".json"))
      .map((entry) => entry.name)
      .sort();
    if (jsonFiles.length === 0) {
      return null;
    }
    const latestFile = jsonFiles[jsonFiles.length - 1];
    const payload = JSON.parse(
      await fs.readFile(path.join(sessionDir, latestFile), "utf8")
    );
    return payload;
  } catch {
    return null;
  }
}

async function fetchLatestSessionBundle(config, sessionId) {
  if (!config.cortexApiBaseUrl) {
    return null;
  }
  const response = await fetch(
    `${config.cortexApiBaseUrl.replace(/\/$/, "")}/v1/sessions/${encodeURIComponent(sessionId)}/startup-bundle/latest`
  );
  if (response.status === 404) {
    return null;
  }
  if (!response.ok) {
    throw new Error(`startup bundle fetch failed: ${response.status}`);
  }
  return await response.json();
}

function renderStartupBundle(bundle) {
  if (!bundle || !Array.isArray(bundle.blocks)) {
    return "";
  }
  const findPayload = (kind) =>
    bundle.blocks.find((block) => block?.kind === kind)?.payload;
  const policy = findPayload("policy");
  const hotContinuity = findPayload("hot_continuity") || [];
  const durableOrientation = findPayload("durable_orientation") || [];
  const knowledgePointers = findPayload("knowledge_pointers") || [];

  const lines = [
    "Cortex startup bundle",
    policy?.bundle_id ? `Policy bundle: ${policy.bundle_id}` : "",
    hotContinuity.length ? `Hot continuity: ${hotContinuity.join(" | ")}` : "",
    durableOrientation.length
      ? `Durable orientation: ${durableOrientation.join(" | ")}`
      : "",
    knowledgePointers.length
      ? `Knowledge pointers: ${knowledgePointers.join(" | ")}`
      : "",
  ].filter(Boolean);

  return lines.join("\n");
}

async function writeEventEnvelope(config, sessionId, eventName, payload) {
  const eventDir = path.join(
    config.spoolDir,
    "events",
    sanitizeSegment(sessionId || "unknown")
  );
  await ensureDir(eventDir);
  const fileName = `${Date.now()}__${sanitizeSegment(eventName)}.json`;
  await fs.writeFile(
    path.join(eventDir, fileName),
    JSON.stringify(payload, null, 2) + "\n",
    "utf8"
  );
}

async function postEventEnvelope(config, payload) {
  if (!config.cortexApiBaseUrl) {
    throw new Error("cortexApiBaseUrl is not configured");
  }
  const response = await fetch(
    `${config.cortexApiBaseUrl.replace(/\/$/, "")}/v1/openclaw/hooks`,
    {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify(payload),
    }
  );
  if (!response.ok) {
    throw new Error(`hook post failed: ${response.status}`);
  }
  return await response.json();
}

function buildEnvelope(eventName, event, ctx, config) {
  return {
    event: eventName,
    captured_at: new Date().toISOString(),
    bridge_mode: config.bridgeMode,
    session_id: safeString(ctx?.sessionId),
    session_key: safeString(ctx?.sessionKey),
    trigger: safeString(ctx?.trigger),
    payload: {
      duration_ms: event?.durationMs ?? null,
      prompt_chars: typeof event?.prompt === "string" ? event.prompt.length : null,
      message_count: Array.isArray(event?.messages) ? event.messages.length : null,
    },
  };
}

async function captureEvent(config, sessionId, eventName, payload) {
  if (config.bridgeMode === "service" && config.cortexApiBaseUrl) {
    try {
      await postEventEnvelope(config, payload);
      return;
    } catch {
      // Fall back to local spool capture so hook visibility is preserved
      // even while the service is unavailable.
    }
  }
  await writeEventEnvelope(config, sessionId, eventName, payload);
}

export default function register(api) {
  const config = resolveConfig(api);

  api.on("before_prompt_build", async (event, ctx) => {
    if (!config.enableEventCapture) {
      return;
    }
    const sessionId = safeString(ctx?.sessionId);
    await captureEvent(
      config,
      sessionId,
      "before_prompt_build",
      buildEnvelope("before_prompt_build", event, ctx, config)
    );

    if (!config.enablePromptInjection || !sessionId) {
      return;
    }

    let bundle = null;
    if (config.bridgeMode === "service" && config.cortexApiBaseUrl) {
      try {
        bundle = await fetchLatestSessionBundle(config, sessionId);
      } catch {
        bundle = null;
      }
    }
    if (!bundle) {
      bundle = await loadLatestSessionBundle(config.startupBundleDir, sessionId);
    }
    const startupContext = renderStartupBundle(bundle);
    if (!startupContext) {
      return;
    }

    return {
      prependSystemContext: startupContext,
    };
  }, { priority: 100 });

  api.on("before_compaction", async (event, ctx) => {
    if (!config.enableEventCapture) {
      return;
    }
    await captureEvent(
      config,
      safeString(ctx?.sessionId),
      "before_compaction",
      buildEnvelope("before_compaction", event, ctx, config)
    );
  }, { priority: 100 });

  api.on("after_compaction", async (event, ctx) => {
    if (!config.enableEventCapture) {
      return;
    }
    await captureEvent(
      config,
      safeString(ctx?.sessionId),
      "after_compaction",
      buildEnvelope("after_compaction", event, ctx, config)
    );
  }, { priority: 100 });

  api.on("agent_end", async (event, ctx) => {
    if (!config.enableEventCapture) {
      return;
    }
    await captureEvent(
      config,
      safeString(ctx?.sessionId),
      "agent_end",
      buildEnvelope("agent_end", event, ctx, config)
    );
  }, { priority: 100 });
}
