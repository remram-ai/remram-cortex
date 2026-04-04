# Mem0 on Moltbox to OpenClaw to Cortex Implementation Plan

## Purpose

This document is the full implementation plan for adopting `Mem0` as the primary memory foundation for `remram-cortex`.

It covers the full path from:

- standing up the baseline `Mem0` architecture on `Moltbox`
- connecting that authority layer to `OpenClaw`
- expanding the stack until it covers the practical Cortex vision

This plan is intentionally `Postgres`-first. It does not force `OpenSearch`.

Reviewed on `April 2, 2026`.

## Blunt Read

`Mem0` is still the fastest believable route to a usable Cortex-like memory authority if we are willing to accept a few disciplined compromises.

The right implementation posture is:

- start close to the stock `Mem0` and `OpenClaw` integration
- use `Postgres + pgvector` as the durable base
- keep `Mem0` as the only durable memory authority
- accept SQLite history at first as a library-owned audit log
- keep graph memory optional and later
- add Cortex-specific provenance, policy, and inspection in layers

Do not start by forcing `OpenSearch` into this path.

Do not start by replacing Mem0's add, update, delete, and no-op lifecycle logic.

Do not let `OpenClaw` Markdown memory become a peer authority beside Mem0.

If the work is done in the right order, the first usable system is realistic in about `1 to 2 weeks` of focused AI-assisted implementation, and a credible "Cortex on Mem0" v1 is realistic in about `5 to 9 weeks`.

## Planning Assumptions

- One human builder, heavily AI-assisted.
- Local and free infrastructure is required.
- Dockerized external services are preferred.
- `OpenSearch` is optional, not mandatory.
- `Dream` is not a gating criterion for platform choice.
- Lowest long-term replatform risk matters more than chasing the richest storage feature list immediately.
- Staying close to the stock library matters more than perfect phase-1 semantic purity.

## Core Architectural Decision

Treat `Mem0` as the durable memory authority.

Treat `Postgres + pgvector` as the implementation store under Mem0, not as an app-owned memory schema.

Treat `OpenClaw` as the runtime shell and session host, not as the durable memory authority.

Treat future Cortex code as a policy and contract layer on top of Mem0, not as a parallel memory platform.

That produces the cleanest long-term shape:

```text
Channels / Agents / Tools
          |
          v
OpenClaw Gateway
  - runtime orchestration
  - session lifecycle
  - tools / hooks / automation
  - Mem0 bridge plugin
          |
          v
Mem0 Authority Layer
  - add / update / delete / none lifecycle
  - scoped memory records
  - search + filters + thresholds + reranking
  - history
  - optional graph enrichment later
          |
          +--> Postgres + pgvector
          |     - durable memory vectors
          |     - metadata payloads
          |
          +--> SQLite history
                - library-owned audit log

Optional later sidecars:
  - Mem0 REST API container
  - Cortex retrieval facade
  - artifact ingest worker
  - maintenance / Dream-lite worker
  - optional graph sidecar
```

## Why PostgreSQL Is The Right Mem0 Compromise

Under Mem0, `OpenSearch` is not the obvious win it might be in other architectures.

Why:

- Mem0's real leverage is the lifecycle engine, not raw search-engine semantics
- the current Mem0 `pgvector` path is first-class and documented
- the current `OpenClaw` plugin already expects a fairly narrow OSS storage contract
- `Postgres + pgvector` is good enough for filtered semantic recall in phase 1
- staying on `Postgres` makes the stack easier to reason about and less likely to force an early migration

The hard trade is simple:

- `OpenSearch` gives a more search-native ceiling
- `Postgres + pgvector` gives a more boring, library-consistent, lower-regret phase 1 for this specific `Mem0` path

That is the right compromise here.

## Why The Baseline Starts In-Process, Not With A Full External Mem0 Service

There is one important upstream nuance.

The stock `@mem0/openclaw-mem0` plugin is a real accelerator.

The stock `Mem0` REST server is useful, but its default server posture currently assumes more graph configuration than we want for a strict `Postgres`-first baseline.

So the cleanest low-regret phase-1 move is:

- run `OpenClaw` with the official Mem0 plugin in OSS mode
- point that plugin at a separate `Postgres + pgvector` container on `Moltbox`
- persist the plugin history DB on a mounted volume

Then, only after the memory loop proves itself:

