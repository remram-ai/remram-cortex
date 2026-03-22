# Typed Signals

Typed signals are Cortex's primary semantic retrieval surface.

Each knowledge object emits a small set of retrieval signals into fixed fields, while the values inside those fields remain open natural language.

## Current Signal Fields

The current first-pass signal set is:

- `domain`: what broad world this knowledge lives in
- `activity`: what someone is doing
- `need`: why the knowledge matters or what problem it helps solve
- `object`: what things or resources are involved
- `mechanism`: how the solution or idea works

This field set is intentionally small and slow-changing.

## Why Typed Signals Exist

Typed signals give OpenSearch a structured multi-field surface for scoring without forcing Cortex into brittle taxonomies.

They let Cortex ask:

- does the query match the same domain
- does it involve the same activity
- is it solving the same need
- is it about the same objects
- does it rely on a similar mechanism

That is much more useful than collapsing everything into one untyped blob of keywords.

## Value Rules

Signal values should be:

- short natural-language phrases
- multi-value when needed
- open-ended rather than enumerated
- generated during reflection or import based on rediscovery usefulness

The schema is fixed.
The values evolve.

## Why The Field Set Must Stay Small

If Cortex starts inventing new signal types in the hot path, retrieval becomes unstable and queries become harder to debug.

Signal-type changes should be rare architectural decisions, not normal runtime behavior.

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Governance Fields](governance-fields.md)
- [Semantic Signature](semantic-signature.md)
- [Bounded Retrieval](bounded-retrieval.md)
- [Reflection](reflection.md)
