# Graphiti + Neo4j Durable Memory

This document defines the active Layer 3 durable-memory posture.

## Role

Layer 3 is the durable semantic authority.

It owns:

- durable beliefs
- preferences
- constraints
- decisions
- support relationships
- supersession and invalidation
- temporal lineage

## Why Graphiti

`Graphiti` is the chosen Layer 3 core because it provides:

- episode-backed provenance
- point-in-time memory semantics
- invalidation instead of blind overwrite
- graph-native retrieval over durable memory

This is the capability that was hardest to reproduce cleanly elsewhere.

## Why Neo4j

`Neo4j` is the current backend because:

- it is durable and disk-backed
- it fits Layer 3 authority better than an in-memory primary graph store
- it is the safer integrity posture for long-lived memory

## Confidence And Trust

The current Graphiti docs clearly support:

- temporal lineage
- episode-backed provenance
- invalidation and supersession

I do not see a documented first-class Graphiti confidence model that replaces Cortex trust states.

So the active architecture should assume:

- Graphiti provides lineage, support, and temporal structure
- Cortex provides explicit trust and confidence states around staged and durable memory

That is why Layer 3 still carries notions and memory-adjacent states such as:

- `tentative`
- `low_confidence`
- `active`
- `superseded`
- `invalidated`
- `stale_support`

## Notion Staging

Durable memory should not be written naively from raw runtime traffic.

The default path is:

1. raw runtime evidence closes into an evidence package
2. the High-Signal Mamba stream emits candidate notions
3. high-signal notions may be written early as tentative cross-thread memory
4. reconciliation confirms, merges, downgrades, or rejects them
5. confirmed outputs become trusted Layer 3 memory

Suggested status fields:

- `tentative`
- `low_confidence`
- `active`
- `superseded`
- `invalidated`
- `stale_support`

## Artifact Lineage In Layer 3

Artifact lineage should be represented in Graphiti as well.

The clean pattern is:

- represent the artifact or document as an entity in the graph
- keep revision pointers back to the Layer 5 canonical source
- connect Layer 3 beliefs, support, or decisions back to the artifact anchor and revision

This gives Layer 3 the same lineage discipline for artifacts that it already wants for runtime evidence.

## Episode Packaging

`Graphiti` should not receive full raw logs as its normal representation.

For runtime evidence, it should receive a compact evidence package containing:

- summary
- timestamps
- thread or session ids
- pointer back to the canonical evidence record
- only Layer 3 appropriate beliefs or support

For documents, the parallel pattern is:

- one summary representation
- pointer to the canonical artifact revision
- only extracted standalone Layer 3 appropriate beliefs or support

In practice, this should usually mean an artifact or document node plus support edges, not a shadow copy of the full document body.

## Guardrails

Layer 3 should be protected by:

- staged notion writes
- oversight review surfaces
- session-end or checkpoint reconciliation
- nightly maintenance
- support-aware invalidation when artifacts change

## Non-Goals

Layer 3 is not:

- working memory
- the full artifact store
- the full decomposition corpus
- a transcript archive
