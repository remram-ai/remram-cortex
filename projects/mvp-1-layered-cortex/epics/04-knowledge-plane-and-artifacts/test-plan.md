# Test Plan

## Core Scenarios

1. Incubation workspaces can exist in Layer 4 without requiring a Layer 5 artifact.
2. External reference material can live in Layer 4 without becoming canonical Git content.
3. Decomposed artifact knowledge remains revision-aware when a canonical artifact does exist.
4. Dirty-state tracking marks anchors when operational knowledge outruns canonical revisions.
5. Publication and re-ingestion realign Layer 4 and Layer 5 when canon is warranted.
6. Once canon exists, meaningful Layer 5 revision can trigger bottom-up reprocessing into Layer 4 and Layer 3 reconciliation.

## Failure Checks

- full artifact bodies should not be copied into Layer 3 as memory
- revision changes should invalidate stale support where appropriate
- publication should not be implicit or hidden
- the system should not force every Layer 4 record into Git

## Evidence Of Completion

- one incubation workspace lifecycle with no canonical artifact
- one external reference lifecycle with summaries and retrieval records
- one artifact lifecycle from canonical source to operational knowledge to redraft
- one re-ingestion pass after canonical revision update
- one bottom-up canonical reprocessing case after a meaningful Layer 5 revision
