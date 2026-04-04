# Weaviate + OpenClaw Lifecycle Architecture

## Purpose

This memo evaluates an end-to-end Cortex path built on:

- `Weaviate` as the durable memory store and retrieval engine
- `OpenClaw` as the runtime shell, lifecycle manager, compaction owner, and plugin surface

The goal is not to ask whether either product already is Cortex.

The goal is to ask a narrower and more useful question:

"If we take those two big bites out of the problem, what architecture is left, what can be done the native way, and what still has to be custom?"

Reviewed on `April 2, 2026`.

## Executive Take

This architecture is credible.

More specifically:

- `Weaviate` is strong enough to hold the long-term durable memory records.
- `OpenClaw` is strong enough to own session lifecycle, compaction, prompt injection, runtime tools, and automation hooks.
- The remaining custom work is real, but it is narrower than a greenfield Cortex build.

The strongest version of this stack is not:

- `Weaviate` alone
- `OpenClaw` alone
- raw workspace Markdown plus a vector sidecar

The strongest version is:

- a `Weaviate`-backed durable memory authority
- an `OpenClaw` memory plugin for tooling and raw recall
- a thin `OpenClaw` context engine for retrieval bundle assembly and turn lifecycle
- a small custom authority module that canonicalizes memory writes into a Cortex-shaped model

Bluntly:

- this is worth a serious spike
- it is better than a storage-only `Weaviate` build
- it is better than relying on OpenClaw memory files as the long-term authority
- it is still not "free"; the memory authority semantics remain ours

## Why This Combination Works Better Than It First Sounds

The important correction is that OpenClaw already has more native lifecycle structure than a simple "chat app with notes" framing suggests.

OpenClaw already exposes:

- a `memory` slot
- a `contextEngine` slot
- typed lifecycle hooks such as `before_prompt_build`, `agent_end`, `before_compaction`, and `after_compaction`
- built-in compaction and pre-compaction memory flush behavior
- plugin tools, services, CLI commands, and hook packs
- proof-by-example memory plugins such as `memory-lancedb`
- proof-by-example external memory integration through `Honcho`

Weaviate already exposes:

- object collections with typed properties
- scalar filters
- hybrid search
- explainable search scores
- named vectors
- bring-your-own vectors
- local/self-host deployment
- local model integrations such as `text2vec-ollama`
- collection aliases and schema migration aids
- optional multi-tenancy

That means the stack already covers:

- runtime lifecycle
- durable object storage
- vector and hybrid retrieval
- prompt-time memory injection
- background maintenance hooks
- local/free deployment

What it does not cover by itself is the Cortex-specific discipline around:

- canonical knowledge objects
- provenance richness
- artifact identity
- typed signal computation
- semantic signature
- merge and reconciliation policy
- Dream-style maintenance

That is a much smaller and more realistic gap than "build an entire memory platform from scratch."

## Inbuilt Extension Points To Exploit

### OpenClaw Native Seams

These are the extension points that matter most.

| OpenClaw seam | What it gives us | How to use it here |
| --- | --- | --- |
| `plugins.slots.memory` | One active memory plugin for memory tools and retrieval behaviors | Replace `memory-core`/`memory-lancedb` with a `Weaviate`-backed memory plugin |
| `plugins.slots.contextEngine` | One active context engine for ingest, assemble, compact, and after-turn lifecycle | Use a thin Cortex-aware engine to shape retrieval bundles and post-turn writes |
| `before_prompt_build` / `before_agent_start` | Prompt mutation and prepended dynamic context | Inject bounded retrieval bundles the OpenClaw way |
| `agent_end` | Post-run analysis and persistence | Save observations, run light reflection, schedule merges |
| `before_compaction` / `after_compaction` | Compaction lifecycle hooks | Flush pending writes, persist continuity summaries, attach compaction metadata |
| `registerTool` | Agent-callable tools | Expose `memory_search`, `memory_get`, diagnostic recall, maybe artifact lookup |
| `registerService` | Background runtime service | Run maintenance loops, queue drains, or periodic reconcile tasks |
| Hook packs | Lightweight local automation | Optional `/new` and `/reset` projections, export jobs, or audit trails |

