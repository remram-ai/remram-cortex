# Cognee on Moltbox to OpenClaw to Cortex Implementation Plan

## Purpose

This document is the full implementation plan for adopting `Cognee` as the primary memory foundation for `remram-cortex`.

It covers the full path from:

- standing up the baseline `Cognee` architecture as separate docker containers on `Moltbox`
- connecting that memory authority layer to `OpenClaw`
- expanding the stack until it covers the practical Cortex vision

Reviewed on `April 2, 2026`.

## Blunt Read

`Cognee` is a credible primary foundation if we use it as a real memory lifecycle platform rather than as a thin retrieval add-on.

The right implementation posture is:

- deploy `Cognee` as a separate service boundary on `Moltbox`
- use separate containers for `cognee-api`, `cognee-mcp`, `postgres/pgvector`, `neo4j`, and `redis`
- connect `OpenClaw` with the official plugin first
- keep `Cognee` as the only durable memory write authority
- add Cortex-specific policy, artifact, provenance, and maintenance layers in phases

Do not start by treating `OpenClaw` Markdown memory as the long-term authority.

Do not start by forking half of Cognee before a live memory loop exists.

Do not start by forcing `OpenSearch` into the baseline just because it is attractive elsewhere.

If the work is done in the right order, the first usable system is realistic in about `1 to 2 weeks` of focused AI-assisted implementation, and a credible "Cortex on Cognee" v1 is realistic in about `6 to 10 weeks`.

## Planning Assumptions

- One human builder, heavily AI-assisted.
- Local and free infrastructure is required.
- Dockerized external services are preferred.
- Separate containers are a feature, not a burden, when they align with `Moltbox`.
- Model APIs are allowed if they reduce extraction risk.
- `OpenSearch` is optional, not mandatory.
- `Dream` is not a gating criterion for platform choice.
- Lowest long-term data replatform risk matters more than shortest possible demo path.

## Core Architectural Decision

Treat `Cognee` as the durable memory authority.

Treat `Postgres`, `pgvector`, `Neo4j`, and `Redis` as Cognee implementation stores, not app-owned schemas.

Treat `OpenClaw` as the runtime shell and agent host, not the durable memory authority.

Treat future Cortex code as a policy and contract layer on top of Cognee, not as a second memory platform.

That produces the cleanest long-term shape:

```text
Channels / Agents / Tools
          |
          v
OpenClaw Gateway
  - runtime orchestration
  - session lifecycle
  - tools / hooks / automation
  - Cognee bridge plugin
          |
          v
Cognee Authority Layer
  - add / update / delete
  - cognify
  - search
  - memify
  - session cache + session persistence
  - datasets / permissions
  - custom DataPoint models and pipelines
          |
          +--> Postgres
          |     - datasets
          |     - metadata
          |     - provenance
          |     - pipeline state
          |
          +--> pgvector
          |     - searchable embeddings
          |
          +--> Neo4j
          |     - graph structure
          |     - durable relationships
          |
          +--> Redis
                - session cache
                - short-term continuity

Optional later sidecars:
  - Cognee MCP server for inspection
  - Cortex retrieval facade
  - artifact import worker
  - maintenance / Dream-lite worker
  - OpenSearch projection or adapter if later justified
```

## Why Separate Containers Are The Right Moltbox Shape

For this stack, separate containers are not premature abstraction.

They are the natural shape of the upstream product and the natural shape of `Moltbox`.

That buys:

- cleaner operational boundaries
- easier independent healthchecks
- simpler volume ownership
- easier local resets without wiping the whole stack
- lower confusion about which service owns which responsibility

The right compromise is:

- one `Moltbox` service bundle
- multiple containers inside that bundle

That preserves operational simplicity without collapsing unlike components into one runtime.

## The Most Important Guardrails

These rules should be fixed before implementation starts:

- `Cognee` is the only durable write path for memory objects.
- `OpenClaw` transcripts are evidence, not authority.
- `OpenClaw` Markdown memory is source material or projection, not the final durable store.
- Direct writes to `Postgres`, `pgvector`, `Neo4j`, or `Redis` are maintenance-only, not app behavior.
- `DataPoint` is the phase-1 durable unit.
- `memify` is the first maintenance surface.
- Phase 1 is allowed to be single-user and effectively single-authority-dataset.
- Fine-grained governance should not depend on stock dataset-routing behavior until it is proven on the chosen self-hosted stack.
- `OpenSearch` stays out of phase 1 unless a specific blocking retrieval need appears.

