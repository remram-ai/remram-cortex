# Knowledge And Artifact Architecture

This document defines the locked relationship between Layer 4 and Layer 5.

## Core Rule

Layer 4 is the operational knowledge authority.

Layer 5 is the source-of-record evidence layer.

Authored canon is one permanent Layer 5 evidence class, not the whole meaning of the layer.

That is the central clarification in this design pass.

## Evidence, Knowledge, And Meaning

The architecture now separates three different jobs:

- Layer 5 stores persisted evidence bodies
- Layer 4 stores processed operational knowledge bodies
- Layer 3 stores durable semantic meaning

That is the clean epistemic model:

- what existed or was seen lives in Layer 5
- what the system is actively working with lives in Layer 4
- what remains semantically true over time lives in Layer 3

## Layer 4: Operational Knowledge Authority

Layer 4 is not merely a projection of Layer 5.

It is authoritative for operational content.

That means:

- if there is no authored Layer 5 artifact, Layer 4 can still be the authority for that content
- if there is Layer 5 evidence behind the content, Layer 4 is still the authority for active work and retrieval
- Layer 4 owns the shaped bodies the system works with, not the raw evidence bodies behind them

Layer 4 should hold:

- incubation workspaces
- working synthesis bodies
- reference-derived knowledge bodies
- decomposed artifact knowledge
- active operational document state
- retrieval-ready operational bodies

Layer 4 should receive bounded derived forms from Layer 5 rather than pulling full raw bodies into operational storage by default.

Useful Layer 4 forms include:

- summaries
- extracted snippets
- decomposition chunks
- workspace-ready notes
- dirty-state and sync fields
- pointers back to Layer 5 evidence

## Layer 4 Content Classes

Layer 4 should explicitly support at least three content classes:

### 1. Working Or Incubation Workspaces

These are medium-horizon operational bodies that may span many threads.

They are:

- incomplete
- unstable
- evolving
- operationally authoritative

They are not bugs in the architecture.

They are a core problem the architecture is explicitly solving.

### 2. External Reference Material

External materials are distinct from authored canon.

Examples:

- uploaded PDFs used for reference
- podcast transcripts
- external articles
- factual sources
- research materials the user does not own

These should not automatically become authored artifacts.

Instead:

- Layer 5 may retain the source body as `reference_cache`
- Layer 4 may hold summaries, linked reference records, extracted operational knowledge, and retrieval-ready material
- Layer 3 stores only the durable meaning that matters

### 3. Authored Operational Work

These are operational bodies connected to authored material that may later warrant canon.

Examples:

- business-plan workspaces
- draft product direction notes
- evolving dossiers
- authored synthesis documents

These may later promote into the `authored_artifact` class inside Layer 5 when publication-grade canon becomes warranted.

## Layer 5: Source-Of-Record Evidence

Layer 5 stores persisted evidence bodies and source records.

It does not own semantic meaning.

It does not own Layer 4 working bodies.

The main Layer 5 evidence classes are:

### 1. Runtime Evidence

This includes:

- session transcripts
- evidence packages
- tool outputs
- runtime captures

This is evidence of what happened.

### 2. Reference Cache

This includes retained or cached external source bodies such as:

- fetched pages
- uploaded files
- temporary source snapshots
- retained external transcripts

This is evidence of what was seen.

### 3. Authored Artifact

This is the permanent and revisioned Layer 5 evidence class used when publication-grade authorship and review really matter.

It may be backed by `Git` or another provider.

This is evidence of what was intentionally published or retained as canon.

## Multiple Ingestion Workflows

The architecture should treat Layer 5 as one evidence layer with multiple intake paths rather than one generic ingestion flow.

The main workflows are:

### 1. Runtime Evidence Capture

This covers:

- chat transcripts
- session logs
- tool outputs
- evidence packages

This is the Phase 1 evidence path and the main source for chat-derived memory work.

### 2. Owned Source Ingestion

This covers authored or owned source material the system intends to keep as high-signal evidence.

Examples:

- user-owned documents
- internal notes ingested as source material
- durable authored content imported into the system

This is stronger than generic reference intake because the source is intentionally retained and treated as part of the user's evidence corpus.

### 3. Reference Ingestion

This covers outside material such as:

- web links
- uploaded reference PDFs
- fetched pages
- borrowed research material

This usually lands first as `reference_cache` and follows different retention rules than owned artifacts.

### 4. Promotion And Reprocessing

This is not normal ingestion.

