# Bounded Retrieval

Bounded retrieval is the Cortex rule that memory search must be constrained before it is ranked.

The system does not search the entire memory graph and then hope ranking fixes the result set.

## Retrieval Shape

The expected flow is:

1. resolve explicit dimensions and constraints
2. filter the knowledge set down to eligible objects
3. rank that bounded set with BM25 and other lexical signals
4. apply vector similarity plus confidence and freshness weighting inside that bounded set
5. enforce token-budget limits
6. return a structured knowledge bundle

Eligibility precedes similarity.

## Why It Exists

This model improves precision, keeps retrieval explainable, and reduces the chance that unrelated high-similarity content contaminates runtime context.

Embeddings are a ranking signal only. They do not define truth, structure, or eligibility.

## Output Contract

Cortex returns a knowledge bundle, not a transcript. Orchestration decides how to inject or present that bundle.

## Related Concepts

- [Dimension](dimension.md)
- [Memory Versus Context](memory-vs-context.md)
- [Knowledge Object](knowledge-object.md)
- [Reflection](reflection.md)
- [Architecture](../remram-cortex/architecture.md)