## What To Accept The Cognee Way

If this path is chosen, several Cortex ideas should be implemented the `Cognee` way instead of forcing a parallel architecture early.

| Cortex intent | Cognee-native equivalent | Decision |
| --- | --- | --- |
| Durable memory object | `DataPoint` | Accept directly |
| Memory lifecycle | `add -> cognify -> search -> memify` | Accept directly |
| Short-term continuity | sessions plus cache | Accept directly |
| Session promotion | session persistence pipeline plus memify | Accept directly |
| Coarse memory partition | dataset | Accept with modification |
| Lightweight work grouping | `belongs_to_set` and `NodeSet` | Accept directly |
| Artifact and document extraction | `cognify` plus custom tasks and chunkers | Accept directly |
| Structured custom memory | custom `DataPoint` models plus `add_data_points` | Accept directly |
| Retrieval specialization | custom retrievers via `use_retriever` | Accept directly |
| Reflection / Dream-lite | `memify` plus custom pipelines | Accept directly |
| Governance-first retrieval | policy wrapper over datasets, NodeSets, retriever config | Custom layer required |
| Retrieval traces and operator policy audit | remram-owned wrapper and logs | Custom layer required |

The main worldview shift is this:

- a Cortex memory object becomes a durable `DataPoint` or a small family of `DataPoint` types
- not a custom flat object store outside the platform

That is a strength if the goal is forward evolution without a rebuild.

## Hard Differences And How To Handle Them

### 1. Dataset isolation is stronger in concept than in the strongest self-hosted stack

Current Cognee docs make multi-user and dataset-scoped isolation look central, and they are.

Current source also shows that some dataset database handler support is narrower than the raw storage adapters themselves, especially once you want `Postgres + pgvector + Neo4j` together in a self-hosted posture.

The practical decision is:

- do not promise strict per-dataset backend routing in phase 1
- start with one primary authority dataset per environment or deployment slice
- keep authentication on
- treat governance and partitioning as an application policy problem until a dedicated dataset-handler spike proves more

This is a real compromise, but not a fatal one for a personal Cortex build.

### 2. The stock OpenClaw plugin is file-memory-first

The official `@cognee/cognee-openclaw` plugin is a real accelerator, but it assumes:

- `OpenClaw` memory files are the source of truth
- Cognee syncs and indexes them
- recall happens from that synced representation

That is excellent for phase 1.

It is not ideal as the final authority shape for Cortex.

The solution is not to reject the plugin.

The solution is:

- use it first
- then extend or fork it once direct Cognee writes are more valuable than file sync

### 3. Cognee is multi-store by design

This is not something to simplify away.

If we choose Cognee, we should embrace:

- relational state in `Postgres`
- semantic recall in `pgvector`
- structural memory in `Neo4j`
- short-term continuity in `Redis`

Trying to force Cognee into a single-store mindset would give up one of its main strengths while keeping most of its complexity.

### 4. Configuration changes are not free

Cognee's docs explicitly warn that provider or schema changes can require prune-and-rebuild behavior.

That means early choices matter:

- stable storage posture
- stable dataset strategy
- stable core `DataPoint` contract

The plan below is intentionally designed to reduce later rebuild pressure.

## Target End State

The final practical architecture should look like this:

```text
OpenClaw
  - channels
  - sessions
  - tools
  - cron / hooks / background work
  - Cognee integration plugin
          |
          v
Cortex Cognee Layer
  - governance compiler
  - ingestion policy
  - retrieval bundle assembly
  - retrieval traces
  - artifact and promotion policy
  - operator inspection API
          |
          v
Cognee Core / Extension Layer
  - DataPoint families
  - cognify
  - search types
  - custom retrievers
  - memify jobs
  - session persistence
          |
          +--> Postgres
          +--> pgvector
          +--> Neo4j
          +--> Redis
          |
          +--> optional MCP inspector
          +--> optional nightly maintenance worker
          +--> optional OpenSearch projection
```

