# Docs

`docs/` is the active architectural documentation surface for `remram-cortex`.

The repository has been reset around the layered architecture and the current chosen stack.

## Structure

- [overview/](overview/README.md): what Cortex is, why it exists, and how the repository is organized
- [glossary.md](glossary.md): locked shared terminology
- [concepts/](concepts/README.md): stable concept definitions that survive implementation changes
- [design/](design/README.md): the active architecture, stack, integration, and deployment docs
- [context-packs/](context-packs/README.md): AI-oriented briefing packs for NotebookLM, audio debriefs, and model onboarding
- [reference/](reference/README.md): curated technical notes for the core technologies currently in use

## Start Here

- [overview/overview.md](overview/overview.md)
- [design/layered-memory-architecture.md](design/layered-memory-architecture.md)
- [design/technology-stack.md](design/technology-stack.md)
- [context-packs/layered-cortex-stack/README.md](context-packs/layered-cortex-stack/README.md)
- [context-packs/layered-cortex-stack/00-high-signal-debrief.md](context-packs/layered-cortex-stack/00-high-signal-debrief.md)
- [concepts/high-signal-mamba-stream.md](concepts/high-signal-mamba-stream.md)

## AI Handoff Path

For a new AI implementation thread, the recommended read order is:

1. [context-packs/layered-cortex-stack/README.md](context-packs/layered-cortex-stack/README.md)
2. [context-packs/layered-cortex-stack/00-high-signal-debrief.md](context-packs/layered-cortex-stack/00-high-signal-debrief.md)
3. [context-packs/layered-cortex-stack/08-mvp-and-delivery-sequence.md](context-packs/layered-cortex-stack/08-mvp-and-delivery-sequence.md)
4. [../projects/mvp-1-layered-cortex/README.md](../projects/mvp-1-layered-cortex/README.md)
5. [../projects/mvp-1-layered-cortex/project-plan.md](../projects/mvp-1-layered-cortex/project-plan.md)

Historical material removed from the active tree now lives under the top-level [archive/](../archive/README.md).
