# Implementation Plan

## Objective

Stand up Layer 4 operational knowledge and the Layer 5 evidence lifecycle without collapsing active work into publication truth.

## Workstreams

1. Define the anchor and evidence model.
   - stable anchor identity
   - revision linkage
   - evidence-class distinctions
   - later dirty-state and publication status
2. Build the Phase 1 Layer 4 support surface in `Postgres + pgvector`.
   - chat-derived summaries
   - concept support bodies
   - fact and belief candidates
   - retrieval and pointer records
3. Add one-way reference decomposition.
   - incubation workspaces
   - external reference records and summaries
   - decomposed knowledge from attached docs and web snapshots
   - source locators, embeddings, lexical fields, and retrieval payloads
4. Add owned-source maintenance and dirty-state semantics.
   - current version versus derived version
   - diff and reconciliation surface
   - reprocessing after owned-source changes
5. Establish authored artifact promotion in `Git`.
   - Git-backed canonical source
   - publication and redraft loop
   - re-ingestion after revision changes
6. Connect Layer 4 and Layer 5 artifacts to Layer 3 correctly.
   - summary plus pointer into durable memory
   - Layer 3 appropriate standalone beliefs only
   - stale-support detection when revisions change
7. Preserve bottom-up canonical reprocessing.
   - once promoted, Layer 5 becomes the canonical source
   - meaningful canonical revisions re-ingest into Layer 4
   - Layer 3 summaries, support, and semantic links reconcile afterward

## Deliverables

- anchor and revision contract
- Layer 4 operational workspace and knowledge schema
- reference-decomposition path
- owned-source maintenance and dirty-state model
- authored artifact flow in `Git`
- re-ingestion path back from Layer 5 into Layer 4 and Layer 3 support
- explicit bottom-up canonical reprocessing contract

## Dependencies

- evidence package model
- Layer 3 support and reconciliation posture

## Exit Criteria

- Layer 4 operational knowledge stays source-linked and revision-aware where applicable
- Layer 5 evidence classes remain explicit
- authored canon is introduced only in the promotion phase
- canonical authored revisions can drive reprocessing back into Layer 4 and Layer 3

## Notes

- Layer 4 is allowed to move ahead of Layer 5.
- Not every Layer 4 record should have a Layer 5 counterpart.
- That freedom is only acceptable when anchor identity, re-ingestion, and dirty-state tracking are explicit.
- Once Layer 5 exists, it must remain a live canonical source rather than dead storage.
