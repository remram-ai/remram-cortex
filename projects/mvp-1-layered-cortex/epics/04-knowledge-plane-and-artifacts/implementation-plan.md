# Implementation Plan

## Objective

Stand up Layer 4 decomposed artifact knowledge and Layer 5 canonical artifact flow without collapsing operational slices into publication truth.

## Workstreams

1. Define the anchor and revision model.
   - stable anchor identity
   - revision linkage
   - dirty-state and publication status
2. Build Layer 4 decomposition in `Postgres + pgvector`.
   - typed slices
   - source locators
   - embeddings and lexical fields
   - retrieval-ready payloads
3. Establish Layer 5 canonical artifact flow.
   - `Git` or provider-backed canonical source
   - publication and redraft loop
   - re-ingestion after revision changes
4. Connect artifacts to Layer 3 correctly.
   - summary plus pointer into durable memory
   - Layer 3 appropriate standalone beliefs only
   - stale-support detection when revisions change

## Deliverables

- anchor and revision contract
- Layer 4 decomposition schema
- canonical artifact flow and dirty-state model
- re-ingestion path back from Layer 5 into Layer 4 and Layer 3 support

## Dependencies

- evidence package model
- Layer 3 support and reconciliation posture

## Exit Criteria

- artifacts have stable anchor and revision identity
- Layer 4 retrieval objects stay source-linked and revision-aware
- Layer 5 remains canonical publication truth

## Notes

- Layer 4 is allowed to move ahead of Layer 5.
- That freedom is only acceptable when re-ingestion and dirty-state tracking are explicit.
