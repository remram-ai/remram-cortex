# Graphiti Foundation Implementation Strategy

## Purpose

This document is the complete implementation strategy and system overview for the chosen Cortex foundation:

- `Graphiti`
- `Neo4j`
- `OpenClaw`
- a small custom Cortex layer

It starts at dependent containers and ends at artifact integration, retrieval shaping, promotion, and operator inspection.

Reviewed on `April 2, 2026`.

## Strategy Summary

The implementation strategy is:

1. stand up the smallest viable container stack
2. build one app-owned memory service that embeds `Graphiti`
3. make deterministic ingest and artifact lineage part of the core, not late hardening
4. connect `OpenClaw` through a dedicated context-engine plugin
5. integrate Git-backed artifacts before adding more providers
6. keep retrieval layered and graph-first
7. add communities and promotion after the authority loop is stable

The main design discipline is:

- one authority graph
- one runtime shell
- one contract layer

## Success Criteria

The stack is successful when it can do all of the following reliably:

- ingest runtime observations into durable graph memory
- ingest Git-backed artifacts and derive durable facts from them
- retrieve compact canonical memory first
- expand to support summaries second
- resolve source artifacts only when needed
- propose promoted artifacts from coherent communities
- keep provenance back to artifacts and episodes
- keep `OpenClaw` free of parallel long-term memory state
- supersede stale derivations when the same artifact lineage changes
- block promoted derivative artifacts from silently reinforcing their own source truth

## Chosen Runtime Topology

The baseline container topology is:

```text
neo4j
  - graph database
  - full-text + vector indexes
  - persisted volume

cortex-memory-service
  - FastAPI app
  - embeds Graphiti library
  - owns schema validation
  - owns retrieval compiler
  - owns artifact + promotion APIs

artifact-sync-worker
  - polls or consumes provider change events
  - normalizes artifacts
  - submits ingest jobs to cortex-memory-service

openclaw-gateway
  - agent runtime
  - context engine plugin
  - tools / hooks / sessions

optional later:
  - graphiti-mcp for operator inspection
  - google-docs-sync-worker
  - lightweight inspector UI
```

Inside `cortex-memory-service`, the system also owns a tiny operational ingest journal.

That journal:

- sequences writes
- stores idempotency keys
- tracks intake state
- supports retry and replay

It is operational reliability infrastructure only.

It is not a second memory authority.

## Why This Topology Wins

This topology keeps the system simple enough to build while preserving the correct long-term seams.

It avoids:

- wrapper service in front of wrapper service
- direct app writes to raw `Neo4j`
- artifact sync logic leaking into OpenClaw
- long-term memory logic leaking into provider adapters

## Resolved Design Decisions

### A. Should we accept a tiny operational queue or ingest journal?

Yes.

The chosen form is:

- a small operational ingest journal owned by `cortex-memory-service`

It exists for:

- ordering
- idempotency
- retry
- auditability

It does not own durable memory truth.

### B. Should human or operator correction write back as first-class episodes or as direct fact-review actions?

Default answer:

- first-class correction episodes

Exception:

- a narrow direct-review admin path is allowed for exceptional operational correction cases

### C. Should artifact reingestion be replace-by-lineage or accumulate-and-reconcile?

Chosen answer:

- replace or supersede by lineage for the same artifact lineage

Use contradiction or invalidation logic primarily across different sources, not for routine edits of the same source lineage.

## Deterministic Ingest Backbone

Deterministic ingest is an early correctness requirement.

Required behaviors from phase 1 onward:

- idempotency keys on every write request
- journaled intake before graph mutation
- per-partition write serialization
- explicit ordering guarantees inside a partition
- deterministic replay handling
- bounded retry and backpressure behavior

Recommended partition key:

- coarse `group_id`

Where needed, a stricter sub-key may be added for high-volume artifact lineages, but the default ordering boundary is the coarse memory partition.

## Intake State Machine

The memory service must expose and persist a lightweight intake state model.

Recommended states:

- `observation_received`
- `accepted_for_extraction`
- `extracted`
- `durable_fact_accepted`
- `superseded`
- `invalidated`
- `rejected`

