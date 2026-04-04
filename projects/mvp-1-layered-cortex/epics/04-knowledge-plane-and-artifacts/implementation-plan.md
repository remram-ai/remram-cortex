# Implementation Plan

## Objective

Stand up Layer 4 operational knowledge and Layer 5 canonical artifact flow without collapsing active work into publication truth.

## Workstreams

1. Define the anchor and revision model.
   - stable anchor identity
   - revision linkage
   - dirty-state and publication status
2. Build Layer 4 operational knowledge in `Postgres + pgvector`.
   - incubation workspaces
   - external reference records and summaries
   - decomposed artifact knowledge where canonical artifacts exist
   - source locators, embeddings, lexical fields, and retrieval payloads
3. Establish Layer 5 canonical artifact flow.
   - `Git` or provider-backed canonical source
   - publication and redraft loop
   - re-ingestion after revision changes
4. Connect artifacts to Layer 3 correctly.
   - summary plus pointer into durable memory
   - Layer 3 appropriate standalone beliefs only
   - stale-support detection when revisions change
5. Preserve bottom-up canonical reprocessing.
   - once promoted, Layer 5 becomes the canonical source
   - meaningful canonical revisions re-ingest into Layer 4
   - Layer 3 summaries, support, and semantic links reconcile afterward

## Deliverables

- anchor and revision contract
- Layer 4 operational workspace and knowledge schema
- canonical artifact flow and dirty-state model
- re-ingestion path back from Layer 5 into Layer 4 and Layer 3 support
- explicit bottom-up canonical reprocessing contract

## Dependencies

- evidence package model
- Layer 3 support and reconciliation posture

## Exit Criteria

- artifacts have stable anchor and revision identity
- Layer 4 operational knowledge stays source-linked and revision-aware where applicable
- Layer 5 remains canonical publication truth

## Notes

- Layer 4 is allowed to move ahead of Layer 5.
- Not every Layer 4 record should have a Layer 5 counterpart.
- That freedom is only acceptable when anchor identity, re-ingestion, and dirty-state tracking are explicit.
- Once Layer 5 exists, it must remain a live canonical source rather than dead storage.
