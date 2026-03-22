# Artifact Intake Capability Spec

## 1. Purpose

Turn imported artifacts into bounded, source-linked knowledge updates through the standard Cortex write path.

## 2. Capability Boundary

This capability is responsible for:

- accepting imported artifacts
- reading text or structured content
- producing bounded slices
- attaching source-location provenance
- emitting candidate knowledge-object updates

This capability is not responsible for:

- long-term Dream reconciliation
- chat prompt injection
- artifact promotion

## 3. MVP Inputs

Supported first-pass import classes:

- Markdown
- plain text
- PDF with extractable text

Each intake run should consume:

- `artifact_id`
- artifact metadata
- raw bytes or provider-resolved content

## 4. MVP Outputs

Each successful intake should produce:

- bounded source slices
- provenance records
- knowledge-object writes or updates
- indexed OpenSearch documents
- import status and counts

## 5. Functional Requirements

- intake uses the same durable model as quick capture
- slices remain source-linked
- chunking is an ingestion tactic, not a second memory tier
- resulting knowledge is immediately eligible for retrieval
- imported artifacts may reinforce existing knowledge rather than always creating net-new objects

## 6. Deferred

- image-native guarantees
- full multimodal parsing
- complex provider-native rich-doc parsing beyond what the MVP needs
