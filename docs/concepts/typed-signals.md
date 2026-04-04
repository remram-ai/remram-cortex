# Typed Signals

Typed signals are a retained Cortex retrieval concept for structured semantic retrieval.

They are not currently a locked phase-1 implementation commitment for the new layered stack.

If adopted, each knowledge object would emit a small set of retrieval signals into fixed fields, while the values inside those fields remain open natural language.

## Current Signal Fields

The previously favored first-pass signal set was:

- `domain`: what broad world this knowledge lives in
- `activity`: what someone is doing
- `need`: why the knowledge matters or what problem it helps solve
- `object`: what things or resources are involved
- `mechanism`: how the solution or idea works

This field set is intentionally small and slow-changing.

## Why Typed Signals Exist

Typed signals would give the knowledge plane a structured multi-field surface for scoring without forcing Cortex into brittle taxonomies.

They would let Cortex ask:

- does the query match the same domain
- does it involve the same activity
- is it solving the same need
- is it about the same objects
- does it rely on a similar mechanism

That is much more useful than collapsing everything into one untyped blob of keywords.

## Value Rules

If used, signal values should be:

- short natural-language phrases
- multi-value when needed
- open-ended rather than enumerated
- generated during reflection or import based on rediscovery usefulness

The design intent is:

- keep the schema relatively fixed
- let the values evolve

## Why The Field Set Must Stay Small

If Cortex starts inventing new signal types in the hot path, retrieval becomes unstable and queries become harder to debug.

Signal-type changes should be rare architectural decisions, not normal runtime behavior.

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Governance Fields](governance-fields.md)
- [Semantic Signature](semantic-signature.md)
- [Bounded Retrieval](bounded-retrieval.md)
- [Reflection](reflection.md)
