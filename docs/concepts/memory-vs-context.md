# Memory Versus Context

Memory and context are not the same thing in Cortex.

## Context

Context is the bounded information injected into a live run. It is assembled for prompt construction and may change from one execution step to the next.

## Memory

Memory is the structured, persistent, evolving knowledge owned by Cortex. It survives transcript compaction, session resets, and other runtime boundaries.

## Why The Distinction Matters

If prompt context is treated as memory, the system starts confusing transient runtime state with durable knowledge. Cortex prevents that drift by keeping memory structured and by retrieving only bounded bundles into context when needed.

## Related Concepts

- [Knowledge Authority](knowledge-authority.md)
- [Knowledge Object](knowledge-object.md)
- [Bounded Retrieval](bounded-retrieval.md)
- [Architecture](../remram-cortex/architecture.md)
