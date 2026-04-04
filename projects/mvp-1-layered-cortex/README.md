# MVP 1: Layered Cortex

This project is the first implementation package for the layered Cortex architecture.

## Goal

Deliver a working Cortex spine that proves:

- custom policy on top of OpenClaw
- OpenClaw-native Layer 2 working memory
- High-Signal Mamba semantic checkpoints
- `Graphiti + Neo4j` durable memory
- `Postgres + pgvector` decomposed knowledge and runtime evidence
- `Git` canonical artifacts

## Definition Of Done

The MVP is done when:

- OpenClaw runtime uses Cortex policy and bounded context assembly
- the Mamba stream is producing usable semantic checkpoints
- high-signal notions can become tentative cross-thread memory
- reconciliation promotes trusted durable memory into Graphiti
- artifact intake produces Layer 4 knowledge and links back to Layer 5 truth
- the project has an inspectable acceptance-test surface

## Documents

- [Project Charter](project-charter.md)
- [Project Plan](project-plan.md)
- [Acceptance Test](acceptance-test.md)
- [Runtime Docs](runtime-docs.md)
- [Seed Prompt](seed-prompt.md)
- [Epics](epics/README.md)
