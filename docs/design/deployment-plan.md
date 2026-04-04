# Deployment Plan

This document records the current deployment posture for Cortex.

## Phase 1 Deployment Shape

The base deployment should include:

- `OpenClaw`
- Cortex policy and integration layer
- High-Signal Mamba stream worker
- `Graphiti`
- `Neo4j`
- `Postgres + pgvector`
- `Git` working repository or provider-backed canonical artifact source

## Service Roles

### OpenClaw

- runtime shell
- sessions
- hooks
- compaction
- tool execution

### Cortex Integration Layer

- policy composition
- layer routing
- notion staging
- oversight routing
- artifact and memory orchestration

### Mamba Worker

- semantic checkpoint production
- continuity compression
- optimistic and nightly stream consumption

This worker is a role, not yet a locked implementation dependency.

### Graphiti + Neo4j

- Layer 3 durable memory
- provenance and temporal memory operations

### Postgres + pgvector

- runtime evidence
- control-plane state
- decomposed knowledge

### Git

- canonical artifact truth

## Bring-Up Order

1. `OpenClaw`
2. `Postgres + pgvector`
3. `Neo4j`
4. `Graphiti`
5. Cortex integration layer
6. Mamba stream worker
7. Git-backed or provider-backed canonical artifact flow

## Early Delivery Priorities

1. get policy and OpenClaw integration stable
2. get the semantic checkpoint stream working
3. stand up durable memory
4. stand up the knowledge plane
5. add oversight and reconciliation

## What Is Explicitly Not In The Base Deployment

- a separate external working-memory store beside OpenClaw Layer 2
- a second graph system beside Layer 3
- a separate search platform unless Layer 4 requirements later justify it
