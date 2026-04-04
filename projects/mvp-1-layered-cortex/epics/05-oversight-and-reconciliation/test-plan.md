# Test Plan

## Core Scenarios

1. Oversight consumes semantic checkpoints and flags suspicious changes.
2. High-impact or low-confidence candidates escalate to evidence-backed review.
3. Session-end reconciliation resolves tentative QMD notions correctly.
4. Reflection keeps QMD lean through prune, merge, demote, and expire behavior.
5. Nightly reconciliation improves trust through merge, supersession, or invalidation.
6. Dream-like maintenance uses Layer 3 relationships to identify Layer 4 grouping and promotion candidates.

## Failure Checks

- oversight should not silently become the memory authority
- approval-sensitive changes should not bypass review
- nightly maintenance should not break provenance links

## Evidence Of Completion

- one oversight-triggered review case
- one session-end promotion or rejection case
- one QMD cleanup case
- one nightly consolidation or stale-support cleanup case
