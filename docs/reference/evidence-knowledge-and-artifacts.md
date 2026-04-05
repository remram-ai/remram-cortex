# Evidence, Knowledge, And Artifacts

The current stack splits evidence and knowledge cleanly:

- Layer 5 source-of-record evidence includes runtime evidence, reference cache, and authored artifacts
- Layer 4 operational knowledge lives in `Postgres + pgvector`
- authored canon may live in `Git` or another authoritative provider when warranted

Design rule:

- raw evidence is not the default consumer surface
- semantic outputs are the default consumer surface
- Layer 4 operational knowledge may move ahead of Layer 5 authored canon during active work
- publication and re-ingestion bring authored canon back into alignment with Layer 4 and Layer 3
- Layer 5 should keep a stable evidence contract even when backend details vary by evidence class or phase

Sequencing note:

- Phase 1 and Phase 2 produce semantic outputs through boundary-triggered processing
- later, Mamba can become the default always-on near-time producer of that same semantic surface

Current upstream docs support the following assumptions:

- `Postgres` already gives a credible lexical retrieval surface through built-in full-text search.
- `pgvector` supports vector similarity inside the same operational database.
- `pgvector` documentation explicitly supports hybrid-search patterns when combined with Postgres full-text search.

That is why the current default is:

- `Postgres + pgvector` first
- add a second search platform only when measured Layer 4 requirements justify it

Operational rule:

- treat runtime evidence, reference-cache bodies, and authored-artifact revisions as different Layer 5 evidence classes behind one logical evidence contract
- keep `Postgres` as the operational middle and Layer 4 authority
- keep Layer 5 source records distinct from Layer 4 operational bodies even when the current implementation shares some infrastructure
- do not make Layer 4 the lifecycle owner of Layer 5 evidence

Do not treat all Layer 4 records as proto-artifacts.

Layer 4 includes:

- incubation workspaces
- external reference material
- authored work that is not ready for canon yet
- decomposed artifact knowledge when canonical artifacts do exist

Official references:

- https://www.postgresql.org/docs/current/textsearch.html
- https://github.com/pgvector/pgvector
