# Cortex Overview

Remram Cortex is the knowledge authority layer for Remram.

It coordinates policy, working memory, durable memory, and knowledge so the system can think in the moment, remember over time, and work against real artifact-backed context without collapsing everything into one storage model.

The key shift is:

**one authority, multiple memory surfaces**

Cortex is not a memory plugin and not a single database pretending to do every job.

It is a layered intelligence architecture where:

- policy governs behavior
- working memory supports live execution
- durable memory compounds learned understanding
- decomposed artifact knowledge supports retrieval and reasoning
- canonical artifacts preserve official temporal truth

Many of the original Cortex concepts remain valid.

They are not being discarded.

They are being remapped into the layered architecture.

## What Cortex Means Now

Cortex is no longer best described as “the memory engine.”

That framing was too narrow.

Cortex is better understood as the coordinating authority over:

- runtime continuity
- durable memory
- artifact-backed knowledge
- revision-aware decomposition
- reflection and publication workflows

The correct architectural posture is:

- not one memory to rule them all
- not one storage substrate
- one cross-layer authority with explicit contracts between layers

## Compatible Concepts, Remapped

The earlier conceptual vocabulary still mostly holds.

The important change is where each concept now lives.

### Working Memory And Context

The older distinction between conversation, context, and memory still matters.

It now maps more cleanly to:

- `conversation layer` and hot continuity -> `Working Memory`
- compact runtime injection -> `Bounded Retrieval`
- durable retained learning -> `Durable Memory`

This preserves the original `memory versus context` distinction instead of collapsing it into one system.

### Durable Memory Semantics

The earlier ideas around durable memory also remain compatible:

- `knowledge authority`
- `knowledge objects`
- `governance fields`
- `typed signals`
- `semantic signature`

These now belong primarily in the `Durable Memory` layer and at the boundary between durable memory and retrieval.

The layer reset does not remove them.

It gives them a cleaner home.

### Retrieval Discipline

The concept of `bounded retrieval` remains central.

The layered model sharpens it:

- startup stance should stay bounded
- only compact working continuity and durable-memory bundles should be injected by default
- deeper artifact knowledge should remain deliberate and tool-driven

### Reflection And Dream

`Reflection` and `Dream Cycle` remain core Cortex behaviors.

They now map to different responsibilities:

- reflection turns evidence into durable-memory updates and artifact-impact updates
- dream and maintenance routines reconcile, consolidate, and strengthen durable memory and publication readiness over time

### Artifact Concepts

The artifact concepts also remain compatible:

- `artifact intake`
- `artifact provider`
- `artifact promotion`

They now sit more clearly inside the `Knowledge` portion of the system:

- canonical artifacts hold publication truth
- decomposed artifact knowledge holds retrieval-ready derived knowledge
- promotion remains the path from working or durable understanding into durable reviewable artifacts

### Bootstrap

`Bootstrap ingestion` still matters.

It now maps to controlled evidence import into the layered system instead of being treated as “load everything into memory.”

## Why This Shift Matters

Different kinds of state have different jobs:

- active task continuity is not the same thing as durable memory
- durable memory is not the same thing as canonical artifact truth
- canonical artifact truth is not the same thing as derived retrieval knowledge
- policy is not memory at all

Trying to force all of those through one substrate creates unnecessary complexity and makes authority harder to reason about, not easier.

The layered approach fixes that.

## The Active Layer Model

The current Cortex foundation is:

1. `Policy`
2. `Working Memory`
3. `Durable Memory`
4. `Decomposed Artifact Knowledge`
5. `Canonical Artifacts`

This is the active conceptual baseline for the repository.

The old concepts still matter.

They should now be read through this layer model instead of through a single-memory-substrate assumption.

## Repository Boundary

This repository owns the implementation and authoritative design for Cortex.

The `remram` repository keeps the approved feature record and broader system references. This repository keeps the Cortex-local contracts, vocabulary, architecture, and active delivery designs.

## Current Architectural Direction

The current foundational architecture is described in:

- [Layered Memory Architecture](../design/layered-memory-architecture.md)

That document is now the best expression of the active Cortex direction.

Some older architecture material still exists and should be read as pre-layered-architecture context unless explicitly updated.

## Related Documents

- [Charter](charter.md)
- [Glossary](../glossary.md)
- [Concepts](../concepts/README.md)
- [Layered Memory Architecture](../design/layered-memory-architecture.md)
- [Design Packages](../design/README.md)
