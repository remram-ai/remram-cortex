# Knowledge Object

A knowledge object is the primary technical durable memory unit in Cortex.

`Memory` is the generic term. `Knowledge object` is the concrete stored record Cortex uses to hold that memory.

It is not a transcript fragment and not a raw tool result. It is an extracted, structured claim or instruction that Cortex is willing to store as memory.

Its identity should remain stable over time even as confidence, provenance, relationships, and promotion state evolve.

## What A Knowledge Object Carries

A knowledge object should carry:

- a canonical statement or structured payload
- an optional short summary when the memory needs a compact gloss
- a type such as fact, preference, constraint, correction, decision, principle, or procedure
- provenance back to runs, artifacts, or tools, including source-location detail where available
- governance fields used for hard eligibility, such as ownership, visibility, scope, and lifecycle state
- typed signal fields used for primary semantic retrieval
- a semantic signature used for soft routing bias
- confidence, freshness, and reinforcement metadata such as reference count or strength
- relationships to other objects or artifacts
- promotion state when the object becomes a promotion candidate or a promoted artifact source

## How It Changes

Knowledge objects are updated by delta. Reflection may add, revise, relate, strengthen, weaken, retire, supersede, contradict, generalize, or specialize them. Dream cycles may later merge duplicates, normalize retrieval cues, raise principles from repeated patterns, or prune weak low-value imports.

One source artifact may reinforce many knowledge objects. One knowledge object may accumulate support from many sessions, tools, or artifacts.

The model is designed for incremental enrichment over time rather than one-shot schema completion.

Cortex should prefer one canonical object with many retrieval paths over duplicate copies filed into different buckets. Groupings, clusters, and project views may be derived later, but the object itself remains primary.

For imported artifacts, bounded chunking may be used to parse large sources. That chunking is an ingestion tactic, not a second durable type below the knowledge object.

## What It Is Not

A knowledge object is not:

- a full conversation transcript
- an append-only event log
- an execution record
- an opaque imported file blob

Those may be evidence, but they are not the memory object itself.

## Related Concepts

- [Knowledge Authority](knowledge-authority.md)
- [Artifact Intake](artifact-intake.md)
- [Memory Versus Context](memory-vs-context.md)
- [Governance Fields](governance-fields.md)
- [Semantic Signature](semantic-signature.md)
- [Typed Signals](typed-signals.md)
- [Reflection](reflection.md)
- [Dream Cycle](dream-cycle.md)