The key point is that even if a Cortex facade is added later, the durable authority stays inside the Cognee stack. That keeps later architecture cleanup from turning into data replatforming.

## Repo Landing Zones

Implementation should stay split by responsibility.

### `moltbox-services`

Add new service bundles here:

- `d:/Development/RemRam/moltbox-services/services/cognee-dev/`
- `d:/Development/RemRam/moltbox-services/services/cognee-test/`
- `d:/Development/RemRam/moltbox-services/services/cognee-prod/`

Each bundle should include:

- `service.yaml`
- `compose.yml.template`
- optional image overrides only if a custom Cognee build becomes necessary

Recommended phase-1 container names inside the bundle:

- `cognee-api`
- `cognee-mcp`
- `cognee-postgres`
- `cognee-neo4j`
- `cognee-redis`

Do not enable the upstream frontend in the baseline bundle.

### `remram`

Add the `OpenClaw` integration and platform docs here:

- `d:/Development/RemRam/remram/platform/plugins/openclaw-cognee/`
- `d:/Development/RemRam/remram/platform/services/cognee/`

The plugin package should eventually own:

- Cognee API client
- lifecycle hooks
- retrieval injection or context assembly integration
- direct write helpers for sessions and promoted memory
- operator tools for memory inspection

### `remram-cortex`

Keep the design, policy, and eventual Cortex contract docs here first:

- this implementation plan
- `DataPoint` family contract docs
- governance and retrieval policy docs
- later, a concrete Cortex facade spec if one is added

## Phase 0: Foundation Freeze

### Objective

Lock the architectural guardrails before any code is written.

### Major Work

- choose `Postgres + pgvector + Neo4j + Redis` as the default serious self-hosted posture
- explicitly keep `OpenSearch` out of the baseline plan
- define the initial dataset strategy
- define the initial `NodeSet` strategy
- define the first-pass `DataPoint` family
- choose the baseline extraction model posture
- decide whether phase 2 stays on the stock plugin or immediately wraps it in a remram-owned plugin package

### Required Decisions

- single primary dataset in phase 1 or early multi-dataset posture
- initial `NodeSet` naming conventions
- first-pass memory object types
- baseline auth strategy
- minimum viable LLM provider for extraction
- whether `Cognee MCP` is operator-only or kept out of phase 1 entirely

### Recommended Outcome

- one primary durable dataset per environment in phase 1
- `NodeSet` used for project, repo, and workflow slices
- `Decision`, `Preference`, `Constraint`, `Procedure`, and `ArtifactReference` defined as first-class future `DataPoint` families
- explicit service account and bearer token are used from the start
- `OpenAI` or `Gemini` is used for extraction until quality is proven

### Exit Criteria

- no unresolved argument remains about the authority model
- no unresolved argument remains about separate containers
- the future plan does not require duplicating memory into another durable store

### AI-Builder Estimate

`1 to 2 days`

## Phase 1: Moltbox Baseline Deployment

### Objective

Stand up a working `Cognee` stack under `Moltbox` with repeatable lifecycle commands and separate service containers.

### Baseline Service Shape

Start with one `Moltbox` service bundle that contains:

- one `cognee-api` container
- one `cognee-mcp` container
- one `cognee-postgres` container
- one `cognee-neo4j` container
- one `cognee-redis` container

All five are separate containers.

They still ship together as one `Moltbox` bundle so deployment remains simple.

### Container Contract

Recommended baseline posture:

- pin the Cognee image or git SHA to a known-good version, not `main`
- pin `neo4j` to a `5.26+` known-good version
- pin `pgvector` to a `pg17` known-good image
- pin `redis` to `7`
- attach all containers to `moltbox_internal`
- persist `Postgres`, `Neo4j`, and `Redis` data outside the containers
- add API healthcheck on `/health`
- keep `cognee-api` reachable on the internal network
- keep `cognee-mcp` internal-only or expose it on a different operator port

### Important Upstream Detail

The current upstream `docker-compose.yml` maps both `cognee` and `cognee-mcp` to host port `8000`.

Do not copy that host-port layout directly into `Moltbox`.

In the `Moltbox` bundle:

- expose `cognee-api` normally
- keep `cognee-mcp` internal-only, or
- give `cognee-mcp` a different external port if operator access is needed

