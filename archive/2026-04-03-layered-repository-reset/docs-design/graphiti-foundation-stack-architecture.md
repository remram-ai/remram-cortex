# Graphiti Foundation Stack Architecture

## Purpose

This document freezes the chosen foundation architecture for the first serious implementation of `Remram Cortex`.

The selected stack is:

- `Graphiti` as the memory engine
- `Neo4j` as the graph persistence layer
- `OpenClaw` as the runtime shell
- a small custom Cortex layer for schema, policy, retrieval shaping, and artifact lifecycle

This is not another contender memo.

This is the architecture we are choosing to build.

Reviewed on `April 2, 2026`.

## Decision Summary

We are building Cortex as a graph-first memory authority.

The architecture rule is:

- `Graphiti` owns durable extracted memory behavior
- `Neo4j` stores the graph and its indexes
- `OpenClaw` owns runtime interaction and context lifecycle
- Cortex custom code owns the public contract, governance, retrieval compiler, and artifact lifecycle

That means we are not trying to turn:

- `Neo4j` into a raw document store
- `OpenClaw` into the long-term authority
- stock `Graphiti` service APIs into the final Cortex contract

## Why The Stack Is Layered This Way

The cleanest build is not "Graphiti alone."

The cleanest build is:

- a graph-native memory engine
- a graph database optimized for that engine
- a runtime shell with a strong integration seam
- an app-owned contract layer that keeps the system future-proof

This split keeps responsibilities coherent.

## Component Roles

### Graphiti

`Graphiti` is responsible for:

- episode ingestion
- entity extraction
- fact and relationship extraction
- temporal validity and invalidation
- graph-aware and hybrid search behavior
- community building
- domain ontology extension through custom entity and edge types

`Graphiti` is not responsible for:

- raw artifact storage
- access-policy ownership
- the final public Cortex API
- provider sync
- promotion decisions

### Neo4j

`Neo4j` is responsible for:

- durable graph persistence
- full-text indexes
- vector indexes
- graph traversal
- inspection through Browser and Cypher
- operational durability of the memory graph

`Neo4j` is not responsible for:

- extraction logic
- runtime orchestration
- raw artifact bytes
- app-level governance semantics

### OpenClaw

`OpenClaw` is responsible for:

- channels and sessions
- tool execution
- hooks and automation
- context assembly seam through the `contextEngine`
- agent-facing ergonomics

`OpenClaw` is not responsible for:

- authoritative long-term memory truth
- graph mutation rules
- artifact sync semantics

### Cortex Custom Layer

The custom Cortex layer is responsible for:

- canonical memory object validation
- transformation into Graphiti-native ingestion shapes
- governance compilation
- retrieval compilation
- layered expansion policy
- artifact identity and revision handling
- promotion rules
- operator inspection APIs

This is the minimum custom layer that keeps the stack coherent without forcing a later rewrite.

## Chosen Service Topology

The chosen topology is:

```text
Artifact Providers
  - Git repos
  - Google Docs later
  - other providers later
            |
            v
Artifact Sync Worker (custom)
  - detects changes
  - normalizes artifact metadata
  - emits ingest jobs
            |
            v
Cortex Memory Service (custom, embeds Graphiti)
  - canonical schema validation
  - policy and governance compiler
  - Graphiti ingestion and search orchestration
  - artifact and promotion APIs
  - operator inspection APIs
            |
            v
Graphiti Core Library
  - episodes
  - entities
  - facts
  - temporal invalidation
  - communities
            |
            v
Neo4j
  - graph store
  - full-text indexes
  - vector indexes

OpenClaw Gateway
  - agent runtime
  - tools
  - hooks
  - graphiti context engine plugin
            |
            +----------> Cortex Memory Service
```

## Why We Are Embedding Graphiti In A Custom Service

This is the most important architecture choice after selecting the stack.

We are not putting a thin custom wrapper in front of a separate stock Graphiti HTTP service.

We are embedding the `Graphiti` library inside an app-owned `cortex-memory-service`.

Why:

- one fewer network hop
- one fewer service to version and debug
- easier ownership of the public contract
- easier schema validation before ingestion
- easier policy and retrieval compilation
- lower long-term maintenance burden than "wrapper around wrapper"

The upstream `Graphiti` server and MCP surfaces are still useful:

- for examples
- for smoke tests
- for operator tooling later

They are not the main app boundary.

## Source Of Truth Rules

The stack only works if the source-of-truth rules remain strict.

### Long-Term Memory Truth

Lives in:

- `Graphiti` data persisted in `Neo4j`

### Raw Artifact Truth

Lives in:

- Git
- Google Docs later
- other provider systems later

### Runtime Session Truth

Lives in:

- OpenClaw session history

But only as runtime evidence and conversational state, not durable memory authority.

### Policy And Contract Truth

Lives in:

- Cortex code and configuration

Not in ad hoc graph conventions alone.

## Deterministic Ingest Requirements

Deterministic ingest is a phase-1 correctness requirement, not late operational hardening.

The stack must include a tiny operational ingest journal or queue from the beginning.

Rules:

- it exists only to sequence, deduplicate, retry, and audit ingest work
- it is not a second memory authority
- it does not own durable truth
- durable truth still lives only in `Graphiti` data persisted in `Neo4j`

Required behaviors:

- every ingest request gets an idempotency key
- every ingest request is written to an operational journal before extraction
- writes are serialized per coarse partition such as `group_id`
- writes inside a partition have a stable processing order
- duplicate or replayed ingest requests resolve deterministically
- retry and backpressure behavior is explicit

The practical implication is:

- `OpenClaw` and artifact workers do not write directly into Graphiti mutation paths
- they submit observations or artifact updates into the Cortex ingest path
- the Cortex ingest path owns ordering and replay handling before Graphiti is invoked

## What Lives In The Graph

The graph should hold extracted and durable semantic memory, not arbitrary blobs.

### Native Graphiti Objects

- `Episode`
- `EntityNode`
- `EntityEdge`
- community structures
- temporal metadata such as `valid_at`, `invalid_at`, and `expired_at`

### Cortex-Specific Additions

- `ArtifactRef` entity type for source and promoted artifacts
- `SupportSummary` entity type for stable expansion-only support context
- custom edge types for provenance and promotion
- richer attributes for governance and inspection

### What Does Not Live In The Graph

- raw PDFs
- full markdown documents as the primary system of record
- full Google Doc contents as durable bytes
- arbitrary app settings

The graph stores durable knowledge and references, not full content archives.

## Canonical Object Contract Above Graphiti

The Cortex contract should be explicit even though the storage is graph-shaped.

The app-level objects should be:

### 1. Artifact Reference

Fields:

- `artifact_id`
- `artifact_lineage_id`
- `provider`
- `provider_uri`
- `canonical_uri`
- `current_revision_id`
- `revision_id`
- `title`
- `mime_type`
- `artifact_kind`
- `ingest_status`

Maps to:

- `ArtifactRef` entity node

### 2. Artifact Revision

Fields:

- `artifact_revision_id`
- `artifact_lineage_id`
- `parent_revision_id`
- `content_hash`
- `provider_revision_ref`
- `revision_status`
- `observed_at`

Maps to:

- revision metadata attached to the `ArtifactRef` node and lineage edges recorded by Cortex

### 3. Evidence Observation

Fields:

- `observation_id`
- `artifact_id` or session source
- `observed_at`
- `actor`
- `content`
- `scope`

Maps to:

- `Episode`

### 4. Durable Memory Fact

Fields:

- `memory_id`
- `fact_text`
- `subject`
- `object`
- `relation`
- `valid_at`
- `invalid_at`
- `support_level`
- `governance_tags`

Maps to:

- `EntityEdge` plus linked nodes

### 5. Support Summary

Fields:

- `summary_id`
- `summary_text`
- `derived_from`
- `scope`
- `relevance_tags`

Maps to:

- dedicated `SupportSummary` entity linked to one or more canonical facts

### 6. Promotion Target

Fields:

- `promotion_id`
- `community_id` or fact-cluster id
- `artifact_id`
- `status`
- `promoted_at`

Maps to:

- promotion edge plus linked `ArtifactRef`

This is the key split:

- Cortex owns the contract
- Graphiti owns the graph mechanics

## SupportSummary Representation Decision

`SupportSummary` is fixed as a dedicated support-layer object.

It is not an ambiguous "sometimes episode" concept.

Rules:

- a `SupportSummary` is a stable expansion object
- it is linked to canonical facts or clusters
- it is not the default truth surface
- it is not a generic summary episode
- it is retrieved primarily at expansion time

This decision is required because the retrieval ladder depends on a stable second-layer surface.

## Artifact Identity, Revision Identity, And Lineage Policy

Artifact identity is split into three related concepts:

### Stable Artifact Identity

`artifact_id` identifies the current application-facing artifact record.

### Artifact Lineage Identity

`artifact_lineage_id` identifies the continuity of the same source artifact over time.

Rename or move within the same logical source should preserve lineage.

### Revision Identity

`artifact_revision_id` identifies one specific observed revision in that lineage.

Examples:

- Git commit plus path plus blob identity
- later Google Docs revision id

The chosen reingestion policy is:

- same-lineage revisions supersede prior derivations by default
- different source lineages may coexist and reconcile through contradiction and invalidation logic