This state model exists to make the system:

- auditable
- replayable
- debuggable

It is not intended to be a second business workflow system.

## Container Plan

### 1. `neo4j`

Responsibility:

- durable graph persistence

Persistent state:

- `/data`
- `/logs`
- `/plugins` only if later needed

Ports:

- `7474` for Browser
- `7687` for Bolt

Baseline env:

- `NEO4J_AUTH`
- `NEO4J_server_memory_heap_initial__size`
- `NEO4J_server_memory_heap_max__size`
- `NEO4J_server_memory_pagecache_size`

### 2. `cortex-memory-service`

Responsibility:

- app-owned memory contract
- Graphiti orchestration
- operational ingest journal and ordering
- retrieval bundle assembly
- operator APIs

Persistent state:

- local config mounts
- small persistent journal volume

Ports:

- `8080` or similar internal API port

Baseline env:

- `NEO4J_URI`
- `NEO4J_USER`
- `NEO4J_PASSWORD`
- `OPENAI_API_KEY` or equivalent provider key
- `MODEL_PROVIDER`
- `MODEL_NAME`
- `EMBEDDING_MODEL`
- `CORTEX_POLICY_CONFIG`

### 3. `artifact-sync-worker`

Responsibility:

- artifact polling
- Git change detection
- normalization
- ingest job dispatch into the Cortex ingest API

Persistent state:

- local cache volume for scan cursors and temporary extraction files

### 4. `openclaw-gateway`

Responsibility:

- runtime shell
- tools
- sessions
- Graphiti context integration

Persistent state:

- OpenClaw config and workspace state as needed

Important rule:

- do not let OpenClaw maintain a second durable long-term memory store

## Recommended Repo Layout

The implementation will go faster if the repo is laid out explicitly.

Recommended structure:

```text
remram-cortex/
  deploy/
    moltbox/
      graphiti-foundation/
        compose.yml
        .env.example
  services/
    cortex-memory-service/
      app/
      tests/
      Dockerfile
      pyproject.toml
    artifact-sync-worker/
      app/
      tests/
      Dockerfile
  plugins/
    openclaw-graphiti/
      openclaw.plugin.json
      src/
      tests/
  config/
    cortex-memory/
      policy.yaml
      partitions.yaml
      ontology.yaml
  docs/
    ...
```

## Phase 0: Prerequisites

Duration:

- `1 to 2 days`

Tasks:

1. Freeze the stack decision in docs.
2. Create deployment folder and `.env.example`.
3. Decide the first extraction provider:
   - `OpenAI` first is the safest baseline
4. Decide the first artifact provider:
   - `Git` first
5. Define the first coarse partitions:
   - `person:<id>`
   - `shared:<id>`
   - `agent:<id>`
   - `sandbox:<id>`
6. Freeze the ingest state machine.
7. Freeze the initial artifact lineage policy.
8. Freeze the `SupportSummary` representation.

Exit criteria:

- all service names, ports, env vars, and partitions are frozen enough to scaffold

## Phase 1: Bring Up Infrastructure Containers And Ingest Backbone

Duration:

- `1 to 2 days`

Tasks:

1. Create `compose.yml` for:
   - `neo4j`
   - `cortex-memory-service`
   - `artifact-sync-worker`
   - `openclaw-gateway`
2. Mount persistent volumes.
3. Mount the ingest journal volume for `cortex-memory-service`.
4. Add health checks:
   - `neo4j` Bolt health
   - `cortex-memory-service /health`
   - `openclaw-gateway` readiness
5. Verify `Neo4j Browser` is reachable.
6. Verify the memory service can connect to `Neo4j`.
7. Verify the ingest journal can accept and replay a test observation deterministically.
8. Verify writes for one partition are serialized in stable order.

Deliverables:

- working local docker stack
- repeatable startup with one command
- operational ingest journal working before any broad memory ingestion

## Phase 2: Build Cortex Memory Service

Duration:

- `3 to 5 days`

Goal:

- create the app-owned boundary over `Graphiti`

Core modules:

### 1. `providers/graphiti.py`

Responsibilities:

- initialize Graphiti client
- ingest episodes
- run search
- build communities
- enforce one write path
- expose lineage-aware supersession hooks

### 2. `schemas/`

Pydantic models for:

- `ArtifactRef`
- `ArtifactRevision`
- `ObservationIn`
- `ObservationState`
- `MemoryFactView`
- `SupportSummary`
- `RetrievalRequest`
- `RetrievalBundle`
- `PromotionProposal`

### 3. `ingest/`

Responsibilities:

- journal write and read
- idempotency checks
- per-partition serialization
- retry bookkeeping
- intake state transitions

### 4. `policy/`

Responsibilities:

- compile `group_id`
- validate governance tags
- compile retrieval filters
- choose expansion depth
- decide whether derivative content may contribute evidence

### 5. `services/ingest.py`

Responsibilities:

- validate observation shape
- validate artifact lineage and revision identity
- transform accepted observations to Graphiti episode input
- attach artifact references
- trigger extraction only through the ordered ingest path

### 6. `services/retrieve.py`

Responsibilities:

- canonical fact-first retrieval
- support-summary expansion
- artifact resolution
- trace generation

### 7. `services/promote.py`

Responsibilities:

- inspect communities
- identify promotion candidates
- materialize promoted artifact links

### 8. `services/revisions.py`

Responsibilities:

- same-lineage supersession
- artifact rename and move handling
- delete and revert policy
- stale-derivation cleanup

Recommended API surface:

- `GET /health`
- `POST /observations`
- `GET /observations/{observation_id}`
- `POST /artifacts/upsert`
- `POST /artifacts/reingest`
- `POST /artifacts/deactivate`
- `POST /retrieve`
- `GET /facts/{memory_id}`
- `GET /communities/{community_id}`
- `POST /communities/rebuild`
- `POST /corrections`
- `POST /promotions/propose`
- `POST /promotions/materialize`
- `GET /traces/{trace_id}`

Important implementation decision:

- the public API speaks Cortex objects, not Graphiti internals

## Phase 3: Freeze The Canonical Schema, Support Layer, And Lineage Contract

Duration:

- `2 to 4 days`

Goal:

- lock the contract above the graph before broad ingestion starts

Decisions to freeze:

- `ArtifactRef` node type
- `ArtifactRevision` shape
- source artifact edge names
- promoted artifact edge names
- `SupportSummary` as a dedicated support-layer object
- initial entity types such as `Person`, `Project`, `ArtifactRef`, `Concept`, `Preference`, `Decision`
- initial relation types such as `PREFERS`, `WORKS_ON`, `DERIVED_FROM_ARTIFACT`, `PROMOTED_TO_ARTIFACT`
- same-lineage supersession semantics
- rename or move lineage semantics
- delete, revert, and reintroduction semantics
- derivative-content protection flags

Implementation work:

- define custom Graphiti entity and edge models
- define schema validators before graph ingestion
- write transformation tests from canonical models to graph objects
- write lineage-resolution tests
- write intake state-transition tests

Exit criteria:

- no broad artifact ingestion before this contract is stable

## Phase 4: Integrate OpenClaw

Duration:

- `3 to 5 days`

Goal:

- make the runtime shell use Graphiti as authority without creating duplicate memory

Build:

### `openclaw-graphiti` plugin

Use:

- plugin config
- context-engine registration
- optional tool registration
- hooks where useful

Recommended OpenClaw config posture:

- `plugins.slots.contextEngine = "openclaw-graphiti"`
- `plugins.slots.memory = "none"` initially

Context engine behavior:

### `assemble`

- call `POST /retrieve`
- inject retrieval bundle into prompt context
- prefer compact facts first

### `afterTurn`

- extract observation candidates from completed turn
- submit durable ones to `POST /observations`

### `compact`

- summarize long sessions into candidate `SupportSummary` objects or decision artifacts
- send those summaries to the memory service only when policy allows

### correction path

- human or operator corrections call `POST /corrections`
- the default implementation writes correction episodes with explicit provenance
- direct fact-review mutation remains admin-only

Optional tools:

- `graphiti_search`
- `graphiti_trace`
- `graphiti_get_fact`

