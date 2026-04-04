# Cognee Layered Stack Implementation Plan

## Purpose

This plan describes how to validate and implement the layered stack with `Cognee` as the central memory-and-knowledge platform.

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
- implement working-memory sidecar
- keep canonical artifacts outside `Cognee`
- define explicit routing between working memory, durable memory, and knowledge

Exit criteria:

- no split-brain writes
- working anchor identity model
- basic startup stance assembly

## Phase 2: Durable Memory Facade

Goals:

- wrap `Cognee` operations in Cortex durable-memory contracts
- define memory object shapes exposed to runtime
- implement confidence, support, and status overlays

Exit criteria:

- memory updates are routed through Cortex contracts
- runtime can ask for compact durable-memory bundles

## Phase 3: Artifact And Knowledge Flow

Goals:

- integrate artifact intake with anchor and revision tracking
- run `Cognee` over decomposed artifact inputs
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
- ensure dirty-anchor behavior is explicit

Exit criteria:

- runtime evidence can update memory now
- artifact redraft can happen later

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
4. Does Cortex still feel like the authority, or does `Cognee` become the product center?
