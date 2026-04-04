# Memory Versus Context

Memory and context are not the same thing in Cortex.

## Context

Context is the bounded information injected into a live run.

In the current architecture, it is assembled over OpenClaw's Layer 2 session surface and may change from one execution step to the next.

## Memory

Memory is the structured, persistent, evolving Layer 3 knowledge owned by Cortex.

It survives transcript compaction, session resets, and other runtime boundaries.

## Decomposed Knowledge

Decomposed artifact knowledge is not the same thing as either runtime context or durable memory.

It is the Layer 4 operational retrieval surface.

## Canonical Artifacts

Canonical artifacts are not memory either.

They are Layer 5 ground truth.

## Why The Distinction Matters

If prompt context is treated as memory, the system starts confusing transient runtime state with durable knowledge.

If decomposed operational knowledge is treated as canonical truth, the system starts confusing derived slices with source authority.

Cortex prevents that drift by keeping the layers separate and by retrieving only bounded bundles into runtime context when needed.

## Related Concepts

- [Knowledge Authority](knowledge-authority.md)
- [Knowledge Object](knowledge-object.md)
- [Bounded Retrieval](bounded-retrieval.md)
- [High-Signal Mamba Stream](high-signal-mamba-stream.md)
- [Layered Memory Architecture](../design/layered-memory-architecture.md)