Exit criteria:

- OpenClaw can recall from Graphiti and write back observations without local durable memory files being authoritative

## Phase 5: Git Artifact Integration

Duration:

- `4 to 7 days`

Goal:

- make artifact-backed memory real

Artifact source of truth:

- Git remains the byte store

What the worker does:

1. detect changed files in configured repos
2. assign stable `artifact_id` and `artifact_lineage_id`
3. record:
   - repo
   - branch or ref
   - path
   - commit SHA
   - blob SHA
   - prior lineage mapping if this is a rename or move
4. extract normalized content from supported file types
5. call `POST /artifacts/upsert`
6. let the memory service create or update:
   - `ArtifactRef`
   - `ArtifactRevision`
   - provenance links
   - episodes derived from artifact content

Lineage rules:

- same-lineage new revisions supersede prior derivations by default
- rename or move preserves lineage
- true replacement creates a new lineage
- revert creates a new revision in the same lineage
- delete deactivates the lineage and triggers policy-controlled invalidation or retention

Derivative protection rules:

- promoted artifacts are marked as derivative content
- derivative content does not automatically reinforce the same cluster or facts on reingest
- derivative reingest requires explicit review or policy approval

Recommended phase-1 supported artifact types:

- `md`
- `txt`
- `json`
- `yaml`
- `py`
- `ts`
- `tsx`

Important rule:

- do not ingest every file blindly

Use allowlists or routing rules so the system learns from meaningful artifacts first.

## Phase 6: Retrieval Compiler And Layered Expansion

Duration:

- `3 to 5 days`

Goal:

- turn Cortex retrieval into deterministic policy, not vague prompting

Retrieval compiler inputs:

- user or agent identity
- workspace or project context
- requested task type
- governance rules
- time window
- entity hints

Compiler outputs:

- target `group_id`
- graph filters
- search recipe
- expansion depth
- whether support summaries are allowed
- whether artifact resolution is allowed
- whether derivative content is excluded by default

Layered retrieval behavior:

### Layer 1

- canonical fact retrieval

### Layer 2

- support-summary expansion

### Layer 3

- source artifact resolution

This must be implemented in code, not left as an informal prompt habit.

## Phase 7: Communities, Promotion, And Visualization Readiness

Duration:

- `4 to 7 days`

Goal:

- make communities useful without confusing them with canonical truth

Tasks:

1. schedule community rebuild jobs
2. create `PromotionProposal` API
3. define thresholds:
   - cluster size
   - relationship density
   - freshness
   - support diversity
4. create promotion materialization flow
5. link promoted artifacts back with `PROMOTED_TO_ARTIFACT`
6. mark promoted outputs as derivative content by default
7. require explicit review before derivative outputs may be reingested as fresh evidence

Outputs:

- promotion candidates
- community summaries
- graph neighborhoods that are ready for future UI surfaces

## Phase 8: Inspection, Audit, And Operator Tooling

Duration:

- `3 to 5 days`

Goal:

- make the system debuggable enough to trust

Add:

- ingest journal inspection endpoint or admin view
- observation state inspection
- retrieval traces
- ingest traces
- fact provenance endpoint
- artifact lineage endpoint
- community inspection endpoint
- read-only Neo4j Browser queries for operators

Optional later:

- Graphiti MCP sidecar for inspection
- lightweight local inspector UI

## Phase 9: Hardening And Operational Safety

Duration:

- `3 to 5 days`

Tasks:

1. backup strategy for `Neo4j` volumes
2. recovery drill
3. journal compaction and retention policy
4. extraction retry tuning
5. throughput and rate-limit tuning
6. operator review path hardening
7. lineage edge-case drills: rename, delete, revert, reintroduction

Important note:

- Graphiti's temporal behavior is safest when writes are not sprayed recklessly in parallel across the same graph partition

## Configuration Strategy

### Docker / Environment

Use `.env` only for:

- secrets
- ports
- container-level toggles

### App Config

Use versioned YAML or JSON files for:

- partitions
- ontology
- retrieval defaults
- provider routing rules
- promotion thresholds

### OpenClaw Config

