# Graphiti + Neo4j + Redis Layered Stack Architecture

## Purpose

This document describes the layered Cortex architecture for:

- `Redis` working memory
- `Graphiti + Neo4j` durable memory
- `OpenSearch` or `Postgres + pgvector` knowledge plane
- `Git` canonical artifacts

## Architecture Summary

```text
Users / Channels / Agents
            |
            v
OpenClaw Runtime
  - tools
  - prompts
  - hooks
  - mode packs
            |
            +-----------------------------+
            |                             |
            v                             v
Working Memory Sidecar             Cortex Coordination Layer
  - Redis hot state                - anchor registry
  - queue state                    - layer routing
  - continuity                     - policy enforcement
  - handoff notes                  - publication workflow
            |                             |
            +--------------+--------------+
                           |
                           v
                    Graphiti Service Layer
               - durable memory writes
               - search / related memory
               - provenance / invalidation
                           |
                           v
                         Neo4j
                           |
                           v
                   Knowledge Plane Service
              - decomposition retrieval
              - vector / lexical search
              - revision-aware slices
                           |
           +---------------+---------------+
           |                               |
           v                               v
      OpenSearch                     Postgres + pgvector
                           |
                           v
                      Canonical Artifacts
                         - Git
                         - provider docs
```

## Layer Contracts

### Working Memory

`Redis` holds:

- hot continuity
- rolling summaries
- task state
- queue state

It must stay bounded.

### Durable Memory

`Graphiti` holds:

- durable memory graph
- entity and relationship structure
- episode-backed provenance
- correction and invalidation lifecycle

### Knowledge

The knowledge plane holds:

- revision-aware artifact decomposition
- embeddings
- lexical retrieval fields
- typed slices and derived payloads

### Canonical Artifacts

`Git` or provider source owns:

- publishable artifact body
- reviewable revision history

## Retrieval Flow

1. runtime starts with policy + working snapshot + durable-memory bundle
2. if deeper memory is needed, query `Graphiti`
3. if artifacts or evidence are needed, resolve anchor and query the knowledge plane
4. fetch canonical artifact body only when publication or full-source inspection is required

## Reflection Flow

1. evidence enters hot sidecar and append-only log
2. reflection proposes:
   - memory updates
   - artifact impacts
3. durable memory updates go to `Graphiti`
4. artifact impacts update decomposition and mark anchors dirty
5. publication later regenerates canonical artifacts and triggers re-ingestion

## Why This Architecture Is Clean

It uses graph where graph is strongest:

- durable memory
- reasoning structure
- high-value routing

It uses a search substrate where search is strongest:

- artifact decomposition
- lexical and vector retrieval
- slice-level evidence lookup

That is the main architectural win.
