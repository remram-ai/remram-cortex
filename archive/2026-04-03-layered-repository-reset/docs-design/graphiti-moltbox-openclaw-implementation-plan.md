# Graphiti on Moltbox to OpenClaw to Cortex Implementation Plan

## Purpose

This document is the full implementation plan for adopting `Graphiti` as the primary long-term memory foundation for `remram-cortex`.

It covers the full path from:

- standing up the baseline `Graphiti + Neo4j` architecture as dockerized Moltbox services
- connecting that authority layer to `OpenClaw`
- expanding the stack until it covers the practical Cortex vision

Reviewed on `April 2, 2026`.

## Blunt Read

`Graphiti` is the strongest primary foundation if the goal is a real memory authority layer rather than a retrieval subsystem.

The right implementation posture is:

- start with `Graphiti` as a separate service boundary on `Moltbox`
- keep `Neo4j` as Graphiti's backing store
- connect `OpenClaw` with a thin plugin or bridge first
- keep `Graphiti` as the only durable memory write authority
- add Cortex-specific policy, governance, artifact, and maintenance layers in phases

Do not start by rebuilding Cortex as a custom service from scratch.

Do not start by forcing `OpenSearch` into the baseline.

Do not let `OpenClaw` keep a second durable memory store in parallel.

If the work is done in the right order, the first usable system is realistic in about `1 to 2 weeks` of focused AI-assisted implementation, and a credible "Cortex on Graphiti" v1 is realistic in about `6 to 10 weeks`.

## Planning Assumptions

- One human builder, heavily AI-assisted.
- Local and free infrastructure is required.
- Dockerized external services are acceptable and preferred.
- Model APIs are allowed if they reduce build risk.
- `OpenSearch` is optional, not mandatory.
- `Dream` is not a gating criterion for platform choice.
- Lowest long-term data replatform risk matters more than shortest possible demo path.

## Core Architectural Decision

Treat `Graphiti` as the durable memory authority.

Treat `Neo4j` as Graphiti's implementation store, not as an app-owned schema.

Treat `OpenClaw` as the runtime shell and agent host, not the memory authority.

Treat future Cortex code as a policy and contract layer on top of Graphiti, not as a second durable store.

That produces the cleanest long-term shape:

```text
Channels / Agents / Tools
          |
          v
OpenClaw Gateway
  - runtime orchestration
  - session lifecycle
  - tools / hooks / automation
  - graphiti bridge plugin
          |
          v
Graphiti Authority Service
  - episode ingestion
  - entity + fact lifecycle
  - search recipes + filters
  - ontology and provenance extensions
          |
          v
Neo4j Community
  - durable graph store
  - indexes
  - vector + keyword + traversal substrate

Optional later sidecars:
  - Graphiti MCP server for inspection
  - Cortex facade service
  - artifact import worker
  - maintenance / Dream-lite worker
  - OpenSearch projection if document search pressure justifies it
```

## The Most Important Guardrails

These rules should be fixed before implementation starts:

- `Graphiti` is the only durable write path for memory objects.
- `OpenClaw` transcripts are evidence, not authority.
- Direct `Cypher` writes are maintenance-only, not app behavior.
- `group_id` is a coarse partition boundary, not a substitute for the entire Cortex governance model.
- Fine-grained governance lives in labels, edge names, and node or edge attributes.
- Imported artifacts keep their source content outside Graphiti; Graphiti stores extracted structure, provenance, and links.
- `OpenSearch` stays out of phase 1 unless a specific blocking retrieval need appears.

## What To Accept The Graphiti Way

If this path is chosen, several Cortex ideas should be implemented the `Graphiti` way instead of being forced into a flat document memory model.

| Cortex intent | Graphiti-native equivalent | Decision |
| --- | --- | --- |
| Evidence intake | `Episode` nodes | Accept directly |
| Durable memory object | `EntityEdge` plus connected `EntityNode` records | Accept directly |
| Temporal truth | `valid_at`, `invalid_at`, `expired_at` | Accept directly |
| Provenance | episode references on facts plus episode content | Accept and extend |
| Memory scope | `group_id` plus filters | Accept with modification |
| Ontology | custom labels and edge names | Accept directly |
| Reflection / reconciliation | community maintenance, graph rebuild jobs, summarization | Accept as Dream-lite starting point |
| Conversation continuity | episodes, sagas, recent-episode retrieval | Accept partially |
| Document memory | text or JSON episodes plus `Document` entities | Accept directly |
| Governance-first retrieval | Graphiti filters plus custom policy wrapper | Custom layer required |

