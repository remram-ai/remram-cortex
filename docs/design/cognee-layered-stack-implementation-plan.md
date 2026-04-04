# Cognee Layered Stack Implementation Plan

## Purpose

This plan describes how to validate and implement the layered stack with `Cognee` as the central memory-and-knowledge platform.

This version assumes a deliberate choice to adopt `Cognee`'s worldview where possible rather than wrapping it in heavy Cortex-first abstractions.

Bluntly:

- this is the "bend the knee" version of the plan
- the goal is to accomplish Cortex outcomes through `Cognee`
- not to force `Cognee` back into a stricter Cortex-native semantic model

## Adoption Posture

If this path is chosen, the operating rule should be:

- let `Cognee` own the multi-store enrichment and retrieval worldview
- let Cortex stay thinner at the center
- keep Cortex responsible for:
  - policy composition
  - working-memory assembly
  - anchor identity
  - canonical artifact authority
  - publication workflows

Do not build custom replacement layers for platform behaviors that `Cognee` already provides unless there is a specific demonstrated gap.

## Phase 0: Prove The Platform Shape

Goals:

- stand up `OpenClaw`, `Cognee`, `Postgres`, and one graph backend
- validate first-party `OpenClaw` integration
- confirm local operational shape is tolerable

Exit criteria:

- working local stack
- successful add, cognify, and search cycle
- clear backend choice between `Neo4j` and `FalkorDB`

## Phase 1: Add Layer Boundaries

Goals:

- implement Cortex anchor registry
- keep OpenClaw as the primary working-memory implementation
- add Cortex policy overlays
- add Mamba-style semantic checkpoint production
- keep canonical artifacts outside `Cognee`
- define the thinnest explicit routing between working memory, durable memory, and knowledge
- add rolling context compression outputs

Exit criteria:

- no split-brain writes
- working anchor identity model
- basic startup stance assembly

Implementation posture:

- do not over-wrap `Cognee`
- prefer direct use of its native ingestion and search surfaces
- only add Cortex translation layers where authority boundaries require them

## Phase 2: Durable Memory Facade

Goals:

- expose `Cognee` memory and retrieval outputs through a thin Cortex durable-memory facade
- define only the minimum memory object shapes needed by runtime
- add support and status overlays only where they are required by actual workflows

Exit criteria:

- memory updates are routed through Cortex contracts
- runtime can ask for compact durable-memory bundles

Implementation posture:

- adopt Cognee's data and pipeline shape where possible
- avoid rebuilding a second durable-memory model on top of Cognee

## Phase 3: Artifact And Knowledge Flow

Goals:

- integrate artifact intake with anchor and revision tracking
- run `Cognee` over decomposed artifact inputs using its native staged pipeline
- support incremental reprocessing

Exit criteria:

- canonical revision tracked
- derived knowledge retrievable
- artifact changes do not require manual rebuild of the whole system

## Phase 4: Reflection Split

Goals:

- branch one evidence feed into:
  - durable-memory updates
  - artifact impacts
- context compression products
- governed preference-policy updates
- ensure dirty-anchor behavior is explicit

Exit criteria:

- runtime evidence can update memory now
- artifact redraft can happen later

Implementation posture:

- use `Cognee` for the branches that match its native strengths
- do not force reflection to mimic Graphiti-style temporal semantics if Cognee can achieve the same practical outcome through its own pipeline model

## Phase 5: Publication And Reconciliation

Goals:

- redraft canonical artifacts from derived knowledge and memory context
- publish through canonical artifact channel
- re-ingest and reconcile support after publication

Exit criteria:

- clean redraft loop
- no stale-support blind spots

## Phase 6: Validate Cost And Throughput

Goals:

- measure cognify throughput
- measure tokens per chunk
- measure graph and vector growth
- measure query latency on real workloads

Exit criteria:

- enough evidence to decide whether `Cognee` remains a viable center or should be dropped

## Main Validation Questions

1. Is the operational overhead acceptable?
2. Does the platform feel native to the layered architecture or too heavy?
3. Is the application-layer hybrid retrieval good enough?
4. Can Cortex stay the coordinating authority without fighting Cognee's core worldview?
5. Are the remaining gaps smaller than the custom stack we would build around `Graphiti`?
