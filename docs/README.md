# Docs

`docs/` is the active architectural documentation surface for `remram-cortex`.

The repository has been reset around the layered architecture and the current chosen stack.

## Structure

- [overview/](overview/README.md): what Cortex is, why it exists, and how the repository is organized
- [authority-map.md](authority-map.md): canonical doc split, read order, and legacy handling
- [glossary.md](glossary.md): locked shared terminology
- [concepts/](concepts/README.md): stable concept definitions that survive implementation changes
- [design/](design/README.md): the active architecture, stack, integration, and deployment docs
- [context-packs/](context-packs/README.md): AI-oriented briefing packs for compact thread start, NotebookLM, and audio debriefs
- [reference/](reference/README.md): curated technical notes for the core technologies currently in use

## Start Here

- [authority-map.md](authority-map.md)
- [overview/overview.md](overview/overview.md)
- [glossary.md](glossary.md)
- [design/layered-memory-architecture.md](design/layered-memory-architecture.md)
- [design/technology-stack.md](design/technology-stack.md)
- [context-packs/cortex-core/README.md](context-packs/cortex-core/README.md)
- [context-packs/layered-cortex-stack/README.md](context-packs/layered-cortex-stack/README.md)

## AI Handoff Path

For a new AI implementation thread, the recommended read order is:

1. [context-packs/cortex-core/README.md](context-packs/cortex-core/README.md)
2. [context-packs/cortex-core/00-repo-orientation.md](context-packs/cortex-core/00-repo-orientation.md)
3. [context-packs/cortex-core/01-terminology-and-legacy.md](context-packs/cortex-core/01-terminology-and-legacy.md)
4. [context-packs/cortex-core/02-layers-and-authority.md](context-packs/cortex-core/02-layers-and-authority.md)
5. [context-packs/cortex-core/05-phases-and-delivery.md](context-packs/cortex-core/05-phases-and-delivery.md)
6. [../projects/mvp-1-practical-cortex/README.md](../projects/mvp-1-practical-cortex/README.md)
7. [../projects/mvp-1-practical-cortex/project-plan.md](../projects/mvp-1-practical-cortex/project-plan.md)

Use the expanded [Layered Cortex Stack](context-packs/layered-cortex-stack/README.md) pack when you want a longer topic-by-topic briefing or audio-oriented source set.

## Canonical Rule

The canonical authority order is:

1. [authority-map.md](authority-map.md)
2. [glossary.md](glossary.md)
3. [design/](design/README.md)
4. supporting summaries in [concepts/](concepts/README.md), [product/](../product/README.md), [projects/](../projects/README.md), and [context-packs/](context-packs/README.md)

Historical material removed from the active tree now lives under the top-level [archive/](../archive/README.md).
