# Dimension

`Dimension` is a legacy Cortex term from earlier drafts.

It used to cover several different ideas at once:

- hard eligibility metadata
- semantic retrieval cues
- sometimes even ranking hints

That overloading made the model harder to reason about.

## Current Split

The current architecture replaces the old umbrella term with two clearer concepts:

- [Governance Fields](governance-fields.md) for hard retrieval eligibility
- [Typed Signals](typed-signals.md) for primary semantic scoring

The [Semantic Signature](semantic-signature.md) then adds a separate soft routing layer on top.

## Why Keep This Page

This page exists so older references to "dimensions" still land somewhere meaningful.

When editing current Cortex docs, prefer the newer terms unless you are explicitly discussing historical drafts.

## Related Concepts

- [Governance Fields](governance-fields.md)
- [Typed Signals](typed-signals.md)
- [Semantic Signature](semantic-signature.md)
- [Bounded Retrieval](bounded-retrieval.md)
