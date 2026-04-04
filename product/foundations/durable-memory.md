# Durable Memory

This document defines the stable product posture for Layer 3.

## Active Direction

Layer 3 is built around:

- `Graphiti`
- `Neo4j`

## Stable Responsibilities

Layer 3 owns:

- concepts and idea clusters
- durable beliefs
- preferences
- constraints
- decisions
- relationship-bearing memory
- provenance and support references
- invalidation and supersession
- semantic continuity across threads and sessions
- concept relationships that help Layer 4 organize itself

## Stable Write Model

The durable-memory product model is:

1. evidence becomes semantic checkpoints
2. semantic checkpoints update notions in `QMD`
3. high-signal notions may appear early as tentative cross-thread memory under tighter rules
4. reconciliation decides what becomes trusted durable memory in Layer 3

Durable memory should normally ingest:

- a compact summary
- provenance or support references
- a pointer back to evidence, a Layer 4 workspace, or a canonical artifact revision

It should not ingest raw transcripts or full artifact bodies as the normal representation.

Layer 3 may represent:

- that several threads belong to one emerging idea
- that several workspaces are related or merged
- that one draft supersedes another
- that references support a concept
- that a workspace is becoming a promotion candidate

## Product Rule

Layer 3 is the semantic memory authority.

It is not:

- working memory
- the evidence log
- the operational workspace body store
- the full artifact corpus
