# Knowledge Object

A knowledge object is the primary durable memory unit in Cortex.

It is not a transcript fragment and not a raw tool result. It is an extracted, structured claim or instruction that Cortex is willing to store as memory.

Its identity should remain stable over time even as confidence, provenance, relationships, and promotion state evolve.

## What A Knowledge Object Carries

A knowledge object should carry:

- a canonical statement or structured payload
- a type such as fact, preference, constraint, correction, decision, principle, or procedure
- provenance back to runs, artifacts, or tools
- confidence and freshness metadata
- dimensions used for retrieval eligibility
- relationships to other objects or artifacts
- promotion state when the object becomes a promotion candidate or a promoted artifact source

## How It Changes

Knowledge objects are updated by delta. Reflection may add, revise, relate, strengthen, weaken, or retire them. Dream cycles may later merge duplicates, surface conflicts, or raise principles from repeated patterns.

The model is designed for incremental enrichment over time rather than one-shot schema completion.

Cortex should prefer entity collections plus typed attributes and relations over unconstrained key-path namespaces. Confidence changes ranking and review priority, but it does not directly drive execution behavior.

## What It Is Not

A knowledge object is not:

- a full conversation transcript
- an append-only event log
- an execution record

Those may be evidence, but they are not the memory object itself.

## Related Concepts

- [Knowledge Authority](knowledge-authority.md)
- [Memory Versus Context](memory-vs-context.md)
- [Dimension](dimension.md)
- [Reflection](reflection.md)
- [Dream Cycle](dream-cycle.md)
