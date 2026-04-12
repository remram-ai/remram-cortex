# Project Charter

## Summary

This MVP proves that Cortex can be brought up as a practical working system, not just as a locked architecture.

The execution rule is:

- start with a baseline assistant that is actually useful
- keep the local fast path small and responsive
- add memory, web, escalation, and specialist agents in bounded layers
- introduce heavier Cortex services only after the baseline operating posture is solid

## Scope

In scope:

- a remote `OpenClaw` proving baseline
- `QMD` as the first working-memory backend, running as a host sidecar
- light memory tuning so the local default model is not overwhelmed
- `web_search` plus `web_fetch` as the initial web baseline
- OpenAI-backed escalation for harder reasoning and coding work
- a lightweight orchestrator that classifies work before invoking memory, web, coding, or escalation
- baseline specialist agents
- remote access and a repeatable dev-to-test loop
- later Cortex augmentation through evidence capture, startup bundles, and bounded semantic hooks

Out of scope for the first practical baseline:

- browser as a default capability
- broad policy redesign before the baseline assistant is usable
- `Graphiti`, `Neo4j`, `Postgres`, or a separate `cortex` service as an early prerequisite
- `OpenSearch`
- `Mamba` or `Intuition`
- pushing early working material into Git-backed canon by default

## Sequencing Rule

The architecture still uses the layered model documented under `docs/design/`.

This project package uses a practical delivery sequence:

- `Phase 1`: OpenClaw foundation
- `Phase 2`: baseline agents and access
- `Phase 3`: dev/test loop
- `Phase 4`: Cortex augmentation
- `Phase 5`: memory services
- `Phase 6`: sources and artifacts
- `Phase 7`: optimization

Those delivery phases are allowed to cut across the long-term architecture loops when that makes implementation more realistic.
