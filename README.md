# remram-cortex

Remram Cortex is the knowledge authority layer for Remram.

It is now organized around a layered architecture:

1. `Policy`
2. `Working Memory`
3. `Durable Memory`
4. `Decomposed Artifact Knowledge`
5. `Canonical Artifacts`

The active stack direction is:

- `OpenClaw` for runtime execution and working-memory mechanics
- Cortex-owned policy composition
- a High-Signal `Mamba` stream for semantic checkpointing and compression
- `Graphiti + Neo4j` for durable memory
- `Postgres + pgvector` for evidence, control-plane state, and decomposed knowledge
- `Git` for canonical artifact truth

## Repository Layout

- [docs/](docs/README.md): active architecture, concepts, references, and integration docs
- [product/](product/README.md): current product-surface documents for the chosen architecture
- [projects/](projects/README.md): active MVP package and execution documents
- [archive/](archive/README.md): dated historical material removed from the active tree

## Start Here

- [docs/overview/overview.md](docs/overview/overview.md)
- [docs/design/layered-memory-architecture.md](docs/design/layered-memory-architecture.md)
- [docs/design/technology-stack.md](docs/design/technology-stack.md)
- [docs/context-packs/layered-cortex-stack/00-high-signal-debrief.md](docs/context-packs/layered-cortex-stack/00-high-signal-debrief.md)
- [projects/mvp-1-layered-cortex/README.md](projects/mvp-1-layered-cortex/README.md)

## Current Direction

The repository is no longer optimizing for candidate comparison.

The active direction is to build Cortex around:

- OpenClaw-native Layer 2 working memory
- policy and semantic compression as Cortex-owned augmentation
- staged notions and reconciliation into Layer 3 durable memory
- a clean split between decomposed operational knowledge and canonical artifact truth

Older decision packages, alternative stack evaluations, and legacy architecture material were moved into the dated archive bucket during the layered repository reset.
