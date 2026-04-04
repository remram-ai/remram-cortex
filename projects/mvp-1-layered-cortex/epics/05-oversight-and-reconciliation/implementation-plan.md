# Implementation Plan

## Objective

Add the trust and hardening layer: oversight, checkpoint review, session-end reconciliation, and nightly consolidation.

## Workstreams

1. Define the oversight model.
   - what is automatically observed
   - what requires review
   - what requires approval or veto
2. Integrate oversight with semantic outputs.
   - default consume boundary-triggered semantic outputs in Phase 1
   - consume the Mamba stream later when available
   - escalate to evidence packages when needed
   - emit review tasks, confidence downgrades, or approval requests
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

- oversight trigger model
- evidence-escalation path
- session-end reconciliation loop
- nightly reconciliation loop
- QMD cleanup rules

## Dependencies

- Phase 1 boundary-triggered semantic processing hooks
- Epic 03 notion and durable-memory state model
- Epic 04 artifact revision and support model

## Exit Criteria

- oversight can observe and intervene on semantic outputs
- tentative memory can be upgraded, downgraded, or rejected at session boundaries
- nightly maintenance can improve trust without changing the authority model

## Notes

- Oversight is a control consumer, not the main memory authority.
- Session-end reconciliation is the main trust boundary for fast cross-thread memory.