The main worldview shift is this:

- a Cortex "knowledge object" becomes a graph fact with linked entities and evidence
- not a single JSON row or search document

That is a feature, not a problem, if the goal is durable memory.

## Hard Differences And How To Handle Them

### 1. `group_id` is singular per stored object

This is the most important modeling constraint.

In stock `Graphiti`, nodes and edges carry one `group_id`. Cortex wants richer scope surfaces like person, family, project, repo, audience, lifecycle, and ownership.

Do not solve this by duplicating facts into many groups.

Instead:

- use `group_id` as the coarse authority partition, such as `jason-main`, `family-main`, `work-main`, or `sandbox`
- put finer scope and governance fields into labels and attributes
- extend the Graphiti service layer so search can compile those governance rules into Graphiti filters before retrieval

This keeps the stored graph forward-compatible and avoids later data migration.

### 2. Stock Graphiti server is intentionally thin

The upstream FastAPI server is enough for smoke tests, but not enough for Cortex.

It currently gives you:

- `/messages`
- `/search`
- `/get-memory`
- simple group deletion and clear endpoints
- basic OpenAI and Neo4j env configuration

It does not give you, out of the box:

- governance policy compilation
- retrieval traces
- artifact identity or revision policy
- richer filter exposure
- Cortex-specific ontology contracts
- promotion or Dream workflows

That is acceptable. The implementation plan assumes we will fork or extend the service layer early.

### 3. Graphiti is not a blob or artifact store

It should not become the canonical store for raw source files, PDFs, promoted docs, or exported artifacts.

Use Graphiti to store:

- extracted knowledge structure
- source references
- revision identifiers
- links to source artifacts
- summaries and derived graph facts

Keep raw source content in the source provider or local artifact storage.

### 4. Strong extraction quality still matters

Graphiti is much stronger with models that support reliable structured output.

The safest early posture is:

- use `OpenAI` or `Gemini` for extraction
- only experiment with local or weaker models after baseline quality is acceptable

Do not let "local models only" become the reason the memory foundation looks worse than it is.

## Target End State

The final practical architecture should look like this:

```text
OpenClaw
  - channels
  - sessions
  - tools
  - cron / hooks / background work
  - graphiti integration plugin
          |
          v
Cortex Graphiti Layer
  - governance compiler
  - ingestion policy
  - retrieval bundle assembly
  - retrieval traces
  - artifact and promotion policy
  - operator inspection API
          |
          v
Graphiti Core / Forked Service
  - episodes
  - entities
  - facts
  - invalidation
  - communities
  - search recipes
          |
          v
Neo4j
          |
          +--> optional MCP inspector
          +--> optional nightly maintenance worker
          +--> optional OpenSearch projection
```

The key point is that even if a Cortex facade is added later, the durable authority stays in the Graphiti graph. That keeps later architecture cleanup from turning into data replatforming.

## Repo Landing Zones

Implementation should stay split by responsibility.

### `moltbox-services`

Add new service bundles here:

- `d:/Development/RemRam/moltbox-services/services/graphiti-dev/`
- `d:/Development/RemRam/moltbox-services/services/graphiti-test/`
- `d:/Development/RemRam/moltbox-services/services/graphiti-prod/`

Each bundle should include:

- `service.yaml`
- `compose.yml.template`
- optional Dockerfile only if a custom Graphiti image becomes necessary

### `remram`

Add the `OpenClaw` integration and platform docs here:

- `d:/Development/RemRam/remram/platform/plugins/openclaw-graphiti/`
- `d:/Development/RemRam/remram/platform/services/graphiti/`

The plugin package should eventually own:

- Graphiti API client
- lifecycle hooks
- retrieval injection or context assembly integration
- operator tools for memory inspection

### `remram-cortex`

Keep the design, policy, and eventual Cortex contract docs here first:

- this implementation plan
- ontology contract docs
- governance and retrieval policy docs
- later, a concrete Cortex facade spec if one is added

## Phase 0: Foundation Freeze

### Objective

Lock the architectural guardrails before any code is written.

### Major Work

- choose `Neo4j Community` as the Graphiti backing store
- explicitly keep `OpenSearch` out of the baseline plan
- define the initial `group_id` strategy
- define the initial label and attribute strategy
- define the minimum viable extraction model posture
- decide whether phase 2 talks directly to Graphiti or to a thin remram-owned Graphiti fork

