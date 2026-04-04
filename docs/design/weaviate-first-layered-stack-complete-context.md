# Weaviate-First Layered Stack Complete Context Pack

## Purpose

This document models a fourth stack option:

**a Cortex-native layered stack built directly on Weaviate as the primary hybrid retrieval platform**

This is not a `Mem0` stack and not a `Graphiti` stack.

It is the highest-control hybrid-first option.

Reviewed on `April 3, 2026`.

## Stack Shape

- `OpenClaw` as runtime shell
- bounded working-memory sidecar
- Cortex-native durable-memory service
- `Weaviate` as the primary hybrid retrieval and object storage platform
- optional small control-plane database for registry and workflow state
- `Git` as canonical artifact authority

## Why This Option Is Worth Modeling

We have discussed `Weaviate` mainly as:

- a `Mem0` backend

This option asks a different question:

**What if the best hybrid retrieval platform becomes the main substrate for both durable memory objects and decomposed knowledge, with Cortex owning the lifecycle semantics itself?**

That is useful because it isolates the hybrid-first option from the product opinions of `Mem0`, `Graphiti`, and `Cognee`.

## What This Stack Optimizes For

- strongest database-native hybrid retrieval posture
- one primary retrieval substrate for durable memory and knowledge
- high control over schema and object types
- less dependence on a third-party memory worldview

## What This Stack Does Not Optimize For

- lowest implementation burden
- native temporal invalidation
- native memory lifecycle semantics
- immediate upstream leverage

This is a control-maximizing option, not a leverage-maximizing option.

## What Weaviate Natively Brings

- native hybrid search
- object collections
- filters
- cross references
- vector indexing
- lexical retrieval
- reranking extensions

That makes it the strongest standalone hybrid substrate modeled so far.

## What Cortex Would Still Have To Build

- durable-memory object lifecycle
- correction and supersession rules
- provenance policy
- memory support reconciliation
- graph-like routing semantics where needed

That is the price of this option.

## Layer Mapping

### Policy

Owned by Cortex orchestration.

### Working Memory

Owned by the hot sidecar.

### Durable Memory

Owned by a Cortex-native durable-memory service backed by `Weaviate` collections.

### Knowledge

Owned by Cortex-managed decomposition collections on the same `Weaviate` substrate.

### Canonical Artifacts

Owned by `Git` or another canonical provider.

## What We Would Be Adopting

- Weaviate as the core hybrid platform
- Cortex-owned memory semantics
- object references and collection discipline instead of a separate graph product

## What We Would Be Fighting

- the absence of a native temporal-memory engine
- the need to design durable-memory semantics ourselves
- higher custom build burden
- lower immediate ecosystem leverage than `Mem0`

## Main Risks

1. This may become a bespoke platform faster than intended.
2. Durable-memory semantics could be weaker than expected if not designed rigorously.
3. Cross-reference graphs may tempt the system into weak graph emulation.

## Why This Option Is Still Serious

It is serious because it is the cleanest way to test a pure hybrid-first philosophy without inheriting someone else's opinionated memory model.
