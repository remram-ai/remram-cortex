# Artifact Promotion

Artifact promotion is the process of moving stabilized knowledge out of Cortex-only memory and into a durable human-managed document or repository artifact.

Promoted artifacts are derived projections of validated knowledge, not the canonical memory source.

They should live in a local Git-backed artifact store so revisions remain reviewable and traceable over time.

## When Promotion Makes Sense

Promotion is appropriate when the result is:

- stable across multiple runs
- reusable by humans or other systems
- reviewable and worth versioning
- better expressed as a document, spec, or other durable artifact

## Promotion Rule

Not every knowledge object should be promoted. Cortex remains the working memory authority. Promotion is for knowledge that benefits from Git-backed history, review, and explicit reuse.

## After Promotion

Promotion requires review and approval before commit.

Promoted artifacts should be linked back to their originating knowledge and reindexed into Cortex as higher-authority document sources.

If the linked knowledge changes later, Dream may redraft the artifact and commit a new version so the artifact store remains synchronized with the evolved knowledge graph.

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Reflection](reflection.md)
- [Dream Cycle](dream-cycle.md)
