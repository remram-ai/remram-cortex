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

- [docs/authority-map.md](docs/authority-map.md)
- [docs/overview/overview.md](docs/overview/overview.md)
- [docs/glossary.md](docs/glossary.md)
- [docs/design/layered-memory-architecture.md](docs/design/layered-memory-architecture.md)
- [docs/design/technology-stack.md](docs/design/technology-stack.md)
- [docs/context-packs/cortex-core/README.md](docs/context-packs/cortex-core/README.md)
- [projects/mvp-1-layered-cortex/README.md](projects/mvp-1-layered-cortex/README.md)

## AI Start Here

For a fresh implementation thread or AI onboarding pass, use this path:

1. [docs/context-packs/cortex-core/README.md](docs/context-packs/cortex-core/README.md)
2. [docs/context-packs/cortex-core/00-repo-orientation.md](docs/context-packs/cortex-core/00-repo-orientation.md)
3. [docs/context-packs/cortex-core/01-terminology-and-legacy.md](docs/context-packs/cortex-core/01-terminology-and-legacy.md)
4. [docs/context-packs/cortex-core/02-layers-and-authority.md](docs/context-packs/cortex-core/02-layers-and-authority.md)
5. [docs/context-packs/cortex-core/05-phases-and-delivery.md](docs/context-packs/cortex-core/05-phases-and-delivery.md)
6. [docs/context-packs/cortex-core/08-live-appliance-quick-start.md](docs/context-packs/cortex-core/08-live-appliance-quick-start.md)
7. [projects/mvp-1-layered-cortex/README.md](projects/mvp-1-layered-cortex/README.md)
8. [projects/mvp-1-layered-cortex/project-plan.md](projects/mvp-1-layered-cortex/project-plan.md)

For a longer NotebookLM or audio-style briefing, use the expanded [Layered Cortex Stack pack](docs/context-packs/layered-cortex-stack/README.md).

## Canonical Docs

When active docs disagree, treat these as the live authority:

- [docs/authority-map.md](docs/authority-map.md)
- [docs/glossary.md](docs/glossary.md)
- [docs/design/layered-memory-architecture.md](docs/design/layered-memory-architecture.md)
- [docs/design/technology-stack.md](docs/design/technology-stack.md)
- [docs/design/openclaw-integration.md](docs/design/openclaw-integration.md)
- [docs/design/graphiti-neo4j-durable-memory.md](docs/design/graphiti-neo4j-durable-memory.md)
- [docs/design/knowledge-and-artifact-architecture.md](docs/design/knowledge-and-artifact-architecture.md)
- [docs/design/deployment-plan.md](docs/design/deployment-plan.md)

## Current Direction

The repository is no longer optimizing for candidate comparison.

The active direction is to build Cortex around:

- OpenClaw-native Layer 2 working memory
- policy and semantic compression as Cortex-owned augmentation
- staged notions and reconciliation into Layer 3 durable memory
- a clean split between operational knowledge and source-of-record evidence

Older decision packages, alternative stack evaluations, and legacy architecture material were moved into the dated archive bucket during the layered repository reset.
They remain historical context only unless the active authority docs explicitly revive them.
