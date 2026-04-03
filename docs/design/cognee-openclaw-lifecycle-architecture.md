# Cognee + OpenClaw Lifecycle Architecture

## Purpose

This memo evaluates an end-to-end Cortex path built on:

- `Cognee` as the memory lifecycle engine and durable memory service
- `OpenClaw` as the runtime shell, session lifecycle owner, tool host, and automation surface

The useful question is not whether either product already is Cortex.

The useful question is:

"If we let Cognee take the largest bite out of memory lifecycle, and let OpenClaw take the largest bite out of runtime orchestration, what architecture is left, what can be done the native way, and what still has to be custom?"

Reviewed on `April 2, 2026`.

## Executive Take

This stack is credible.

More specifically:

- `Cognee` already has a real staged memory lifecycle: `add -> cognify -> search -> memify`
- `Cognee` already has the right kind of extension seams: `DataPoint`, custom tasks, custom pipelines, custom retrievers, session persistence, permissions, datasets, API, and MCP
- `OpenClaw` already has the right host seams: plugin slots, lifecycle hooks, CLI, tools, and automation
- there is already an official `@cognee/cognee-openclaw` plugin

That makes this materially stronger than a raw storage-plus-runtime composition.

Bluntly:

- this is a better Cortex contender than a storage-only stack
- it is more authority-like than `Weaviate + OpenClaw`
- it is less semantically clean than `Graphiti + OpenClaw`
- it is faster to get usable than `Graphiti + OpenClaw`
- it has one serious hard edge: the strongest `Postgres + pgvector + Neo4j + Redis` posture is not the cleanest stock fit for Cognee's backend-access-control mode

The strongest version of this architecture is:

- `OpenClaw` as the runtime shell
- `Cognee` as the only durable memory authority
- the official OpenClaw plugin as the phase-1 bridge
- a later thin plugin fork or adapter once we need direct session persistence, richer retrieval policy, and stronger Cortex object semantics

The wrong version is:

- OpenClaw Markdown files remaining the true durable authority
- Cognee being treated as a smart index over those files
- session continuity living only in OpenClaw while durable memory lives somewhere else

That would recreate split-brain memory.

## Why This Combination Works Better Than It First Sounds

`OpenClaw` already exposes more lifecycle structure than a simple "agent shell" framing suggests.

It already gives us:

- a `memory` plugin slot
- a `contextEngine` slot
- lifecycle hooks
- background automation
- tools and CLI
- proof that an external memory system can be the real authority

`Cognee` already exposes more memory machinery than a simple "RAG platform" framing suggests.

It already gives us:

- dataset-scoped ingestion and search
- graph plus vector plus relational state
- custom `DataPoint` models
- custom `Task` composition
- custom pipelines through `run_custom_pipeline`
- custom retriever registration through `use_retriever`
- session cache and session APIs
- a session persistence memify pipeline
- provenance fields on `DataPoint`
- first-party API and MCP surfaces
- a first-party OpenClaw integration

That means the stack already covers:

- prompt-time recall
- post-turn indexing
- cross-session memory
- graph and vector retrieval
- background enrichment
- memory inspection
- self-hosted dockerized deployment

The remaining custom work is not trivial, but it is much narrower than building a memory authority from scratch.

## The Most Important Architectural Insight

If we choose this path, the right stance is:

- do memory lifecycle the `Cognee` way first
- do runtime lifecycle the `OpenClaw` way first
- add Cortex discipline as a thin overlay

That means:

- accept `DataPoint` as the phase-1 durable unit
- accept datasets and `NodeSet` as early scoping primitives
- accept `memify` as the first maintenance surface
- accept session cache and session persistence as the first continuity path

If we instead replace:

- Cognee's pipeline model
- Cognee's retriever model
- OpenClaw's injection lifecycle
- OpenClaw's plugin model

up front, then we pay the integration tax without getting the leverage.

## Inbuilt Extension Points To Exploit

### OpenClaw Native Seams

