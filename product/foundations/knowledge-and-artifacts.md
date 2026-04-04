# Knowledge And Artifacts

This document defines the stable product posture for Layers 4 and 5.

## Layer 4: Operational Knowledge

Layer 4 is the operational knowledge authority.

It is built around:

- evolving workspaces
- reference summaries and linked records
- decomposed artifact knowledge
- typed slices and retrieval records
- dirty-state and workflow fields
- source-linked and revision-aware operational bodies

The default implementation posture is `Postgres + pgvector`.

Layer 4 is allowed to move quickly, and in many cases it is the only authority for active work.

Layer 4 may hold:

- incubation workspaces with no Layer 5 counterpart yet
- external reference material that should not become canonical Git artifacts
- active operational document state for authored work before publication

Layer 4 must remain:

- source-linked where applicable
- revision-aware where applicable
- explicit about whether a Layer 5 counterpart exists
- explicit about dirty-state and sync posture when a Layer 5 counterpart does exist

## Layer 5: Canonical Artifacts

Layer 5 is the publication-truth layer.

It is built around:

- `Git`
- provider-backed authoritative sources
- reviewed redrafts

## Stable Product Rule

Layer 4 may move ahead of Layer 5 during active work.

That is not an exception.

It is the normal operational posture.

When a Layer 5 counterpart exists, the system must make the gap explicit through:

- the anchor is explicit
- dirty-state tracking is explicit
- publication and re-ingestion are part of the design

Only compact summary + pointer + Layer 3 appropriate beliefs should flow upward into durable memory.

Once a Layer 4 workspace is promoted, Layer 5 becomes the canonical source for that artifact.

After that point, meaningful Layer 5 revisions must be able to:

- trigger re-ingestion into Layer 4
- realign operational knowledge with canonical truth
- reconcile Layer 3 support, summaries, and semantic links as needed

Hard boundary:

- Layer 4 owns operational knowledge bodies
- Layer 3 owns durable semantic truth about those bodies
- Layer 5 owns canonical publication truth only when canonical publication is warranted
