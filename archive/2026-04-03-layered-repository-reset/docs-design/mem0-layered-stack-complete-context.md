# Mem0 Layered Stack Complete Context Pack

## Purpose

This document models `Mem0` as the durable-memory base inside the layered Cortex architecture.

It assumes:

- working memory is separate
- canonical artifacts are separate
- knowledge decomposition is separate

The question is:

**What does the layered stack look like if Mem0 stays the memory base instead of trying to become the whole architecture?**

Reviewed on `April 3, 2026`.

## Stack Shape

- `OpenClaw` as runtime shell
- OpenClaw session surface as the working-memory implementation
- policy overlays and Mamba-stream augmentation
- `Mem0 OSS` as durable-memory base
- `Weaviate` as the main vector and hybrid-ready substrate
- `Git` as canonical artifact authority
- separate decomposition collections and metadata surfaces under Cortex control

## Why This Stack Is Still Strong

This is the strongest function-first stack.

It keeps:

- official `OpenClaw` integration
- best published retrieval-latency evidence among the reviewed memory contenders
- easier first-build behavior
- a mainstream extension path instead of a niche fork posture

It also fits the layered reset better than the earlier “Mem0 does everything” framing.

## What Mem0 Actually Owns Here

`Mem0` owns:

- durable memory extraction and update logic
- memory lifecycle decisions
- canonical memory records
- memory recall into runtime

It does not own:

- working memory
- canonical artifacts
- raw artifact storage
- the full artifact decomposition layer

That is the important correction.

## Why Weaviate Still Matters Here

`Weaviate` gives this stack:

- native hybrid lexical plus vector retrieval
- strong metadata filtering
- local self-hosting
- object references if needed
- a shared retrieval substrate for both memory and knowledge surfaces

The layered version of this stack should treat `Weaviate` as:

- a shared infrastructure substrate

not:

- proof that the layers are collapsed

Logical separation still matters even if the substrate is shared.

## What This Stack Optimizes For

- first-build pragmatism
- lower custom integration burden
- fast selective memory retrieval
- upstream-friendly extension posture
- graph added later only if it proves value

## What This Stack Does Not Optimize For

- native temporal graph semantics
- graph-native provenance
- multi-hop memory as the primary retrieval model
- strong graph-first authority

## Layer Mapping

### Policy

Owned by Cortex orchestration.

### Working Memory

Owned by the OpenClaw session surface, augmented by Cortex policy and the Mamba stream.

### Durable Memory

Owned by `Mem0` memory records.

### Knowledge

Owned by Cortex-managed decomposition and retrieval collections on `Weaviate`.

### Canonical Artifacts

Owned by `Git` or another canonical provider.

## What We Would Be Adopting

- record-first durable memory
- shared hybrid-capable search substrate
- official runtime integration
- graph as a later optional extension or reflection layer

## What We Would Be Fighting

- weaker native temporal semantics
- provenance that is more metadata-shaped than graph-shaped
- the fact that stock `Mem0` does not expose every raw `Weaviate` capability directly
- any desire to treat graph as a first-class authority too early

## Main Risks

1. Temporal and provenance needs may outgrow the memory-record model.
2. Shared `Weaviate` substrate can create schema sprawl if memory and knowledge are not separated cleanly.
3. Graph reflection may arrive later than hoped if it is treated as optional forever.

## Why This Stack Remains Serious

It remains serious because it is the least self-deceptive function-first path.

It does not pretend that graph semantics are already earned.

It gives:

- fast usable memory
- strong retrieval
- room to grow

without forcing the full stack through an early graph commitment.
