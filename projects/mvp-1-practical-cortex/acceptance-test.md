# Acceptance Test

This acceptance surface covers the current practical baseline target:

- `Phase 1` foundation
- enough of `Phase 2` and `Phase 3` to make the system usable and repeatable

It should prove the following end-to-end behaviors:

1. the remote `OpenClaw` baseline runs cleanly on the proving lane
2. `QMD` runs as a host sidecar and can be selected as the working-memory backend
3. memory retrieval is intentionally light enough for the local default model
4. the orchestrator decides whether memory is needed before it injects memory
5. `web_search` and `web_fetch` form the working web baseline without browser
6. harder reasoning or coding tasks can escalate to OpenAI cleanly
7. the default assistant can hand work off to baseline specialist agents
8. remote usage and inspection are possible without relying on the user's local workstation for every task
9. the dev-to-test workflow uses official Moltbox validation and rollback surfaces rather than normalizing host-only drift

Later phases add Cortex evidence flow, durable memory services, maintained sources, authored artifacts, and optimization.
They are not part of the first practical acceptance gate.
