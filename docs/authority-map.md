# Authority Map

This document defines the active documentation authority split for `remram-cortex`.

Use it when the repo feels repetitive and you need to know which document actually decides the architecture.

## Core Rule

When active documents disagree:

1. follow the canonical docs listed here
2. update the drifted supporting docs to match
3. treat `archive/` as historical context, not live authority

## Canonical Design Authority

These documents define the active Cortex architecture.

- [Overview](overview/overview.md): system frame, five-layer model, current direction
- [Charter](overview/charter.md): repository-level commitments and non-goals
- [Glossary](glossary.md): canonical terminology, legacy-term handling, deferred-term handling
- [Layered Memory Architecture](design/layered-memory-architecture.md): canonical layer boundaries, authority rules, lifecycles, sequencing
- [Technology Stack](design/technology-stack.md): canonical stack posture, active components, deferred components
- [OpenClaw Integration](design/openclaw-integration.md): canonical OpenClaw boundary and Layer 1 or Layer 2 integration posture
- [Graphiti + Neo4j Durable Memory](design/graphiti-neo4j-durable-memory.md): canonical Layer 3 posture
- [Knowledge And Artifact Architecture](design/knowledge-and-artifact-architecture.md): canonical Layer 4 and Layer 5 split, intake, promotion, reprocessing
- [Deployment Plan](design/deployment-plan.md): canonical phase bring-up and service posture

## Canonical Execution Authority

These documents define the active delivery package for the current MVP without redefining the architecture.

- [MVP 1 README](../projects/mvp-1-layered-cortex/README.md): execution package entry point
- [Project Charter](../projects/mvp-1-layered-cortex/project-charter.md): MVP scope and exclusions
- [Project Plan](../projects/mvp-1-layered-cortex/project-plan.md): phased delivery sequence for the locked architecture
- [Acceptance Test](../projects/mvp-1-layered-cortex/acceptance-test.md): current proof surface
- [Runtime Docs](../projects/mvp-1-layered-cortex/runtime-docs.md): current scaffold and runtime-facing proof posture

## Supporting But Non-Authoritative Summaries

These docs should agree with the canonical design set above, but they do not get to silently redefine it.

- [Concepts](concepts/README.md): stable concept explainers and retrieval-language notes
- [Product Foundations](../product/foundations/README.md): stable product-surface restatements
- [Context Packs](context-packs/README.md): AI-oriented summaries and onboarding bundles
- [Reference Notes](reference/README.md): implementation-facing technology notes for the chosen stack

## External Live-Appliance Authority

For live Moltbox appliance behavior, this repo is not the final operator authority.

Use:

- `moltbox-gateway` for the live CLI contract, operator workflows, verification surfaces, recovery model, and current web-tooling baseline
- `moltbox-services` for baseline service definitions and service-local docs
- `moltbox-runtime` for promoted runtime artifacts and overlays

In this repo, the matching Cortex authority doc is [OpenClaw Integration](design/openclaw-integration.md) plus the concept note [Live Appliance Authority](concepts/live-appliance-authority.md).

## Legacy And Deferred Terms

The active repo keeps older terms only when they are handled explicitly.

- `Dimension` is a legacy umbrella term. Use `Governance Fields`, `Typed Signals`, and `Semantic Signature` instead.
- `Conversation Layer` is a retained deferred concept, not an MVP 1 commitment.
- `Typed Signals` and `Semantic Signature` are retained retrieval concepts, not locked Phase 1 implementation requirements.
- `Authored canon` is acceptable shorthand, but the precise Layer 5 evidence-class term is `authored_artifact`.
- `Dream Cycle` remains an acceptable longer form, but `Dream` is the preferred short form in active docs.

## Read Order

For a new human reader:

1. [Overview](overview/overview.md)
2. [Authority Map](authority-map.md)
3. [Glossary](glossary.md)
4. [Layered Memory Architecture](design/layered-memory-architecture.md)
5. [Technology Stack](design/technology-stack.md)
6. [Knowledge And Artifact Architecture](design/knowledge-and-artifact-architecture.md)
7. [Deployment Plan](design/deployment-plan.md)

For a new AI thread:

1. [Cortex Core Context Pack](context-packs/cortex-core/README.md)
2. [MVP 1 README](../projects/mvp-1-layered-cortex/README.md)
3. [Project Plan](../projects/mvp-1-layered-cortex/project-plan.md)
