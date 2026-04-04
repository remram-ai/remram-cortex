# MVP 1 Seed Prompt

Use the layered Cortex architecture.

Assume:

- OpenClaw owns sessions and runtime execution
- Cortex owns policy, semantic checkpoints, durable-memory orchestration, and artifact routing
- the active stack is `Graphiti + Neo4j + Postgres + pgvector + Git`

Before changing implementation details:

- read `docs/design/layered-memory-architecture.md`
- read `docs/design/openclaw-integration.md`
- read `docs/design/graphiti-neo4j-durable-memory.md`
- read `docs/design/knowledge-and-artifact-architecture.md`
- read this project package
