# Cognee Layered Stack Complete Context Pack

## Purpose

This document models `Cognee` as the center of the layered Cortex stack.

It assumes the new layered architecture is real:

- working memory is separate
- durable memory is separate
- canonical artifacts are separate
- decomposed knowledge is separate

The question here is:

**What does the stack look like if Cognee becomes the main durable-memory and knowledge-orchestration platform under Cortex?**

Reviewed on `April 3, 2026`.

## Stack Shape

- `OpenClaw` as runtime shell
- OpenClaw session surface as the working-memory implementation
- policy overlays and Mamba-stream augmentation
- `Cognee` as the multi-source memory and knowledge platform
- `Postgres` as Cognee relational backbone
- `Neo4j` or `FalkorDB` as graph backend
- vector backend selected through Cognee
- `Git` as canonical artifact authority

## Why This Stack Is Interesting Now

Earlier, the main negative on `Cognee` was architectural weight.

That negative is weaker after the layered-architecture reset.

The current design already assumes:

- multiple layers
- multiple stores
- separate working memory
- separate canonical artifacts
- separate derived knowledge

That means `Cognee` is no longer disqualified for being multi-layered.

It becomes interesting because it was built for a multi-source, multi-store worldview from the start.

## What Cognee Natively Brings

`Cognee` is strongest when the system wants:

- dataset-oriented ingestion
- staged processing
- graph plus vector retrieval
- incremental loading
- platform-level orchestration across stores

Its native worldview is closer to:

- add
- cognify
- memify
- search

than to either:

- pure graph-first memory
- or simple memory-record storage

## Why This Fits The Layered Architecture

This stack is clean if Cortex uses `Cognee` for:

- durable-memory enrichment
- artifact-derived knowledge processing
- graph and vector retrieval orchestration

and does not ask `Cognee` to do:

- hot working memory
- prompt assembly authority
- canonical artifact ownership

That split makes the architecture much more defensible.

## What This Stack Optimizes For

This stack optimizes for:

- multi-source ingestion
- pipeline-native enrichment
- structured batch processing
- graph plus vector retrieval without hand-assembling every component
- a platform that already expects multiple storage layers

## What This Stack Does Not Optimize For

This stack does not optimize for:

- minimum moving parts
- a single sharp durable-memory object model
- pure first-pass retrieval simplicity
- lightweight solo-builder operations

It is a platform choice, not a minimal-substrate choice.

## Layer Mapping

### Policy

Owned by Cortex orchestration, not by `Cognee`.

### Working Memory

Owned by the OpenClaw session surface, augmented by Cortex policy and the Mamba stream, not by `Cognee`.

### Durable Memory

Primarily coordinated through `Cognee` data points, graph links, summaries, and memory-like outputs.

### Knowledge

Best fit for `Cognee`.

This is where it is strongest:

- ingesting multiple sources
- extracting graph structure
- producing summaries
- coordinating graph and vector surfaces

### Canonical Artifacts

Remain outside `Cognee`, typically in `Git` or another canonical provider.

## Authority Read

The authority story here is:

- Cortex remains the overall authority
- canonical artifacts remain publication authority
- `Cognee` becomes the platform authority for derived memory and knowledge surfaces

This is different from:

- `Mem0`, where memory records are the center
- `Graphiti`, where graph facts are the center

Here, the center is the platform pipeline.

## What We Would Be Adopting

- dataset-oriented knowledge workflows
- staged transformation as a normal part of the system
- multi-store coordination as a feature, not a workaround
- application-layer hybrid retrieval
- incremental loading and reprocessing as standard lifecycle behavior

## What We Would Be Fighting

- a simpler always-live memory object model
- a single obvious durable-memory authority object
- low-ops expectations
- a narrow “memory plugin” mental model

## Main Risks

1. Cortex may end up shaped too much like `Cognee` and not enough like Cortex.
2. Working memory is still outside the platform, so it does not actually remove all layering.
3. Hybrid retrieval is platform-level, not the same thing as a single database-native hybrid operator.
4. The relational layer does not go away.

## Why This Stack Is Still Credible

It is credible because the architecture is already multi-layer.

If the system truly wants:

- multiple evidence sources
- graph and vector retrieval
- staged enrichment
- artifact-aware ingestion

then `Cognee` is no longer the odd one out.

It becomes the contender that was designed for the same shape we are now accepting.
