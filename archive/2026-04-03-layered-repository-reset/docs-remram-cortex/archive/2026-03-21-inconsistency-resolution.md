# 2026-03-21 Inconsistency Resolution

This note archives the inconsistencies that were active before the first hard architecture redraft.

They were resolved at the conceptual level in the current architecture pass and no longer need to remain as open contradictions in the live tracker.

## Resolved Items

### 1. Conversation Object Ownership Split

Resolved direction:

- conversation objects, if adopted, are durably owned by Cortex
- orchestration may provide continuation, fork, or preference hints at runtime
- durable attachment, storage, merge, and archival remain Cortex responsibilities

See:

- [architecture.md](../architecture.md)
- [conversation-layer.md](../../concepts/conversation-layer.md)

### 2. Bootstrap Transcript Access Boundary

Resolved direction:

- bootstrap should prefer exports, backfill jobs, and other controlled read-only surfaces
- migration-phase direct file ingestion may still exist as one-time operational tooling
- direct coupling to mutable runtime internals is not the desired long-term service contract

See:

- [architecture.md](../architecture.md)
- [bootstrap-ingestion.md](../../concepts/bootstrap-ingestion.md)

### 3. Migration-Phase Memory Authority

Resolved direction:

- target state remains Cortex as the durable knowledge authority
- migration may temporarily dual-run or use OpenClaw-native memory as evidence or fallback
- that migration posture does not create a second durable authority once Cortex retrieval is active

Operational cutover criteria remain a later rollout-spec question, not an architectural contradiction.

See:

- [architecture.md](../architecture.md)

## Previously Resolved Boundaries Still Held

The following earlier resolutions were preserved by the redraft:

- Gateway is the control plane, not the runtime execution layer
- `/ingest` and `/reflect` both mutate Cortex state with distinct responsibilities
- promoted artifacts do not replace knowledge objects as canonical memory
- Dream enriches memory but does not directly mutate prompts
- Gateway does not consume retrieval bundles
