# Semantic Signature

A semantic signature is a retained Cortex retrieval concept for coarse semantic routing.

It is not currently a locked phase-1 implementation commitment.

If adopted later, it would act as a compact routing code attached to a knowledge object and generated for a query.

## What It Does

The signature would answer a limited question:

"What kind of thing is this, in a very compressed way?"

It could help Cortex:

- bias retrieval toward the right semantic region
- cheaply preselect candidates before deeper scoring
- provide a stable routing hint for Dream and other maintenance flows

## What It Does Not Do

A semantic signature is not:

- a hard filter by exact equality
- a replacement for signal matching
- a source of memory truth
- expressive enough to identify named things on its own

Two different memories may share the same signature and still need typed signals, text matching, and links to distinguish them.

## Retrieval Role

If adopted, the signature should be used as a soft routing or score-bias signal.

Typical behavior:

- lower Hamming distance between query and object signatures boosts relevance
- far signatures are less preferred but not impossible

If signature matching becomes a strict gate, recall will collapse.

## Related Concepts

- [Governance Fields](governance-fields.md)
- [Typed Signals](typed-signals.md)
- [Bounded Retrieval](bounded-retrieval.md)
- [Reflection](reflection.md)
- [Layered Memory Architecture](../design/layered-memory-architecture.md)
