# Knowledge And Artifacts

This document defines the stable product posture for Layers 4 and 5.

## Layer 4: Decomposed Artifact Knowledge

Layer 4 is the operational retrieval layer.

It is built around:

- decomposition records
- typed slices
- embeddings
- lexical fields
- source-linked offsets
- revision-aware retrieval payloads

The default implementation posture is `Postgres + pgvector`.

Layer 4 is allowed to move quickly, but it must remain:

- source-linked
- revision-aware
- subordinate to canonical artifact truth

## Layer 5: Canonical Artifacts

Layer 5 is the publication-truth layer.

It is built around:

- `Git`
- provider-backed authoritative sources
- reviewed redrafts

## Stable Product Rule

Layer 4 may move ahead of Layer 5 during active work.

That is allowed only if:

- the anchor is explicit
- dirty-state tracking is explicit
- publication and re-ingestion are part of the design

Only compact summary + pointer + Layer 3 appropriate beliefs should flow upward into durable memory.
