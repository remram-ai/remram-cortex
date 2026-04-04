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
OpenClaw Session Surface             Cortex Coordination Layer
  - transcripts                      - anchor identity
  - session evidence                 - layer routing
  - native compaction                - policy enforcement
  - context-engine inputs            - publication workflow
            |                               |
            +---------------+---------------+
                            |
                            v
                    Context Compression
              - rolling summaries
              - Mamba-style continuity
              - working-state distillation
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

## OpenClaw Extension Surface Mapping

In OpenClaw terms, this stack maps to four main extension surfaces.

### 1. Context Engine

The context engine should assemble:

- policy
- working memory from the session surface
- compact durable-memory bundle

It should not inject deep knowledge by default.

### 2. Memory Engine

The memory-engine slot should expose durable memory through a Cortex facade over `Cognee`.

That means the runtime still sees a memory interface, even though the backing behavior resolves through `Cognee` platform operations.

### 3. Reflection Pipeline

Reflection should run after or alongside execution and branch evidence into:

- durable-memory updates
- artifact or knowledge impacts
- context compression products
- governed preference-policy updates

This should not live in the context engine hot path.

### 4. Knowledge Tool Interface

Deep knowledge access should be exposed as tools.

Agents should use tools to:

- inspect derived knowledge
- query artifacts
- fetch supporting evidence
- escalate to canonical artifact bodies

## Layer Interfaces In This Stack

### Policy Interface

Owned by Cortex orchestration.

`Cognee` consumes policy outcomes but does not own them.

### Working Memory Interface

Owned by the OpenClaw session surface.

Cortex augments this layer through policy-aware assembly and Mamba-style semantic compression.

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

1. runtime events are captured into the session surface and evidence log
2. reflection selects memory and artifact-impact candidates
3. reflection produces context compression outputs
4. governed preference-policy changes route through a separate path
5. Cortex routes durable candidates into `Cognee`
6. Cortex routes artifact bodies and revisions into canonical artifact intake
7. `Cognee` processes derived knowledge from those sources

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
