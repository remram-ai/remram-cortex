# Evidence, Knowledge, And Artifacts

The current stack splits evidence and knowledge cleanly:

- runtime raw evidence closes into `Postgres`
- decomposed operational knowledge lives in `Postgres + pgvector`
- canonical artifacts live in `Git` or another authoritative provider

Design rule:

- raw evidence is not the default consumer surface
- the High-Signal Mamba stream is the default semantic consumer surface
- Layer 4 operational knowledge may move ahead of Layer 5 canonical artifacts during active work
- publication and re-ingestion bring them back into alignment
