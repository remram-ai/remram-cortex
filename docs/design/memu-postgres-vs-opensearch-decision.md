# memU Fork Storage Decision: Postgres vs OpenSearch

## Purpose

This document answers one narrow design question:

If `remram-cortex` forks `memU`, should the fork stay on `Postgres` first or force an `OpenSearch` retrieval substrate early?

As of April 1, 2026, the recommended decision is:

- start the fork on `Postgres` plus `pgvector`
- keep the system-of-record model in Postgres
- preserve a clean path to add `OpenSearch` later as a retrieval engine or side index
- do not force OpenSearch into Phase 0 just to match current roadmap language

This is a staged decision, not a permanent rejection of OpenSearch.

## Executive Decision

For a memU-based fork, choose `Postgres` first.

Reason:

- it stays closest to memU's existing architecture
- it preserves transactional correctness for mutable memory and provenance
- it keeps the implementation path shorter for Phase 0 through Phase 2
- it is good enough for early hybrid retrieval if we accept some manual assembly

Revisit that decision when Cortex starts needing search-engine-native behavior rather than database-native behavior.

If `OpenSearch-first` is non-negotiable from the beginning, that is a warning sign that a memU fork may no longer be the right base.

## The Hard Difference

The real difference is not "database speed" in the abstract.

The hard difference is this:

- `Postgres` is better as the transactional system of record for mutable knowledge objects
- `OpenSearch` is better as the search corpus and retrieval engine for ranked document search

That distinction matters because Cortex needs both:

- durable memory mutation
- strong provenance and joins
- governance-first retrieval
- good document and passage retrieval

The decision is really about which side we optimize first.

## Hard Differences

| Concern | Postgres + `pgvector` | OpenSearch | Why Cortex Cares |
| --- | --- | --- | --- |
| Primary role | transactional database | search engine | Cortex mutates memory records and also retrieves ranked evidence |
| Write visibility | immediate read-your-writes | near-real-time refresh behavior | fresh captures are easier to inspect immediately in Postgres |
| Document storage | strong `jsonb`, joins, update semantics | strong indexed document corpus | Cortex stores documents as artifacts but searches them as evidence |
| Lexical search | built-in full-text search, `tsvector`, `GIN` | native relevance-oriented text search | Cortex will need lexical recall, not only vectors |
| Vector search | `pgvector` exact and approximate ANN | native vector and hybrid retrieval features | Cortex needs semantic recall but not as the only signal |
| Hybrid search | possible, but application-assembled | first-class `hybrid` query with shared filter and score pipeline | Cortex wants lexical, vector, and typed signals working together |
| Filtered ANN | workable, but approximate filtering is weaker and often tuning-heavy | efficient k-NN filtering options are built in | governance-first retrieval makes filters non-optional |
| Passage retrieval | usually modeled with chunk tables and custom joins | chunking, embedding, nested hits, and search pipelines are search-native | Cortex imports long documents and wants evidence slices, not just whole files |
| Facets and aggregations | SQL can do it, but not search-native | built for search-oriented aggregations and ranking experiments | operator inspection and retrieval diagnostics get easier in OpenSearch |
| Mutation and merge workflows | much stronger | possible, but not the natural center | Cortex reflection and provenance updates are mutation-heavy |
| Operational simplicity | one primary system | better once search is core, but heavier to stand up early | memU fork acceleration favors fewer moving parts |

## What "Postgres Handles Documents Well" Actually Means

That instinct is right, but there are two different meanings of "documents."

`Postgres` handles documents well as application data:

- `jsonb` storage
- transactional updates
- joins across artifact, provenance, and memory tables
- built-in text search
- flexible indexing with `GIN`

`OpenSearch` handles documents well as ranked search corpus:

- inverted index oriented toward relevance scoring
- vector and lexical search in one retrieval surface
- passage chunking and embedding pipelines
- nested search and hit-level explanation
- search-time aggregations and ranking controls

So the real question is not whether Postgres can store documents.

It can.

The question is whether we want the document layer optimized first for:

- mutation and truth management

or for:

- ranked retrieval over large or passage-heavy corpora

For a memU fork, the first option is the more natural fit.

## Similar Plugin And Extension Paths On The Postgres Side

There are credible Postgres-side building blocks.

### Core Building Blocks

- `pgvector` gives vector columns and exact or approximate nearest-neighbor search
- PostgreSQL full-text search gives lexical search with dictionaries, ranking, and highlighting controls
- `GIN` indexes support efficient searching over composite values like arrays and `jsonb`

### Performance-Oriented Extension Path

- `pgvectorscale` extends Postgres vector search with `StreamingDiskANN` and label-based filtered vector search

This is useful, but it does not erase the architectural difference.

Important constraint:

- `pgvectorscale` label-filtered search is strongest when the filter is encoded as indexed labels
- arbitrary `WHERE` clause filtering still falls back to post-filter behavior

That means Postgres extensions can narrow the gap, especially for vector speed, but they do not fully turn Postgres into a search engine.