### Required Decisions

- `group_id` coarse partitioning scheme
- initial authority partitions such as `jason-main`, `family-main`, `sandbox`
- minimum first-pass ontology
- baseline LLM provider for extraction
- whether Neo4j Browser is exposed only on LAN admin ports or only through local operator access

### Recommended Outcome

- `group_id` is coarse and stable
- governance fields live in attributes
- `OpenAI` or `Gemini` is used for ingestion until quality is proven
- `Neo4j` and `Graphiti` are deployed as one Moltbox service bundle at first

### Exit Criteria

- no unresolved argument remains about the authority model
- the future plan does not require duplicating memory into another store

### AI-Builder Estimate

`1 to 2 days`

## Phase 1: Moltbox Baseline Deployment

### Objective

Stand up a working `Graphiti + Neo4j` stack under Moltbox with repeatable lifecycle commands.

### Baseline Service Shape

Start with one Moltbox service bundle that contains:

- one `Graphiti` API container
- one `Neo4j` container

That is simpler than splitting them immediately and keeps the service easy to operate.

### Service Contract

Recommended baseline posture:

- pin `zepai/graphiti` to a specific known-good version, not `latest`
- pin `neo4j` to a `5.26+` known-good version
- attach both containers to `moltbox_internal`
- persist Neo4j data outside the container
- mount a backup path if available
- add Graphiti healthcheck on `/healthcheck`
- keep the Graphiti API reachable on the internal network
- expose Neo4j Browser only if operator inspection is needed

### Expected Files

- `d:/Development/RemRam/moltbox-services/services/graphiti-dev/service.yaml`
- `d:/Development/RemRam/moltbox-services/services/graphiti-dev/compose.yml.template`
- matching `test` and `prod` variants later if the runtime profile split is kept

### Major Work

- create the service bundle
- define env and secret injection for `OPENAI_API_KEY`, `NEO4J_USER`, `NEO4J_PASSWORD`, `NEO4J_URI`
- wire persistent volumes
- document operator lifecycle commands
- smoke test Graphiti startup and index creation
- smoke test manual `/messages`, `/search`, `/get-memory`

### Exit Criteria

- `moltbox gateway service deploy graphiti-dev` brings the stack up cleanly
- Graphiti passes healthcheck
- a test message batch can be ingested
- a search returns facts from the graph

### AI-Builder Estimate

`2 to 4 days`

## Phase 2: OpenClaw Bridge v0

### Objective

Connect OpenClaw to Graphiti with the thinnest path that gives a usable memory loop.

### Recommended Implementation

Build a new plugin package:

- `d:/Development/RemRam/remram/platform/plugins/openclaw-graphiti/`

Do not try to fully recreate Cortex in this phase.

The bridge only needs to do two things well:

- write runtime evidence into Graphiti
- fetch bounded relevant memory for the next turn

### Ingestion Path

Use OpenClaw lifecycle surfaces that already exist instead of modifying core.

Best first-pass ingestion events:

- `message:preprocessed` for enriched inbound messages
- `message:sent` for final outbound assistant messages
- `session:compact:after` if you want to preserve compaction summaries as synthetic evidence

### Retrieval Path

The retrieval side should start simple:

- map the session into one coarse `group_id`
- send the recent message window to Graphiti `/get-memory`
- inject only the top bounded fact set into prompt context

If a clean context-assembly integration point is readily available in the current OpenClaw plugin API, use it.

If not, the fallback is still acceptable:

- register explicit Graphiti tools
- call retrieval during prompt assembly from the plugin path available today

### Operator Tools

Add a small set of inspection tools early:

- `graphiti_search_facts`
- `graphiti_recent_episodes`
- `graphiti_get_edge`
- `graphiti_clear_group` only for dev and test, not prod

### Exit Criteria

- a normal OpenClaw conversation writes inbound and outbound events into Graphiti
- the next turn can retrieve bounded facts from Graphiti automatically
- disabling the plugin leaves OpenClaw stable

### AI-Builder Estimate

`3 to 6 days`

## Phase 3: Graphiti-Native Authority Hardening

### Objective

Stop treating the system like a demo memory plugin and make the stored graph structurally compatible with Cortex.

### Major Work

