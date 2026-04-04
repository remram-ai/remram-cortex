# Cognee Layered Stack Architecture

## Purpose

This document describes the layered Cortex architecture if `Cognee` is used as the central memory-and-knowledge platform.

## Architecture Summary

```text
Users / Channels / Agents
            |
            v
OpenClaw Runtime
  - tools
  - mode packs
  - prompt assembly
  - runtime hooks
            |
            +-------------------------------+
            |                               |
            v                               v
Working Memory Sidecar                Cortex Coordination Layer
  - hot continuity                    - anchor identity
  - task state                        - layer routing
  - recent tool outcomes              - policy enforcement
  - evidence queue                    - publication workflow
            |                               |
            +---------------+---------------+
                            |
                            v
                        Cognee Platform
                  - add / cognify / memify / search
                  - graph extraction
                  - summaries
                  - incremental loading
                            |
           +----------------+----------------+
           |                                 |
           v                                 v
        Postgres                      Graph + Vector Backends
   - control / metadata               - Neo4j or FalkorDB
   - dataset state                    - vector backend per Cognee config
                                       - retrieval surfaces
                            |
                            v
                    Canonical Artifact Plane
                      - Git
                      - provider-backed documents
```

## Layer Interfaces In This Stack

### Policy Interface

Owned by Cortex orchestration.

`Cognee` consumes policy outcomes but does not own them.

### Working Memory Interface

Owned by the hot sidecar.

`Cognee` should not be in the critical path for low-latency continuity.

### Durable Memory Interface

Implemented as a Cortex facade over `Cognee` operations.

Core durable-memory writes should land through:

- `upsert_memory`
- `reconcile_memory`
- `search_memory`

but the backing implementation resolves into `Cognee` pipelines and stores.

### Artifact Registry Interface

Owned by Cortex, not by `Cognee`.

`Cognee` receives source descriptors and anchor bindings.

### Decomposition Interface

Best implemented through `Cognee` ingestion and derived search outputs.

### Publication Interface

Owned by Cortex redraft and review flows.

Canonical publication stays outside `Cognee`.

## Evidence Flow

1. runtime events are captured into working memory and evidence log
2. reflection selects memory and artifact-impact candidates
3. Cortex routes durable candidates into `Cognee`
4. Cortex routes artifact bodies and revisions into canonical artifact intake
5. `Cognee` processes derived knowledge from those sources

## Retrieval Flow

1. Cortex assembles startup stance from policy, working memory, and compact durable memory
2. deeper retrieval routes into `Cognee`
3. `Cognee` combines graph, vector, and summarization surfaces
4. canonical artifact body is only fetched when required

## Architectural Strength

The main strength of this stack is that it does not pretend the system is simple when it is not.

It embraces:

- multiple stores
- multiple source types
- derived knowledge workflows
- staged enrichment

without forcing Cortex to invent that platform shape alone.

## Architectural Constraint

The key constraint is that Cortex must still retain final authority over:

- anchor identity
- canonical artifact state
- layer write rules
- redraft and publication

If those are surrendered to `Cognee`, the system stops being Cortex-shaped.
