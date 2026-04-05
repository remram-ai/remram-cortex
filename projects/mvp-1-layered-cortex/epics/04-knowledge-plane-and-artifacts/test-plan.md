# Test Plan

## Core Scenarios

1. Chat-derived Layer 4 support bodies can exist without requiring an authored Layer 5 artifact.
2. External reference material can live in Layer 4 without becoming authored Git content.
3. Owned-source documents can introduce dirty-state dual-version semantics without becoming authored canon immediately.
4. Decomposed knowledge remains revision-aware when an authored artifact does exist.
5. Publication and re-ingestion realign Layer 4 and Layer 5 when authored canon is warranted.
6. Once authored canon exists, meaningful Layer 5 revision can trigger bottom-up reprocessing into Layer 4 and Layer 3 reconciliation.

## Failure Checks

- full artifact bodies should not be copied into Layer 3 as memory
- revision changes should invalidate stale support where appropriate
- publication should not be implicit or hidden
- the system should not force every Layer 4 record into Git

## Evidence Of Completion

- one chat-derived support-body lifecycle with no authored artifact
- one external reference lifecycle with summaries and retrieval records
- one owned-source maintenance lifecycle with dirty-state and reprocessing
- one artifact lifecycle from canonical source to operational knowledge to redraft
- one re-ingestion pass after canonical revision update
- one bottom-up canonical reprocessing case after a meaningful Layer 5 revision
