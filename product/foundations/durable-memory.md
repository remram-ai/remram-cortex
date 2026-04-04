# Durable Memory

This document defines the stable product posture for Layer 3.

## Active Direction

Layer 3 is built around:

- `Graphiti`
- `Neo4j`

## Stable Responsibilities

Layer 3 owns:

- durable beliefs
- preferences
- constraints
- decisions
- relationship-bearing memory
- provenance and support references
- invalidation and supersession

## Stable Write Model

The durable-memory product model is:

1. evidence becomes semantic checkpoints
2. semantic checkpoints emit candidate notions
3. high-signal notions may appear early as tentative memory
4. reconciliation decides what becomes trusted durable memory

Durable memory should normally ingest:

- a compact summary
- provenance or support references
- a pointer back to evidence or canonical artifact revision

It should not ingest raw transcripts or full artifact bodies as the normal representation.

## Product Rule

Layer 3 is the semantic memory authority.

It is not:

- working memory
- the evidence log
- the full artifact corpus
