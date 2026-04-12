# MVP 1 Seed Prompt

Use the locked layered Cortex architecture, but follow the practical delivery package rather than the archived architecture-first execution plan.

## Initial Context To Read

Read these first, in order:

1. `docs/context-packs/cortex-core/README.md`
2. `docs/context-packs/cortex-core/00-repo-orientation.md`
3. `docs/context-packs/cortex-core/01-terminology-and-legacy.md`
4. `docs/context-packs/cortex-core/02-layers-and-authority.md`
5. `docs/context-packs/cortex-core/05-phases-and-delivery.md`
6. `docs/context-packs/cortex-core/08-live-appliance-quick-start.md`
7. `projects/mvp-1-practical-cortex/README.md`
8. `projects/mvp-1-practical-cortex/project-plan.md`
9. `projects/mvp-1-practical-cortex/acceptance-test.md`

Then use these canonical architecture docs as needed:

- `docs/authority-map.md`
- `docs/glossary.md`
- `docs/design/layered-memory-architecture.md`
- `docs/design/openclaw-integration.md`
- `docs/design/technology-stack.md`
- `docs/design/deployment-plan.md`

## Locked Architecture Summary

Assume:

- `OpenClaw` is the chosen runtime shell.
- `QMD` is the intended hot working-memory layer.
- `Graphiti + Neo4j`, `Postgres`, and the wider knowledge stack remain part of the long-term design.
- `Mamba` and `Intuition` remain later optimization work.

## Practical Delivery Summary

The active project sequence is:

- `Phase 1`: OpenClaw foundation
- `Phase 2`: baseline agents and access
- `Phase 3`: dev/test loop
- `Phase 4`: Cortex augmentation
- `Phase 5`: memory services
- `Phase 6`: sources and artifacts
- `Phase 7`: optimization

The current target is the first practical baseline:

- remote `OpenClaw`
- `QMD` sidecar
- light memory tuning
- web baseline
- OpenAI escalation
- lightweight routing

## Implementation Rule

The orchestrator should decide whether memory is needed before memory is injected.

Treat memory as a bounded retrieval capability.
Do not turn the default path into background prompt stuffing for the local model.

If tradeoffs are needed:

1. preserve a useful and fast baseline
2. preserve operator safety and the Gateway contract
3. preserve architecture boundaries
4. defer heavier Cortex service work
