# Graphiti + Neo4j + Session-Surface Layered Stack Implementation Plan

## Purpose

This plan describes how to implement the layered stack built around:

- OpenClaw session-surface working memory
- `Graphiti + Neo4j` durable memory
- `OpenSearch` or `Postgres + pgvector` knowledge plane

## Phase 0: Lock The Knowledge Plane

Goals:

- choose `OpenSearch` or `Postgres + pgvector`
- define anchor and revision model
- define minimum knowledge-plane schema

Exit criteria:

- one knowledge-plane backend selected
- interface contract agreed

## Phase 1: OpenClaw Working-Memory Integration And Evidence Backbone

Goals:

- keep OpenClaw as the primary working-memory implementation
- add Cortex policy overlays
- add Mamba-style semantic checkpoint production
- add append-only evidence log
- support bounded continuity assembly through OpenClaw-native surfaces
- keep compression products ready before compaction needs them

Exit criteria:

- working continuity
- replayable evidence stream
- compression-aware context assembly without introducing a separate hot store

## Phase 2: Graphiti Durable Memory Integration

Goals:

- stand up `Graphiti + Neo4j`
- implement `OpenClaw -> Graphiti` durable-memory bridge
- enforce no direct graph writes outside the service boundary

Exit criteria:

- durable memory writes and reads working
- provenance and invalidation visible

## Phase 3: Knowledge Plane MVP

Goals:

- ingest canonical artifact revisions
- produce revision-aware decomposition
- expose vector and lexical retrieval over derived knowledge

Exit criteria:

- artifact slices queryable
- anchors bound to decomposition records

## Phase 4: Reflection Split

Goals:

- branch evidence into:
  - memory updates for `Graphiti`
  - artifact impacts for the knowledge plane
  - context compression products
  - governed preference-policy updates

Exit criteria:

- same evidence can update memory and artifact-derived knowledge without conflating them

## Phase 5: Publication Loop

Goals:

- mark dirty anchors
- redraft canonical artifacts
- publish to `Git`
- re-ingest revised decomposition
- reconcile stale support in graph memory

Exit criteria:

- clean revision-aware artifact cycle

## Phase 6: Integrity Hardening

Goals:

- add audit logs for graph writes
- add multi-pass verification for high-impact graph updates
- add maintenance and reconciliation jobs

Exit criteria:

- graph write safety is acceptable
- stale support and contradiction surfaces are inspectable