| OpenClaw seam | What it gives us | How to use it here |
| --- | --- | --- |
| `plugins.slots.memory` | One active memory plugin | Use the official Cognee plugin first |
| `plugins.slots.contextEngine` | One active context assembly surface | Stay on the stock path early; add a thin Cortex-aware engine later if needed |
| `before_prompt_build` | Prompt-time injection | Bound recalled Cognee context and add retrieval instructions |
| `agent_end` | Post-turn persistence | Trigger extra sync, trace capture, or session persistence scheduling |
| `before_compaction` / `after_compaction` | Compaction lifecycle | Flush pending writes and optionally persist continuity summaries |
| `registerTool` | Agent-callable tools | Keep Cognee inspection and search tools visible to the agent |
| `registerService` | Background service seam | Run maintenance or export loops if needed |
| hook packs | Lightweight automation | Add reset, audit, or periodic persist helpers without forking runtime code |

The key point is that OpenClaw does not force durable memory to stay in Markdown files.

### Cognee Native Seams

| Cognee seam | What it gives us | How to use it here |
| --- | --- | --- |
| `@cognee/cognee-openclaw` | Existing host integration | Start here instead of inventing the bridge |
| `DataPoint` | Structured durable memory primitive | Define Cortex-shaped memory objects instead of relying only on chunk extraction |
| `belongs_to_set` and `NodeSet` | Lightweight grouping and retrieval scoping | Use for project, person, repo, or workflow slices |
| datasets and permissions | Coarse authority partitioning | Use as the main memory namespace boundary |
| `cognify` with `graph_model` / `custom_prompt` | Extraction control | Narrow domain extraction before writing custom graph builders |
| `memify` | Background enrichment and consolidation | Use as Dream-lite maintenance before building bespoke reflection |
| custom `Task` and `run_custom_pipeline` | Direct pipeline composition | Add artifact ingest, promotion, and cleanup flows the Cognee way |
| `use_retriever` | Search extension seam | Register Cortex-specific retrieval behavior without replacing Cognee search wholesale |
| session APIs and `SessionManager` | Short-term continuity and feedback capture | Use session-aware search, then persist important sessions into the graph |
| session persistence memify pipeline | Bridge between short-term and durable memory | Promote sessions into the graph on schedule or trigger |
| `source_pipeline`, `source_task`, `source_node_set`, `source_user` | Built-in provenance fields | Extend rather than invent provenance from scratch |
| API and MCP server | Stable service and inspection surfaces | Keep runtime integration on API; use MCP for debugging or external assistants |

The most important reduction in custom work is this:

- Cognee already has a first-class opinion about how to ingest, enrich, search, and re-process memory

That is exactly the machinery that usually eats time.

## What The Official OpenClaw Plugin Gives Us For Free

The official `@cognee/cognee-openclaw` integration is already substantive.

From the current docs, it already gives:

- auto-index of `MEMORY.md` and `memory/*.md`
- hash-based change detection
- automatic cleanup of deleted memory files
- auto-recall before each agent run
- injected `<cognee_memories>` context
- dataset mapping and sync state
- support for `GRAPH_COMPLETION`, `CHUNKS`, and `SUMMARIES`
- config for `datasetName`, `searchPrompt`, `deleteMode`, `maxResults`, `minScore`, `maxTokens`, `autoRecall`, `autoIndex`, and `autoCognify`
- CLI commands for manual indexing and status

That means a phase-0 system can already:

- keep OpenClaw memory files searchable through Cognee
- recall graph-backed memory before response
- sync changes without writing a custom crawler
- inspect sync status operationally

For speed-to-usable-system, that is a major accelerant.

## The Important Limitation In The Stock Plugin

The stock plugin is file-memory-first.

That is the main architectural wrinkle.

Its current mental model is:

- OpenClaw memory files are the source material
- Cognee syncs and indexes them
- Cognee answers recall queries against that indexed memory

That is good for phase 1.

It is not the ideal final authority posture for Cortex.

For Cortex, the stronger long-term shape is:

- OpenClaw memory files become editable source artifacts or human-friendly projections
- live runtime memory, promoted session memory, and structured memory objects flow into Cognee directly
- Cognee becomes the durable authority

So the best path is:

- start with the official plugin
- then fork or wrap it once you need direct writes to Cognee APIs and session promotion

That is still much cheaper than building the whole bridge from scratch.

## The Real Hard Edge

The strongest self-hosted dockerized posture for Cognee is still:

