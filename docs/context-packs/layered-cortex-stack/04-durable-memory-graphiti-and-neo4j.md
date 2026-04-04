# Durable Memory: Graphiti And Neo4j

## The Main Decision

Layer 3 durable memory is built around:

- `Graphiti`
- `Neo4j`

This is the semantic memory center of the chosen stack.

## Why Layer 3 Exists

Layer 3 exists to store long-lived semantic knowledge that should survive:

- session resets
- compaction
- short-term runtime noise
- transient working-memory state

It is the durable semantic authority.

## What Layer 3 Owns

Layer 3 owns:

- durable beliefs
- preferences
- constraints
- decisions
- relationship-bearing memory
- support references
- temporal lineage
- invalidation and supersession

Layer 3 does not own:

- the working transcript
- raw evidence logs
- full document bodies
- the full decomposition corpus

## Why Graphiti

Graphiti is the chosen Layer 3 core because it provides the memory semantics Cortex cares about most:

- episode-backed provenance
- temporal memory
- invalidation instead of blind overwrite
- graph-native retrieval over durable memory

That combination is what made it hard to replace cleanly.

## Why Neo4j

Neo4j is the backend because it is:

- disk-backed
- durable
- better aligned with integrity than an in-memory primary graph store

The current posture is that Layer 3 should optimize for integrity and temporal memory behavior, not for the fastest possible RAM-heavy graph substrate.

## Notion Staging

Layer 3 should not ingest raw runtime traffic directly.

The intended path is:

1. raw evidence closes into an evidence package
2. the High-Signal Mamba Stream emits candidate notions
3. high-signal notions may be written early as tentative cross-thread memory
4. reconciliation decides what becomes trusted durable memory

This means durable memory is not a naive real-time extraction sink.

It is a staged semantic authority.

## Memory States

The important Layer 3 states are:

- `tentative`
- `low_confidence`
- `active`
- `superseded`
- `invalidated`
- `stale_support`

These states matter because they let the system be fast without lying about certainty.

## How Runtime Evidence Enters Graphiti

Graphiti should not receive the whole raw session log as its normal representation.

Instead, a runtime evidence package should usually contain:

- a compact summary
- timestamps
- thread or session ids
- a pointer back to the canonical evidence record
- only Layer 3 appropriate beliefs or support

This keeps Graphiti focused on semantic memory rather than transcript storage.

## How Document Evidence Enters Graphiti

Document artifacts should follow the same restraint.

Graphiti should get:

- one compact summary representation
- a pointer to the canonical artifact revision
- only extracted standalone Layer 3 appropriate beliefs or support

The full document body should remain outside Layer 3.

## Guardrails Around Layer 3

Layer 3 should be protected by:

- notion staging
- oversight review
- checkpoint and session-end reconciliation
- nightly maintenance
- support-aware invalidation when artifacts change

This is how the system avoids letting a few bad extractions poison the whole semantic memory layer.

## Why Layer 3 Is Not Working Memory

Layer 3 is deliberately slower and more trusted than working memory.

Working memory supports the current session.

Layer 3 supports durable cross-session and cross-thread orientation.

If Layer 3 is treated like working memory, the graph fills with noise.

If working memory is treated like Layer 3, runtime continuity becomes too slow and rigid.

## What Makes This The Memory Core

If one part of the stack is the semantic heart, it is Layer 3.

Policy lives above it.

OpenClaw working memory lives beside it.

Artifacts live below it.

But durable semantic truth compounds here.

That is why Graphiti plus Neo4j is the center of the chosen memory posture.
