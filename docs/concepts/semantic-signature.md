# Semantic Signature

A semantic signature is a compact 16-32 bit routing code attached to a knowledge object and generated for a query.

It is Cortex's coarse semantic partitioning layer.

## What It Does

The signature answers a limited question:

"What kind of thing is this, in a very compressed way?"

It helps Cortex:

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

The signature should be used as a soft routing or score-bias signal.

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
