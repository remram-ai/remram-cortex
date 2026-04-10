# Artifact Intake

Artifact intake is the Layer 5 to Layer 4 entry path for non-runtime source material.

It covers source bodies such as:

- uploaded reference documents
- fetched web snapshots
- owned high-signal documents
- retained source files that should become part of the user's evidence corpus

It does not mean:

- runtime transcript capture
- authored artifact promotion
- direct durable-memory writes from raw bodies

Those are separate flows.

## Why Intake Exists

Without a formal intake path, every upload or fetched source risks becoming:

- an opaque attachment
- an ad hoc retrieval blob
- a silent Layer 3 write

Artifact intake keeps the boundary clean:

- Layer 5 stores the source-of-record body
- Layer 4 stores bounded operational forms derived from it
- Layer 3 stores only durable meaning that survives reflection and reconciliation

## Intake Flow

Artifact intake should:

- create or update a stable Cortex-managed source anchor
- store the source body in Layer 5 under the right evidence class
- extract bounded operational forms for Layer 4
- attach source pointers and provenance to those derived forms
- allow reflection and later Dream work to decide what durable meaning belongs in Layer 3

The key rule is:

- raw source bodies belong in Layer 5
- shaped working bodies belong in Layer 4
- durable semantic conclusions belong in Layer 3

## Intake Lanes

The main intake lanes are:

### Reference Intake

For outside material such as:

- web links
- uploaded PDFs
- research sources

This usually lands first as `reference_cache`.

It is one-way by default and follows shorter retention rules.

### Owned-Source Intake

For user-owned or intentionally retained high-signal material such as:

- business plans
- budgets
- structured personal documents
- durable internal notes

This has a stronger trust and retention posture than generic references.

It becomes the basis for later source maintenance and dirty-state workflows.

## What Layer 4 Should Receive

Artifact intake should produce bounded Layer 4 forms such as:

- summaries
- extracted snippets
- decomposition chunks
- linked source records
- retrieval-ready operational bodies

It should not copy entire raw bodies into Layer 4 by default.

## Identity And Provenance

Each intake result should preserve enough source linkage to support:

- review
- reprocessing
- dirty-state comparison
- later promotion or supersession

Useful source references include:

- stable source anchor or evidence id
- revision or fetch identifier when available
- page, section, region, or offset hints when available

## Related Concepts

- [Artifact Provider](artifact-provider.md)
- [Artifact Promotion](artifact-promotion.md)
- [Bootstrap Ingestion](bootstrap-ingestion.md)
- [Reflection](reflection.md)
- [Dream](dream-cycle.md)
- [Knowledge And Artifact Architecture](../design/knowledge-and-artifact-architecture.md)
