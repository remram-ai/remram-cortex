# Knowledge And Artifact Architecture

This document defines the locked relationship between Layer 4 and Layer 5.

## Core Rule

Layer 4 is the operational knowledge authority.

Layer 5 is the canonical publication authority when canon is actually warranted.

That is the central clarification in this design pass.

## Layer 4: Operational Knowledge Authority

Layer 4 is not merely a projection of canonical artifacts.

It is authoritative for operational content.

That means:

- if there is no Layer 5 artifact, Layer 4 is the authority for that content
- if there is a Layer 5 artifact, Layer 4 is still the authority for active work and retrieval
- Layer 5 becomes relevant when publication-grade canon is required

Layer 4 should hold:

- incubation workspaces
- working synthesis bodies
- reference-derived knowledge bodies
- decomposed artifact knowledge
- active operational document state
- retrieval-ready operational bodies

## Layer 4 Content Classes

Layer 4 should explicitly support at least three content classes:

### 1. Working Or Incubation Workspaces

These are the medium-horizon operational bodies that may span many threads.

They are:

- incomplete
- unstable
- evolving
- operationally authoritative

They are not bugs in the architecture.

They are a core problem the architecture is explicitly solving.

### 2. External Reference Material

External materials are distinct from authored canonical artifacts.

Examples:

- uploaded PDFs used for reference
- podcast transcripts
- external articles
- factual sources
- research materials the user does not own

These should not automatically become Git-backed canonical artifacts.

Instead, Layer 4 may hold:

- summaries
- linked reference records
- extracted operational knowledge
- retrieval-ready material

Layer 3 stores only the durable meaning that matters.

### 3. Authored Artifact Knowledge

These are operational bodies connected to things that may eventually become canonical artifacts.

Examples:

- business-plan workspaces
- draft product direction notes
- evolving dossiers
- authored synthesis documents

These may later promote into Layer 5 when canonical publication becomes warranted.

## Layer 5: Canonical Publication Truth

Layer 5 exists for publication-grade canonical artifacts.

It is not the default destination for every useful idea.

It should hold:

- Git-backed canonical artifacts
- provider-backed canonical records when appropriate
- reviewable published bodies
- canonical revision history

Layer 5 is used only when canonical authorship and revision really matter.

## Postgres Role

`Postgres` is the operational middle-layer authority for now.

It should cover:

- runtime evidence authority
- Layer 4 workspace bodies
- reference summaries and links
- decomposed artifact knowledge
- retrieval metadata
- workflow fields
- dirty-state and sync tracking

This is why `OpenSearch` is not in the current architecture.

`OpenSearch` is attractive for some retrieval slices, but it is too small a slice of the total system problem to justify another standing service right now.

## No OpenSearch For Now

Make this explicit:

- do not add `OpenSearch` now
- do not design around a standing `OpenSearch` service
- keep the architecture centered on fewer moving pieces

If artifact retrieval ever becomes dominant enough to justify a dedicated search substrate later, that can be reconsidered then.

It is not part of the active stack or MVP.

## Dirty-State And Sync Rules

Because Layer 4 is operationally authoritative and Layer 5 is canon only when applicable, the gap between them must be governed explicitly.

Useful fields include:

- `dirty`
- `pending_redraft`
- `unsynced_to_canonical`
- `redraft_ready`
- `published`

These fields explain whether:

- Layer 4 is ahead of Layer 5
- redraft is needed
- publication is pending
- Layer 5 exists at all

## Budding Ideas Do Not Jump Straight To Git

This is a hard architecture rule.

A spark of an idea may begin as a sentence and evolve across many threads.

That should first become:

- a Layer 3 concept relationship network
- a Layer 4 evolving workspace body

It should not immediately become:

- a Git-backed canonical artifact

Layer 5 is for canonical publication once the work is actually ready.

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

## Canonical Artifact Pattern

When a Layer 5 artifact exists, the pattern should be:

1. Layer 4 remains the operational working body
2. Layer 3 stores the durable semantic truth and support structure around it
3. Layer 5 stores the canonical publication body
4. dirty-state and sync rules govern the gap

## Bottom-Up Canonical Reprocessing Loop

Promotion to Layer 5 is not a one-way archival move.

Once a Layer 4 workspace is promoted, Layer 5 becomes the canonical source for that artifact.

After that point, meaningful Layer 5 revision must be able to trigger:

1. re-ingestion back into Layer 4 so operational knowledge stays aligned with canonical truth
2. reconciliation of Layer 3 summaries, support links, supersession, and related semantic structure
3. dirty-state clearing or re-marking depending on whether the canonical revision resolves or deepens the gap

This rule prevents Layer 5 from becoming dead storage.

Canonical artifacts must remain able to update lower operational layers through reprocessing.

## Bottom Line

Layer 4 is the operational knowledge authority.

Layer 5 is canonical publication truth only when applicable.

External references, incubation workspaces, and authored operational bodies all belong first-class inside Layer 4, without requiring a sixth layer.
