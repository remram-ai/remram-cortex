# Implementation Plan

## Objective

Stand up Layer 3 durable memory with `Graphiti + Neo4j`, including reconciliation from `QMD` notions, tentative cross-thread memory, and promotion into trusted durable memory.

## Workstreams

1. Bring up the Layer 3 runtime.
   - `Neo4j` deployment and connection posture
   - `Graphiti` service configuration
   - evidence package to episode mapping
2. Define the durable-memory trust model.
   - QMD notion input shape
   - tentative and low-confidence states
   - active, superseded, invalidated, and stale-support states
3. Implement bounded Graphiti episode packaging.
   - summary
   - pointer to evidence or canonical revision
   - only Layer 3 appropriate beliefs or support
4. Implement reconciliation.
   - session-end or checkpoint promotion
   - merge, downgrade, reject, or supersede
   - artifact-support-aware invalidation

## Deliverables

- running `Graphiti + Neo4j` Layer 3 environment
- Layer 3 trust-state and promotion rules
- episode packaging contract
- reconciliation flow for tentative cross-thread memory

## Dependencies

- Epic 02 semantic checkpoint stream
- evidence package model

## Exit Criteria

- high-signal QMD notions can appear cross-thread as tentative memory
- reconciliation can promote, merge, or reject them
- Graphiti receives bounded evidence packages instead of raw log dumps

## Notes

- Layer 3 is the semantic authority, not the evidence store.
- Bulk historical ingest should be treated carefully where invalidation correctness matters.
