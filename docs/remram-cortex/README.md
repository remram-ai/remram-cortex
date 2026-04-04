# Remram Cortex Docs

This folder holds the canonical design documents for Remram Cortex.

## Documents

- [../overview/overview.md](../overview/overview.md): the high-level explanation of what Cortex is and why it exists
- [../glossary.md](../glossary.md): the locked baseline terminology
- [../design/layered-memory-architecture.md](../design/layered-memory-architecture.md): the current foundational layered architecture direction
- [architecture.md](architecture.md): the older canonical architecture document, still useful as detailed system context but not yet fully reconciled to the layered reset
- [inconsistencies.md](inconsistencies.md): current inconsistency status and links to archived resolution notes
- [../concepts/](../concepts/README.md): the normalized vocabulary used by the architecture doc

## Editing Rule

Update the layered foundation first when architecture direction changes.

Use `architecture.md` carefully until it is fully reconciled to the layered model.

Track unresolved contradictions in `inconsistencies.md` instead of letting competing models coexist silently inside `architecture.md`.
