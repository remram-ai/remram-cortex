# Artifact Intake

Artifact intake is the multimodal evidence path that turns external documents and images into Cortex evidence, decomposed knowledge, and eventually durable memory where appropriate.

It gives Cortex one consistent entry point for imported artifacts instead of treating every upload as an opaque attachment.

After intake, Cortex should own the artifact record even when the backing provider is external. The original external location may remain in provenance, but it is not the authoritative organization or identity surface inside Cortex.

## Intake Flow

Artifact intake should:

- create or update a Cortex-managed artifact record and assign a stable internal `artifact_id`
- run an Artifact Parser over the source to extract structure and meaning
- emit a summary, highlights, and bounded source-linked import slices
- deduplicate those slices against existing memory and existing decomposition
- create or reinforce Layer 3 appropriate knowledge from the resulting evidence
- index the resulting decomposition and intake metadata in the knowledge plane

A Qwen-VL-class model is a likely fit for the first Artifact Parser profile because the same intake path should be able to read both documents and images.

The parser may use chunking internally to keep large artifacts bounded. Those chunks are not a second durable memory tier. The durable Cortex record remains the knowledge object created or updated by each source-linked slice.

Context-aware chunking and related RAG ingestion strategies are most relevant here. They help preserve document structure before knowledge extraction without turning chunks themselves into the durable memory model.

## Why Source Location Matters

Each imported slice should carry source references such as:

- `artifact_id`
- page, section, frame, or region
- character or offset range when available

This keeps memory traceable, reviewable, and updatable when the source artifact changes.

External source location is provenance, not organization. Cortex should be able to preserve where an artifact came from without depending on that source path for its internal layout, retrieval behavior, or human inspection hierarchy.

## Canonical Artifact Identity

Import should create a Cortex-managed artifact record with:

- a stable internal `artifact_id`
- provider identity and provider-local location
- a deterministic Cortex resolution path
- source provenance such as original URI, Drive file ID, chat attachment reference, or import session
- authority mode such as `cortex_owned` or `external_authoritative`
- links to resulting knowledge objects and later promoted artifacts

That separation matters because imported source systems are allowed to drift. Files may be renamed, moved, re-sliced, or deleted in their original environment while Cortex still needs a stable evidence surface.

## Storage Boundary

- the configured artifact provider or `Git` keeps the canonical artifact body
- the knowledge plane keeps decomposition, retrieval indexes, and intake metadata
- Cortex remains the mutation authority over Layer 3 durable memory

Imported artifacts are evidence. Promoted artifacts are derived human-facing outputs. Both should be addressable through the same Cortex artifact identity model even if their backing providers differ.

## Retention And Pruning

Not every imported artifact deserves permanence.

Dream or other REM routines may:

- prune artifacts that produced no durable reused memory
- retire weak import-only knowledge objects
- keep a lightweight retained record with summary and provenance when the original file should no longer stay resident

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Typed Signals](typed-signals.md)
- [Bootstrap Ingestion](bootstrap-ingestion.md)
- [Reflection](reflection.md)
- [Dream Cycle](dream-cycle.md)
- [Artifact Provider](artifact-provider.md)
- [Artifact Promotion](artifact-promotion.md)
- [Knowledge And Artifact Architecture](../design/knowledge-and-artifact-architecture.md)
