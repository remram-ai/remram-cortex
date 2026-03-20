# Knowledge Authority

The knowledge authority is the system layer that decides what counts as durable memory.

In Remram, Cortex is that layer.

## What Cortex Owns

Cortex owns:

- structured memory
- semantic retrieval over that memory
- reflection that extracts knowledge from runtime evidence
- dream-cycle reconciliation across accumulated knowledge
- the only authoritative retrieval surface for durable Remram memory
- the only mutation path for durable knowledge objects

## What Cortex Does Not Own

Cortex does not own:

- execution
- runtime packaging
- behavior or prompt policy

OpenClaw executes. Orchestration decides behavior. Cortex remembers.

## Why This Boundary Matters

Without a single memory authority, transcripts, prompts, and runtime state get confused with actual knowledge. Cortex prevents that drift by making extracted knowledge objects the default durable memory unit inside the broader concept of memory.

All durable semantic recall flows through Cortex. Other runtime memory features may exist as implementation details, and storage backends such as Git or OpenSearch may hold originals or indexes, but they do not become competing knowledge authorities or mutation paths.

Cortex is also not a vector store that defines truth. Vectors help rank knowledge during retrieval, but structure, dimensions, provenance, and confidence still govern memory.

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Memory Versus Context](memory-vs-context.md)
- [Reflection](reflection.md)
- [Dream Cycle](dream-cycle.md)
- [Architecture](../remram-cortex/architecture.md)
