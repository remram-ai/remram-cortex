# Artifact Promotion

Artifact promotion is the process of moving stabilized knowledge out of Cortex-only memory and into a durable human-managed document or repository artifact.

Promoted artifacts are derived projections of validated knowledge, not the canonical memory source.

They should be written through a configurable artifact provider so revisions remain reviewable and traceable over time.

Imported source artifacts may live behind that same provider abstraction, but they enter Cortex through [Artifact Intake](artifact-intake.md). Promotion is the reverse direction: validated memory becoming a durable human-facing artifact.

The shared provider model does not imply shared semantics. Imported artifacts are evidence surfaces with preserved provenance. Promoted artifacts are Cortex-authored outputs. Neither should inherit their canonical organization from an external folder tree.

## When Promotion Makes Sense

Promotion is appropriate when the result is:

- stable across multiple runs
- reusable by humans or other systems
- reviewable and worth versioning
- better expressed as a document, spec, or other durable artifact

For collaborative human-readable artifacts, a Google Workspace provider may be the most practical default. For private or workflow-oriented artifacts, a local Git provider may still be preferred.

## Promotion Rule

Not every knowledge object should be promoted. Cortex remains the working memory authority. Promotion is for knowledge that benefits from durable history, review, and explicit reuse.

Promotion target should be chosen by artifact policy, not hardcoded globally.

## After Promotion

Promotion requires review and approval before commit or publish.

Promoted artifacts should be linked back to their originating knowledge and reindexed into Cortex as higher-authority document sources.

If the linked knowledge changes later, Dream may redraft the artifact and update the provider copy so the artifact surface remains synchronized with the evolved knowledge graph.

If the provider supports watchable collaborative edits, human changes may trigger re-ingestion or reconciliation back into Cortex rather than silently drifting away from the knowledge graph.

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Artifact Intake](artifact-intake.md)
- [Artifact Provider](artifact-provider.md)
- [Reflection](reflection.md)
- [Dream Cycle](dream-cycle.md)