### Recommended Phase-1 Environment

At minimum, plan for these settings:

```text
DB_PROVIDER=postgres
DB_HOST=cognee-postgres
DB_PORT=5432
DB_NAME=cognee_db
DB_USERNAME=cognee
DB_PASSWORD=...

VECTOR_DB_PROVIDER=pgvector
VECTOR_DB_HOST=cognee-postgres
VECTOR_DB_PORT=5432
VECTOR_DB_NAME=cognee_db
VECTOR_DB_USERNAME=cognee
VECTOR_DB_PASSWORD=...

GRAPH_DATABASE_PROVIDER=neo4j
GRAPH_DATABASE_HOST=cognee-neo4j
GRAPH_DATABASE_PORT=7687
GRAPH_DATABASE_USERNAME=neo4j
GRAPH_DATABASE_PASSWORD=...

CACHING=true
CACHE_BACKEND=redis
CACHE_HOST=cognee-redis
CACHE_PORT=6379

REQUIRE_AUTHENTICATION=true
ENABLE_BACKEND_ACCESS_CONTROL=false
```

The `ENABLE_BACKEND_ACCESS_CONTROL=false` recommendation is intentional for phase 1.

Why:

- it reduces early friction on the strongest self-hosted service mix
- it avoids over-promising dataset-routed isolation before the self-hosted handler story is proven
- it keeps phase 1 focused on one working durable memory loop

If a spike later proves that `Postgres + pgvector + Neo4j` behaves cleanly with the exact dataset-routing posture you want, that can be revisited.

### Authentication Posture

Do not rely on Cognee's default-user convenience path for the long-term plan.

The current docs and source expose a few auth surfaces:

- user registration
- bearer-token login
- a development default user
- plugin auto-login behavior if no token is provided

The right `Moltbox` posture is:

- provision an explicit Cognee service account
- mint a bearer token
- store it as a secret
- pass it explicitly into the `OpenClaw` plugin

That removes ambiguity and keeps development and later environments aligned.

### Major Work

- create the `cognee-dev` bundle
- define env and secret injection
- wire persistent volumes
- document operator lifecycle commands
- smoke test API startup and auth
- smoke test `add`, `cognify`, `search`, and session-backed search
- smoke test `cognee-mcp` only after the API path is healthy

### Exit Criteria

- `moltbox gateway service deploy cognee-dev` brings the stack up cleanly
- `cognee-api` passes healthcheck
- an authenticated request can add and search data
- session-backed search works with `Redis`
- `Neo4j` and `Postgres` persist data across restarts

### AI-Builder Estimate

`3 to 5 days`

## Phase 2: OpenClaw Bridge v0

### Objective

Connect `OpenClaw` to `Cognee` with the thinnest path that gives a usable memory loop.

### Recommended Implementation

Start with the official plugin:

- `@cognee/cognee-openclaw`

Do not build a full custom bridge before the stock lifecycle has been exercised.

### Phase-1 Plugin Posture

Recommended baseline config:

- `baseUrl` points to `cognee-api`
- `apiKey` is explicitly set from the Cognee service account token
- `datasetName` points at the one primary phase-1 dataset
- `searchType` starts with `GRAPH_COMPLETION`
- `autoRecall=true`
- `autoIndex=true`
- `autoCognify=true`

### Why This Is Good Enough

The official plugin already gives you:

- auto-indexing of `MEMORY.md` and `memory/*.md`
- hash-based change detection
- cleanup for deleted files
- auto-recall before each agent run
- bounded recall injection
- CLI inspection and sync status

That is enough to prove:

- memory persistence is useful
- graph-backed recall helps prompt construction
- the runtime shell and durable authority can already work together

### What To Watch Carefully

The plugin is file-memory-first.

That means phase 2 should be treated as:

- proof of a live memory loop
- not proof that the final authority model is complete

### Operator Tools

Add a small set of inspection tools early:

- `cognee_search`
- `cognee_dataset_status`
- `cognee_recent_memories`
- `cognee_reindex`

If the stock plugin tools are not enough, wrap them in a remram-owned plugin layer rather than immediately reimplementing the sync logic.

### Exit Criteria