Use `openclaw.json` for:

- active plugin slots
- model defaults
- compaction behavior
- plugin-specific options

## Testing Strategy

The testing plan should not wait until the end.

### Unit Tests

- canonical schema validation
- policy compilation
- artifact-id generation
- transformation into Graphiti inputs

### Integration Tests

- `Neo4j` + memory service startup
- observation ingestion through journal
- retrieval bundle generation
- Git artifact upsert flow
- OpenClaw context injection
- same-lineage supersession
- derivative artifact non-reinforcement

### Scenario Tests

- contradiction and invalidation
- promotion from community to artifact link
- retrieval ladder fact -> summary -> artifact
- partition isolation via `group_id`
- rename without lineage break
- revert within same lineage
- operator correction episode

## Recommended First Milestone

The first serious milestone should be:

- docker stack up
- one OpenClaw agent connected
- one Git repo watched
- one artifact ingested
- one observation visible in the intake state machine
- one fact retrieved in prompt assembly
- one trace proving provenance back to the artifact

That is the first end-to-end proof that the architecture is real.

## Recommended Second Milestone

The second major milestone should be:

- support-summary expansion working
- community rebuild working
- first promotion candidate proposed from graph structure
- one promoted artifact linked back into the graph
- derivative reingest blocked by default for that promoted artifact

That proves the stack is not only remembering, but beginning to synthesize.

## What To Delay On Purpose

Delay these until the core loop is stable:

- Google Docs integration
- OpenSearch
- advanced UI
- multi-user fine-grained ACL complexity
- local-only extraction models

They are all worthwhile later.

They are not needed to prove the foundation.

## Architectural Risk Status

Closed by this hardened implementation plan:

- deterministic ingest is now phase-1 or phase-2 work, not late hardening
- artifact lineage and same-lineage supersession are explicit before broad ingestion
- `SupportSummary` is fixed as a dedicated support-layer object
- derivative artifact self-reinforcement is blocked by default
- correction policy defaults to auditable correction episodes

Intentionally deferred:

- Google Docs provider work
- advanced UI over communities and lineage
- fine-grained governance beyond coarse partitions plus policy metadata
- local-model optimization

Why the approach remains architecturally sound:

- one authority graph still owns durable truth
- operational reliability infrastructure is now explicit without becoming a second authority
- the remaining deferred items are breadth and ergonomics, not foundation correctness blockers

## Bottom Line

The implementation path should be:

- containerize the graph substrate first
- own the memory contract in one Cortex service
- connect OpenClaw through a context engine
- integrate Git artifacts early
- keep retrieval layered
- add communities and promotion after the core authority loop is trustworthy

That build order stays faithful to the decision and avoids the two biggest failure modes:

- split-brain memory
- overbuilding before the first end-to-end authority loop works

## Sources

- Graphiti overview: <https://help.getzep.com/graphiti/graphiti/overview>
- Graphiti quick start: <https://help.getzep.com/graphiti/getting-started/quick-start>
- Graphiti adding episodes: <https://help.getzep.com/graphiti/core-concepts/adding-episodes>
- Graphiti custom entity and edge types: <https://help.getzep.com/graphiti/graphiti/custom-entity-and-edge-types>
- Graphiti graph namespacing: <https://help.getzep.com/graphiti/graphiti/graph-namespacing>
- Graphiti MCP server: <https://help.getzep.com/graphiti/getting-started/mcp-server>
- OpenClaw plugins: <https://docs.openclaw.ai/plugins>
- OpenClaw memory overview: <https://docs.openclaw.ai/concepts/memory>
- OpenClaw hooks: <https://docs.openclaw.ai/automation/hooks>
- OpenClaw context engine: <https://docs.openclaw.ai/concepts/context-engine>
- OpenClaw context overview: <https://docs.openclaw.ai/concepts/context>
- OpenClaw compaction: <https://docs.openclaw.ai/compaction>
- Neo4j Docker introduction: <https://neo4j.com/docs/operations-manual/current/docker/introduction/>
- Neo4j full-text indexes: <https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/full-text-indexes/>
- Neo4j vector indexes: <https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes>
