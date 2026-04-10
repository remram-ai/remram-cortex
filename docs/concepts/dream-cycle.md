# Dream

`Dream Cycle` remains an acceptable longer form in older docs.

Prefer `Dream` in active docs.

Dream is the scheduled reconciliation and consolidation pass over accumulated Cortex memory.

Reflection captures local deltas from one run. Dream cleans up and synthesizes the larger knowledge graph over time.

## What Dream Does

Dream is responsible for:

- deduplicating overlapping knowledge objects
- surfacing contradictions instead of hiding them
- consolidating duplicate or low-value retrieval cues
- adjusting confidence based on corroboration, conflict, and recency
- allowing stale or weak knowledge to decay or be demoted over time
- forming higher-order principles from repeated consistent patterns
- identifying artifact-promotion candidates
- reopening low-confidence notions or tentative memory that aged badly
- reconciling stale support when artifacts or evidence packages changed

Dream should improve the quality of retrieval without turning retrieval into a reasoning-heavy live step.

That means it may:

- normalize synonymous signal values
- prune weak signal phrases that never help retrieval
- compress stale continuity summaries
- propose architectural pressure for new signal-field types without changing the hot-path schema automatically

## Why Dream Is Separate

Reconciliation is broader and slower than reflection. Keeping it asynchronous avoids turning normal runtime completion into a global memory maintenance step.

## Related Concepts

- [Reflection](reflection.md)
- [Knowledge Object](knowledge-object.md)
- [Notion](notion.md)
- [Intuition](intuition.md)
- [Typed Signals](typed-signals.md)
- [Artifact Promotion](artifact-promotion.md)
- [Graphiti + Neo4j Durable Memory](../design/graphiti-neo4j-durable-memory.md)