- a normal OpenClaw conversation triggers recall from Cognee automatically
- memory file changes sync into Cognee reliably
- the plugin behaves cleanly with explicit bearer-token auth
- disabling the plugin leaves OpenClaw stable

### AI-Builder Estimate

`2 to 4 days`

## Phase 3: Durable Authority Hardening

### Objective

Stop treating the system like a smart file index and make the stored knowledge structurally compatible with Cortex.

### Major Work

- define the first stable Cortex-on-Cognee `DataPoint` families
- keep Markdown memory as editable source or projection, not final authority
- add direct write paths for higher-value memory objects
- standardize `NodeSet` conventions
- standardize provenance fields and metadata usage
- standardize duplicate-resistant ingest behavior

### Recommended First `DataPoint` Families

At minimum:

- `Decision`
- `Preference`
- `Constraint`
- `Procedure`
- `ArtifactReference`
- `ProjectFact`

These should not all require phase-3 retrieval logic, but they should start landing in the durable model early enough to avoid a rebuild later.

### Provenance Fields To Preserve Early

At minimum, land enough fields to keep later architecture cleanup cheap:

- `source_kind`
- `source_provider`
- `source_uri`
- `artifact_id`
- `artifact_revision`
- `project_id`
- `repo_id`
- `session_id`
- `source_user`
- `source_pipeline`
- `source_task`
- `promotion_state`
- `confidence`

Use Cognee's existing provenance and metadata surfaces first.

Do not create a separate parallel provenance system unless the native shape proves insufficient.

### Important Compromise

Do not try to solve all governance and policy at the storage layer in phase 3.

Early on:

- store the fields cleanly
- thread them through `DataPoint` metadata and graph relations
- let the application layer own policy enforcement until usage patterns are real

### Exit Criteria

- important memory objects can be written directly into Cognee without going through Markdown memory files
- new data lands with enough provenance and governance shape to survive later cleanup
- there is no need to throw away phase-2 data to move forward

### AI-Builder Estimate

`4 to 7 days`

## Phase 4: Retrieval and Governance Layer

### Objective

Add the custom layer that Cognee does not natively provide: governance-first retrieval and stable Cortex-shaped retrieval bundles.

### What Gets Built

This phase adds a thin remram-owned wrapper in front of raw Cognee retrieval.

Responsibilities:

- compile Cortex governance inputs into dataset choice, `NodeSet`, search type, and retriever configuration
- cap and format retrieval bundles for `OpenClaw`
- record retrieval traces
- expose inspectable operator APIs

### Why This Phase Matters

Cognee search is strong, but Cortex wants:

- stable partitioning rules
- explicit bundle assembly
- inspectable retrieval reasoning
- a stronger contract than "whatever retriever came back"

That logic should live in a remram-owned layer, not inside raw prompt assembly.

### Implementation Choice

Fastest path:

- wrap Cognee search inside the `OpenClaw` plugin and a small service helper

Lower-regret path:

- create a dedicated `cortex-cognee` facade once phase-2 and phase-3 behavior stabilize

Recommendation:

- keep the retrieval wrapper close to the plugin first
- do not build a separate large service until the retrieval contract settles

### Cognee-Native Levers To Exploit

Use these before replacing retrieval:

- search type selection
- `session_id`
- `NodeSet`
- custom retrievers through `use_retriever`
- `retriever_specific_config`
- `memify`-enriched subgraphs

### Exit Criteria

- OpenClaw retrieves memory through a remram-owned policy surface, not only through raw plugin defaults
- retrieval traces exist for debugging and tuning
- governance and scope decisions are inspectable

### AI-Builder Estimate

`4 to 8 days`

## Phase 5: Artifact and Document Ingestion

### Objective

Expand beyond turn memory into artifact-backed knowledge and document-backed memory.

### Cognee-Native Approach

Do this the Cognee way:

- ingest source artifacts through `add`
- use `cognify` for document extraction
- use custom chunkers and prompts only where needed
- add structured `DataPoint` objects for high-value durable outputs
- run custom pipelines when plain document extraction is not enough

Do not create a parallel document-intake authority just because Cortex eventually wants stronger artifact semantics.

### Raw Content Rule

Keep raw source content authoritative outside the memory graph when possible.

For example:

- git repos stay authoritative in git
- provider documents stay authoritative in their source provider
- local files stay authoritative in local artifact storage

Cognee may still ingest copies or processed text for extraction, but Cortex should not become dependent on Cognee being the only place raw artifacts can be reconstructed from.

### Major Work

- build import workers for local and provider-backed artifacts
- define `ArtifactReference` and related `DataPoint` contracts
- preserve artifact locator and revision metadata
- standardize long-document ingestion rules
- expose provenance inspection endpoints

### Exit Criteria

- imported documents and artifacts create durable structured memory
- graph and vector recall can be walked back to source artifacts or revisions
- the authority model remains Cognee-centered rather than fragmenting into side stores

### AI-Builder Estimate

`4 to 7 days`

## Phase 6: Sessions, Promotion, And Dream-Lite

### Objective

Add continuity, promotion, and maintenance without putting heavy reasoning back in the live path.

### Native Cognee Levers

Start with what Cognee already gives you:

- session-aware search
- Redis-backed session cache
- feedback capture
- session persistence into the knowledge graph
- `memify`
- custom enrichment pipelines

### Recommended Execution Model

Use `OpenClaw` lifecycle hooks and background work to trigger:

- post-turn session persistence checks
- periodic `memify` jobs
- stale-memory review passes
- promotion-candidate detection

Keep the actual durable writes inside Cognee.

### Custom Cortex Work

Add small remram-owned jobs for:

- promotion review
- stale fact cleanup
- summary rebuilds
- artifact linkage cleanup
- retrieval trace audits

### Exit Criteria

- the system improves memory quality between live turns
- important sessions can be promoted into durable graph-backed memory
- maintenance work is inspectable and not coupled to one active chat session

### AI-Builder Estimate

`3 to 6 days`

## Phase 7: Cortex Parity Layer

### Objective

Close the remaining gap between "Cognee with integrations" and a credible Cortex implementation.

### What Still Needs To Be Custom

- retrieval trace ledger and audit surfaces
- stable operator inspection endpoints
- stronger canonical memory-object rules
- artifact provider identity and revision policy
- typed signal compiler and normalization rules
- promotion and review workflows
- retention and lifecycle policy enforcement
- export, backup, import, and rebuild tooling

### What Probably Does Not Need A Full Rebuild

- the durable memory store
- the staged memory lifecycle
- short-term versus long-term separation
- graph plus semantic retrieval foundation
- background enrichment pipeline shape

That is why this Cognee path is attractive. Most of the late work is policy and productization, not wholesale replatforming.

### AI-Builder Estimate

`6 to 12 days`

## Minimal Supporting Components To Accept In Phase 1

These are worth accepting immediately:

- `Cognee API`
- `Postgres + pgvector`
- `Neo4j`
- `Redis`
- one strong hosted extraction model provider
- the official `@cognee/cognee-openclaw` plugin

These are acceptable but not required in phase 1:

- `Cognee MCP`
- a small maintenance worker
- a thin remram-owned wrapper plugin around the stock OpenClaw integration

These should stay out until justified:

- `OpenSearch`
- the upstream frontend
- a second durable memory backend
- a large custom Cortex service

## What The Architecture Looks Like After The Two Big Bites

After `Cognee` and `OpenClaw` do their part, the remaining custom architecture is smaller than it first appears.

You are left building roughly five remram-owned modules:

1. `openclaw-cognee`
   Starts on the stock plugin path and later owns direct-write lifecycle upgrades.

2. `cortex-datapoints`
   Defines the durable object families that matter most.

3. `retrieval-policy-wrapper`
   Converts Cortex scope and governance into Cognee retrieval constraints and records traces.

4. `artifact-ingest-worker`
   Turns source documents and tool outputs into durable `DataPoint` objects and structured graph memory.

5. `maintenance-worker`
   Runs session promotion, `memify`, cleanup, and audits.

That is materially less work than building an authority platform from first principles.

## Where `OpenSearch` Still Fits

`OpenSearch` is not part of the baseline recommendation, but it is not forbidden forever.

It becomes reasonable only if one of these becomes true:

- passage-oriented document search matters more than Cognee's current vector and graph posture
- you want heavy search analytics or faceting across imported corpora
- a tested community `OpenSearch` adapter becomes stable enough to trust
- you want a projection for operator search without making it the authority

