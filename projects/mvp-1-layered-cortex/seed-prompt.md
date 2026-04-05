# MVP 1 Seed Prompt

Use the layered Cortex architecture.

Assume:

- OpenClaw owns sessions and runtime execution
- Cortex owns policy, Layer 2 notion rules, durable-memory orchestration, and operational-knowledge routing
- the Phase 0 baseline is `OpenClaw + local model + safe config + QMD + compaction/pruning`
- the Phase 1 stack adds `Cortex policy + Layer 5 runtime evidence + boundary-triggered semantic processing + Graphiti + Neo4j + Postgres`
- `Mamba` belongs to the later optimization phase rather than the initial proof surface

Before changing implementation details:

- read `docs/design/layered-memory-architecture.md`
- read `docs/design/openclaw-integration.md`
- read `docs/design/graphiti-neo4j-durable-memory.md`
- read `docs/design/knowledge-and-artifact-architecture.md`
- read this project package