- add a small Mem0 server fork or wrapper
- or a thin REST adapter plugin

That keeps us close to the stock library while still moving toward a cleaner external-service boundary later.

## The Most Important Guardrails

These rules should be fixed before implementation starts:

- `Mem0` is the only durable write path for memory objects.
- `OpenClaw` transcripts are evidence, not authority.
- `OpenClaw` Markdown memory is projection or editable source, not the durable authority.
- `Postgres + pgvector` stores Mem0 records, not app-owned parallel objects.
- SQLite history is acceptable in phase 1 because it is audit support, not the authority store.
- Graph memory is optional and should stay optional until the vector-plus-metadata path proves insufficient.
- `OpenSearch` stays out of phase 1.
- Metadata discipline begins on day 1 even if the phase-1 object is still "just" a Mem0 record.

## What To Accept The Mem0 Way

If this path is chosen, several Cortex ideas should be implemented the `Mem0` way instead of forcing a parallel system too early.

| Cortex intent | Mem0-native equivalent | Decision |
| --- | --- | --- |
| Durable memory object | memory record plus metadata plus history | Accept directly |
| Memory lifecycle | add, update, delete, none | Accept directly |
| Coarse scope boundary | `user_id`, `agent_id`, `run_id` | Accept directly |
| Retrieval policy start point | search, filters, thresholds, rerankers | Accept directly |
| Evidence and correction trail | history log plus metadata | Accept with modification |
| Relationship awareness | optional graph memory | Accept later, not baseline |
| Reflection / Dream-lite | plugin skills and maintenance jobs | Accept later |
| Operator access | tools, CLI, optional REST server | Accept directly |
| Governance-first retrieval | metadata discipline plus wrapper | Custom layer required |
| Artifact identity and provider identity | metadata contract | Custom layer required |
| Retrieval traces and audit views | remram-owned wrapper | Custom layer required |

The main worldview shift is this:

- a Cortex memory object becomes a disciplined Mem0 memory record first
- not a bespoke canonical object system beside Mem0

That is the compromise that saves the most time.

## Hard Differences And How To Handle Them

### 1. The native durable unit is still a memory record

This is the core semantic compromise.

Mem0 stores extracted memory records, not graph-native facts or typed domain objects by default.

The correct response is not to reject Mem0.

The correct response is:

- impose a metadata contract early
- keep the text concise and canonical
- treat each record as a proto-knowledge object

This is good enough for phase 1 and phase 2.

### 2. History is SQLite

Current Mem0 OSS keeps history in SQLite.

That is not ideal if you want every durable component to live in one service family.

It is still acceptable because:

- history is audit support, not the recall authority
- the actual durable memory records live in `Postgres + pgvector`
- the simplest safe move is to persist the SQLite file on a mounted volume and move on

Do not rebuild Mem0 just to eliminate this compromise in phase 1.

### 3. The official OpenClaw plugin is stronger than the official Mem0 server for this exact baseline

The official plugin already gives:

- auto-recall
- auto-capture
- five memory tools
- scope handling
- filtering
- per-agent isolation
- non-interactive trigger filtering
- a built-in Dream-lite and skills path in source

By contrast, the official Mem0 REST server is useful, but its default startup posture is less aligned with a clean graph-off `Postgres`-only baseline.

So phase 1 should use the plugin, not force the server.

### 4. Graph memory is enrichment, not baseline authority

Mem0 graph memory can help later, but it does not need to anchor the initial architecture.

Baseline recommendation:

- start vector-plus-metadata only
- use retrieval filters and rerankers first
- only add graph memory if relationship recall becomes a proven need

### 5. If we want graph later and still want to stay on PostgreSQL, accept the compromises openly

If relationship memory later matters and we still want to stay in the PostgreSQL family, the most aligned compromise is:

- keep `pgvector` for vector search
- add `Apache AGE` as the graph store only if justified

That stays close to the Mem0 library and stays inside the PostgreSQL family, but it comes with tradeoffs:

- graph search does not become the primary ranking engine
- similarity support is not as elegant as a dedicated graph stack
- it is good enough for moderate scale, not the fanciest possible design

That is acceptable for a personal Cortex build.

## Target End State

The final practical architecture should look like this:

```text
OpenClaw
  - channels
  - sessions
  - tools
  - cron / hooks / background work
  - Mem0 integration plugin
          |
          v
Cortex Mem0 Layer
  - metadata contract
  - provenance compiler
  - retrieval bundle assembly
  - retrieval traces
  - artifact and promotion policy
  - operator inspection API
          |
          v
Mem0 Core / Extension Layer
  - extraction and update prompts
  - search + filters + reranking
  - history
  - optional graph enrichment
          |
          +--> Postgres + pgvector
          +--> SQLite history
          +--> optional REST server
          +--> optional graph sidecar
```

The key point is that even if a Cortex facade is added later, the durable memory authority stays inside Mem0. That keeps later cleanup from turning into data replatforming.

## Repo Landing Zones

Implementation should stay split by responsibility.

### `moltbox-services`

Add new service bundles here:

- `d:/Development/RemRam/moltbox-services/services/mem0-dev/`
- `d:/Development/RemRam/moltbox-services/services/mem0-test/`
- `d:/Development/RemRam/moltbox-services/services/mem0-prod/`

Phase-1 bundle contents:

- `mem0-postgres` container
- optional `mem0-api` container later, not required on day 1

Each bundle should include:

- `service.yaml`
- `compose.yml.template`

### `remram`

Add the `OpenClaw` integration and platform docs here:

- `d:/Development/RemRam/remram/platform/plugins/openclaw-mem0/`
- `d:/Development/RemRam/remram/platform/services/mem0/`

The plugin package should eventually own:

- stock-plugin configuration overlays
- metadata contract helpers
- provenance sidecars
- optional REST transport later
- operator tools for memory inspection

### `remram-cortex`

Keep the design, policy, and contract docs here first:

- this implementation plan
- metadata contract docs
- governance and retrieval policy docs
- later, any Cortex facade spec if one is added

## Phase 0: Foundation Freeze

### Objective

Lock the architectural guardrails before any code is written.

### Major Work

- choose `Postgres + pgvector` as the baseline durable store
- explicitly keep `OpenSearch` out of the baseline plan
- decide to start with the official OpenClaw plugin in OSS mode
- define the first metadata envelope
- decide whether graph memory is deferred entirely or treated as an explicit later option
- choose the baseline extraction model posture

### Required Decisions

- initial `user_id`, `agent_id`, and `run_id` mapping rules
- first-pass metadata fields
- history persistence location
- minimum viable LLM provider for extraction
- whether phase 3 introduces a REST service boundary or stays plugin-only longer

### Recommended Outcome

- `Postgres + pgvector` is the baseline
- official `@mem0/openclaw-mem0` plugin is the phase-1 bridge
- history SQLite file is persisted on disk and accepted as a compromise
- graph memory is deferred
- `OpenAI` or `Gemini` is used for extraction until quality is proven

### Exit Criteria

- no unresolved argument remains about the authority model
- no unresolved argument remains about using `Postgres` instead of `OpenSearch`
- the future plan does not require a second durable memory authority

### AI-Builder Estimate

`1 to 2 days`

## Phase 1: Moltbox Baseline Deployment

### Objective

Stand up a working `Mem0` baseline on `Moltbox` with `Postgres + pgvector` as the durable base and `OpenClaw` as the runtime shell.

### Baseline Service Shape

Start with two running pieces:

- existing `OpenClaw` service on `Moltbox`
- one new `mem0-postgres` container on `Moltbox`

In phase 1, Mem0 itself runs inside the official OpenClaw plugin process in OSS mode.

That is deliberate.

It avoids a premature server fork while still externalizing the durable store.

### Container Contract

Recommended baseline posture:

- pin a known-good `pgvector` image, ideally the same family used by the upstream Mem0 server compose
- attach `mem0-postgres` to `moltbox_internal`
- persist the Postgres data volume outside the container
- create the `vector` extension at startup
- keep the Mem0 history file on a persistent OpenClaw-mounted path

### Recommended Phase-1 Plugin Config

Use the official plugin in OSS mode with an explicit `pgvector` override:

```json5
"openclaw-mem0": {
  "enabled": true,
  "config": {
    "mode": "open-source",
    "userId": "jason-main",
    "topK": 8,
    "searchThreshold": 0.5,
    "oss": {
      "embedder": {
        "provider": "openai",
        "config": { "model": "text-embedding-3-small" }
      },
      "vectorStore": {
        "provider": "pgvector",
        "config": {
          "host": "mem0-postgres",
          "port": 5432,
          "dbname": "mem0",
          "user": "mem0",
          "password": "${MEM0_POSTGRES_PASSWORD}",
          "collectionName": "memories",
          "embeddingModelDims": 1536,
          "hnsw": false,
          "diskann": false
        }
      },
      "llm": {
        "provider": "openai",
        "config": { "model": "gpt-4.1-nano-2025-04-14", "temperature": 0.2 }
      },
      "historyDbPath": ".openclaw/mem0/history.db"
    }
  }
}
```

### Why This Phase-1 Posture Is Correct

It buys:

- no library fork yet
- no second plugin yet
- real durability in `Postgres + pgvector`
- minimal gap from the official docs and plugin code

It accepts:

- history is still SQLite
- Mem0 is still in-process inside the plugin
- operator access is initially plugin and CLI centric, not service centric

Those are the right compromises for phase 1.

### Major Work

- create the `mem0-dev` bundle with `mem0-postgres`
- wire secrets and persistent volume paths
- update `openclaw-dev` config to install and configure `@mem0/openclaw-mem0`
- smoke test add, recall, explicit memory tools, and persistence across restarts
- inspect the actual stored records and history file

### Exit Criteria

- `mem0-postgres` comes up cleanly on `Moltbox`
- OpenClaw can recall memories from `pgvector`
- OpenClaw can capture memories into `pgvector`
- memory records persist across service restarts
- the history file persists across container restarts

### AI-Builder Estimate

`2 to 4 days`

## Phase 2: OpenClaw Bridge v0

### Objective

Prove a live memory loop with the stock plugin before adding any custom service boundary or large policy layer.

### Recommended Implementation

Use the official plugin as-is first:

- `@mem0/openclaw-mem0`

Keep it in legacy mode first.

Do not enable the more advanced skills path before we understand baseline recall and capture quality.

### What The Stock Plugin Already Gives

- auto-recall before reply
- auto-capture after reply
- five memory tools
- scope handling with `userId`, session `run_id`, and per-agent namespace logic
- non-interactive trigger filtering
- subagent protection behavior
- operator CLI

That is enough to prove:

- memory helps live runtime
- the scope model is workable
- Mem0 can already anchor the durable authority role

### What To Watch Carefully

The plugin's default worldview is still "capture conversational facts."

That means phase 2 should be treated as:

- proof of the memory loop
- not proof that the final object model is complete

### Operator Tools

Use the stock tools and add a few local conventions:

- `memory_search`
- `memory_list`
- `memory_store`
- `memory_get`
- `memory_forget`

Also use CLI checks:

- `openclaw mem0 search`
- `openclaw mem0 stats`

### Exit Criteria

- a normal OpenClaw conversation triggers recall from Mem0 automatically
- post-turn capture stores useful records in `pgvector`
- session and long-term scopes behave as expected
- disabling the plugin leaves OpenClaw stable

### AI-Builder Estimate

`2 to 4 days`

## Phase 3: Service Boundary Hardening

### Objective

Introduce a cleaner external Mem0 service boundary only after the stock plugin path proves itself.

### Why This Phase Exists

The stock plugin is the fastest start.

It is probably not the final operational shape if you want:

- a clearer external service boundary on `Moltbox`
- API-key auth
- language-neutral access
- richer operator inspection
- access to Mem0 surfaces that the stock plugin does not expose cleanly

### Recommended Implementation

Create a minimal remram-owned Mem0 server wrapper or fork based on the upstream REST server.

The wrapper should do as little as possible:

- keep the upstream API surface
- keep the upstream Mem0 library underneath
- remove the hard assumption that graph storage is enabled by default
- make the startup config explicitly `pgvector`-first
- persist history on a mounted volume

### Important Constraint

Do not rewrite the Mem0 library.

Do not build a bespoke memory service.

Only adapt the upstream server startup posture so it aligns with the chosen baseline.

### OpenClaw Integration Move

Once that server exists, create a thin plugin adapter or fork of `@mem0/openclaw-mem0` that changes the transport layer, not the whole behavior model.

That adapter should:

- preserve the recall and capture logic
- preserve filtering and scope handling
- call the local Mem0 REST API instead of the in-process SDK

### Exit Criteria