If `OpenSearch` is added later, it should usually be:

- a projection
- a secondary retrieval surface
- or a cautiously validated vector adapter

It should not replace the Cognee-centered authority model unless the whole foundation choice changes.

## Recommended Sequence

If you want the shortest serious path with the lowest rebuild risk, do the work in this order:

1. Phase 0 foundation freeze
2. Phase 1 Moltbox baseline
3. Phase 2 OpenClaw bridge v0
4. Phase 3 durable authority hardening
5. Phase 4 retrieval and governance layer
6. Phase 5 artifact and document ingestion
7. Phase 6 sessions, promotion, and Dream-lite
8. Phase 7 Cortex parity layer

Do not jump to phase 4 first.

Do not build a large custom Cortex service before the live memory loop exists.

Do not over-invest in multi-dataset policy until the chosen self-hosted handler posture is proven.

## Recommendation

Use `Cognee` as the primary foundation if the priority is:

- fast progress to a usable system
- strong built-in lifecycle machinery
- real extension seams
- dockerized external services that fit naturally on `Moltbox`

Start with:

- `Cognee API + Postgres + pgvector + Neo4j + Redis` as separate containers in one `Moltbox` bundle
- the official `@cognee/cognee-openclaw` plugin
- explicit bearer-token auth
- one primary dataset in phase 1
- one strong hosted model provider for extraction quality

Keep phase 1 intentionally narrow:

- deploy the stack cleanly
- authenticate cleanly
- sync memory files
- retrieve bounded context
- prove a live memory loop

Then harden the durable model and build Cortex-specific policy in layers.

This is not the cleanest authority model in the field.

It is probably the best balance of:

- rich lifecycle leverage
- acceptable long-term replatform risk
- strong self-hosted service posture
- and realistic time to usefulness

## Primary Sources Reviewed

- `https://github.com/topoteretes/cognee`
- `https://github.com/topoteretes/cognee/blob/main/docker-compose.yml`
- `https://docs.cognee.ai/guides/deploy-rest-api-server`
- `https://docs.cognee.ai/integrations/openclaw-integration`
- `https://docs.cognee.ai/core-concepts/building-blocks/datapoints`
- `https://docs.cognee.ai/how-to-guides/own-data-model`
- `https://docs.cognee.ai/core-concepts/main-operations/search`
- `https://docs.cognee.ai/core-concepts/main-operations/memify`
- `https://docs.cognee.ai/guides/memify-quickstart`
- `https://docs.cognee.ai/core-concepts/sessions-and-caching`
- `https://docs.cognee.ai/guides/sessions`
- `https://docs.cognee.ai/setup-configuration/permissions`
- `https://docs.cognee.ai/core-concepts/multi-user-mode/multi-user-mode-overview`
- `https://docs.cognee.ai/cognee-mcp/mcp-quickstart`

## Local References Reviewed

- `d:/Development/RemRam/remram-cortex/docs/design/cognee-complete-context.md`
- `d:/Development/RemRam/remram-cortex/docs/design/cognee-openclaw-lifecycle-architecture.md`
- `d:/Development/RemRam/moltbox-services/services/openclaw-dev/service.yaml`
- `d:/Development/RemRam/moltbox-services/services/openclaw-dev/compose.yml.template`
- `d:/Development/RemRam/moltbox-services/services/openclaw-test/service.yaml`
- `d:/Development/RemRam/moltbox-services/services/openclaw-prod/service.yaml`
- `d:/Development/RemRam/_diag/cognee-upstream/.env.template`
- `d:/Development/RemRam/_diag/cognee-upstream/docker-compose.yml`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/infrastructure/engine/models/DataPoint.py`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/modules/memify/memify.py`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/memify_pipelines/persist_sessions_in_knowledge_graph.py`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/infrastructure/session/session_manager.py`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/api/v1/search/search.py`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/modules/retrieval/register_retriever.py`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/modules/run_custom_pipeline/run_custom_pipeline.py`
- `d:/Development/RemRam/_diag/cognee-upstream/examples/guides/custom_tasks_and_pipelines.py`
- `d:/Development/RemRam/_diag/cognee-upstream/examples/demos/conversation_session_persistence_example.py`
