# Test Plan

## Core Scenarios

1. Artifact decomposition remains revision-aware.
2. Layer 4 slices preserve source locators back to the canonical artifact.
3. Dirty-state tracking marks anchors when operational knowledge outruns canonical revisions.
4. Publication and re-ingestion realign Layer 4 and Layer 5.

## Failure Checks

- full artifact bodies should not be copied into Layer 3 as memory
- revision changes should invalidate stale support where appropriate
- publication should not be implicit or hidden

## Evidence Of Completion

- one artifact lifecycle from canonical source to decomposition to redraft
- one re-ingestion pass after canonical revision update