- define the initial Cortex-on-Graphiti ontology
- add or extend labels for entities such as `Person`, `Project`, `Repository`, `Artifact`, `Document`, `Preference`, `Constraint`, `Decision`, and `Procedure`
- standardize edge names for facts that should become durable memory surfaces
- standardize node and edge attributes for governance and retrieval
- extend the Graphiti service layer so filters are available to the application
- add idempotent or duplicate-resistant ingest behavior where needed

### Required Attribute Surfaces

At minimum, preserve enough fields to avoid a future data rebuild:

- `owner_id`
- `audience`
- `project_id`
- `repo_id`
- `artifact_id`
- `artifact_revision`
- `session_id`
- `source_kind`
- `confidence`
- `freshness`
- `retention_state`
- `promotion_state`

These do not all need to affect phase-3 retrieval, but they should start landing in the graph.

### Important Compromise

Do not try to implement every Cortex retrieval field as a first-class Neo4j index immediately.

Early on:

- store the fields cleanly
- expose them through filters where reasonable
- optimize only once the real query patterns are known

### Exit Criteria

- new data lands in the graph with enough provenance and governance fields to survive later architecture cleanup
- there is no need to throw away phase-2 data to move forward

### AI-Builder Estimate

`4 to 8 days`

## Phase 4: Cortex Retrieval and Governance Layer

### Objective

Add the custom layer that Graphiti does not natively provide: governance-first retrieval and stable Cortex-shaped retrieval bundles.

### What Gets Built

This phase adds a thin remram-owned service or forked service layer in front of raw Graphiti retrieval.

Responsibilities:

- compile Cortex governance inputs into `group_id`, labels, edge names, and property filters
- choose the appropriate Graphiti search recipe
- cap and format retrieval bundles for OpenClaw
- record retrieval traces
- expose inspectable operator APIs

### Why This Phase Matters

Graphiti search is powerful, but Cortex wants:

- hard filter first
- semantic and graph scoring second
- explicit traces about what was retrieved and why

That logic should live in a remram-owned layer, not inside OpenClaw prompt code.

### Implementation Choice

Fastest path:

- extend the Python Graphiti service and keep the bridge simple

Lower-regret path:

- create a separate `cortex-graphiti` facade once phase-2 behavior is stable

Recommendation:

- do not build a separate Go facade yet
- keep this layer close to Graphiti until the query contract settles

The data model is the expensive part. The transport layer is not.

### Exit Criteria

- OpenClaw retrieves memory through a remram-owned Cortex policy surface, not directly from raw Graphiti endpoints
- retrieval traces exist for debugging and tuning

### AI-Builder Estimate

`5 to 8 days`

## Phase 5: Artifact and Document Ingestion

### Objective

Expand beyond turn memory into artifact-backed knowledge and document-backed memory.

### Graphiti-Native Approach

Do this the Graphiti way:

- import source text or structured payloads as episodes
- create or update `Document` and `Artifact` entities
- connect facts back to those entities and episodes
- preserve source revision identity in attributes

Do not create a parallel chunk warehouse and call that the authority layer.

### Major Work

- build import workers for local and provider-backed documents
- store artifact locator and revision metadata in graph attributes
- define a document ingestion convention for long-form sources
- create read-only inspection endpoints for evidence and provenance chains

### Recommended Compromise

Keep raw source content outside Graphiti.

Graphiti should store:

- source references
- derived facts
- document entities
- provenance links
- summaries where useful

### Exit Criteria

- imported documents create durable graph memory with traceable provenance
- graph facts can be walked back to the source artifact or revision

### AI-Builder Estimate

`4 to 7 days`

## Phase 6: Reflection and Dream-Lite

### Objective

Add maintenance and reconciliation without putting heavy reasoning back in the live path.

### Native Graphiti Levers

Start with what Graphiti already gives you:

- community building
- graph maintenance jobs
- temporal invalidation
- episode-based historical inspection

### Custom Cortex Work

Add small remram-owned jobs for:

- stale fact review
- promotion candidate detection
- project or person summary rebuilds
- artifact linkage cleanup
- retrieval trace audits

### Execution Surface

Run these through:

- OpenClaw cron and background tasks first, if that is simpler
- a dedicated maintenance worker later, if job volume grows

### Exit Criteria

- the system improves memory quality between live turns
- maintenance work is inspectable and not coupled to one active chat session

### AI-Builder Estimate

`4 to 7 days`

## Phase 7: Cortex Parity Layer

### Objective

Close the remaining gap between "Graphiti with integrations" and a credible Cortex implementation.

