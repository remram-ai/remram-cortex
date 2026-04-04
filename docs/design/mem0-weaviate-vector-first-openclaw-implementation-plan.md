# Mem0 + Weaviate Vector-First OpenClaw Implementation Plan

## Purpose

This document is the implementation plan for the currently preferred path:

- `OpenClaw` runtime
- `Mem0 OSS` authority
- `Weaviate` vector substrate
- graph added later through reflection

It covers the full path from a baseline containerized install through artifact integration and later graph and hybrid retrieval expansion.

Reviewed on `April 3, 2026`.

## Blunt Read

This is the right implementation path if the goal is:

- build something real quickly
- keep memory authority understandable
- leave room for graph and hybrid search later
- avoid paying graph-first complexity before it proves value

The right implementation order is:

1. stock `OpenClaw + Mem0 + Weaviate`
2. metadata and provenance discipline
3. artifact intake integration
4. graph reflection worker
5. optional hybrid retrieval facade

Do not invert that order.

## Planning Assumptions

- one builder, heavily AI-assisted
- local Docker deployment is acceptable
- `OpenClaw` remains the runtime shell
- `Mem0` remains the only write authority for durable memory
- `Weaviate` is chosen for vector storage now and retrieval headroom later
- graph starts as a derived, rebuildable layer

## Target End State

```text
OpenClaw
  - sessions
  - tools
  - hooks
  - Mem0 plugin
        |
        v
Mem0
  - canonical memory writes
  - canonical memory search
  - metadata
  - history
        |
        v
Weaviate
  - Mem0-owned vector collection
  - Cortex-owned derived projection collections
        |
        +--> Artifact intake worker
        +--> Graph reflection worker
        +--> Optional hybrid retrieval facade
```

## Phase 0: Environment Baseline

Goal:

- prove the stack starts, persists, and answers memory queries

Containers:

- `openclaw`
- `weaviate`
- optional local LLM and embedding service if not using remote providers

Baseline configuration posture:

- `OpenClaw` uses the official `Mem0` plugin in OSS mode
- `Mem0` points at `Weaviate`
- `Weaviate` runs with persistent volume mounts
- no graph layer yet
- no custom retrieval facade yet

Verification:

- store memories
- search memories
- restart containers
- verify persistence
- verify per-user and per-agent scoping

Exit criteria:

- durable memory works end to end through `OpenClaw`

## Phase 1: Canonical Metadata Contract

Goal:

- make phase-1 memories survive later architecture growth

Add a strict metadata contract for every memory write:

- `memory_type`
- `source_kind`
- `provider`
- `artifact_id`
- `artifact_revision_id`
- `scope_class`
- `confidence_tier`
- `promotion_state`

Implementation posture:

- use `Mem0` prompts and categories first
- add a thin normalization layer before writes if necessary
- do not create a second durable memory store

Verification:

- all new memories are inspectable with consistent metadata
- filters behave predictably

Exit criteria:

- we can explain any memory object from metadata alone

## Phase 2: Artifact Intake Integration

Goal:

- bring external artifacts into memory without flattening raw artifacts into the authority layer

Build a small artifact intake worker that:

1. reads from chosen artifact sources
2. extracts text or multimodal signals
3. normalizes artifact metadata
4. writes extracted memory through Mem0

Recommended first sources:

- Git-backed markdown or docs
- local files
- screenshots or images if useful

Keep out of phase 2:

- full Google Docs sync
- complex bidirectional artifact update workflows

Verification:

- one artifact produces multiple canonical memories with stable provenance fields
- reingesting a changed artifact updates or supersedes memories through Mem0 rather than duplicating blindly

Exit criteria:

- artifact-derived memory is real and inspectable

## Phase 3: Inspection And Retrieval Trace

Goal:

- make the system debuggable before adding more semantics

Add:

- search trace logging
- memory inspection view
- artifact-to-memory inspection
- memory-to-artifact inspection

This can start as:

- CLI helpers
- admin scripts
- lightweight internal endpoints

Exit criteria:

- we can explain why a memory was returned
- we can explain where a memory came from

## Phase 4: Graph Reflection Worker

Goal:

- add graph value without changing the authority model

Build a worker that reads new or updated canonical memories and produces derived `Weaviate` collections:

- `CortexMemoryProjection`
- `CortexEntity`
- `CortexRelation`
- `CortexCluster`

Responsibilities:

- entity extraction
- relation extraction
- memory-to-entity links
- cluster building
- contradiction candidate detection
- promotion candidate detection

Important rule:

- graph output is rebuildable projection
- never write graph objects as canonical memories

Verification:

- projection can be rebuilt from canonical memory
- graph lag does not break normal retrieval

Exit criteria:

- graph enrichment exists without contaminating authority boundaries

## Phase 5: Graph-Enriched Expansion

Goal:

- use graph only where it has already proved useful

Add a bounded expansion path:

1. run normal Mem0 retrieval
2. resolve top memory ids
3. fetch nearby graph context
4. attach compact expansion bundle

Use graph for:

- related entities
- related memories
- cluster context
- contradiction hints

Do not use graph for:

- replacing first-pass ranking
- unrestricted traversal

Exit criteria:

- graph materially improves expansion quality on real tasks

## Phase 6: Optional Hybrid Retrieval Facade

Goal:

- use direct `Weaviate` hybrid retrieval only if stock Mem0 retrieval proves insufficient

Build a thin facade that:

- runs hybrid search against `CortexMemoryProjection`
- returns canonical `memory_id`
- resolves to Mem0 records
- optionally attaches graph context

Why this is phase 6:

- hybrid retrieval should be added because we have evidence it improves results
- not because it feels architecturally elegant

Exit criteria:

- measurable improvement over vector-only baseline on real retrieval cases

## Phase 7: Promotion And Support Layer

Goal:

- move from memory recall to higher-order Cortex behavior

Add:

- support-summary objects or secondary memory surfaces
- promotion candidates from clusters
- artifact proposal flows
- contradiction review UI or workflow

This is where the stack starts to feel recognizably Cortex-like.

## Recommended Container Layout

### Baseline

- `openclaw`
- `weaviate`
- optional `ollama`

### Phase 2 onward

- `artifact-intake-worker`

### Phase 4 onward

- `graph-reflection-worker`

### Phase 6 onward

- `cortex-retrieval-facade`

This keeps the stack incremental.

## Files And Modules To Expect

Suggested repo-level implementation boundaries:

- `deploy/moltbox/mem0-weaviate/compose.yml`
- `plugins/openclaw-mem0-cortex/`
- `services/artifact-intake-worker/`
- `services/graph-reflection-worker/`
- `services/cortex-retrieval-facade/`
- `packages/cortex-memory-contract/`

## What Not To Build Early

Do not build these in phase 0 to phase 2:

- custom memory engine replacing Mem0
- second durable memory authority
- full graph database sidecar
- direct raw Weaviate writes as peer authority
- promotion system before inspection works
- hybrid retrieval facade before vector baseline is tested

## Main Risks And Mitigations

### Risk: adapter ceiling

Problem:

- Mem0’s stock Weaviate adapter may not expose every Weaviate feature we want

Mitigation:

- keep authority in Mem0
- add a thin retrieval facade later instead of forking the whole stack early

### Risk: graph drift

Problem:

- derived graph and canonical memories diverge

Mitigation:

- use canonical `memory_id` everywhere
- make reflection rebuildable
- never allow graph-only truth

### Risk: overusing references in Weaviate

Problem:

- Weaviate cross-references become heavy if treated like a full graph database

Mitigation:

- keep graph bounded and derivative
- use it for expansion and clustering, not full graph-first retrieval

## Time Estimate

AI-assisted, realistic rough estimate:

- first usable baseline: `3 to 7 days`
- artifact-aware memory loop: `1 to 2 weeks`
- graph reflection prototype: `2 to 4 weeks`
- hybrid retrieval facade if needed: `1 additional week`
- credible Cortex-shaped v1 on this stack: `5 to 8 weeks`

## Blunt Recommendation

If we are choosing this path, the implementation philosophy should be:

- stay stock as long as possible
- keep Mem0 authoritative
- use Weaviate for what it is already good at
- let graph arrive as reflection, not doctrine
- only build custom retrieval once the baseline proves where it is weak

That is the right way to keep this path practical and still let it grow into something recognizably Cortex-like.

## Source Map

- https://docs.mem0.ai/integrations/openclaw
- https://docs.mem0.ai/components/vectordbs/dbs/weaviate
- https://docs.mem0.ai/open-source/features/reranker-search
- https://docs.mem0.ai/open-source/graph_memory/overview
- https://docs.mem0.ai/platform/features/graph-memory
- https://docs.weaviate.io/weaviate/search/hybrid
- https://docs.weaviate.io/weaviate/search/filters
- https://docs.weaviate.io/weaviate/tutorials/cross-references
- https://docs.weaviate.io/weaviate/manage-objects/import