- a local `mem0-api` container runs cleanly on `Moltbox`
- `OpenClaw` can talk to it through a thin plugin adapter
- phase-1 behavior does not regress when the transport changes
- the architecture now has a clean external service boundary

### AI-Builder Estimate

`3 to 6 days`

## Phase 4: Durable Authority Hardening

### Objective

Stop treating the system like "helpful memory capture" and make the stored records structurally compatible with Cortex.

### Major Work

- define the metadata envelope that every important memory record must carry
- standardize `memory_kind`
- standardize source and artifact fields
- standardize update discipline
- standardize long-term versus session policy

### Recommended First Metadata Envelope

At minimum:

- `memory_kind`
- `source_type`
- `source_locator`
- `artifact_id`
- `artifact_revision`
- `project_id`
- `repo_id`
- `scope_kind`
- `confidence`
- `promotion_state`
- `trace_id`

This is the most important move for keeping migration risk down.

### Mem0-Native Levers To Exploit

Use the library before replacing it:

- `customPrompt` or custom fact extraction prompt to narrow what gets stored
- custom update memory prompt once the service path exposes it cleanly
- metadata filters
- reranking
- history

### Important Compromise

Do not try to build a full typed object model beside Mem0 in phase 4.

Early on:

- use disciplined record text
- enforce disciplined metadata
- capture provenance aggressively

That is enough to move forward without starting a second system.

### Exit Criteria

- important memories carry the metadata needed for later evolution
- records are no longer just free-form memory text with ad hoc tags
- there is no need to throw away phase-1 or phase-2 data to continue

### AI-Builder Estimate

`4 to 7 days`

## Phase 5: Retrieval and Governance Layer

### Objective

Add the custom layer that Mem0 does not natively provide: governance-first retrieval and stable Cortex-shaped retrieval bundles.

### What Gets Built

This phase adds a thin remram-owned wrapper around Mem0 retrieval.

Responsibilities:

- compile Cortex scope and governance inputs into Mem0 filters
- choose thresholds and rerankers deterministically
- cap and format retrieval bundles for OpenClaw
- record retrieval traces
- expose inspectable operator APIs

### Why This Phase Matters

Mem0 search is already useful.

Cortex still wants:

- stable retrieval contracts
- deterministic scope boundaries
- inspectable trace output
- clear distinction between raw candidates and injected context

That logic belongs in a remram-owned layer, not only in prompt assembly.

### Mem0-Native Levers To Exploit First

Before replacing retrieval behavior, use:

- metadata filters
- `user_id`, `agent_id`, `run_id`
- thresholds
- rerankers
- history lookups

### Exit Criteria

- OpenClaw retrieves memory through a remram-owned policy surface, not just raw plugin defaults
- retrieval traces exist
- policy decisions are inspectable

### AI-Builder Estimate

`4 to 7 days`

## Phase 6: Artifact and Document Ingestion

### Objective

Expand beyond conversational memory into artifact-backed memory while still staying close to the Mem0 library.

### Mem0-Native Approach

Do this the Mem0 way first:

- convert artifacts into disciplined memory facts
- store artifact identity and source metadata on the resulting records
- use batch add or controlled add flows
- use update prompts to keep records current when artifacts change

Do not create a second durable artifact-memory store in phase 6.

### Raw Content Rule

Keep raw source artifacts authoritative outside Mem0 when possible.

For example:

- git remains authoritative for repos
- provider documents remain authoritative in their source system
- local files remain authoritative in local storage

Mem0 should store:

- distilled durable facts
- source links
- revision identifiers
- provenance

That is enough to keep the architecture coherent.

### Major Work

- define artifact-backed memory kinds
- define extraction rules for documents and tool outputs
- preserve source locator and revision metadata
- expose provenance inspection tools

### Exit Criteria

- imported artifacts create durable Mem0 records with traceable provenance
- recalled memory can be walked back to a source artifact or revision
- Mem0 remains the sole durable authority

### AI-Builder Estimate

`4 to 7 days`

## Phase 7: Maintenance, Dream-Lite, And Promotion

### Objective

Add consolidation and maintenance without replacing Mem0's core lifecycle engine.

### Native Levers

Start with what already exists:

- Mem0 update logic
- Mem0 history
- plugin-side skills and dream concepts
- scheduled cleanup and audit jobs

### Recommended Phase Order

Start small:

- stale-record review
- repeated-update detection
- promotion-candidate tagging
- summary rebuild jobs

