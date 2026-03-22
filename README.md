# remram-cortex

Remram Cortex is the knowledge authority for Remram.

It turns runtime evidence, tool outputs, and imported artifacts into durable knowledge, then serves bounded retrieval back to orchestration. Cortex owns memory. It does not own execution, runtime policy, or prompt assembly.

## What Cortex Is

Cortex is:

- the durable memory layer for Remram
- the retrieval authority for structured knowledge
- the home of reflection, reconciliation, and artifact promotion
- a local-first service boundary, not a prompt-side convenience feature

## What Cortex Is Not

Cortex is not:

- a transcript archive
- a vector-only memory store
- the execution runtime
- the orchestration or prompt-policy layer

OpenClaw executes. Orchestration governs behavior. Gateway governs the control plane. Cortex remembers.

## Repository Status

This repository is currently documentation-first. The baseline conceptual architecture is being locked in before deeper implementation detail is added.

The active repository structure is:

- `docs/` for architecture, vocabulary, and cross-cutting design context
- `product/` for stable Cortex product capabilities, dependency overlays, and regression expectations
- `projects/` for project-scoped execution packages, acceptance records, and epic work packages

The source of truth is split by artifact type:

- `docs/` owns repository-wide architecture, terminology, and design context
- `product/` owns stable capability and dependency contracts
- `projects/` owns execution sequencing, acceptance, HAT, and leave-behind delivery artifacts

Use the `docs/` tree for the current conceptual baseline:

- [docs/README.md](docs/README.md) for the documentation map
- [docs/overview/](docs/overview/README.md) for the high-level role and boundary
- [docs/glossary.md](docs/glossary.md) for normalized terminology
- [docs/concepts/](docs/concepts/README.md) for short concept definitions
- [docs/remram-cortex/architecture.md](docs/remram-cortex/architecture.md) for the canonical architecture
- [docs/remram-cortex/inconsistencies.md](docs/remram-cortex/inconsistencies.md) for current inconsistency status and archive links

## Core Model

The current architectural baseline is:

- transcripts are evidence, not knowledge
- memory is composed of structured knowledge objects with multi-source provenance
- governance fields hard-filter eligibility before ranking
- semantic signature acts as soft routing bias
- typed signal fields form the primary OpenSearch retrieval surface
- imported documents and images enter through one source-linked artifact-intake path
- retrieval is filter-first, bounded, and inspectable
- reflection performs immediate post-run mutation and thread-memory compression
- dream performs later reconciliation, conflict handling, and promotion
- promoted artifacts are Git-backed projections, not replacements for canonical memory

## Repository Boundary

This repository owns Cortex-local design and implementation material.

The broader `remram` repository holds the system-level feature record and adjacent platform context. This repository holds the authoritative Cortex vocabulary, architecture, and future service implementation.

## Start Here

- If you are orienting to Cortex as a system, start with [docs/README.md](docs/README.md) and [docs/remram-cortex/architecture.md](docs/remram-cortex/architecture.md).
- If you are changing stable Cortex behavior, start with [product/README.md](product/README.md), then open the specific `spec.md` and `regression-plan.md` together.
- If you are working the current delivery slice, start with [projects/README.md](projects/README.md), then [projects/v0_1 MVP/README.md](projects/v0_1 MVP/README.md).
- If you are starting a new AI or implementation thread, use [projects/v0_1 MVP/seed-prompt.md](projects/v0_1 MVP/seed-prompt.md) and then jump to the specific epic or product folder named in the thread.
- If you are reviewing current proof and operator flow, start with [projects/v0_1 MVP/acceptance-test.md](projects/v0_1 MVP/acceptance-test.md) and [projects/v0_1 MVP/runtime-docs.md](projects/v0_1 MVP/runtime-docs.md).

## Working Surfaces

- [product/README.md](product/README.md) is the stable Cortex product surface
- [projects/README.md](projects/README.md) is the execution-package surface
