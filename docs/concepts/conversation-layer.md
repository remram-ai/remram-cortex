# Conversation Layer

The conversation layer is a proposed semantic continuity layer between runtime sessions and durable knowledge objects.

It exists to preserve direction and continuity across sessions without turning Cortex into a transcript store.

## Session Versus Conversation Versus Knowledge

A session is a runtime execution grouping owned by OpenClaw.

A conversation is a semantic continuity object that may span multiple sessions.

A knowledge object is an atomic durable statement or relation owned by Cortex.

## What The Conversation Layer Stores

If adopted, the conversation layer should store dense continuity data such as:

- referenced session identifiers
- a canonical rolling summary
- governance scope, signature, and retrieval metadata such as recency and prominence
- optional links to artifacts or archived continuity state

It should not store full transcripts.

## Why It Exists

Raw transcript persistence does not scale into durable memory. The conversation layer preserves semantic continuity while knowledge objects continue to hold atomic durable facts, constraints, principles, and related memory.

This keeps continuity compaction-agnostic: OpenClaw may compact sessions while Cortex still retains meaning.

## Ownership Boundary

If conversation objects are adopted, they should be durably owned by Cortex.

Orchestration may still provide runtime hints such as:

- continue this thread
- fork into a new thread
- prefer a related prior thread

But durable attachment, merge, and continuity storage should remain Cortex responsibilities.

## Related Concepts

- [Memory Versus Context](memory-vs-context.md)
- [Knowledge Object](knowledge-object.md)
- [Reflection](reflection.md)
- [Dream Cycle](dream-cycle.md)
- [Architecture](../remram-cortex/architecture.md)
