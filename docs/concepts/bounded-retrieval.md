# Bounded Retrieval

Bounded retrieval is the Cortex rule that memory search must be constrained before it is ranked.

The system does not search the entire memory graph and then hope ranking fixes the result set.

## Retrieval Shape

The expected flow is:

1. resolve scope, ownership, and other governance constraints
2. filter the knowledge set down to eligible objects using governance fields
3. bias or preselect with semantic signature similarity
4. score the bounded set across typed signal fields with lexical search
5. optionally boost recall with vector similarity inside that already-bounded set
6. enrich with relationship expansion and rerank using confidence, freshness, and reinforcement
7. enforce token-budget and bundle-shape limits
8. return a structured knowledge bundle plus an inspectable retrieval trace when needed

Eligibility precedes similarity.

## Why It Exists

This model improves precision, keeps retrieval explainable, and reduces the chance that unrelated high-similarity content contaminates runtime context.

Embeddings are a ranking signal only. They do not define truth, structure, or eligibility.

The expensive work should already have happened during reflection and Dream. Retrieval is where Cortex cashes in that prior work, not where it tries to rediscover memory structure from scratch.

## Output Contract

Cortex returns a knowledge bundle, not a transcript. Orchestration decides how to inject or present that bundle.

## Related Concepts

- [Governance Fields](governance-fields.md)
- [Semantic Signature](semantic-signature.md)
- [Typed Signals](typed-signals.md)
- [Memory Versus Context](memory-vs-context.md)
- [Knowledge Object](knowledge-object.md)
- [Reflection](reflection.md)
- [Layered Memory Architecture](../design/layered-memory-architecture.md)
