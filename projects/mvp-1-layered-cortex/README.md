# MVP 1: Layered Cortex

This project is the first implementation package for the locked layered Cortex architecture.

## Goal

Deliver a working Cortex spine that proves:

- custom policy on top of OpenClaw
- `QMD` hot Layer 2 working memory and notions
- turn-end and session-end semantic processing
- `Graphiti + Neo4j` durable semantic memory
- `Postgres` as the operational middle-layer authority
- `Git` canonical artifacts only when canonical publication is warranted

`Mamba` is still part of the long-term architecture.

It is deferred by default and moved to Phase 3 unless the post-Phase-1 decision gate pulls it forward.

## Definition Of Done

The MVP is done when:

- OpenClaw runtime uses Cortex policy and bounded context assembly
- `QMD` supports hot continuity and notion storage
- boundary-triggered semantic processing produces usable typed continuity outputs
- Layer 3 durable memory organizes concepts and relationships without becoming a body store
- Layer 4 operational knowledge supports evolving workspaces and reference material
- Layer 5 is used only for canonical publication when warranted
- the project has an inspectable acceptance-test surface

## Documents

- [Project Charter](project-charter.md)
- [Project Plan](project-plan.md)
- [Acceptance Test](acceptance-test.md)
- [Runtime Docs](runtime-docs.md)
- [Seed Prompt](seed-prompt.md)
- [Epics](epics/README.md)
