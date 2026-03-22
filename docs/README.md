# Docs

`docs/` is the human-readable design layer for `remram-cortex`.

This repository is still early, so the documentation tree is organized around a clear conceptual baseline instead of a large implementation tree.

## Current Structure

- `overview/` explains what Cortex is and why the repository exists
- `glossary.md` locks the shared Cortex vocabulary
- `concepts/` defines the canonical Cortex vocabulary
- `design/` holds scoped design packages for active delivery slices
- `reference/` captures external technical references that inform Cortex design
- `remram-cortex/` contains the authoritative Cortex design documents

## Start Here

- read [overview/](overview/README.md) for the high-level role and repository boundary
- read [glossary.md](glossary.md) to align on locked terminology
- read [concepts/](concepts/README.md) for short concept definitions built on that glossary
- read [architecture.md](remram-cortex/architecture.md) for the canonical system design
- use [inconsistencies.md](remram-cortex/inconsistencies.md) to see whether any active inconsistencies remain and where prior ones were archived
- use [reference/](reference/README.md) for external guides and supporting material that inform design choices
- read [remram-cortex/](remram-cortex/README.md) for the local document map
