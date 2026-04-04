# Graphiti + Neo4j + Redis Layered Stack Complete Context Pack

## Purpose

This document models the layered Cortex stack around:

- bounded `Redis` working memory
- `Graphiti + Neo4j` for durable memory
- `OpenSearch` or `Postgres + pgvector` for the knowledge plane
- `Git` for canonical artifacts

This is the current hopeful graph-first layered stack.

Reviewed on `April 3, 2026`.

## Stack Shape

- `OpenClaw` as runtime shell
- bounded `Redis` working-memory sidecar
- evidence log and replay channel
- `Graphiti` as durable-memory authority
- `Neo4j` as durable graph store
- knowledge plane on:
  - `OpenSearch`, or
  - `Postgres + pgvector`
- `Git` as canonical artifact authority

## Why This Stack Is Attractive

It gives each layer a substrate that fits its job:

- working memory stays hot and cheap
- durable memory gets graph-native temporal semantics
- knowledge gets a retrieval-optimized search substrate
- canonical artifacts stay revisioned and reviewable

This is a cleaner expression of the graph path than earlier “Graphiti does everything” framings.

## What This Stack Optimizes For

- strongest temporal and provenance semantics in durable memory
- native graph reasoning and expansion
- explicit artifact authority outside the graph
- knowledge retrieval optimized independently from the durable graph
- clear split between live work, durable memory, and artifact retrieval

## What Graphiti Actually Owns Here

`Graphiti` owns:

- durable memory objects
- graph relationships
- episode-backed provenance
- corrections and invalidation
- graph-native retrieval over durable memory

It does not own:

- working memory
- canonical artifacts
- raw decomposition corpus
- knowledge-plane full-text or vector retrieval

That narrowing makes the stack more plausible.

## Why Neo4j Still Matters Here

This stack treats `Neo4j` as the durable graph backend because:

- RAM is not sufficient for an in-memory primary graph substrate
- data integrity matters more than raw traversal speed
- `Graphiti` already has a more mature documented path with `Neo4j`

This is the safer graph backend under the current constraints.

## Why Redis Still Makes Sense Here

`Redis` only makes sense here as a bounded operational layer:

- hot continuity
- task state
- queue state
- handoff buffers

It should not be treated as a primary durable memory substrate.

## Why The Knowledge Plane Is Separate

This is the most important correction in the stack.

The graph should not be forced to carry:

- every artifact slice
- every lexical retrieval surface
- every vectorized decomposition record

The knowledge plane exists so that:

- the graph routes and reasons
- the knowledge layer retrieves evidence

### `OpenSearch` Variant

This variant is strongest when:

- lexical retrieval matters heavily
- schema-rich search and filters matter
- large document retrieval is the main concern

### `Postgres + pgvector` Variant

This variant is strongest when:

- operational simplicity matters more
- typed relational control over decomposition matters
- one database for typed records plus vectors is preferred

## What We Would Be Adopting

- graph-first durable memory
- separate working memory
- separate knowledge plane
- artifact authority outside memory
- explicit cross-layer routing

## What We Would Be Fighting

- more custom integration than `Mem0`
- heavier ingestion cost than vector-first stacks
- more responsibility for cross-layer reconciliation
- a sharper need for write discipline and auditability

## Main Risks

1. The graph write path can be semantically corrupted by bad extraction if guardrails are weak.
2. The knowledge plane choice can sprawl if both `OpenSearch` and `Postgres` are treated as co-equal.
3. Working memory plus graph plus knowledge can become split-brain if contracts are not enforced.

## Why This Stack Remains Serious

It remains serious because it no longer asks the graph to be:

- working memory
- artifact store
- universal retrieval substrate

It lets `Graphiti` focus on the thing it is best at:

- durable semantic memory with temporal correctness and graph-native retrieval
