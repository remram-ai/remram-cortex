# Graphiti + Neo4j + Session-Surface Layered Stack Architecture

## Purpose

This document describes the layered Cortex architecture for:

- OpenClaw session-surface working memory
- OpenClaw-native working-memory behavior
- semantic checkpoint stream over raw evidence
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
OpenClaw Session Surface           Cortex Coordination Layer
  - transcripts                    - anchor registry
  - session-scoped evidence        - layer routing
  - native compaction              - policy enforcement
  - context-engine inputs          - publication workflow
            |                             |
            +--------------+--------------+
                           |
                           v
                Raw Evidence Authority
         - Postgres evidence packages for runtime
         - Git / provider source for documents
                           |
                           v
               Semantic Checkpoint Stream
              - rolling summaries
              - Mamba-style continuity
              - notion candidates
              - oversight flags
              - artifact impact hints
                           |
          +----------------+----------------+
          |                                 |
          v                                 v
  Context Engine Assembly             Graphiti Service Layer
  - bounded session continuity       - notion staging
  - small-window runtime bundle      - durable memory writes
  - turn-time context assembly       - search / related memory
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
                         +--------------------+--------------------+
                         |                                         |
                         v                                         v
                    OpenSearch                              Postgres + pgvector
                           |
                           v
                      Canonical Artifacts
                         - Git
                         - provider docs
```

## OpenClaw Extension Surface Mapping

In OpenClaw terms, this stack maps cleanly onto four extension surfaces.

### 1. Context Engine

The context engine layer should assemble:

- policy
- working memory from the session surface
- compact `Graphiti` memory bundle

This is where bounded runtime injection is enforced.

OpenClaw should remain the primary working-memory implementation.

Cortex should augment that surface rather than replace it.

### 2. Memory Engine

The memory-engine slot should talk to the `Graphiti` service boundary.

That slot owns:

- durable-memory recall
- durable-memory writes
- compact memory retrieval into runtime

### 3. Reflection Pipeline

Reflection should branch runtime evidence into:

- staged notions and durable-memory updates for `Graphiti`
- knowledge-plane artifact impacts
- context compression products
- governed preference-policy updates

It should also be the right place for:

- oversight consumption
- verification
- audit
- maintenance triggers

### 4. Knowledge Tool Interface

Deeper artifact-backed knowledge should be accessed through tools, not default prompt injection.

That tool surface should expose:

- decomposition retrieval
- support inspection
- canonical artifact fetch when required

## Layer Contracts

### Working Memory

Working memory is anchored on the OpenClaw session surface and context engine.

It should assemble:

- hot continuity
- rolling summaries
- active task state
- compressed continuity objects

The raw session log is the recovery surface.

The semantic checkpoint stream is the main operational consumer surface.

No external hot store is assumed for phase 1.

### Durable Memory

`Graphiti` holds:

- durable memory graph
- entity and relationship structure
- episode-backed provenance
- correction and invalidation lifecycle
- reconciled Layer 3 memory
- tentative high-signal notions when early cross-thread visibility is worth the risk

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

1. evidence enters the OpenClaw session surface and raw evidence log
2. Mamba-style compression emits the semantic checkpoint stream
3. default consumers use the semantic checkpoint stream for:
   - context assembly
   - notion staging
   - oversight
   - artifact impact hints
4. reflection proposes:
   - staged notions and memory updates
   - artifact impacts
   - context compression products
   - governed preference-policy updates
5. high-signal notions may be written early as tentative cross-thread memory
6. session end or checkpoint hooks close the raw evidence window and persist an evidence package
7. reconciliation verifies notions against:
   - the closed evidence package
   - existing durable memory
   - oversight results
   - artifact support
8. `Graphiti` receives a compact episode package:
   - summary
   - pointer to evidence
   - source metadata
   - selected Layer 3 appropriate beliefs or support
9. artifact impacts update decomposition and mark anchors dirty
10. publication later regenerates canonical artifacts and triggers re-ingestion

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