Only later consider enabling the plugin's richer skills and dream path if the baseline system is stable and the changed lifecycle is actually useful.

### Why Not Turn On Skills Mode Immediately

The current plugin source shows that skills mode changes the lifecycle significantly.

It is powerful, but it is not the simplest route to proving the baseline architecture.

So:

- do not start there
- evaluate it only after the normal recall and capture loop is trustworthy

### Exit Criteria

- the system improves memory quality between live turns
- maintenance work is inspectable
- promotion is becoming explicit instead of ad hoc

### AI-Builder Estimate

`3 to 6 days`

## Phase 8: Optional PostgreSQL-Family Graph Upgrade

### Objective

Add relationship memory only if the vector-plus-metadata architecture proves insufficient.

### Recommended PostgreSQL-First Option

If you want to stay in the PostgreSQL family, the cleanest Mem0-aligned option is:

- keep `pgvector` as the vector store
- add `Apache AGE` as the graph store

### Why This Is Only Optional

Mem0 graph memory:

- enriches recall
- adds related entities
- does not automatically become the core ranking engine

That means graph memory is useful, but not required to get a credible Cortex-like memory authority running.

### Hard Tradeoffs To Accept

If you choose this path, accept:

- more operational and migration complexity than the vector-only baseline
- less graph sophistication than a dedicated graph-first foundation
- good-enough relationship memory rather than a graph-native authority model

### Exit Criteria

- graph memory is only introduced in response to a real retrieval need
- the authority model still stays inside Mem0
- the graph layer is additive, not a second authority

### AI-Builder Estimate

`3 to 6 days`

## Phase 9: Cortex Parity Layer

### Objective

Close the remaining gap between "Mem0 with disciplined overlays" and a credible Cortex implementation.

### What Still Needs To Be Custom

- retrieval trace ledger and audit surfaces
- stable operator inspection endpoints
- stronger provenance normalization
- artifact provider identity and revision policy
- typed signals and semantic signature if retained in the vision
- promotion and review workflows
- export, backup, import, and rebuild tooling

### What Probably Does Not Need A Full Rebuild

- the durable memory authority
- the scope model
- the basic add, update, delete, and no-op lifecycle
- filtered recall
- the runtime integration shape

That is why this Mem0 path stays attractive. Most of the late work is policy and productization, not a full data migration.

### AI-Builder Estimate

`5 to 10 days`

## Minimal Supporting Components To Accept In Phase 1

These are worth accepting immediately:

- `OpenClaw`
- official `@mem0/openclaw-mem0` plugin
- `Postgres + pgvector`
- one strong hosted extraction model provider
- persisted SQLite history file

These are acceptable but not required in phase 1:

- a thin Mem0 REST wrapper later
- a small maintenance worker
- a reranker once recall quality needs help

These should stay out until justified:

- `OpenSearch`
- graph memory
- a large custom Cortex service
- a second durable memory backend

## What The Architecture Looks Like After The Two Big Bites

After `Mem0` and `OpenClaw` do their part, the remaining custom architecture is smaller than it first appears.

You are left building roughly five remram-owned modules:

1. `openclaw-mem0`
   Starts with the stock plugin and later owns configuration or transport hardening.

2. `mem0-metadata-contract`
   Defines the provenance, artifact, and lifecycle metadata envelope.

3. `retrieval-policy-wrapper`
   Converts Cortex scope and governance inputs into Mem0 retrieval constraints and records traces.

4. `artifact-ingest-worker`
   Turns source artifacts and tool outputs into disciplined Mem0 records.

5. `maintenance-worker`
   Runs review, cleanup, promotion, and audit flows.

That is materially less work than building a memory authority from scratch.

## Where `OpenSearch` Still Fits

`OpenSearch` is not forbidden forever, but it is not the right baseline in this architecture.

It becomes reasonable only if one of these becomes true:

- passage-oriented document retrieval becomes much more important than disciplined memory records
- Mem0's `Postgres + pgvector` path proves too limited for the actual retrieval workload
- a future Mem0 adapter or service posture makes `OpenSearch` materially more attractive than it is today

If `OpenSearch` is added later, it should usually be:

- a later storage migration inside the Mem0 path, or
- a projection or secondary search surface

It should not be introduced in phase 1 just because it is powerful elsewhere.

## Recommended Sequence

