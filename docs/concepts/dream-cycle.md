# Dream Cycle

A dream cycle is the scheduled reconciliation and consolidation pass over accumulated Cortex memory.

Reflection captures local deltas from one run. Dream cycles clean up and synthesize the larger knowledge graph over time.

## What Dream Cycles Do

Dream cycles are responsible for:

- deduplicating overlapping knowledge objects
- surfacing contradictions instead of hiding them
- adjusting confidence based on corroboration, conflict, and recency
- allowing stale or weak knowledge to decay or be demoted over time
- forming higher-order principles from repeated consistent patterns
- promoting stable candidate dimensions into canonical ones
- identifying artifact-promotion candidates

## Why Dream Cycles Are Separate

Reconciliation is broader and slower than reflection. Keeping it asynchronous avoids turning normal runtime completion into a global memory maintenance step.

## Related Concepts

- [Reflection](reflection.md)
- [Knowledge Object](knowledge-object.md)
- [Artifact Promotion](artifact-promotion.md)
- [Architecture](../remram-cortex/architecture.md)
