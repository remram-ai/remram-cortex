# Mem0 + Weaviate Vector-First Complete Context Pack

## Purpose

This document is the full context pack for the currently favored `Mem0` path:

- `Mem0 OSS` as the memory authority
- `Weaviate` as the vector storage substrate
- `OpenClaw` as the runtime shell
- graph added later as a derived reflection layer, not as the initial authority model

This is not just another contender memo.

It is meant to answer:

- what this stack actually is
- why it is a stronger fit than the earlier generic `Mem0 + Weaviate` framing
- what should be accepted the platform way
- what still has to be custom for Cortex
- where the real risks and extension seams are

Reviewed on `April 3, 2026`.

## Current Read

This is the strongest `Mem0` variant considered so far.

Bluntly:

- it keeps the first build on the most proven memory foundation we have found
- it keeps first-pass retrieval vector-first and easy to reason about
- it gives us a cleaner long-term search posture than the lighter `Qdrant` path
- it leaves room for graph, reflection, clustering, and hybrid retrieval later without forcing those into the authority model up front

It is not the lightest `Mem0` path.
But it is the one that best balances:

- practical buildability
- future retrieval headroom
- respect for the original Cortex direction
- low likelihood of early architectural regret

## What This Stack Is Natively

### `Mem0`

`Mem0` is the lifecycle engine.

It already owns:

- extraction of candidate memories
- add, update, delete, or none decisions
- scope handling through `user_id`, `agent_id`, and `run_id`
- history
- metadata filters
- rerankers
- official `OpenClaw` integration

That means it is still the memory product in this architecture.
It is not just a thin wrapper around `Weaviate`.

### `Weaviate`

`Weaviate` is the storage and retrieval substrate.

It natively gives us:

- vector storage
- rich metadata filters
- hybrid lexical plus vector search
- reranking modules
- cross-references between objects
- local Docker deployment
- collection aliases and decent schema-evolution ergonomics

The important nuance is that `Mem0` does not expose the whole raw `Weaviate` surface by default.

So the right stance is:

- use the stock `Mem0 -> Weaviate` adapter for phase 1
- use direct `Weaviate` access later only through a thin Cortex retrieval or reflection layer

### `OpenClaw`

`OpenClaw` is the runtime shell.

It already gives us:

- tool hosting
- session lifecycle
- prompt-time memory injection
- post-turn capture points
- CLI
- hook packs
- a documented `Mem0` integration

That means the runtime bridge is already largely solved.

## Why This Path Is Different From Earlier Mem0 Paths

Earlier `Mem0` evaluations mostly split into two shapes:

- fastest path: `Mem0 + OpenClaw + Qdrant`
- stronger storage posture: `Mem0 + Weaviate + OpenClaw`

The missing piece was architectural intent.

The improved read is:

- `Weaviate` is not just a nicer vector backend
- it is the right base if we want to stay vector-first now, then layer in hybrid retrieval and graph reflection later

That makes this path more than "Mem0 with a different database."

It becomes:

- vector-first memory authority
- hybrid-ready retrieval substrate
- graph-friendly reflection substrate

without forcing graph-first memory too early.

## Native Durable Unit

The canonical durable unit is still a disciplined `Mem0` memory record.

That is important.

The memory record should carry:

- stable memory id
- concise canonical text
- scope fields
- artifact and provenance metadata
- timestamps
- optional confidence or status metadata

This should stay true even after graph reflection appears.

Graph outputs must point back to canonical memory ids.

## Why Vector-First Authority Is Actually A Strength

For this stack, vector-first is not a compromise to apologize for.

It is the reason the architecture is sane.

It means:

- retrieval starts with a proven, inspectable search path
- the write path stays simple
- artifact-backed memory remains understandable
- graph has to earn its role instead of being assumed

This is closer to the original Cortex design than a graph-first rewrite because the original design already assumed:

- canonical objects
- bounded retrieval
- support-layer expansion
- higher-order maintenance outside the hot path

This path keeps those ideas intact.

## Artifact Handling

This stack is good for artifact-derived memory if we keep the boundary clean.

The right rule is:

- artifacts live in external systems
- `Mem0` stores extracted durable memories plus artifact references
- `Weaviate` stores the searchable projection of those canonical memories
- graph reflection works from canonical memories, not directly from raw documents as authority

### What Mem0 helps with

`Mem0` already gives useful seams for artifact intake:

- custom fact extraction prompts
- custom update prompts
- multimodal support for images
- metadata and categories

That is enough to support:

- note and doc ingestion
- image-derived memory
- screenshot-derived memory
- artifact-linked update and correction behavior

### What should remain outside

Do not put raw artifact authority into `Mem0`.

Keep outside:

- full Git content
- Google Docs storage
- binary artifacts
- raw corpora
- final promoted artifact bodies

Store in `Mem0` metadata:

- `artifact_id`
- `artifact_revision_id`
- `provider`
- `source_kind`
- `source_uri` or lookup pointer

That preserves inspectable provenance without overloading the memory store.

## Retrieval Shape

### Phase 1

Use stock `Mem0` retrieval:

- vector search
- metadata filters
- thresholds
- optional reranking

