# Mem0 + Weaviate Vector-First OpenClaw Architecture

## Purpose

This memo defines the intended lifecycle architecture for:

- `OpenClaw` as runtime shell
- `Mem0 OSS` as memory authority
- `Weaviate` as vector and retrieval substrate
- graph added later as a derived reflection layer

This is the architecture version of the current preferred path.

Reviewed on `April 3, 2026`.

## Executive Take

This is the most coherent way to keep the first build practical while still leaving room for a more Cortex-shaped future.

The architecture works because the roles are clean:

- `OpenClaw` handles runtime
- `Mem0` handles memory lifecycle
- `Weaviate` handles storage and advanced retrieval substrate concerns
- Cortex handles contract, provenance, reflection, and promotion

The main discipline is simple:

- only `Mem0` is authoritative for durable memory
- everything else is projection, retrieval infrastructure, or runtime plumbing

## The Core Rule

Canonical memory lives in `Mem0`.

Everything else is derived from it or points back to it.

That means:

- raw artifacts are not the memory authority
- `OpenClaw` transcripts are not the memory authority
- derived `Weaviate` graph objects are not the memory authority
- a later hybrid search facade is not the memory authority

This single rule prevents almost all long-term confusion.

## High-Level Shape

```text
Channels / CLI / Apps
        |
        v
OpenClaw Runtime
  - agent execution
  - hooks
  - tools
  - session lifecycle
  - stock Mem0 plugin first
        |
        v
Mem0 Authority Layer
  - extraction
  - add / update / delete / none
  - canonical memory ids
  - metadata
  - history
  - vector-first recall
        |
        v
Weaviate Authority Substrate
  - Mem0-owned vector storage
  - Mem0-owned filterable objects
  - optional direct hybrid search facade later
        |
        +--> Artifact Intake Worker
        |     - external sources
        |     - text or image extraction
        |     - memory writes through Mem0 only
        |
        +--> Graph Reflection Worker
        |     - entity extraction
        |     - relation extraction
        |     - cluster building
        |     - contradiction and promotion hints
        |     - writes derived Cortex collections into Weaviate
        |
        +--> Optional Retrieval Facade
              - direct Weaviate hybrid retrieval
              - resolve memory ids back to Mem0
              - attach graph expansion context
```

## Phase Boundaries

### Phase 1

Only these are live:

- `OpenClaw`
- stock `Mem0` plugin
- `Mem0 OSS`
- `Weaviate`

Retrieval is:

- stock Mem0 vector search
- metadata filters
- optional reranker

No graph yet.
No custom retrieval facade yet.

### Phase 2

Add artifact intake discipline.

Still:

- all durable writes flow through Mem0
- artifacts remain external

### Phase 3

Add derived graph reflection.

This means:

- create Cortex-owned derived collections in Weaviate
- build entity, relation, and cluster structures from canonical memories
- keep all graph outputs rebuildable

### Phase 4

Only if needed, add hybrid retrieval facade.

That facade:

- queries the `CortexMemoryProjection` collection in Weaviate using hybrid search
- returns `memory_id`
- resolves to Mem0 canonical records
- optionally attaches graph context

This is the right place to get hybrid retrieval if stock Mem0 proves too narrow.

## Artifact Lifecycle

### Source of truth

Artifacts remain in:

- Git
- Google Docs
- other providers later

### Intake path

1. detect or receive artifact input
2. extract text or multimodal signals
3. normalize provenance fields
4. write to Mem0
5. attach artifact metadata to canonical memory
6. emit reflection event

### Required metadata

Every artifact-derived canonical memory should include:

- `artifact_id`
- `artifact_revision_id` when available
- `provider`
- `source_kind`
- `source_uri` or lookup pointer
- optional ingestion timestamp

## Retrieval Ladder

This architecture keeps the retrieval ladder explicit.

### First pass

- query Mem0
- return compact canonical memories

### Second pass

- if needed, use direct Weaviate hybrid search through the facade
- resolve back to canonical memory ids

### Third pass

- if needed, attach graph-derived context
- nearby entities
- nearby relations
- cluster summaries
- contradiction hints

### Final pass

- resolve back to raw artifact only when necessary

This preserves bounded retrieval and keeps graph in the right role.

## Why Graph Lives In Reflection

Graph should not live in the write path initially because:

- first-pass authority should stay simple
- graph semantics are still a hypothesis to validate
- Mem0 already gives a workable retrieval surface without it
- out-of-process reflection is easier to inspect, replay, and rebuild

This also matches the Cortex instinct that higher-order maintenance belongs outside the hot path.

## Derived Collections Design

### `CortexMemoryProjection`

Purpose:

- bridge between authoritative Mem0 records and advanced `Weaviate` retrieval

Fields:

- `memory_id`
- text
- scope
- artifact fields
- timestamps
- confidence
- salience if later needed

### `CortexEntity`

Purpose:

- structured entity projection

Fields:

- `entity_id`
- label
- type
- aliases

### `CortexRelation`

Purpose:

- explicit relation projection

Fields:

- `relation_id`
- relation type
- source entity ref
- target entity ref
- supporting memory refs

### `CortexCluster`

Purpose:

- promotion and neighborhood surface

Fields:

- `cluster_id`
- title
- summary
- member refs
- promotion state

These collections are derived and rebuildable.
They are not canonical authority.

## What Mem0 Should Continue To Own

Do not replace Mem0’s native behaviors early.

Mem0 should continue to own:

- memory capture decisions
- updates and merges
- deletes and no-op decisions
- canonical memory ids
- standard search
- scope model
- history

If we override all of that immediately, the foundation choice was wrong.

## What Cortex Should Own

Cortex should own:

- metadata contract
- provenance normalization
- artifact identity
- artifact intake worker
- graph reflection worker
- contradiction review surfaces
- retrieval tracing
- optional hybrid retrieval facade
- support-summary and promotion policy

That is the right custom layer.

## Where Weaviate Actually Adds Value

`Weaviate` matters here in four ways:

1. it gives the base Mem0 path a stronger long-term vector substrate
2. it gives us a plausible later hybrid retrieval surface
3. it gives us enough reference support to host a derived graph projection
4. it lets us keep these capabilities inside one local service family for a while

That is a stronger reason to choose it than generic "better database" talk.

## Risks

The biggest risks are:

- trying to force graph into primary retrieval too early
- overusing Weaviate cross-references as if it were a dedicated graph database
- letting derived projections drift from canonical Mem0 memory ids
- adding a hybrid retrieval facade before baseline vector retrieval has been validated

## Recommendation

This should be treated as the target lifecycle architecture for the current preferred path.

Bluntly:

- start stock
- keep Mem0 authoritative
- use Weaviate for vector now
- add hybrid only through a thin facade when it becomes worth it
- add graph in reflection and keep it derived

That is the cleanest architecture found so far for staying practical without flattening Cortex into plain vector search.

