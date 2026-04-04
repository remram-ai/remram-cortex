# Cortex Overview

Remram Cortex is the knowledge authority layer for Remram.

It coordinates policy, working memory, durable memory, decomposed knowledge, and canonical artifacts so the system can think in the moment, remember over time, and work against real grounded source material without collapsing everything into one storage model.

The current architectural posture is:

**one authority, multiple memory surfaces**

## Active Layer Model

1. `Policy`
2. `Working Memory`
3. `Durable Memory`
4. `Decomposed Artifact Knowledge`
5. `Canonical Artifacts`

The important distinction is:

- Layer 2 is operational and session-shaped
- Layer 3 is durable and semantic
- Layer 4 is decomposed and retrieval-optimized
- Layer 5 is canonical and publication-grade

## Chosen Stack

The current active stack direction is:

- `OpenClaw` for runtime execution and working-memory mechanics
- Cortex-owned policy composition
- a High-Signal `Mamba` stream for semantic checkpoints and compression
- `Graphiti + Neo4j` for durable memory
- `Postgres + pgvector` for runtime evidence, control-plane state, and decomposed knowledge
- `Git` for canonical artifacts

## What Cortex Owns

Cortex owns:

- policy composition above runtime execution
- the semantic checkpoint stream
- durable memory contracts and reconciliation
- the split between decomposed knowledge and canonical artifacts
- notion staging, oversight, and promotion rules

## What Cortex Does Not Own

Cortex does not own:

- raw OpenClaw execution
- prompt-time runtime mechanics below the OpenClaw boundary
- canonical artifact authoring outside approved publication workflows
- durable memory truth outside Layer 3 contracts

## Repository Direction

This repository has been reset around the layered architecture.

The active surfaces now aim to be:

- fewer
- cleaner
- technology-specific only where the stack is actually chosen
- free of older decision clutter in the active tree

Historical alternatives, pre-reset plans, and superseded design packages live in the top-level archive.
