# Governance Fields

Governance fields are the hard-bounding retrieval fields in Cortex.

They decide whether a knowledge object is even eligible for a query before semantic scoring begins.

## What Governance Fields Do

Governance fields exist to enforce:

- ownership and audience boundaries
- project, household, family, person, provider, or system scope
- role, visibility, or approval boundaries in multi-party systems
- lifecycle state such as active, retired, or superseded
- temporal validity windows and freshness constraints
- other exact or bounded policy filters that should exclude an object entirely

These fields are not meant to describe everything a memory is about.

They exist to keep the candidate set safe and bounded before ranking.

## What Governance Fields Are Not

Governance fields are not:

- open-ended topic tags
- semantic descriptors
- vector axes
- a replacement for full-text or embedding search

If a field needs an unbounded vocabulary to stay useful, it probably belongs in a typed signal field instead.

## Multi-Party Rule

Governance fields are where Cortex keeps multi-party retrieval safe.

If a product needs distinctions such as:

- self versus family
- family versus caregiver
- trusted helper versus provider
- visible versus private
- editable versus review-only

those distinctions belong in governance, not in semantic ranking.

## Why They Matter

Without governance fields, semantically similar but wrong-scope memory leaks into retrieval.

Cortex needs exact or bounded filters for ownership, visibility, and lifecycle before any lexical or vector score is allowed to matter.

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Semantic Signature](semantic-signature.md)
- [Typed Signals](typed-signals.md)
- [Bounded Retrieval](bounded-retrieval.md)
- [Layered Memory Architecture](../design/layered-memory-architecture.md)