OpenClaw's existing plugin examples are especially useful here:

- `memory-lancedb` proves that a memory plugin can already do auto-recall and auto-capture using lifecycle hooks.
- `Honcho` proves that OpenClaw already supports a dedicated external memory service pattern with cross-session persistence and prompt-time recall.
- the `contextEngine` contract proves OpenClaw already expects third-party context assembly and post-turn indexing logic.

That matters because it means a `Weaviate` path is not fighting the host runtime.

### Weaviate Native Seams

These are the `Weaviate` features that materially reduce custom work.

| Weaviate seam | What it gives us | How to use it here |
| --- | --- | --- |
| Typed collection properties | Durable object fields, not just chunk payloads | Store canonical statement, signals, governance, provenance keys, artifact ids |
| Hybrid search | BM25 + vector fusion | Make typed fields and canonical text the primary retrieval surface |
| Search score explanation | Inspectable scoring | Keep bundle assembly debuggable |
| Filters | Hard preconditions on result eligibility | Implement governance-like scoping and lifecycle filtering |
| Named vectors | Multiple embedding surfaces per object | Separate `statement`, `summary`, and optionally `continuity` vectors |
| Bring your own vectors | External embedding control | Keep embedding strategy portable and avoid lock-in |
| Local model integrations | Local/free vectorization path | Use `text2vec-ollama` if desired |
| Collection aliases | Safer schema and vectorizer migration | Evolve the model without moving application callers |
| Multi-tenancy | Hard shard-level isolation | Use only if we want explicit workspace or persona isolation |
| Cross-references | Object linkage | Use sparingly for artifact/evidence inspection, not as the whole memory design |

The most important `Weaviate` extension choice is this:

- prefer typed properties + filters + hybrid search first
- use vectors as assistive ranking
- use cross-references selectively

That is the closest fit to the Cortex direction of travel.

## Recommended Architecture

### Long-Term Shape

```text
Channels / CLI / Apps
        |
        v
OpenClaw Gateway + Runtime
        |
        +-- Weaviate Memory Plugin
        |     - raw recall tools
        |     - memory CLI/debug
        |     - optional direct store/forget tools
        |
        +-- Cortex Context Engine
        |     - assemble retrieval bundle
        |     - ingest completed turns
        |     - compaction callbacks
        |     - optional continuity summaries
        |
        +-- Optional Hook Pack
              - /new and /reset projections
              - export / audit / backup hooks
              - scheduled maintenance triggers
        |
        v
Cortex Authority Module
        - canonicalization
        - knowledge-object upsert logic
        - provenance shaping
        - signal/signature computation
        - artifact registry
        - Dream-lite maintenance
        |
        v
Weaviate
        - knowledge_objects
        - observations
        - artifacts
        - continuity_records (optional)
```

### The Core Rule

`Weaviate` must be the only durable memory authority.

That means:

- workspace Markdown is optional projection or fallback
- session transcripts are evidence, not memory
- OpenClaw session state is runtime state, not authority

If Markdown files and `Weaviate` are both treated as first-class durable memory, the architecture becomes confused immediately.

## Recommended Module Split

### 1. `openclaw-weaviate-memory`

This should be the active memory plugin.

It should own:

- `memory_search`
- `memory_get` or an equivalent targeted fetch tool
- optional `memory_store` and `memory_forget`
- operator CLI such as status, search, maybe reindex or backfill
- direct raw access to stored knowledge/observation objects for debugging

This is the closest replacement for `memory-core` and the cleanest adaptation target from `memory-lancedb`.

### 2. `openclaw-cortex-context`

This should be the active context engine.

It should own:

- `assemble()` for retrieval bundle construction
- `ingestBatch()` or `afterTurn()` for turn-level observation capture
- `compact()` initially in delegating mode
- compaction-adjacent continuity handling
- optional `systemPromptAddition` with retrieval instructions and bundle metadata

Recommended initial posture:

- `ownsCompaction: false`
- delegate compaction to OpenClaw's runtime first

That keeps the early version simpler and reduces the risk of breaking prompt lifecycle behavior.

### 3. `cortex-authority`

This is the minimum custom module that still matters.

It should own:

- knowledge-object schema
- idempotent write keys
- merge rules
- typed signal extraction
- semantic signature computation
- provenance tuples
- artifact identity and source-location records
- retrieval bundle ranking policy

This can begin life as a library called by the plugin package.

It should eventually become a standalone service if the system matures.

The key point is that the stored data model should already match the future service boundary so extraction later is organizational, not migrational.

## Data Model In Weaviate

### Collection 1: `knowledge_objects`

This is the primary durable memory unit.

Suggested fields:

- `knowledge_id`
- `canonical_statement`
- `summary`
- `kind`
- `status`
- `confidence`
- `freshness`
- `reinforcement_count`
- `governance_owner`
- `governance_audience`
- `governance_space`
- `governance_state`
- `valid_from`
- `valid_to`
- `signal_domain`
- `signal_activity`
- `signal_need`
- `signal_object`
- `signal_mechanism`
- `semantic_signature`
- `artifact_ids`
- `session_ids`
- `source_refs`
- `support_keys`
- `link_ids`
- `created_at`
- `updated_at`

Suggested vectors:

- `statement_vector`
- `summary_vector`
- optional `continuity_vector`

Use named vectors only when they serve clearly different retrieval surfaces.

### Collection 2: `observations`

This is the append-only evidence layer.

Suggested fields:

- `observation_id`
- `session_id`
- `turn_id`
- `role`
- `text`
- `workspace`
- `channel`
- `timestamp`
- `capture_reason`
- `durability_hint`
- `artifact_id`
- `source_locator`
- `reflection_status`

This collection gives us a bridge between raw transcript evidence and canonical knowledge.

It also gives us a safe place to start before the full knowledge-object merge logic is mature.

### Collection 3: `artifacts`

This is the artifact/provider registry.

Suggested fields:

- `artifact_id`
- `provider_kind`
- `provider_ref`
- `authority_mode`
- `title`
- `mime_type`
- `checksum`
- `imported_at`
- `source_uri`
- `source_locator_scheme`
- `retention_state`
- `derived_knowledge_ids`

This is where Cortex begins to stop depending on external provider identity as its internal organization model.

### Collection 4: `continuity_records` (Optional)

This is useful if we want a lightweight conversation layer.

Suggested fields:

- `continuity_id`
- `session_ids`
- `summary`
- `semantic_signature`
- `recency`
- `scope`
- `linked_knowledge_ids`

This should remain optional.

If skipped early, `observations` plus `knowledge_objects` are enough.

### Cross-Reference Guidance

Use `Weaviate` cross-references sparingly.

Recommended default:

- store scalar foreign keys first
- store denormalized inspection metadata when helpful
- add cross-references only where they materially improve inspection or query ergonomics

This is the `Weaviate` way that best respects its own performance guidance.

## Lifecycle Flows

### 1. Live Turn Retrieval

Use the `contextEngine.assemble()` path.

Flow:

1. OpenClaw receives a message.
2. The context engine derives a query surface from:
   - current user text
   - session metadata
   - active workspace/scope
   - optional recency/continuity state
3. The authority module queries `Weaviate` using:
   - hard filters first
   - hybrid search second
   - named vector target only where justified
4. The engine assembles a bounded retrieval bundle.
5. The engine injects:
   - a compact context message
   - optional retrieval instructions through `systemPromptAddition`

This should be the main live recall path.

It is cleaner than relying only on ad hoc tool calls because it makes recall deterministic and inspectable.

### 2. Turn Commit And Reflection

