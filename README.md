# remram-cortex

Remram Cortex is the knowledge authority layer for Remram.

It is now organized around a layered architecture:

1. `Policy`
2. `Working Memory`
3. `Durable Memory`
4. `Operational Knowledge`
5. `Evidence`

The active stack direction is:

- `OpenClaw` for runtime execution and working-memory mechanics
- Cortex-owned policy composition
- `QMD` for hot working memory and notions
- a High-Signal `Mamba` stream later as a narrow continuity supercharge
- `Graphiti + Neo4j` for durable memory
- `Postgres` for the operational middle of the stack and control-plane state
- a Layer 5 evidence system with `runtime_evidence`, `reference_cache`, and `authored_artifact` as the main source-of-record classes

## Repository Layout

- [docs/](docs/README.md): active architecture, concepts, references, and integration docs
- [product/](product/README.md): current product-surface documents for the chosen architecture
- [projects/](projects/README.md): active MVP package and execution documents
- [archive/](archive/README.md): dated historical material removed from the active tree

## Start Here

- [docs/overview/overview.md](docs/overview/overview.md)
- [docs/design/layered-memory-architecture.md](docs/design/layered-memory-architecture.md)
- [docs/design/technology-stack.md](docs/design/technology-stack.md)
- [docs/context-packs/layered-cortex-stack/README.md](docs/context-packs/layered-cortex-stack/README.md)
- [docs/context-packs/layered-cortex-stack/00-high-signal-debrief.md](docs/context-packs/layered-cortex-stack/00-high-signal-debrief.md)
- [projects/mvp-1-layered-cortex/README.md](projects/mvp-1-layered-cortex/README.md)

## AI Start Here

For a fresh implementation thread or AI onboarding pass, use this path:

1. [docs/context-packs/layered-cortex-stack/README.md](docs/context-packs/layered-cortex-stack/README.md)
2. [docs/context-packs/layered-cortex-stack/00-high-signal-debrief.md](docs/context-packs/layered-cortex-stack/00-high-signal-debrief.md)
3. [docs/context-packs/layered-cortex-stack/08-mvp-and-delivery-sequence.md](docs/context-packs/layered-cortex-stack/08-mvp-and-delivery-sequence.md)
4. [projects/mvp-1-layered-cortex/README.md](projects/mvp-1-layered-cortex/README.md)
5. [projects/mvp-1-layered-cortex/project-plan.md](projects/mvp-1-layered-cortex/project-plan.md)

## Current Direction

The repository is no longer optimizing for candidate comparison.

The active direction is to build Cortex around:

- OpenClaw-native Layer 2 working memory
- policy and semantic compression as Cortex-owned augmentation
- staged notions and reconciliation into Layer 3 durable memory
- a clean split between operational knowledge and source-of-record evidence

Older decision packages, alternative stack evaluations, and legacy architecture material were moved into the dated archive bucket during the layered repository reset.