That means routine edits to the same source artifact should not create stale parallel truths by default.

### Same-Lineage Events

For the same lineage:

- edit: supersede prior derivations from the lineage
- rename or move: preserve lineage, create a new revision, supersede prior derivations
- revert: create a new revision that may produce previously seen facts again, but it still supersedes the intervening revisions
- reintroduction under the same lineage: treat as a later revision in the same lineage

### Replacement Events

If the source is genuinely a different logical artifact:

- create a new lineage
- do not silently merge it into the old one

### Delete Events

Delete does not mean historical memory is erased automatically.

Delete means:

- the artifact lineage becomes inactive
- source availability changes
- derived facts from the latest active revision may be invalidated or retained based on policy

The important rule is:

- derivations always point to specific revisions, not vague artifact identity alone

## Artifact Relationship Model

We are explicitly choosing at least two artifact relationships.

### Source Artifact Relationship

Recommended edge names:

- `DERIVED_FROM_ARTIFACT`
- `SUPPORTED_BY_ARTIFACT`
- `HAS_SOURCE_ARTIFACT`

Purpose:

- provenance
- re-ingestion
- evidence traceability

### Promoted Artifact Relationship

Recommended edge names:

- `PROMOTED_TO_ARTIFACT`
- `SUMMARIZED_AS`
- `EXTERNALIZED_AS`

Purpose:

- outward promotion
- writing to Git or another provider
- linking a graph cluster to a human-facing artifact

These must remain semantically separate.

Source artifacts are evidence.

Promoted artifacts are projections.

## Derivative Artifact Protection

Promoted artifacts are derived projections, not fresh independent evidence by default.

Rules:

- promoted artifacts do not automatically reinforce the same underlying fact cluster when re-seen by artifact monitoring
- promoted artifacts are marked as derivative content
- derivative artifacts require an explicit review or policy path before they can contribute fresh authority evidence
- source artifacts remain the default evidence path

This prevents self-reinforcement loops where the system promotes a graph cluster, re-ingests the promoted output, and silently amplifies its own prior conclusions.

## Partitioning And Governance

`group_id` is used for coarse walls only.

Recommended early partitions:

- `person:<user-id>`
- `shared:<household-or-team>`
- `agent:<agent-id>`
- `sandbox:<experiment-or-test>`

Do not encode the whole governance model into `group_id`.

Fine-grained control belongs in:

- node labels
- edge types
- attributes
- app-level retrieval policy

This keeps the graph from fragmenting into unmanageable shards.

## Intake State Machine

The write path uses a lightweight but explicit state model.

Recommended states:

- `observation_received`
- `accepted_for_extraction`
- `extracted`
- `durable_fact_accepted`
- `superseded`
- `invalidated`
- `rejected`

State meanings:

- `observation_received`: the request entered the operational ingest path
- `accepted_for_extraction`: policy accepted it for Graphiti processing
- `extracted`: Graphiti extraction completed and produced candidate graph changes
- `durable_fact_accepted`: the candidate changes were committed as accepted graph memory
- `superseded`: later same-lineage revision or correction replaced the prior accepted derivation
- `invalidated`: contradiction, delete policy, or explicit correction retired the prior truth
- `rejected`: the observation did not pass policy, quality, or parsing checks

This state machine is intentionally lightweight.

Its purpose is:

- auditability
- replayability
- debugging
- deterministic lifecycle handling

## Retrieval Model

The retrieval ladder is:

1. search compact canonical facts
2. expand to support summaries if needed
3. resolve source artifacts only when needed

That means:

- compact truth is the default search surface
- richer context is expansion-time context
- raw artifacts stay external until actually required

This is much cleaner than starting from documents every time.

## Read Path

The default read path should be:

1. OpenClaw asks the Cortex memory service for context.
2. Cortex compiles:
   - coarse `group_id`
   - governance filters
   - entity and edge preferences
   - temporal windows
   - expansion policy
3. Graphiti executes search and graph expansion.
4. Cortex shapes the result into a retrieval bundle.
5. OpenClaw inserts the bundle into prompt assembly.

## Write Path

The default write path should be:

1. OpenClaw turn or artifact change produces an observation candidate.
2. Cortex writes the request into the operational ingest journal with an idempotency key.
3. Cortex validates canonical shape and artifact lineage metadata.
4. Cortex selects the target `group_id` and governance attributes.
5. Cortex advances the request to `accepted_for_extraction`.
6. Graphiti processes the observation in partition order and produces candidate graph changes.
7. Cortex records extracted state, accepted facts, and lineage-specific supersession where needed.
8. Cortex records artifact links, support summaries, and promotion edges where needed.

## Correction Policy

