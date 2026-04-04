# Graphiti Complete Context Pack

## Purpose

This document is a full working context pack for `Graphiti` as a long-term foundation candidate for `remram-cortex`.

It is meant to answer:

- what `Graphiti` actually is today
- what parts of the Cortex direction it already matches unusually well
- what worldview we would need to accept if we build on it
- what service and storage posture makes sense
- what still has to be custom
- how much long-term regret risk we take if we start here

Reviewed on `April 2, 2026`.

## Current Read

`Graphiti` remains the strongest long-term authority-model fit of the practical contenders.

Bluntly:

- it already thinks in episodes, entities, facts, and temporal validity
- it already handles contradiction and invalidation more like a real memory system than a typical agent memory product
- it already supports hybrid retrieval, filtering, and ontology customization
- its data model looks much closer to a plausible final Cortex authority than `Mem0`'s record-centric model
- the price is higher implementation and operational burden

Under a normal solo-builder lens, `Mem0` is easier.

Under your stated "AI is doing most of the building" lens, `Graphiti` becomes more attractive because the remaining gap is more integration and policy than greenfield invention.

## What Graphiti Is Natively

`Graphiti` is a temporal knowledge-graph framework for dynamic agent context.

Its native behavior already includes:

- episodic ingestion from text, messages, or JSON
- extraction into entities and facts
- explicit temporal validity fields
- automatic invalidation of contradicted facts
- hybrid retrieval across embeddings, BM25, and graph structure
- graph partitioning through `group_id`
- customizable entity and edge types via Pydantic models
- maintenance primitives such as community building
- direct library use, a FastAPI service, and an experimental MCP server

This is not "vector memory with graph flavor."

It is a real graph-shaped memory lifecycle system.

## Native Data Model

The most important reason `Graphiti` stayed in the top two is its durable model.

Its primitives are already close to what a memory authority should store:

- `Episode`: source evidence or observed event
- `Entity`: stable things the system knows about
- `EntityEdge`: facts or relationships between entities
- `valid_at`, `invalid_at`, `expired_at`: temporal semantics for fact lifecycle
- `Community`: higher-level clustered graph structures
- `Saga`: an additional grouping construct for related sequences
- `group_id`: namespace or partition boundary

This matters more than almost any feature checkbox.

If the stored object model is already good, later feature work compounds.

If the stored object model is wrong, later feature work becomes translation and migration work.

## Cortex Mapping

| Cortex concern | Closest Graphiti equivalent | Accept the Graphiti way? | Custom work still needed |
| --- | --- | --- | --- |
| Durable memory authority | Episode plus entity plus fact graph | Yes | Add Cortex policy surfaces and inspection |
| Source evidence | Episodes | Yes | Add stricter provenance fields where needed |
| Canonical fact object | Entity edge | Yes | Add artifact/provider identity where needed |
| Temporal truth and correction | `valid_at`, `invalid_at`, `expired_at` plus invalidation | Yes | Tune policy and reviewability |
| Multi-tenant or partitioned memory | `group_id` | Yes | Standardize namespace rules |
| Retrieval | Hybrid search recipes plus filters | Yes | Add governance wrapper and retrieval traces |
| Ontology evolution | Custom entity and edge types | Yes | Define a Cortex-specific ontology contract |
| Dream-like maintenance | Community building and maintenance jobs | Partly | Add explicit reflection or promotion jobs |
| Operator interfaces | FastAPI service and MCP server | Yes | Decide whether MCP is primary or sidecar |
| Storage authority | Neo4j-first graph backend | Yes | Keep raw DB writes out of app code |

This is why `Graphiti` is so compelling.

The core question is not "can Graphiti do memory."

The real question is "are we comfortable accepting a graph-first authority model from the beginning."

## What To Accept The Graphiti Way

If we choose `Graphiti`, we should deliberately accept its worldview instead of sanding it down into generic document memory.

### 1. Accept episodes as first-class evidence

Do not collapse everything into immediately rewritten summaries.

Let observed conversations, imported documents, and structured events enter the system as episodes.

### 2. Accept facts as relationships, not just rows

