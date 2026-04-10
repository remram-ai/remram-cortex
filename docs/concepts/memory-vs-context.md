# Memory Versus Context

Memory and context are not the same thing in Cortex.

## Context

Context is the bounded information injected into a live run.

In the current architecture, it is assembled over OpenClaw's Layer 2 session surface and may change from one execution step to the next.

## Memory

Memory is the structured, persistent, evolving Layer 3 knowledge owned by Cortex.

It survives transcript compaction, session resets, and other runtime boundaries.

## Operational Knowledge

Decomposed artifact knowledge is not the same thing as either runtime context or durable memory.

It is part of the Layer 4 operational retrieval surface.

That same Layer 4 surface may also include chronicle bodies, needs workspaces, and other medium-horizon operational continuity bodies.

## Evidence

Layer 5 evidence is not memory either.

It is source-of-record material, not semantic meaning.

Canonical authored artifacts are only one Layer 5 evidence class.

Other common Layer 5 evidence classes are runtime evidence and cached external references.

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
