---
name: cortex-phase1-bridge
description: Preparation-stage OpenClaw bridge for Cortex Phase 1 hook capture, startup bundle injection, and inspectable spool output.
user-invocable: false
metadata: {"openclaw":{"homepage":"https://github.com/remram-ai/remram-cortex/tree/main/integrations/openclaw/packages/cortex-phase1-bridge"}}
---

# Cortex Phase 1 Bridge

This package installs a plugin-backed OpenClaw skill that prepares the Phase 1 Cortex hook boundary without requiring a live Cortex service yet.

## What It Does

- Captures bounded OpenClaw lifecycle envelopes at:
  - `before_prompt_build`
  - `before_compaction`
  - `after_compaction`
  - `agent_end`
- Optionally injects the latest prepared startup bundle for the current session
- Writes inspectable spool artifacts to a runtime-local directory

## What It Does Not Do Yet

- own OpenClaw session mechanics
- replace OpenClaw compaction
- write directly into Postgres, Neo4j, or Graphiti
- require a live Moltbox deployment
- require a live Cortex API

## Install

Use the normal OpenClaw plugin workflow:

```bash
openclaw plugins install -l {baseDir}
```

Then allow the plugin explicitly and merge the matching config overlay from:

- `{workspaceRoot}/integrations/openclaw/config/phase1-cortex-overlay.json5`

## Runtime Modes

- `dry-run`
  - default
  - writes hook envelopes to the spool directory
  - reads prepared startup bundles from `startupBundleDir`
- `service`
  - reserved for the later Cortex API integration pass
  - configuration is present now so the package contract does not have to churn later

## Expected Spool Layout

- `{spoolDir}/events/<session-id>/...`
- `{startupBundleDir}/<session-id>/...`

## Operational Notes

- This package is intentionally safe to enable in a test lane first.
- It is a bridge surface, not a second working-memory system.
- Layer 2 stays OpenClaw-native.
