# Evidence Package

An evidence package is a closed, immutable record used for audit, replay, reconciliation, and provenance.

It is the durable wrapper around a bounded piece of raw evidence.

## What It Is

An evidence package is:

- immutable once closed
- source-linked
- time-bounded
- replayable
- suitable for audit and later verification

It is not the same thing as durable memory.

## Why Evidence Packages Exist

Cortex should not rely on live session state or loose document pointers when memory quality matters.

Evidence packages give the system a stable, inspectable support surface for:

- notion reconciliation
- deeper review when signal quality or trust posture requires it
- Graphiti episode packaging
- artifact impact analysis
- replay after logic changes

## Typical Sources

Evidence packages may be created from:

- an OpenClaw session boundary
- a checkpoint boundary
- a document ingestion event
- a canonical artifact revision

In the active design:

- runtime evidence usually closes into `Postgres`
- canonical document evidence usually remains in `Git` or another authoritative provider

## Typical Contents

An evidence package should usually include:

- a stable evidence id
- timestamps
- source or session identifiers
- a compact summary
- pointers to the raw backing material
- relevant metadata
- optional extracted Layer 3 support items

## Relationship To Graphiti

`Graphiti` should usually receive a compact episode package derived from evidence, not an unbounded raw log dump.

That means the evidence package is often the bridge between:

- raw evidence authority
- durable semantic memory

## Retention Rule

Evidence packages can be trimmed more aggressively than raw live session state only after:

- durable memory is trusted
- provenance remains inspectable
- enough metadata remains for audit and replay

## Related Concepts

- [High-Signal Mamba Stream](high-signal-mamba-stream.md)
- [Notion](notion.md)
- [Reflection](reflection.md)
- [Intuition](intuition.md)
