# MVP 1 Seed Prompt

Use the layered Cortex architecture.

Assume:

- OpenClaw owns sessions and runtime execution
- Cortex owns policy, Layer 2 notion rules, durable-memory orchestration, and operational-knowledge routing
- the Phase 1 stack is `OpenClaw + QMD + boundary-triggered semantic processing + Graphiti + Neo4j + Postgres + Git`
- `Mamba` is part of the later architecture but deferred by default

Before changing implementation details:

- read `docs/design/layered-memory-architecture.md`
- read `docs/design/openclaw-integration.md`
- read `docs/design/graphiti-neo4j-durable-memory.md`
- read `docs/design/knowledge-and-artifact-architecture.md`
- read this project package
