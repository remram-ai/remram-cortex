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
