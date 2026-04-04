# Implementation Plan

## Objective

Add the trust and hardening layer through checkpoint review, session-end reconciliation, nightly consolidation, and later Intuition when Mamba exists.

## Workstreams

1. Finalize the reconciliation model.
   - what is automatically reconciled
   - what remains tentative
   - what requires stronger evidence before trust elevation
2. Define Intuition as a later Mamba-side evaluator.
   - consume the Mamba stream later when available
   - decide when hotter layered ingestion should wake
   - route high-signal windows into reflection or notion updates
   - leave deeper review to evidence-backed downstream work
3. Finalize session-end reconciliation.
   - close evidence packages
   - resolve tentative QMD notions
   - update Layer 3 trust state
4. Finalize nightly reconciliation and Dream-like maintenance.
   - deduplication
   - contradiction checks
   - stale-support cleanup
   - higher-confidence consolidation
   - Layer 3 assisted grouping of Layer 4 workspaces
   - promotion candidate detection
5. Add reflection-side QMD cleanup.
   - prune low-value notions
   - merge notion duplicates
   - demote stale notions
   - keep QMD lean and fast

## Deliverables

- Intuition trigger model
- evidence-escalation path for deeper review
- session-end reconciliation loop
- nightly reconciliation loop
- QMD cleanup rules

## Dependencies

- Phase 1 boundary-triggered semantic processing hooks
- Epic 03 notion and durable-memory state model
- Epic 04 artifact revision and support model

## Exit Criteria

- tentative memory can be upgraded, downgraded, or rejected at session boundaries
- nightly maintenance can improve trust without changing the authority model
- Intuition is clearly defined as a later Mamba-gated evaluator rather than a base architecture module

## Notes

- Intuition is not part of the base Phase 1 proof surface.
- Session-end reconciliation is the main trust boundary for fast cross-thread memory.
