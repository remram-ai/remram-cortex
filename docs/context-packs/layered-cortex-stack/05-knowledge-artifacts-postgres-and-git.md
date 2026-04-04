# Knowledge, Artifacts, Postgres, And Git

## The Main Decision

Layers 4 and 5 are intentionally separate.

Layer 4 is:

- decomposed
- operational
- retrieval-ready

Layer 5 is:

- canonical
- reviewable
- publication-grade

This is one of the most important distinctions in the whole architecture.

## Layer 4: Decomposed Artifact Knowledge

Layer 4 is the machine-usable artifact layer.

It contains:

- decomposition records
- typed slices
- extracted structures
- embeddings
- lexical fields
- source-linked offsets
- revision-aware retrieval payloads

The current default substrate is `Postgres + pgvector`.

## Layer 5: Canonical Artifacts

Layer 5 is the ground-truth layer for artifacts.

It contains:

- Git-backed canonical documents
- provider-backed authoritative source records
- published redrafts
- revision history

The default posture is to use `Git` when it fits the artifact type.

## Why The Split Exists

The split exists because the system needs both:

- a machine-ready operational surface
- a human-reviewable publication truth

If those are collapsed into one layer, the system loses either:

- operational speed and decomposition flexibility
- or clear publication truth and reviewability

## What Postgres Is Doing

In the current stack, `Postgres + pgvector` is doing three jobs:

- runtime evidence authority
- control-plane state
- Layer 4 decomposed knowledge

That is acceptable because these are all operational, queryable, revision-aware surfaces.

## What Git Is Doing

Git is doing the canonical artifact job.

It provides:

- explicit revisions
- reviewable changes
- publication truth
- clean re-ingestion boundaries

Git is not the decomposed operational retrieval plane.

It is the canonical source plane.

## Artifact Indexing Pattern

Artifacts should follow the same pattern as session evidence:

1. keep the raw source in the canonical layer
2. derive decomposition and retrieval structures separately
3. send only summary plus pointer plus Layer 3 appropriate beliefs into durable memory

This keeps each layer focused on its own job.

## Anchor Identity

Artifacts should have stable Cortex identity through an `anchor_id`.

That allows:

- one artifact to appear in Git, Postgres, and Graphiti without becoming separate semantic objects
- revision-aware support tracking
- re-ingestion and reconciliation after publication

## Dirty-State And Publication

Layer 4 is allowed to move ahead of Layer 5 during active work, but only with explicit dirty-state tracking.

Important artifact states include:

- `dirty`
- `pending_redraft`
- `unsynced_to_canonical`
- `redraft_ready`

Those states tell the system when the operational artifact view has outrun publication truth.

## Publication Cycle

The publication loop is:

1. Layer 4 changes mark an anchor dirty
2. the redraft process gathers latest Layer 4 knowledge and Layer 3 memory support
3. review or approval happens if needed
4. Layer 5 is updated
5. the new revision is re-ingested
6. Layer 3 support can be reconciled against the new revision

This is how the system supports live change without collapsing publication truth.

## What Layer 3 Should See From Artifacts

Layer 3 should only receive:

- compact summary representations
- pointers to canonical revisions
- standalone facts or beliefs that are appropriate for semantic memory

Layer 3 should not become a shadow artifact store.

## Bottom Line

Layer 4 and Layer 5 exist so Cortex can reason over artifacts aggressively during active work without corrupting publication truth.

Postgres powers the operational artifact plane.

Git powers the canonical artifact plane.

The system needs both.
