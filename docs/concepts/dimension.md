# Dimension

A dimension is a hard-bounding retrieval axis in Cortex.

Dimensions are used to decide whether a knowledge object is even eligible for a query before semantic ranking begins.

## Typical Dimensions

Initial dimensions are expected to cover:

- person or subject
- workspace, tenant, or organization scope
- repository, project, or feature scope
- domain or topic scope
- environment or deployment scope
- knowledge or artifact type
- time horizon or recency class

## Dimension Versus Tag

A dimension is not just descriptive metadata.

A tag may be useful for annotation. A dimension affects eligibility and can exclude an object from retrieval entirely.

## Promotion Rule

New dimensions should start as candidates. They may emerge during reflection, but they only become canonical during dream reconciliation when they are stable, reused across queries, and improve retrieval quality without fragmenting the memory space.

Dimensions are structured metadata fields, not vector axes.

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Memory Versus Context](memory-vs-context.md)
- [Bounded Retrieval](bounded-retrieval.md)
- [Architecture](../remram-cortex/architecture.md)
