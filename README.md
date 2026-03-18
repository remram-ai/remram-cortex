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

The `docs/` tree is the source of truth for the current design:

- [docs/overview/](docs/overview/README.md) for the high-level role and boundary
- [docs/glossary.md](docs/glossary.md) for normalized terminology
- [docs/concepts/](docs/concepts/README.md) for short concept definitions
- [docs/remram-cortex/architecture.md](docs/remram-cortex/architecture.md) for the canonical architecture
- [docs/remram-cortex/inconsistencies.md](docs/remram-cortex/inconsistencies.md) for the small set of unresolved design boundaries

## Core Model

The current architectural baseline is:

- transcripts are evidence, not knowledge
- memory is composed of structured knowledge objects
- retrieval is filter-first, bounded, and inspectable
- reflection performs immediate post-run mutation and thread-memory compression
- dream performs later reconciliation, conflict handling, and promotion
- promoted artifacts are Git-backed projections, not replacements for canonical memory

## Repository Boundary

This repository owns Cortex-local design and implementation material.

The broader `remram` repository holds the system-level feature record and adjacent platform context. This repository holds the authoritative Cortex vocabulary, architecture, and future service implementation.
