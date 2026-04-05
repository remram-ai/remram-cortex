# Cortex Bridge Service Contract

This is the initial HTTP contract between the OpenClaw bridge package and the later deployed Cortex service.

It is intentionally narrow.

The bridge should not become a second orchestration layer.
It should only:

- fetch bounded startup context
- hand off bounded hook envelopes
- hand off explicit boundary-processing requests when the service-backed path is enabled

## Base URL

Example local base URL:

```text
http://127.0.0.1:8091
```

Example appliance-side base URL later:

```text
http://cortex:8091
```

## Endpoints

### `GET /healthz`

Purpose:

- liveness check for the bridge service

Response:

```json
{
  "data_root": ".runtime/cortex",
  "service": "cortex-bridge-prep",
  "status": "ok"
}
```

### `GET /v1/sessions/{session_id}/startup-bundle/latest`

Purpose:

- return the latest prepared startup bundle for bounded prompt injection

Success response:

- `200 OK`
- body is the startup bundle JSON

Not found:

- `404`
- body:

```json
{
  "error": "startup_bundle_not_found"
}
```

### `POST /v1/openclaw/hooks`

Purpose:

- accept bounded OpenClaw lifecycle envelopes from the bridge plugin

Current expected event names:

- `before_prompt_build`
- `before_compaction`
- `after_compaction`
- `agent_end`

Request shape:

```json
{
  "bridge_mode": "service",
  "captured_at": "2026-04-04T21:00:00Z",
  "event": "agent_end",
  "payload": {
    "duration_ms": 842,
    "message_count": 9,
    "prompt_chars": 1420
  },
  "session_id": "session-001",
  "session_key": "chat:abc",
  "trigger": "reply"
}
```

Response:

```json
{
  "status": "accepted",
  "stored_at": ".runtime/cortex/ingest/openclaw_hook_events/session-001/agent_end__...json"
}
```

### `POST /v1/openclaw/boundaries`

Purpose:

- process an explicit turn-end, session-end, or checkpoint boundary through the Cortex Phase 1 prep runtime

Request shape:

- the body is the same shape as `BoundaryInput`
- optional keys:
  - `mode`
  - `preference_overlays`

Example:

```json
{
  "session_id": "session-001",
  "conversation_id": "conversation-layered-cortex",
  "user_id": "user-jason",
  "trigger": "session_end",
  "messages": [
    {
      "role": "user",
      "content": "I prefer inspectable staging surfaces."
    }
  ],
  "mode": "standard",
  "preference_overlays": {
    "tone": "direct"
  }
}
```

Response:

```json
{
  "result": {
    "checkpoint_id": "session_end-...",
    "evidence_path": "...",
    "semantic_checkpoint_path": "...",
    "qmd_mutation_path": "...",
    "layer4_outbox_path": "...",
    "layer3_outbox_path": "...",
    "reflection_hook_path": "...",
    "dream_hook_path": "...",
    "next_startup_bundle_path": "..."
  },
  "startup_bundle": {
    "bundle_id": "startup-...",
    "blocks": []
  }
}
```

## Contract Rules

1. The bridge fetches only bounded startup bundles, not whole transcripts.
2. Hook envelopes are observational and pointer-oriented.
3. Layer 2 remains OpenClaw-native.
4. The service may stage work for Layer 4 and Layer 3, but it must not turn Layer 3 into a transcript body store.
5. The bridge package should degrade safely if the service is unavailable.

## Current Implementation Status

The current repo includes a runnable preparation implementation of this contract through:

- `python -m remram_cortex serve`

That service is for development and appliance-contract rehearsal.
It is not yet the final deployed Cortex service.