### What Still Needs To Be Custom

- retrieval trace ledger and audit surfaces
- stable operator inspection endpoints
- typed signal compiler and normalization rules
- artifact promotion and published artifact workflows
- retention and lifecycle policy enforcement
- export, backup, import, and rebuild tooling
- explicit review and correction surfaces for important facts

### What Probably Does Not Need A Full Rebuild

- the durable memory store
- the ontology backbone
- temporal fact lifecycle
- evidence provenance model

That is why this Graphiti path is attractive. Most of the late work is policy and productization, not data migration.

### AI-Builder Estimate

`7 to 14 days`

## Minimal Supporting Components To Accept In Phase 1

These are worth accepting immediately:

- `Graphiti` FastAPI service
- `Neo4j Community`
- one custom `OpenClaw` plugin bridge
- one strong hosted extraction model provider

These are acceptable but not required in phase 1:

- Graphiti MCP server for inspection
- a small maintenance worker
- a separate Cortex facade service

These should stay out until justified:

- `OpenSearch`
- a second durable memory backend
- a large custom UI

## What The Architecture Looks Like After The Two Big Bites

After `Graphiti` and `OpenClaw` do their part, the remaining custom architecture is smaller than it first appears.

You are left building roughly five remram-owned modules:

1. `openclaw-graphiti`
   Writes episodes, fetches memory, exposes operator tools.

2. `graphiti-service-extension`
   Exposes richer filters, policy hooks, and remram-specific endpoints.

3. `governance-compiler`
   Converts Cortex scope and policy into Graphiti retrieval constraints.

4. `artifact-ingest-worker`
   Turns source documents and tool outputs into graph-backed memory.

5. `maintenance-worker`
   Runs community rebuilds, reflection jobs, promotion detection, and audits.

That is a lot less than building an entire authority platform from first principles.

## Where `OpenSearch` Still Fits

`OpenSearch` is not part of the baseline recommendation, but it is not ruled out forever.

Add it only if one of these becomes true:

- passage-oriented document search becomes more important than graph fact retrieval
- you want heavy faceting and search analytics across imported corpora
- operator inspection needs a second document-oriented projection
- Graphiti plus Neo4j full-text and vector search stop being sufficient

If `OpenSearch` is added later, it should usually be:

- a projection
- a secondary search surface
- or a document import sidecar

It should not replace the Graphiti graph as authority unless the whole foundation choice changes.

## Recommended Sequence

If you want the shortest serious path with the lowest rebuild risk, do the work in this order:

1. Phase 0 foundation freeze
2. Phase 1 Moltbox baseline
3. Phase 2 OpenClaw bridge v0
4. Phase 3 authority hardening
5. Phase 4 retrieval and governance layer
6. Phase 5 artifact and document ingestion
7. Phase 6 Dream-lite maintenance
8. Phase 7 Cortex parity layer

Do not jump to phase 4 first.

Do not build a large custom Cortex service before the graph is actually serving live turns.

## Recommendation

Use `Graphiti` as the primary foundation.

Start with:

- `Graphiti + Neo4j` containerized as one Moltbox service bundle
- one thin `OpenClaw` bridge plugin
- one strong hosted model provider for structured extraction

Keep phase 1 intentionally narrow:

- ingest messages
- retrieve bounded facts
- prove a live memory loop

Then harden the graph and build Cortex-specific policy in layers.

This is the best balance of:

- strong memory authority fit
- fast path to something usable
- low data replatform risk
- low long-term regret

## Primary Sources Reviewed

- `https://github.com/getzep/graphiti`
- `https://help.getzep.com/graphiti/getting-started/mcp-server`
- `https://docs.openclaw.ai/plugins/building-plugins`
- `https://docs.openclaw.ai/automation`
- `https://docs.openclaw.ai/automation/hooks`

## Local References Reviewed

- `d:/Development/RemRam/remram-cortex/docs/design/graphiti-complete-context.md`
- `d:/Development/RemRam/remram-cortex/docs/design/graphiti-neo4j-openclaw-lifecycle-architecture.md`
- `d:/Development/RemRam/remram-cortex/docs/remram-cortex/architecture.md`
- `d:/Development/RemRam/moltbox-services/services/openclaw-dev/service.yaml`
- `d:/Development/RemRam/moltbox-services/services/openclaw-dev/compose.yml.template`
- `d:/Development/RemRam/remram/reference/cli-reference.md`