The native durable knowledge object in `Graphiti` is much closer to a graph fact than to a flat note.

That is a strength, not a liability, if Cortex really wants durable structured memory.

### 3. Accept temporal semantics early

`Graphiti` is strongest when we keep:

- when something became true
- when it stopped being true
- what episode supported it

That is exactly the kind of early architectural decision that reduces later regret.

### 4. Accept graph partitioning as a core namespace mechanism

`group_id` is not just a handy filter.

It is a real partitioning primitive and can cleanly support:

- per-user graphs
- per-agent graphs
- per-project or per-workspace graphs

### 5. Accept that "Dream" is not the main differentiator

`Graphiti` already gives enough maintenance shape that missing a named Dream cycle is not a reason to reject it.

Community building, re-indexing, targeted repair, and explicit maintenance jobs are already enough to support a later reflective layer.

## Service and Deployment Posture

`Graphiti` gives three main ways to use it.

### 1. Direct library integration

Best when:

- we want maximal control
- we are comfortable owning the ingestion and retrieval calls directly
- we want the thinnest possible architecture

### 2. FastAPI service

Best when:

- we want a clean process boundary
- we want a stable HTTP surface between runtime shell and memory engine
- we want a dockerized memory service

The service already exposes:

- queued message ingestion
- search
- memory retrieval from messages
- delete and clear operations

### 3. MCP server

Best when:

- we want immediate assistant tooling
- we want operator or IDE access
- we want a sidecar inspection surface

I do not currently think the MCP server should be the primary authority integration for Cortex.

It is more useful as a convenience and inspection surface than as the main runtime bridge.

## Storage Posture

`Graphiti` is graph-first.

That single fact should dominate storage decisions.

### Default posture

The default serious posture is:

- `Neo4j` as the graph database
- `Graphiti` as the only write authority over that graph

This is still the cleanest production-shaped route.

### Other backend notes

Upstream now also shows:

- `FalkorDB` support
- `Kuzu` support
- `Neptune` support
- a `neo4j-opensearch` optional extra in `graphiti-core`

Important nuance:

- `Neo4j` is still the main documented serious path
- the `neo4j-opensearch` extra does not currently read like "replace Neo4j with OpenSearch"
- it looks more like a supporting integration posture than a new primary authority model
- `Neptune` explicitly uses `OpenSearch` as a full-text backend

So for local or dockerized use, the honest answer is still:

- `Neo4j` is the right default store if we choose `Graphiti`
- `OpenSearch` is not the primary reason to choose `Graphiti`

## Search and Retrieval Strength

`Graphiti` is unusually strong here.

It already includes configurable search recipes that combine:

- BM25
- cosine similarity
- hybrid retrieval
- node distance reranking
- episode mention reranking
- MMR and RRF-style combinations
- cross-encoder recipes
- temporal and property filters

That matters because Cortex does not only need memory storage.

It needs inspectable, policy-shaped retrieval over durable memory.

`Graphiti` is much closer to that out of the box than most contenders.

## Built-In Extension Points

`Graphiti` has the right kind of seams for a Cortex-shaped build.

### Data and ontology seams

- custom entity types
- excluded entity types
- custom edge types
- source and source-description on episodes
- `group_id` namespacing
- saga grouping

### Retrieval seams

- alternative search configs
- lower-level `search_` access
- filter objects for labels, edge types, temporal windows, and properties
- center-node and BFS-origin style search shaping

### Runtime seams

- direct Python library
- FastAPI service
- MCP server
- dockerized service image for the FastAPI surface

### Practical meaning for Cortex

This is enough to build Cortex as:

- policy layer
- namespace and ontology contract
- inspection layer
- runtime shell bridge

rather than as a replacement memory engine.

## What Still Has To Be Custom

Even on the optimistic read, `Graphiti` is not "Cortex finished."

We still need custom work for:

- artifact and provider identity
- a first-class Cortex provenance contract above raw episodes
- retrieval tracing and operator inspection surfaces
- explicit governance and permission rules
- document ingestion policy and chunking discipline
- Dream or promotion jobs if we want reflective maintenance naming and reporting
- runtime integration if we want `OpenClaw` or another shell to speak Graphiti cleanly

