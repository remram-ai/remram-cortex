# Cognee Complete Context Pack

## Purpose

This document is a full working context pack for `Cognee` as a serious Cortex foundation contender.

It is not another short fit memo.

It is meant to answer:

- what `Cognee` actually is today
- what it already solves natively
- what worldview we would need to accept if we build on it
- what storage and service posture makes sense for a serious self-hosted build
- what still has to be custom for Cortex
- where the real migration and architecture risks are

Reviewed on `April 2, 2026`.

## Current Read

`Cognee` deserves a real deep dive.

After a fuller pass, the important conclusion is:

- it is more than a retrieval subsystem
- it already has a meaningful memory lifecycle shape
- it is unusually extensible
- it is a strong wildcard if you are comfortable with a multi-store architecture
- it still has more long-term model risk than `Graphiti`
- it still has more operational and architectural complexity than `Mem0`

Bluntly:

- `Graphiti` is still the strongest authority-model fit
- `Mem0` is still the easiest fast-path foundation
- `Cognee` is the most interesting "platform kit" option if you want richer extensibility without going fully custom

## What Cognee Is Natively

`Cognee` is a knowledge engine built around four main operations:

- `add`
- `cognify`
- `search`
- `memify`

That matters because it already sees memory as a staged system, not as a single retrieval call over a vector index.

From current docs and source, it already includes:

- dataset-scoped ingestion
- graph construction from documents and text
- semantic plus graph-aware search
- enrichment pipelines over an existing graph
- sessions and cache-backed short-term conversational memory
- permissions, tenants, roles, and dataset ACL surfaces
- HTTP API
- MCP server
- OpenClaw integration
- custom `DataPoint` models
- custom `Task` and pipeline composition
- community adapters for additional databases

That is a serious platform surface.

## Native Data Model

The most important native unit in `Cognee` is the `DataPoint`.

That is a stronger primitive than a casual first read suggests.

Official docs describe `DataPoints` as atomic units of knowledge, shared across the relational, vector, and graph layers through the same `id`.

Key implications:

- the durable unit is not just a chunk
- it can be a structured Pydantic object
- it can create graph relationships directly
- it controls its own vector indexing through `metadata.index_fields`
- it can be grouped through `belongs_to_set`

This is the best reason not to dismiss `Cognee` too quickly.

If we want a foundation that can evolve from extracted document memory into more explicit structured objects, `DataPoint` is a believable bridge.

## Architecture Shape

`Cognee` is explicitly multi-store.

Its own architecture docs say no single database handles all aspects of memory, so it combines:

- relational store for documents, metadata, provenance, and system state
- vector store for embeddings and semantic similarity
- graph store for entities and relationships

That is not accidental.

It is the intended architecture.

This matters for Cortex because it means `Cognee` already separates:

- source tracking
- semantic recall
- structural memory

from the start.

## Cortex Mapping

| Cortex concern | Closest Cognee equivalent | Accept the Cognee way? | Custom work still needed |
| --- | --- | --- | --- |
| Durable memory authority | `DataPoint` plus dataset-scoped graph/vector/relational state | Partly | Add stronger canonical contract and inspection layer |
| Memory lifecycle | `add -> cognify -> search -> memify` | Yes | Add Cortex-specific policy and promotion rules |
| Source-linked evidence | Relational provenance plus document and chunk tracking | Yes, early | Strengthen provenance shape and source references |
| Relationship memory | Graph store with extracted entities and edges | Yes | Refine ontology and retrieval governance |
| Scoped memory | Datasets, permissions, users, tenants, roles | Yes | Standardize Cortex namespace model |
| Session continuity | Cache-backed session memory plus session persistence pipeline | Yes | Decide what should remain short-term vs promoted |
| Semantic retrieval | Vector search across indexed DataPoints and chunks | Yes | Add retrieval traces and stricter ranking policy |
| Structured custom objects | Custom `DataPoint` models and direct graph insertion | Yes | Define Cortex-specific object schemas |
| Tooling surfaces | HTTP API, MCP, OpenClaw plugin | Yes | Add thin policy wrappers where needed |
| Dream-like maintenance | `memify` pipelines | Yes, directionally | Add explicit promotion and review semantics |

The key judgment is:

`Cognee` can play the authority role if we accept that the authority is a dataset-scoped knowledge platform built out of `DataPoints`, not a single monolithic object store.

## What To Accept The Cognee Way

If we build on `Cognee`, we should accept several things instead of fighting them.

### 1. Accept datasets as the primary storage boundary

`Cognee` thinks in datasets.

That means:

- ingestion is dataset-scoped
- permissions are dataset-scoped
- processing is dataset-scoped
- search is dataset-aware

This is a good fit if we want clean memory partitions.

It is a worse fit if we want one giant undifferentiated global memory pool.

### 2. Accept multi-store architecture early

With `Cognee`, the three-store split is fundamental, not optional.

That buys:

- better separation of concerns
- cleaner provenance storage
- graph plus semantic retrieval

But it also means:

- more moving parts
- more operational coupling
- more configuration surface

### 3. Accept `DataPoint` as the phase-1 durable unit

This is the right way to use `Cognee`.

Do not reduce it to only text chunks and generic graph extraction.

If we choose `Cognee`, we should use:

- built-in document and summary `DataPoints`
- custom `DataPoints` for higher-value structured memory
- `NodeSet` grouping where lightweight scoping is enough

### 4. Accept `memify` as the native maintenance surface

`memify` is real.

It is not just a nice label for "do another search."

Official docs and source show it supports:

- default coding-rules enrichment
- triplet embeddings
- session persistence into the graph
- entity consolidation
- custom extraction and enrichment tasks

That is close enough to a Cortex maintenance layer that we should build around it, not around a replacement system.

### 5. Accept short-term session memory as separate from graph memory

`Cognee` explicitly distinguishes:

- session cache memory
- durable graph memory

That is good.

It means the short-term conversational layer does not have to be treated as permanent memory until a pipeline promotes it.

## Strongest Self-Hosted Posture

For a serious self-hosted `Cognee` build, I would not use the file-backed default stack.

I would use:

- `Cognee API`
- `Cognee MCP`
- `Postgres` for relational state
- `pgvector` for vector storage
- `Neo4j` for graph storage
- `Redis` for sessions and cache

Why this is the strongest posture:

- `Postgres` is the documented production relational choice
- `pgvector` is first-class, not community-only
- `Neo4j` is the documented production graph choice
- `Redis` is the best session backend for shared or multi-process execution
- all four work cleanly as dockerized services

This is the best version of `Cognee` to compare against `Mem0` and `Graphiti`.

## OpenSearch Posture

The OpenSearch story is better than the earlier memo implied, but still not a reason to choose `Cognee`.

Current nuance:

- core `Cognee` docs do not list `OpenSearch` as a core vector backend
- current core repo source does not contain built-in OpenSearch support
- current community docs list `OpenSearch` as a community-maintained vector adapter
- the `cognee-community` repo README now lists `cognee-community-vector-adapter-opensearch`

So:

- `OpenSearch` is now a plausible extension path
- it is not a first-class core path
- I would not treat it as a stable default architecture decision for `Cognee` yet

If OpenSearch is the whole reason to choose a foundation, `Cognee` is still not the best match.

## Built-In Extension Points

`Cognee` has one of the strongest extension surfaces in the field.

### Data model seams

- custom `DataPoint` models
- explicit control over indexed fields
- direct graph relationships between `DataPoints`
- `NodeSet` grouping

### Pipeline seams

- custom `Task` objects
- custom pipelines
- built-in pipeline executor and background execution modes
- explicit extraction and enrichment separation in `memify`

### Database seams

- swappable relational, vector, and graph providers
- dataset database handlers
- community adapters for additional vector, graph, and hybrid stores

### Runtime seams

- Python API
- HTTP API
- MCP server with standalone and shared API modes
- OpenClaw integration

That means `Cognee` is highly usable if the plan is:

- start with defaults or near-defaults
- gradually replace or extend specific layers
- keep the core lifecycle operations intact

## What Still Has To Be Custom

Even on the optimistic read, `Cognee` does not eliminate the main Cortex work.

We still need custom work for:

- a stricter canonical memory-object contract
- artifact and provider identity
- stronger provenance normalization
- governance-first retrieval policy
- retrieval traces and operator inspection
- promotion rules and review semantics
- a final export shape not tied to Cognee internals

The difference is that `Cognee` gives more internal extension points than most contenders, so more of that work can be layered in rather than replacing the system.

## Hard Edges

`Cognee`'s real hard edges are clearer after the deeper pass.

### 1. Permission mode and backend routing are constrained

Docs say backend access control is on by default and organize storage by user and dataset.

Source shows built-in dataset database handlers are currently limited to:

- `lancedb`
- `pgvector`
- `kuzu`
- `neo4j_aura_dev`

That means a serious self-hosted `Neo4j` deployment with automatic per-dataset backend routing is not fully turnkey today.

This is an inference from source and docs together:

- docs present Neo4j as the production graph choice
- source currently exposes `neo4j_aura_dev` as the built-in Neo4j dataset handler

So if we want secure dataset-routed backend isolation on self-hosted Neo4j, we should assume some custom handler work.

### 2. Configuration changes are not cheap

Official setup docs explicitly recommend pruning before re-cognifying when switching providers or changing configuration.

Official cognify docs also say schema changes may require:

- deleting the dataset
- re-adding source files
- re-running cognify

That is a real long-term risk signal.

It does not disqualify `Cognee`, but it does mean the early storage and model choices matter.

### 3. The authority model is still platform-shaped, not canonical-memory-shaped

`DataPoint` is a strong primitive, but `Cognee` still feels like:

- a memory platform
- a graph-plus-vector processing engine
- a customizable knowledge runtime

more than it feels like one opinionated canonical memory authority model.

That is both its strength and its risk.

## Main Risks