- `Postgres`
- `pgvector`
- `Neo4j`
- `Redis`
- `Cognee API`
- `Cognee MCP`

But the stock backend-access-control posture is not equally mature across that stack.

Current upstream configuration shows:

- `Postgres` is supported for relational state
- `pgvector` is supported for vector storage
- `Neo4j` is supported for graph storage
- `Redis` is supported for cache and sessions
- strict dataset-to-database handler support is more limited for graph and vector multi-user isolation than the raw storage adapters themselves

That means the practical architecture should assume:

- `ENABLE_BACKEND_ACCESS_CONTROL` may need to stay off in the strongest `Postgres + pgvector + Neo4j` setup
- datasets and permissions still exist as logical application-layer boundaries
- strict physical backend isolation per dataset is something we would likely need to extend if it becomes non-negotiable

This is not a deal-breaker for a personal Cortex build.

It is the main reason this path is slightly less clean than `Graphiti`.

## Recommended Architecture

### Long-Term Shape

```text
Channels / CLI / Apps
        |
        v
OpenClaw Gateway + Runtime
        |
        +-- Cognee Memory Plugin
        |     - auto-recall
        |     - file sync in phase 1
        |     - operator CLI/status
        |
        +-- Optional thin Context Engine
        |     - retrieval bundle shaping
        |     - post-turn scheduling
        |     - compaction callbacks
        |
        +-- Hook pack / service helpers
              - session persist triggers
              - audits
              - export jobs
        |
        v
Cognee API
        - add / update / delete
        - cognify
        - search
        - memify
        - session APIs
        - permissions / datasets
        |
        +-- Postgres
        |     - datasets
        |     - permissions
        |     - documents / metadata
        |     - pipeline runs
        |
        +-- pgvector
        |     - searchable embeddings
        |     - DataPoint vector surfaces
        |
        +-- Neo4j
        |     - graph structure
        |     - DataPoint relationships
        |     - NodeSets and graph retrieval
        |
        +-- Redis
              - session cache
              - feedback / recent QA continuity

Optional sidecars:
  - Cognee MCP for inspection and IDE usage
  - Cognee UI for operator inspection
  - custom promotion worker
  - artifact import worker
```

### Authority Rule

If we pursue this stack, we should enforce one simple rule:

- `Cognee` is the only durable memory authority

That means:

- OpenClaw transcripts are evidence
- OpenClaw memory Markdown is source material or projection
- Postgres, pgvector, and Neo4j are Cognee implementation stores, not separate app-owned schemas
- direct writes to those databases should be exceptional maintenance work, not normal application behavior

## What To Do The Cognee Way

### 1. Accept datasets as the primary partition

Use datasets as the coarse memory boundary.

That is the cleanest built-in surface for:

- personal versus family versus project memory
- experiments versus durable memory
- import-specific staging

Do not start with one giant undifferentiated memory pool.

### 2. Accept `NodeSet` as the first lightweight scope tool

Use `NodeSet` for:

- project scoping
- repo scoping
- people or topic slices
- maintenance targets
- promotion buckets

This is cheaper than forcing a heavyweight schema too early.

### 3. Accept `DataPoint` as the phase-1 durable object

This is the most important Cognee-native modeling move.

Do not reduce the system to:

- documents
- chunks
- extracted graph edges

Instead define structured `DataPoint` models for high-value memory shapes such as:

- `Decision`
- `Preference`
- `Constraint`
- `Procedure`
- `ArtifactReference`
- `ProjectFact`

That is how the data model gets closer to Cortex without a rebuild.

### 4. Accept session cache plus session persistence

Cognee already distinguishes:

- short-term session memory
- durable graph memory

That is useful.

Use session-aware search in the live path, then use the existing session persistence memify pipeline to promote selected sessions into the durable graph.

### 5. Accept `memify` as Dream-lite

`Memify` is already the right built-in maintenance surface for:

- derived rule extraction
- subgraph enrichment
- session promotion
- feedback-weight adjustments
- entity consolidation

Do not replace that with a separate reflection system on day one.

### 6. Accept multiple retrieval modes

Cognee already exposes multiple search types and custom retriever registration.

That means we should use:

- stock search types where they are good enough
- custom retrievers only where Cortex truly needs different behavior