It is the Layer 4 to Layer 5 authored publication path plus the bottom-up reprocessing loop from authored canon back into Layer 4 and Layer 3.

This workflow exists so authored Layer 5 revisions do not become dead storage.

## Layer 5 Is Not Just Git

Git is one Layer 5 backend for one Layer 5 evidence class.

It is not the definition of the whole layer.

Layer 5 should instead be read as the source-of-record evidence system, with different evidence classes and retention horizons behind one stable contract.

## Layer 5 Storage Posture

Layer 5 should be interface-first rather than backend-first.

That means Cortex should be able to rely on one stable evidence contract even when storage differs by phase or evidence class.

In the active posture:

- Phase 1 uses filesystem-backed runtime evidence
- reference-cache bodies may follow shorter-lived cache semantics
- authored artifacts later introduce `Git` as the first canonical backend

The important boundary is:

- Layer 5 owns evidence-body storage and lifecycle behavior
- Layer 4 may point at Layer 5, but it should not become Layer 5's keeper

## Postgres Role

`Postgres` remains the operational middle-layer authority for now.

It should cover:

- Layer 1 policy and control data
- Layer 4 workspace bodies
- reference summaries and links
- decomposed artifact knowledge
- retrieval metadata
- workflow fields
- dirty-state and sync tracking

It may also hold operational evidence metadata where needed, but it should not be treated as the semantic definition of Layer 5.

This is why `OpenSearch` is not in the current architecture.

`OpenSearch` is attractive for some retrieval slices, but it is too small a slice of the total system problem to justify another standing service right now.

## No OpenSearch For Now

Make this explicit:

- do not add `OpenSearch` now
- do not design around a standing `OpenSearch` service
- keep the architecture centered on fewer moving pieces

If retrieval pressure later justifies a dedicated search substrate, that can be reconsidered then.

It is not part of the active stack or MVP.

## Dirty-State And Sync Rules

Because Layer 4 is operationally authoritative and Layer 5 is the source-of-record evidence layer, the gap between them must be governed explicitly.

Useful fields include:

- `dirty`
- `pending_redraft`
- `unsynced_to_canonical`
- `redraft_ready`
- `published`

These fields explain whether:

- Layer 4 is ahead of an authored artifact revision
- redraft is needed
- publication is pending
- an authored artifact counterpart exists at all

## Budding Ideas Do Not Jump Straight To Canon

This is a hard architecture rule.

A spark of an idea may begin as a sentence and evolve across many threads.

That should first become:

- a Layer 3 concept relationship network
- a Layer 4 evolving workspace body

It should not immediately become:

- a Layer 5 authored artifact

Layer 5 authored canon is for publication once the work is actually ready.

## Layer 3 Relationship To Layer 4

Layer 3 helps Layer 4 organize itself.

It can help identify:

- that many threads belong to the same emerging concept
- that multiple workspaces should merge
- that a workspace is becoming a promotion candidate
- that certain references support the same operational body

Layer 4 may receive connector fields such as:

- `idea_cluster_id`
- `related_workspace_ids`
- `candidate_for_promotion`
- `promotion_readiness`

The bodies stay in Layer 4.

The semantic relationship network stays in Layer 3.

## Layer 4 To Layer 5 Contract

When Layer 5 evidence exists, the pattern should be:

1. Layer 4 remains the operational working body
2. Layer 3 stores the durable semantic truth and support structure around it
3. Layer 5 stores the source-of-record evidence body
4. pointers and dirty-state rules govern the gap

Layer 4 may reference Layer 5 evidence, but it does not own Layer 5 lifecycle.

## Bottom-Up Canonical Reprocessing Loop

Promotion to a Layer 5 authored artifact is not a one-way archival move.

Once a Layer 4 workspace is promoted, that authored artifact becomes the canonical source for that body.

After that point, meaningful Layer 5 authored revision must be able to trigger:

1. re-ingestion back into Layer 4 so operational knowledge stays aligned with authored canon
2. reconciliation of Layer 3 summaries, support links, supersession, and related semantic structure
3. dirty-state clearing or re-marking depending on whether the canonical revision resolves or deepens the gap

This rule prevents Layer 5 from becoming dead storage.

Authored canon must remain able to update lower operational layers through reprocessing.

## Bottom Line

Layer 4 is the operational knowledge authority.

Layer 5 is the source-of-record evidence layer.

Authored canon is a special Layer 5 class, not the whole layer.

External references, runtime evidence, incubation workspaces, and authored operational bodies all fit cleanly into this model without requiring a sixth layer.