Use `ingestBatch()` or `afterTurn()`.

Flow:

1. Capture the completed turn as one logical unit.
2. Write raw or lightly normalized evidence into `observations`.
3. Run lightweight reflection:
   - detect durable candidates
   - compute kind and scope hints
   - compute typed signals
   - compute semantic signature
   - derive idempotency/support keys
4. Upsert or reinforce `knowledge_objects`.

This is where most Cortex value starts to appear.

Importantly, this can begin simple:

- one pass of "store observation"
- a second pass of "promote obvious durable items"

It does not require Dream to exist on day one.

### 3. Compaction

OpenClaw already owns this lifecycle well enough.

Recommended phase-1 behavior:

- keep runtime compaction
- keep `ownsCompaction: false`
- use `before_compaction` to ensure pending writes are flushed
- use `after_compaction` to store compact summaries or continuity markers

The OpenClaw pre-compaction memory flush is still useful, but its target should change conceptually:

- not "write authoritative memory to Markdown"
- instead "ensure pending durable state has been committed somewhere authoritative"

That can mean:

- committing to `Weaviate`
- or, at minimum, writing a projection note that is explicitly non-authoritative

### 4. Session Reset And `/new`

OpenClaw's `session-memory` hook can still be useful.

But in this architecture it should be treated as:

- human-readable export
- projection
- notebook-style continuity aid

It should not be the canonical write path for durable memory.

### 5. Artifact Intake

This is where `Weaviate` helps more than OpenClaw.

Flow:

1. Import an artifact.
2. Create an `artifacts` record.
3. Create bounded evidence slices or observation records.
4. Reflect them into `knowledge_objects`.
5. Keep source location and provider metadata attached.

This is much closer to Cortex than relying on raw Markdown memory files.

### 6. Dream-Lite Maintenance

This should start as a background service, not a major subsystem.

Use `registerService()` or an external worker for:

- dedupe checks
- merge suggestions
- signal normalization
- reinforcement decay or freshness updates
- promotion candidate detection

This is the right place to keep Dream small and incremental.

## What Should Be Done The OpenClaw Way

Use OpenClaw natively for:

- session ownership
- transcripts and evidence capture boundaries
- compaction lifecycle
- runtime prompt assembly entry points
- plugin packaging and configuration
- tool registration
- background services
- hook-driven automation
- local operator ergonomics

Do not rebuild those surfaces elsewhere unless OpenClaw proves inadequate.

## What Should Be Done The Weaviate Way

Use Weaviate natively for:

- structured durable objects
- filters
- hybrid retrieval
- vector storage
- named vectors
- score explanation
- schema evolution through collection/version patterns
- local embedding integrations when useful

Do not fight `Weaviate` by turning it into:

- a graph-first engine
- a transcript archive pretending to be knowledge
- a place where every relationship must be a cross-reference

## What Still Must Be Custom

The unavoidable custom layer is:

- canonical knowledge-object schema
- idempotent merge rules
- typed signal extraction
- semantic signature generation
- provenance model
- artifact registry
- retrieval bundle shaping
- maintenance and reconciliation policy

That is still substantial work.

But it is exactly the work that is most worth owning.

## Three Implementation Shapes

### Shape A: Memory Plugin Only

This is the fastest spike.

Model it after `memory-lancedb`:

- `before_prompt_build` or `before_agent_start` for auto-recall
- `agent_end` for auto-capture
- `memory_*` tools for direct access

Pros:

- fastest path
- leverages existing OpenClaw patterns directly
- enough to prove storage and recall

Cons:

- weaker retrieval bundle control
- weaker turn batching
- harder to reason about deterministic live context

### Shape B: Memory Plugin + Hooks

This is a moderate step up.

Add:

- `before_compaction`
- `after_compaction`
- `before_reset`
- optional `/new` export hooks

Pros:

- better lifecycle coverage
- improved continuity handling
- still lightweight

Cons:

- recall/injection logic is still hook-driven rather than centered in a context engine

### Shape C: Memory Plugin + Context Engine + Authority Module

This is the recommended architecture.

Pros:

- clearest ownership boundaries
- best fit for a durable authority layer
- deterministic bundle assembly
- cleanest path toward future standalone Cortex service

Cons:

- more initial implementation effort
- two OpenClaw plugin seams instead of one

This is the shape most likely to avoid later regret.

## Practical Tradeoffs

### 1. Markdown Memory Stops Being Canonical

This is the biggest conceptual shift.

If that feels uncomfortable, the architecture will drift.

### 2. Weaviate Is Still A Search Database, Not A Memory Policy Engine

It gives us the substrate.

It does not give us:

- canonicalization
- contradiction handling
- reinforcement policy
- promotion policy

### 3. OpenClaw Context Engines Are Powerful But Operationally Important

If the selected engine is broken, runs fail.

That means:

- keep the first version thin
- keep a clean fallback to `legacy`

### 4. Cross-References Are Useful But Not Free

Use them where they improve inspection.

Do not model the whole system around them.

### 5. Weaviate Vectorizer Choices Matter Early

If we want the lowest migration risk, the safest early posture is:

- either bring our own vectors
- or use named vectors with clear semantics plus collection aliases for later evolution

### 6. Dream Is Easy To Bolt On Here

This architecture does not need Dream early to be valuable.

That is a strength, not a weakness.

## Recommendation

This is a strong contender for a practical Cortex path.

If we choose it, the recommended phase-1 acceptance is:

- `Weaviate` is the durable memory authority
- OpenClaw keeps runtime lifecycle and compaction
- build a `Weaviate` memory plugin first
- add a thin context engine immediately after, not much later
- keep compaction delegated to OpenClaw initially
- keep Markdown memory as projection only

What still has to be custom:

- knowledge-object modeling
- reflection/upsert logic
- provenance
- artifact identity
- signal/signature computation
- Dream-lite maintenance

The key reason this architecture is attractive is that the custom work is concentrated in the high-value semantic layer, while lifecycle, storage, and recall infrastructure are mostly borrowed from systems that already want to do those jobs.

## Sources

Official docs reviewed:

- `OpenClaw` Memory Overview: <https://docs.openclaw.ai/concepts/memory>
- `OpenClaw` Context Engine: <https://docs.openclaw.ai/concepts/context-engine>
- `OpenClaw` Plugins: <https://docs.openclaw.ai/tools/plugin>
- `OpenClaw` Hooks: <https://docs.openclaw.ai/automation/hooks>
- `OpenClaw` Honcho Memory: <https://docs.openclaw.ai/concepts/memory-honcho>
- `Weaviate` Hybrid Search: <https://docs.weaviate.io/weaviate/search/hybrid>
- `Weaviate` Filters: <https://docs.weaviate.io/weaviate/search/filters>
- `Weaviate` Vector Search / named vectors / bring-your-own vectors: <https://docs.weaviate.io/weaviate/concepts/search/vector-search>
- `Weaviate` Vector Indexing: <https://docs.weaviate.io/weaviate/concepts/vector-index>
- `Weaviate` Cross-references: <https://docs.weaviate.io/weaviate/tutorials/cross-references>
- `Weaviate` Multi-tenancy: <https://docs.weaviate.io/weaviate/manage-collections/multi-tenancy>
- `Weaviate` Docker install: <https://docs.weaviate.io/weaviate/installation/docker-compose>
- `Weaviate` Ollama embeddings: <https://docs.weaviate.io/weaviate/model-providers/ollama/embeddings>

OpenClaw local source reviewed:

- `extensions/memory-lancedb/index.ts`
- `src/auto-reply/reply/memory-flush.ts`
- `src/agents/tools/memory-tool.ts`
- `src/agents/memory-search.ts`
- `src/context-engine/types.ts`
- `docs/reference/session-management-compaction.md`
