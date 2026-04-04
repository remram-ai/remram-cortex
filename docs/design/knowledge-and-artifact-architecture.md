# Knowledge And Artifact Architecture

This document defines Layers 4 and 5.

## Layer 4: Decomposed Artifact Knowledge

Layer 4 is the operational knowledge layer.

It holds:

- decomposition records
- typed slices
- embeddings
- lexical fields
- source-linked offsets
- revision-aware retrieval payloads

The default substrate is `Postgres + pgvector`.

## Layer 5: Canonical Artifacts

Layer 5 is the ground-truth layer.

It holds:

- Git-backed canonical artifacts
- provider-backed authoritative source documents
- publication-grade redrafts
- revision history

Layer 5 is where publication truth lives.

## Design Rule

Layer 4 can move ahead of Layer 5 during active work.

That is allowed only if:

- the artifact anchor is explicit
- the canonical revision is known
- dirty-state tracking is explicit
- publication and re-ingestion can catch back up later

## Artifact Indexing Pattern

Artifacts should be treated the same way session evidence is treated:

- keep the raw source in the canonical layer
- build decomposed operational knowledge separately
- send only compact summary + pointer + Layer 3 appropriate beliefs into durable memory

That means:

- full documents stay in Layer 5
- retrieval-ready slices live in Layer 4
- durable memory receives only what is appropriate for semantic memory

## Postgres Role

`Postgres` is doing three jobs in the current design:

- runtime evidence authority
- control-plane state
- decomposed artifact knowledge

This is acceptable because those are all operational, queryable, revision-aware surfaces.

## Git Role

`Git` remains the preferred canonical artifact posture because it gives:

- reviewable revisions
- clean publication
- explicit redraft flow
- easy inspection

## Publication Cycle

The publication loop is:

1. decomposition changes mark the anchor dirty
2. redraft gathers latest Layer 4 knowledge and Layer 3 memory support
3. review or approval happens if needed
4. canonical artifact is updated
5. new revision is re-ingested
6. stale support in Layer 3 is reconciled
