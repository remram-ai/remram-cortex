# Knowledge, Artifacts, Postgres, And Git

## The Main Clarification

Layer 4 is the operational knowledge authority.

Layer 5 is the source-of-record evidence layer.

Layer 4 is not just a projection of Layer 5.

## What Layer 4 Holds

Layer 4 should hold:

- working or incubation workspaces
- reference-derived knowledge bodies
- decomposed artifact knowledge
- active operational document state

This means Layer 4 can be authoritative even when there is no authored Layer 5 artifact at all.

Layer 5 stores evidence bodies.

Layer 4 stores the shaped operational knowledge derived from them.

## External References

External references are distinct from authored artifacts.

Examples:

- uploaded PDFs
- podcast transcripts
- articles
- research sources

These should not automatically become authored canon.

Instead:

- Layer 5 may retain the source body as `reference_cache`
- Layer 4 holds summaries, linked records, and extracted operational knowledge
- Layer 3 stores only durable meaning that matters

## Layer 5 Evidence Classes

Layer 5 should be read as three main evidence classes:

- `runtime_evidence`
- `reference_cache`
- `authored_artifact`

Only the authored-artifact class depends on publication-grade authorship and revision.

`Git` is one backend for that class.

Layer 5 should be treated as one stable evidence contract even when the backend differs by class or phase.

That means:

- filesystem-backed runtime evidence early
- shorter-lived retained references where appropriate
- `Git` later for `authored_artifact`

Layer 4 should reference Layer 5 evidence, not become its lifecycle owner.

The phase story is:

- `Phase 1` uses Layer 5 for chat-derived `runtime_evidence`
- `Phase 2` adds one-way `reference_cache`
- `Phase 3` adds retained owned-source evidence with source-maintenance semantics
- `Phase 4` introduces `authored_artifact` as canonical published output

## Multiple Ingestion Workflows

Layer 5 is one evidence layer, but not one ingestion workflow.

The main workflows are:

- `runtime_evidence` capture for chat transcripts and tool outputs
- reference ingestion for web links and other outside material
- owned-source ingestion for high-signal user content
- authored promotion and reprocessing for Layer 4 work that becomes canon

The promotion path is not the same thing as reference or artifact ingestion.

Once a Layer 4 workspace is promoted into an authored artifact, Layer 5 becomes the canonical source for that body.

That does not make Layer 5 dead storage.

Meaningful authored revision must be able to trigger:

- re-ingestion back into Layer 4 so the operational body stays aligned
- reconciliation in Layer 3 so summaries, support, and semantic links stay current

## Why Postgres Matters

Postgres is the operational middle-layer authority for now.

It covers:

- Layer 4 bodies
- reference records and summaries
- decomposed artifact knowledge where authored artifacts exist
- metadata
- workflow fields

This is why the architecture is not adding `OpenSearch` now.

The goal is fewer moving pieces and cleaner authority boundaries.

## Budding Ideas

Budding ideas do not jump straight to authored canon.

They live first as:

- Layer 3 relationship structure
- Layer 4 evolving workspace bodies

Layer 5 already exists as evidence.

Only the authored-artifact subset appears later when canon is warranted.