Human or operator correction should default to first-class correction episodes.

Why:

- better provenance
- better auditability
- better alignment with graph-native evidence handling

A narrow direct fact-review or admin path is still allowed for exceptional operational correction cases, but it should remain the exception, not the default write path.

## Configuration Surfaces

The configuration split should stay explicit.

### Infrastructure Configuration

Owned by:

- Docker Compose
- environment variables

Examples:

- `NEO4J_AUTH`
- `NEO4J_server_memory_heap_max__size`
- volume paths
- exposed ports

### Graphiti Runtime Configuration

Owned by:

- Cortex memory service config
- provider env vars

Examples:

- LLM provider and model
- embedding provider and model
- extraction instructions
- concurrency limits
- telemetry disablement

### Cortex Policy Configuration

Owned by:

- app YAML or JSON config in the Cortex repo

Examples:

- partition rules
- governance tags
- artifact routing rules
- promotion thresholds
- retrieval ladder defaults

### OpenClaw Configuration

Owned by:

- `openclaw.json`
- plugin config

Examples:

- `plugins.slots.contextEngine = "openclaw-graphiti"`
- `plugins.slots.memory = "none"` early, unless a specific plugin tool is justified
- compaction model
- agent defaults

## What Is Native Versus Custom

| Concern | Native owner | Custom owner |
| --- | --- | --- |
| Episode ingestion | `Graphiti` | Cortex chooses what becomes an episode |
| Fact extraction | `Graphiti` | Cortex controls extraction policy and ontology |
| Temporal invalidation | `Graphiti` | Cortex adds review and operator surfaces |
| Graph persistence | `Neo4j` | Cortex adds backup and migration scripts |
| Context assembly | `OpenClaw` seam | `openclaw-graphiti` plugin and retrieval shaping |
| Artifact sync | None | Cortex worker |
| Canonical schema | None | Cortex |
| Promotion | Communities help | Cortex decides when and where to externalize |
| Inspection | Neo4j Browser and MCP assist | Cortex operator API and UI |

## What We Should Not Build In Phase 1

Do not add in phase 1:

- `OpenSearch`
- a second durable relational store for memory truth
- parallel OpenClaw markdown memory
- direct app-owned `Cypher` writes bypassing Graphiti
- full raw-document storage inside `Neo4j`

Those would all weaken the chosen design.

## Architectural Risk Status

Closed by this hardened plan:

- deterministic ingest is now an early correctness rule
- artifact lineage and supersession policy are explicit
- `SupportSummary` is fixed as a dedicated support-layer object
- promoted artifact self-reinforcement is explicitly blocked by default

Intentionally deferred:

- fine-grained multi-user governance beyond coarse partitions plus policy metadata
- Google Docs integration
- advanced operator UI beyond API and read-only graph inspection

Why the approach remains sound:

- the unresolved work is now contract and product-surface work
- the correctness-critical lifecycle rules are explicit early
- the stack still keeps one durable authority and one clean runtime shell

## Bottom Line

The chosen stack is not:

- `Graphiti` replacing Cortex

It is:

- `Graphiti` as the memory engine
- `Neo4j` as the graph substrate
- `OpenClaw` as the runtime shell
- Cortex custom code as the contract, policy, and artifact integration layer

That is the cleanest architecture that stays faithful to the foundation decision and minimizes long-term regret.

## Sources

- Graphiti overview: <https://help.getzep.com/graphiti/graphiti/overview>
- Graphiti quick start: <https://help.getzep.com/graphiti/getting-started/quick-start>
- Graphiti adding episodes: <https://help.getzep.com/graphiti/core-concepts/adding-episodes>
- Graphiti custom entity and edge types: <https://help.getzep.com/graphiti/graphiti/custom-entity-and-edge-types>
- Graphiti graph namespacing: <https://help.getzep.com/graphiti/graphiti/graph-namespacing>
- Graphiti MCP server: <https://help.getzep.com/graphiti/getting-started/mcp-server>
- OpenClaw context engine: <https://docs.openclaw.ai/concepts/context-engine>
- OpenClaw plugins: <https://docs.openclaw.ai/plugins>
- OpenClaw plugin registry and tools: <https://docs.openclaw.ai/tools/plugin>
- OpenClaw memory overview: <https://docs.openclaw.ai/concepts/memory>
- OpenClaw hooks: <https://docs.openclaw.ai/automation/hooks>
- OpenClaw agent loop: <https://docs.openclaw.ai/concepts/agent-loop>
- Neo4j Docker introduction: <https://neo4j.com/docs/operations-manual/current/docker/introduction/>
- Neo4j full-text indexes: <https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/full-text-indexes/>
- Neo4j vector indexes: <https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes>