If you want the shortest serious path with the lowest rebuild risk, do the work in this order:

1. Phase 0 foundation freeze
2. Phase 1 Moltbox baseline
3. Phase 2 OpenClaw bridge v0
4. Phase 3 service boundary hardening
5. Phase 4 durable authority hardening
6. Phase 5 retrieval and governance layer
7. Phase 6 artifact and document ingestion
8. Phase 7 maintenance, Dream-lite, and promotion
9. Phase 8 optional PostgreSQL-family graph upgrade
10. Phase 9 Cortex parity layer

Do not jump to graph memory first.

Do not build a large custom Cortex service before the live memory loop exists.

Do not force an external Mem0 server before the plugin path proves itself unless external-service purity matters more than speed.

## Recommendation

Use `Mem0` as the primary foundation if the priority is:

- fastest path to a usable memory authority
- staying close to a real memory lifecycle engine
- keeping `Postgres` as the durable base
- making a few pragmatic compromises rather than rebuilding the library

Start with:

- `OpenClaw` on `Moltbox`
- official `@mem0/openclaw-mem0` plugin in OSS mode
- `Postgres + pgvector` as the durable store
- persisted SQLite history
- one strong hosted model provider for extraction quality

Keep phase 1 intentionally narrow:

- deploy the store
- configure the plugin
- prove recall and capture
- inspect the stored records
- confirm that disciplined metadata can keep the data on a forward path

Then harden the service boundary and add Cortex-specific policy in layers.

This is not the cleanest authority model in the field.

It is the best balance here of:

- speed to something useful
- reasonable long-term replatform risk
- library consistency
- and a clear PostgreSQL-first posture

## Primary Sources Reviewed

- `https://github.com/mem0ai/mem0`
- `https://github.com/mem0ai/mem0/blob/main/openclaw/README.md`
- `https://github.com/mem0ai/mem0/blob/main/openclaw/index.ts`
- `https://github.com/mem0ai/mem0/blob/main/server/docker-compose.yaml`
- `https://docs.mem0.ai/open-source/overview`
- `https://docs.mem0.ai/integrations/openclaw`
- `https://docs.mem0.ai/open-source/features/graph-memory`
- `https://docs.mem0.ai/open-source/features/rest-api`
- `https://docs.mem0.ai/open-source/features/custom-update-memory-prompt`
- `https://docs.mem0.ai/open-source/features/metadata-filtering`
- `https://docs.mem0.ai/components/vectordbs/dbs/pgvector`
- `https://docs.mem0.ai/components/vectordbs/dbs/opensearch`

## Local References Reviewed

- `d:/Development/RemRam/remram-cortex/docs/design/mem0-complete-context.md`
- `d:/Development/RemRam/remram-cortex/docs/design/mem0-openclaw-lifecycle-architecture.md`
- `d:/Development/RemRam/remram-cortex/docs/design/mem0-weaviate-openclaw-lifecycle-architecture.md`
- `d:/Development/RemRam/moltbox-services/services/openclaw-dev/compose.yml.template`
- `d:/Development/RemRam/_diag/mem0/openclaw/README.md`
- `d:/Development/RemRam/_diag/mem0/openclaw/index.ts`
- `d:/Development/RemRam/_diag/mem0/openclaw/providers.ts`
- `d:/Development/RemRam/_diag/mem0/server/docker-compose.yaml`
- `d:/Development/RemRam/_diag/mem0/server/main.py`
- `d:/Development/RemRam/_diag/mem0/mem0/configs/base.py`
- `d:/Development/RemRam/_diag/mem0/mem0/memory/main.py`
- `d:/Development/RemRam/_diag/mem0/docs/open-source/overview.mdx`
- `d:/Development/RemRam/_diag/mem0/docs/open-source/features/graph-memory.mdx`
- `d:/Development/RemRam/_diag/mem0/docs/open-source/features/rest-api.mdx`
- `d:/Development/RemRam/_diag/mem0/docs/open-source/features/custom-update-memory-prompt.mdx`
- `d:/Development/RemRam/_diag/mem0/docs/open-source/features/metadata-filtering.mdx`
- `d:/Development/RemRam/_diag/mem0/docs/components/vectordbs/dbs/pgvector.mdx`
- `d:/Development/RemRam/_diag/mem0/docs/components/vectordbs/dbs/opensearch.mdx`