The good news is that these feel like the right kind of custom work.

They are mostly policy, packaging, and integration work on top of a strong authority model.

## Main Risks

`Graphiti` is not risk-free.

The real risks are:

- heavier operational footprint than `Mem0`
- more graph-model literacy required
- more up-front ontology and namespace decisions
- more care needed around ingestion ordering and maintenance
- potential temptation to bypass Graphiti and write directly to Neo4j

That last one matters a lot.

If we choose `Graphiti`, raw Neo4j should not become the app-facing API.

The memory authority is `Graphiti`, not the database underneath it.

## Long-Term Migration Risk

`Graphiti` has the lowest data-model regret risk of the practical contenders.

Why:

- episodes are durable evidence units
- entities and facts are durable semantic units
- temporal validity is first-class
- contradiction handling already exists
- graph partitioning is native

If Cortex's direction of travel is even roughly "structured, evolving, temporally-aware memory authority," then `Graphiti` starts unusually close to the right shape.

The biggest migration risk is not the model.

It is the operational choice:

- if we later decide we do not want graph-first memory at all, then we would replatform
- if graph-first memory is directionally right, `Graphiti` is a very safe place to begin

## Recommended Build Posture If We Choose Graphiti

If `Graphiti` is the foundation, the right posture is:

1. Keep `Graphiti` as the only durable write authority.
2. Use `Neo4j` as the default local or dockerized store.
3. Put a thin Cortex policy layer above Graphiti, not a parallel object store beside it.
4. Treat episodes as evidence and entity edges as first-class facts.
5. Use the FastAPI service boundary unless direct library integration is clearly simpler.

That keeps the architecture honest.

## Phase-0 Spike Questions

Before committing, the most useful spike questions are:

1. How well does Graphiti handle our real conversation and document shapes as episodes?
2. How inspectable are invalidation and temporal changes for operator trust?
3. How much ontology definition do we need up front before productivity drops?
4. Does the FastAPI service boundary feel sufficient, or do we want a tighter library bridge?
5. What are the real operational costs of `Neo4j` in a dockerized local setup?
6. What export shape should we standardize so a future Cortex layer is not locked to internal Graphiti classes?

## Blunt Recommendation

If you are optimizing for the strongest long-term authority foundation and you accept a graph-first memory model, `Graphiti` is the best primary foundation.

Use it if you want:

- the closest native fit to a durable memory authority
- temporal truth management from the beginning
- lower long-term semantic regret
- a system whose stored model already looks like real memory, not just recallable notes

Do not use it if your real priority is:

- fastest possible path to a useful memory system
- the lightest operational footprint
- minimizing graph complexity early

That is where `Mem0` is stronger.

## Source Map

- https://github.com/getzep/graphiti
- https://github.com/getzep/graphiti/blob/main/README.md
- https://github.com/getzep/graphiti/blob/main/pyproject.toml
- https://github.com/getzep/graphiti/blob/main/graphiti_core/graphiti.py
- https://github.com/getzep/graphiti/blob/main/graphiti_core/edges.py
- https://github.com/getzep/graphiti/blob/main/graphiti_core/nodes.py
- https://github.com/getzep/graphiti/blob/main/graphiti_core/search/search_config_recipes.py
- https://github.com/getzep/graphiti/blob/main/graphiti_core/search/search_filters.py
- https://github.com/getzep/graphiti/blob/main/server/README.md
- https://github.com/getzep/graphiti/blob/main/server/graph_service/routers/ingest.py
- https://github.com/getzep/graphiti/blob/main/server/graph_service/routers/retrieve.py
- https://github.com/getzep/graphiti/blob/main/mcp_server/README.md
- https://help.getzep.com/graphiti/graphiti/overview
- https://help.getzep.com/graphiti/getting-started/quick-start
- https://help.getzep.com/graphiti/working-with-data/searching
- https://help.getzep.com/graphiti/core-concepts/custom-entity-and-edge-types
- https://help.getzep.com/graphiti/core-concepts/graph-namespacing
- https://help.getzep.com/graphiti/getting-started/mcp-server