## The Tradeoffs We Actually Care About

### Where Postgres Wins

- mutable knowledge objects and patch workflows
- provenance joins and update discipline
- one transactional source of truth
- memU architectural compatibility
- simpler early deployment
- immediate validation of newly written records

### Where OpenSearch Wins

- filtered vector plus lexical hybrid retrieval
- shared filter semantics across retrieval modes
- passage-oriented document search
- ranking experiments and explainability
- faceting and search-oriented aggregations
- larger search corpora and higher query concurrency

### Where The "Speed" Concern Is Real

If by "speed" we mean:

- one record written and immediately readable
- simple joins and point lookups

then Postgres is not the weaker option.

If by "speed" we mean:

- top-k ranked retrieval across many chunks with filters, hybrid scoring, and passage assembly

then OpenSearch has the stronger native posture.

So the speed concern is real, but it is workload-specific.

## Do We Care Yet?

For an early memU fork, probably not enough to justify forcing OpenSearch first.

Early Cortex fork phases mainly need:

- memory capture
- reflection and mutation
- provenance growth
- governance fields
- usable retrieval on a modest corpus

That is a good match for `Postgres` first.

We should care more about `OpenSearch` once one or more of these become painful:

- governance-filtered ANN loses too much recall or requires too much tuning
- imported long-form documents need strong passage retrieval
- hybrid ranking becomes a product feature rather than a convenience
- retrieval traces need search-engine-level explainability
- corpus size or query concurrency outgrows acceptable Postgres behavior

## Decision For The memU Fork

Choose this posture:

1. `Postgres` remains the system of record.
2. `pgvector` is the default early vector layer.
3. Full-text and typed lexical retrieval live in Postgres first.
4. Chunk records, typed signals, provenance, and retrieval traces are modeled in durable tables or structured fields rather than only in index documents.
5. `OpenSearch` is introduced later only when retrieval needs justify the additional operational complexity.

This keeps the fork architecturally honest.

It says:

- optimize first for memory correctness and evolution
- add search-engine acceleration later when search actually becomes the bottleneck or product differentiator

## Compromises We Accept If We Choose Postgres First

- hybrid retrieval will be more application-assembled than engine-native
- filtered ANN will need more tuning and query-shaping
- passage retrieval ergonomics will be less elegant early
- later migration or dual-write work remains on the roadmap

These are acceptable compromises if Phase 0 through Phase 2 are about proving Cortex semantics on top of memU rather than maximizing retrieval sophistication immediately.

## Compromises We Should Not Accept

- trapping governance or typed signals only inside opaque JSON forever
- treating vector similarity as sufficient without strong lexical or typed retrieval
- assuming Postgres extensions completely erase the OpenSearch search-model advantage
- letting the storage decision distort the canonical Cortex object model

## Revisit Triggers

Move the architecture discussion back to the table when any of these become true:

- Postgres retrieval requires unstable tuning to satisfy governance-bounded recall
- document import quality depends on passage search and evidence slicing
- search relevance work starts dominating roadmap effort
- operators need first-class facets, ranking controls, or search explainability
- dual-write cost becomes lower than continued Postgres-side search assembly

## Recommendation

If we fork `memU`, start with `Postgres`.

That is not a retreat from Cortex goals.

It is the shortest honest path to:

- a working fork
- durable memory mutation
- stronger provenance
- scoped retrieval
- a later, cleaner decision on whether OpenSearch is truly needed

If Cortex decides that `OpenSearch-first` is mandatory from the first serious implementation, we should be much less confident that a memU fork is the right starting point.

## Related Docs

- [memU Fork Feasibility](../reference/memu-fork-feasibility.md)
- [memU Fork Phased Plan](memu-fork-phased-plan.md)
- [memU Spike Evaluation](memu-spike-evaluation.md)
- [Cortex Architecture](../remram-cortex/architecture.md)

## Sources

- `pgvector` README: https://github.com/pgvector/pgvector
- PostgreSQL `jsonb` docs: https://www.postgresql.org/docs/current/datatype-json.html
- PostgreSQL full-text search docs: https://www.postgresql.org/docs/current/textsearch-controls.html
- PostgreSQL `GIN` docs: https://www.postgresql.org/docs/current/gin.html
- `pgvectorscale` README: https://github.com/timescale/pgvectorscale
- OpenSearch hybrid query docs: https://docs.opensearch.org/latest/query-dsl/compound/hybrid/
- OpenSearch efficient k-NN filtering docs: https://docs.opensearch.org/2.6/search-plugins/knn/filter-search-knn/
- OpenSearch refresh docs: https://docs.opensearch.org/latest/api-reference/index-apis/refresh/
- OpenSearch text embedding docs: https://docs.opensearch.org/latest/ingest-pipelines/processors/text-embedding/
- OpenSearch text chunking docs: https://docs.opensearch.org/3.1/ingest-pipelines/processors/text-chunking/