This is the hot path.

### Phase 2

Add an optional thin retrieval facade over `Weaviate` for hybrid search.

That facade should:

- query a derived search projection in `Weaviate`
- use lexical plus vector hybrid retrieval
- return canonical `memory_id` values
- resolve those ids back to authoritative `Mem0` records

This is important:

- `Mem0` remains the authority
- `Weaviate` can still do more advanced retrieval than stock Mem0 exposes

### Phase 3

Add graph enrichment after first-pass retrieval:

- neighborhood context
- related entities
- contradiction hints
- cluster summaries

That graph context should remain expansion, not first-pass ranking, until it proves value.

## Graph Reflection Shape

Graph should be generated out of process from authoritative memories.

That means:

- the worker reads new or updated canonical memories
- extracts entities and relations
- builds graph projections and clusters
- writes them into derived collections inside `Weaviate`

Why `Weaviate` is acceptable here:

- it supports cross-references
- it supports filters over references
- it is already in the stack
- graph here is projection, not the only truth

Important caveat:

`Weaviate` itself warns that cross-references can hurt performance and are not always the best schema shape at scale.

That is acceptable here because:

- this graph is not the primary search engine
- it is used for bounded reflection and enrichment
- it can be rebuilt

So phase-2 graph in `Weaviate` is credible as long as we do not pretend it is a general-purpose graph analytics system.

## Derived Weaviate Schema Worth Planning For

The best shape is to keep the authoritative Mem0 collection untouched and create derived Cortex collections beside it.

Suggested derived collections:

- `CortexMemoryProjection`
- `CortexEntity`
- `CortexRelation`
- `CortexCluster`

### `CortexMemoryProjection`

Minimal derived copy keyed by canonical `memory_id`.

Store:

- `memory_id`
- canonical text
- scope fields
- artifact identifiers
- timestamps
- optional confidence or salience

This collection is useful for:

- hybrid search facade
- graph linking
- operator inspection

### `CortexEntity`

Store:

- entity id
- entity label
- entity type
- aliases
- supporting memory ids

### `CortexRelation`

Store:

- relation id
- source entity id
- target entity id
- relation type
- supporting memory ids
- confidence

### `CortexCluster`

Store:

- cluster id
- title or summary
- member memory ids
- member entity ids
- promotion state

This is enough to support:

- graph expansion
- contradiction review
- promotion candidates
- neighborhood views

without moving authority away from `Mem0`.

## Extension Surface We Should Actually Exploit

### Mem0 seams

- custom fact extraction prompts
- custom update prompts
- custom categories
- metadata filters
- rerankers
- multimodal support
- graph memory if useful later
- official `OpenClaw` plugin

### Weaviate seams

- hybrid search
- rich filters
- object references
- reranking
- aliases for safer schema migration
- local Docker deployment

### OpenClaw seams

- memory plugin slot
- prompt build hooks
- after-turn hooks
- tools
- services
- CLI

The important part is to use these as layers, not all at once.

## What Still Has To Be Custom

Even on the optimistic read, this stack does not eliminate the Cortex work.

We still need:

- metadata contract
- artifact intake normalization
- provenance normalization
- retrieval tracing
- graph reflection worker
- contradiction and supersession review
- support-summary layer
- promotion policy
- operator inspection surfaces
- optional hybrid retrieval facade

This is still real work.
It is just the right kind of work.

## Main Risks

The real risks are:

- we overbuild graph before it proves value
- the Mem0/Weaviate adapter remains narrower than we want and we have to add a small retrieval facade earlier
- graph projection drifts from canonical memory if the sync contract is sloppy
- cross-reference-heavy Weaviate graph structures get overused and become slow or messy
- the team starts treating derived graph objects as authority instead of projection

## Why This Path Is Stronger Than Plain Mem0

Compared with simpler `Mem0` paths, this one gives us:

- better long-term search posture
- a clean route to hybrid retrieval later
- a cleaner route to graph reflection later
- fewer reasons to replatform just because retrieval got smarter

## Why This Path Is Safer Than Graph-First

Compared with `Graphiti` or another graph-first path, this one gives us:

- lower first-build complexity
- simpler provenance
- clearer authority boundaries
- stronger official OpenClaw integration
- less epistemic overcommitment

## Blunt Recommendation

If the current question is "what Mem0 path best matches Cortex without forcing graph-first architecture too early?", this is the answer.

Bluntly:

- choose `Mem0`
- use `Weaviate` as the vector substrate
- keep retrieval vector-first at first
- add hybrid retrieval through a thin facade only when it pays for itself
- add graph in reflection as a derived layer, not as authority

That is the cleanest serious path found so far.

## Source Map

- https://docs.mem0.ai/integrations/openclaw
- https://docs.mem0.ai/components/vectordbs/dbs/weaviate
- https://docs.mem0.ai/open-source/features/reranker-search
- https://docs.mem0.ai/open-source/graph_memory/overview
- https://docs.mem0.ai/platform/features/graph-memory
- https://docs.weaviate.io/weaviate/search/hybrid
- https://docs.weaviate.io/weaviate/search/filters
- https://docs.weaviate.io/weaviate/tutorials/cross-references