The real risks are:

- more moving parts than `Mem0`
- more architectural indirection than `Graphiti`
- dataset/backend access control complexity
- higher chance of prune-and-rebuild moments when schemas or providers change
- more temptation to over-customize because the extension surface is so large

If we choose `Cognee`, we need discipline.

The right use is:

- extend selectively
- standardize one durable `DataPoint` contract
- keep one storage posture stable early

The wrong use is:

- continuously swapping providers
- using community adapters casually in a core path without validation
- building multiple parallel semantics for the same memory object

## Long-Term Migration Risk

`Cognee` has moderate migration risk.

Why it is not low:

- its authority shape is platform-centric
- provider changes can require pruning
- dataset-routing and access-control behavior depends on provider/handler compatibility

Why it is not high:

- `DataPoint` is a real durable primitive
- datasets and permissions are strong boundaries
- the API surface is broad
- custom tasks and models reduce the need for a hard fork early

My practical read is:

- lower model regret than storage-only systems
- higher model regret than `Graphiti`
- roughly comparable or slightly higher long-term complexity risk than `Mem0`

## Recommended Build Posture If We Choose Cognee

If `Cognee` is the foundation, the right posture is:

1. Treat `DataPoint` as the phase-1 canonical memory unit.
2. Use one stable dockerized stack: `Postgres + pgvector + Neo4j + Redis`.
3. Keep `Cognee` as the only memory authority, not one component among several competing stores.
4. Build Cortex semantics through custom `DataPoints`, targeted tasks, and policy wrappers.
5. Avoid community adapters in the critical path unless we validate them first.

That keeps the architecture coherent.

## Phase-0 Spike Questions

Before committing, the most useful spike questions are:

1. Can we define one Cortex-shaped `DataPoint` family that survives forward without a rebuild?
2. Does the `Postgres + pgvector + Neo4j + Redis` stack behave cleanly under real dataset and permission flows?
3. How much custom work is required to make self-hosted `Neo4j` behave well under backend access control?
4. How often do storage or schema changes force prune-and-rebuild in practice?
5. Can we get a useful Cortex inspection surface from Cognee’s API and MCP without building too much custom tooling?
6. Does the OpenClaw integration plus Cognee API already cover enough lifecycle to get a usable first system quickly?

## Blunt Recommendation

`Cognee` is worth deep consideration, but it is still my third choice behind `Graphiti` and `Mem0`.

Use it if you want:

- a highly extensible memory platform
- real graph plus vector plus relational separation
- stronger custom object and pipeline control than `Mem0`
- a serious dockerized service posture

Do not use it if your real priority is:

- the cleanest canonical authority model
- the lightest operational burden
- minimal ambiguity about long-term storage semantics

That is where `Graphiti` and `Mem0` still stay ahead.

## Source Map

- https://github.com/topoteretes/cognee
- https://github.com/topoteretes/cognee/blob/main/README.md
- https://github.com/topoteretes/cognee/blob/main/pyproject.toml
- https://github.com/topoteretes/cognee/blob/main/docker-compose.yml
- https://github.com/topoteretes/cognee/blob/main/cognee/api/client.py
- https://github.com/topoteretes/cognee/blob/main/cognee/context_global_variables.py
- https://github.com/topoteretes/cognee/blob/main/cognee/modules/memify/memify.py
- https://github.com/topoteretes/cognee/blob/main/cognee/modules/search/types/SearchType.py
- https://github.com/topoteretes/cognee/blob/main/cognee/modules/search/methods/get_search_type_retriever_instance.py
- https://github.com/topoteretes/cognee/blob/main/cognee/infrastructure/databases/dataset_database_handler/supported_dataset_database_handlers.py
- https://github.com/topoteretes/cognee-community
- https://docs.cognee.ai/getting-started/introduction
- https://docs.cognee.ai/core-concepts/architecture
- https://docs.cognee.ai/core-concepts/building-blocks/datapoints
- https://docs.cognee.ai/core-concepts/building-blocks/tasks
- https://docs.cognee.ai/core-concepts/main-operations/cognify
- https://docs.cognee.ai/core-concepts/main-operations/memify
- https://docs.cognee.ai/core-concepts/further-concepts/datasets
- https://docs.cognee.ai/core-concepts/multi-user-mode/multi-user-mode-overview
- https://docs.cognee.ai/core-concepts/sessions-and-caching
- https://docs.cognee.ai/setup-configuration/overview
- https://docs.cognee.ai/setup-configuration/relational-databases
- https://docs.cognee.ai/setup-configuration/vector-stores
- https://docs.cognee.ai/setup-configuration/graph-stores
- https://docs.cognee.ai/setup-configuration/permissions
- https://docs.cognee.ai/setup-configuration/community-maintained/overview
- https://docs.cognee.ai/guides/custom-data-models
- https://docs.cognee.ai/integrations/openclaw-integration
- https://docs.cognee.ai/cognee-mcp/mcp-overview
- https://docs.cognee.ai/cognee-mcp/mcp-tools
