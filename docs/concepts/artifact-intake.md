# Artifact Intake

Artifact intake is the multimodal evidence path that turns external documents and images into Cortex memory.

It gives Cortex one consistent entry point for imported artifacts instead of treating every upload as an opaque attachment.

## Intake Flow

Artifact intake should:

- store the original artifact in a local Git-backed artifact store
- run an Artifact Parser over the source to extract structure and meaning
- emit a summary, highlights, and bounded source-linked import slices
- deduplicate those slices against existing memory
- create or reinforce knowledge objects from the resulting evidence
- index the resulting memory and intake metadata in OpenSearch

A Qwen-VL-class model is a likely fit for the first Artifact Parser profile because the same intake path should be able to read both documents and images.

The parser may use chunking internally to keep large artifacts bounded. Those chunks are not a second durable memory tier. The durable Cortex record remains the knowledge object created or updated by each source-linked slice.

## Why Source Location Matters

Each imported slice should carry source references such as:

- `artifact_id`
- page, section, frame, or region
- character or offset range when available

This keeps memory traceable, reviewable, and updatable when the source artifact changes.

## Storage Boundary

- the Git-backed artifact store keeps the original imported file
- OpenSearch keeps knowledge objects, retrieval indexes, and intake metadata
- Cortex remains the only mutation authority over durable memory

Imported artifacts are evidence. Promoted artifacts are derived human-facing outputs. Both may live in the Git-backed store, but they enter the system through different workflows.

## Retention And Pruning

Not every imported artifact deserves permanence.

Dream or other REM routines may:

- prune artifacts that produced no durable reused memory
- retire weak import-only knowledge objects
- keep a lightweight retained record with summary and provenance when the original file should no longer stay resident

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Bootstrap Ingestion](bootstrap-ingestion.md)
- [Reflection](reflection.md)
- [Dream Cycle](dream-cycle.md)
- [Artifact Promotion](artifact-promotion.md)
- [Architecture](../remram-cortex/architecture.md)
