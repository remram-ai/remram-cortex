# Layered Stack Options Decision Matrix

## Purpose

This document compares the current layered-stack options without forcing a recommendation.

It is meant to answer:

- what each stack is optimizing for
- what each stack assumes
- where each stack is likely to fit or hurt

Reviewed on `April 3, 2026`.

## Compared Stacks

### Stack A

`Cognee` layered stack

### Stack B

`Graphiti + Neo4j + Session-Surface Working Memory + OpenSearch/Postgres + Git`

### Stack C

`Mem0 + Weaviate + Git` layered stack

### Stack D

`Weaviate-first` layered stack

## Common Assumptions

All four stacks assume:

- `OpenClaw` remains the runtime shell
- working memory is separate from durable memory
- canonical artifacts remain outside the memory authority
- artifact decomposition is revision-aware
- Cortex remains the cross-layer authority

## Comparison Matrix

| Dimension | Stack A: Cognee | Stack B: Graphiti + Neo4j + Session Surface | Stack C: Mem0 + Weaviate | Stack D: Weaviate-First |
| --- | --- | --- | --- | --- |
| Core posture | platform-first | graph-first durable memory | memory-first | hybrid-platform-first |
| Working memory fit | OpenClaw session surface + Mamba stream augmentation | OpenClaw session surface + Mamba stream augmentation | OpenClaw session surface + Mamba stream augmentation | OpenClaw session surface + Mamba stream augmentation |
| Durable-memory clarity | medium | high | high | medium |
| Knowledge-layer fit | high | high | medium-high | high |
| Hybrid retrieval shape | application-layer | graph + search layered retrieval | substrate-native available through Weaviate, but not fully exposed by stock Mem0 | database-native |
| Temporal semantics | medium | high | medium-low | low unless built |
| Provenance richness | medium | high | medium | medium if built well |
| Upstream leverage | medium | medium | high | low |
| Operational complexity | high | medium-high | medium | medium-high |
| Custom lifecycle burden | medium | medium | low-medium | high |
| Artifact workflow fit | high | high | medium-high | high |
| Best use case | multi-source knowledge platform | strongest durable memory semantics | function-first layered memory | highest-control hybrid-first platform |

## What Each Stack Is Adopting

### Stack A: Cognee

Adopts:

- platform-native multi-store orchestration
- staged knowledge processing
- dataset-oriented ingestion

### Stack B: Graphiti + Neo4j + Session Surface

Adopts:

- graph-first durable memory
- session-surface working memory with bounded context assembly
- separate knowledge plane

### Stack C: Mem0 + Weaviate

Adopts:

- record-first durable memory
- strong pragmatic runtime path
- shared hybrid-capable substrate

### Stack D: Weaviate-First

Adopts:

- hybrid retrieval as the primary substrate
- Cortex-owned memory semantics
- maximum schema and retrieval control

## What Each Stack Is Fighting

### Stack A: Cognee

Fighting:

- simplicity
- a narrow memory-plugin worldview

### Stack B: Graphiti + Neo4j + Session Surface

Fighting:

- ingest cost
- custom integration burden
- graph-write integrity concerns

### Stack C: Mem0 + Weaviate

Fighting:

- weaker native temporal semantics
- weaker graph-native provenance

### Stack D: Weaviate-First

Fighting:

- the need to invent durable-memory semantics directly
- lower upstream leverage

## Decision Pressure Points

### Choose Stack A If

- the architecture is truly accepted as multi-store and multi-source
- a platform-native orchestration layer is preferred over assembling one

### Choose Stack B If

- durable memory quality matters more than ingestion simplicity
- graph-native temporal semantics remain important
- working memory and knowledge are explicitly separated

### Choose Stack C If

- function before architecture remains the governing rule
- official integration and faster usable memory matter most

### Choose Stack D If

- hybrid retrieval is the main center of gravity
- Cortex should own lifecycle semantics directly
- custom platform work is acceptable

## Validation Questions

1. Which stack gives the clearest durable-memory authority in practice?
2. Which stack keeps artifact lifecycle clean without overloading memory?
3. How much graph is actually needed in the durable layer?
4. Does application-layer hybrid retrieval feel sufficient, or is database-native hybrid important?
5. How much custom semantic burden is acceptable?

## Bottom Line

These four stacks are no longer being compared as single-memory products.

They are being compared as different ways to populate the same layered architecture:

- platform-first
- graph-first
- memory-first
- hybrid-platform-first

That is the correct comparison frame going forward.