This is much cheaper than replacing the entire retrieval surface.

## What Still Needs To Be Custom For Cortex

Even in the best version of this stack, several things still remain ours:

- stronger canonical object semantics than generic `DataPoint`
- governance-first retrieval policy
- retrieval traces and audit surfaces
- artifact provider identity and revision policy
- stable promotion rules
- stricter provenance shape for imported artifacts and tool outputs
- typed signals and semantic signature if those remain part of the vision
- operator inspection that is Cortex-specific rather than generic Cognee inspection

The encouraging part is that these are mostly policy and product-shaping gaps, not "throw away the data model and start over" gaps.

## What Architecture Is Left After The Big Bites

If we let `Cognee` own memory lifecycle and `OpenClaw` own runtime lifecycle, the remaining custom architecture is relatively small:

1. A thin `OpenClaw -> Cognee` plugin extension or fork.
   This upgrades the stock file-sync plugin into a direct Cortex-aware bridge.

2. A Cortex `DataPoint` model pack.
   This defines the durable objects we actually care about.

3. A retrieval policy wrapper.
   This compiles Cortex scope and governance inputs into datasets, NodeSets, search types, and retriever config.

4. An artifact import and promotion worker.
   This turns documents, tool outputs, and selected sessions into structured durable memory.

5. A maintenance worker.
   This runs memify jobs, consolidation, cleanup, and promotion review.

That is a materially smaller system than building a memory authority from scratch.

## Recommended Path

The strongest path is phased:

### Phase 0

- deploy `Cognee API + Postgres + pgvector + Neo4j + Redis`
- optionally deploy `Cognee MCP`
- keep Cognee as the only durable authority

### Phase 1

- use the stock `@cognee/cognee-openclaw` plugin
- index OpenClaw memory files
- use auto-recall and auto-cognify
- prove that graph-backed recall is useful in live runtime

### Phase 2

- add Cortex `DataPoint` models
- add direct ingest paths beyond Markdown memory
- start using custom tasks or pipelines for higher-value memory objects

### Phase 3

- extend or fork the OpenClaw plugin
- write session and runtime evidence directly into Cognee APIs
- use session persistence and memify to promote continuity into durable memory

### Phase 4

- add governance-aware retrieval wrapper
- add artifact identity and provenance discipline
- add Dream-lite maintenance and promotion review

This keeps phase-1 speed while still moving toward a cleaner final authority model.

## Recommendation

`Cognee + OpenClaw` is worth a serious spike.

The best version is:

- `OpenClaw` as the shell
- `Cognee` as the only durable memory authority
- `Postgres + pgvector + Neo4j + Redis` as the serious self-hosted storage posture
- the official OpenClaw plugin as the starting bridge
- a later thin plugin fork or adapter as the likely phase-2 or phase-3 move

This is not as clean a final authority model as `Graphiti + OpenClaw`.

It is probably faster to get useful.

If the goal is:

- fast progress
- real extension seams
- self-hosted dockerized services
- a path that still evolves toward Cortex

then this architecture is absolutely worth keeping in the field.

## Primary Sources Reviewed

- `https://github.com/topoteretes/cognee`
- `https://docs.cognee.ai/integrations/openclaw-integration`
- `https://docs.cognee.ai/how-to-guides/cognee-sdk/index`
- `https://docs.cognee.ai/core-concepts/main-operations/search`
- `https://docs.cognee.ai/how-to-guides/own-data-model`
- `https://docs.cognee.ai/guides/memify-quickstart`

## Local Sources Reviewed

- `d:/Development/RemRam/remram-cortex/docs/design/cognee-complete-context.md`
- `d:/Development/RemRam/remram-cortex/docs/reference/cognee-cortex-fit-analysis.md`
- `d:/Development/RemRam/_diag/cognee-upstream/docker-compose.yml`
- `d:/Development/RemRam/_diag/cognee-upstream/.env.template`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/infrastructure/engine/models/DataPoint.py`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/modules/memify/memify.py`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/memify_pipelines/persist_sessions_in_knowledge_graph.py`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/api/v1/search/search.py`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/api/v1/session/session.py`
- `d:/Development/RemRam/_diag/cognee-upstream/cognee/modules/retrieval/register_retriever.py`
