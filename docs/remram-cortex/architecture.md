# Remram Cortex Architecture

## 1. Overview

Remram Cortex is the memory engine and knowledge authority layer in Remram. It turns transient conversations, tool outputs, and artifacts into durable, normalized knowledge objects.

It owns structured memory, bounded semantic retrieval, post-run reflection, and scheduled dream-cycle reconciliation.

Cortex is not a transcript archive and not a vector-only memory system. It persists structured knowledge; embeddings are only one ranking signal used during retrieval.

Cortex is not a memory plugin. It is a system-level intelligence layer for knowledge maturation.

Cortex must never become a second transcript store. OpenClaw owns transcripts, sessions, and transcript compaction. Cortex stores extracted knowledge and other bounded semantic continuity objects only.

Cortex does not own execution, runtime packaging, or agent behavior. OpenClaw executes. Orchestration decides policy and prompt assembly. Applications present results.

Agents interpret. OpenClaw executes. Gateway governs the control plane. Cortex remembers.

The core rule is simple: transcripts are evidence, not knowledge. Cortex extracts, structures, and reconciles durable knowledge objects from runtime activity so Remram can improve over time without depending on raw transcript sprawl.

The knowledge lifecycle is: interaction -> extraction -> structured object -> reinforcement -> reconciliation -> promotion.

Memory captures experience. Cortex is the layer that distills experience into durable knowledge.

The first end-to-end execution path is: capture -> reflection -> storage -> retrieval -> injection.

## 2. Core Principles

- Transcript vs Knowledge: raw transcripts, tool logs, and artifacts are runtime evidence; only extracted and reconciled knowledge objects are treated as durable memory.
- No Transcript Duplication: Cortex may reference session identifiers and persisted evidence, but it must not duplicate full transcripts or recreate transcript storage under another name.
- Separation of Authority: Cortex owns durable knowledge and its maturation lifecycle. OpenClaw owns execution, and orchestration owns behavior and prompt policy.
- Local-first Memory: Cortex should preserve useful memory locally and remain valuable without depending on remote control planes.
- Memory vs Context: prompt context is a per-run injection surface; memory is structured, persistent, and expected to survive transcript compaction and session boundaries.
- Knowledge Maturation Over Recall: Cortex is designed to mature extracted memory into scored, reconciled, promotable knowledge rather than merely persist recall snippets.
- Behavioral Improvement Over Persistence: memory only justifies its cost if it produces observable improvement in later runs, not merely a larger store of retained data.
- Semantic Continuity Over Temporal History: long-term continuity should preserve meaning, recency, and direction rather than raw chronological detail.
- Bootstrap Before Live Evolution: historical backfill is a first-class conditioning path for initializing knowledge before live reflection and dream loops take over.
- Reflection Before Reconciliation: each run produces candidate knowledge deltas first; broader cleanup and synthesis happen later in dream cycles.
- Bounded Retrieval: eligibility precedes similarity. Retrieval starts with explicit scope and dimension filters, then applies ranking only inside that bounded set.
- Vectors Are Subordinate: embeddings and vector similarity are ranking signals only; they do not define truth, structure, or eligibility.

## 3. System Architecture

Cortex sits beside the runtime, not inside it.

Cortex is a standalone Go service with explicit HTTP API boundaries. It does not access OpenClaw internals directly, and runtime clients do not read or write Cortex storage or indexes directly.

It should be treated as infrastructure rather than as a plugin extension. Bootstrap ingestion, retrieval, reflection, dream, and promotion all run through the same service boundary and authority model.

The near-term MVP path operationalizes the minimum closed loop: lifecycle capture -> structured reflection -> knowledge-object storage -> bounded retrieval -> prompt injection. Dream and richer promotion flows extend that loop rather than replacing it.

The implementation is layered as:

- `api/`: transport and request handling
- `core/`: memory, retrieval, and reconciliation logic
- `storage/`: OpenSearch integration and persistence abstractions

- Gateway is the OpenClaw control plane for deployment, snapshotting, safe change management, and operational access. It is not a runtime execution surface and does not query knowledge directly.
- OpenClaw runtime hooks emit evidence needed for ingestion and reflection.
- Orchestration decides when to query Cortex, what constraints to apply, and how returned knowledge is injected.
- Prompt assembly, escalation framing, and final prompt payload construction remain orchestration concerns that may consume Cortex retrieval as one input.
- Applications read Cortex-backed knowledge for user-facing views and controls.

Service boundaries are:

- ingestion of runtime evidence and promoted artifacts
- storage of structured knowledge objects and relationships
- retrieval of bounded knowledge bundles
- asynchronous reconciliation, consolidation, and reindexing

All durable semantic recall flows through Cortex. Runtime-native memory features must not become competing knowledge authorities.

OpenSearch is the primary retrieval backend owned by Cortex. It stores knowledge objects as documents and supports lexical ranking, vector similarity, and dimension-based filtering under Cortex control.

The target service surface is:

- `/health`: report service and dependency readiness
- `/retrieve`: return a bounded structured knowledge bundle
- `/ingest`: accept persisted tool outputs and imported evidence
- `/reflect`: apply candidate knowledge updates
- `/dream`: run reconciliation over accumulated knowledge
- `/promote`: finalize artifact generation and reindex promoted outputs
- `/dimensions`: inspect canonical and candidate dimensions and manage promotion state

The MVP-required subset is:

- `/health`
- `/retrieve`
- `/ingest`
- `/reflect`

## 4. Knowledge Model

The primary unit is the knowledge object: a durable, typed record about some subject, entity, or relationship in Remram memory.

Knowledge object identity remains stable over time. What changes is the object's confidence, supporting evidence, relationships, and promotion state.

Each knowledge object should carry:

- a canonical statement or structured payload
- a type such as fact, preference, constraint, correction, decision, principle, or procedure
- provenance linking back to runs, artifacts, tools, or promoted documents
- confidence and freshness metadata
- dimensions used for retrieval eligibility
- relationships to other knowledge objects, entities, and artifacts
- promotion state describing whether the knowledge remains internal, is a promotion candidate, or is backed by a promoted artifact

Knowledge should normalize around entity collections plus typed attributes and relations rather than unconstrained key-path namespaces. Dimensions are structured metadata fields on objects, not vector axes. The system should build knowledge incrementally through capture and reflection rather than relying on large pre-authored schemas.

Knowledge objects are updated by delta, not by rewriting the entire memory set on each run.

Confidence increases through reinforcement, recurrence, and corroborating tool or artifact validation. It decreases through contradiction and decay. Confidence influences retrieval ranking and review priority, not direct execution control.

A proposed adjacent object type is the conversation object: a semantic continuity record that links related sessions without storing their transcripts. If adopted, it would sit beside knowledge objects rather than replacing them.

A conversation object would likely carry:

- referenced `session_ids[]`
- a canonical rolling summary designed to stay dense and compressible
- embedding and dimension tags for retrieval
- recency and prominence metadata
- optional links to artifacts or archived continuity state

Conversation objects are not raw memory dumps. They are a pre-knowledge or adjacent continuity layer that preserves semantic direction across sessions while keeping canonical durable facts in knowledge objects.

## 5. Dimension System

Dimensions provide the hard-bounding layer for retrieval eligibility before semantic scoring.

Initial canonical dimensions are:

- person or subject
- workspace, organization, or tenant scope
- repository, project, or feature scope
- domain or topic scope
- environment or deployment scope
- artifact or knowledge type
- time horizon or recency class

Objects are indexed across many dimensions simultaneously so Cortex can filter by eligibility before applying similarity signals.

Candidate dimensions may emerge during reflection, but only become canonical during dream reconciliation when they are stable, reused across queries, and improve retrieval precision without causing fragmentation.

Dimensions are structured metadata fields, not vector-space coordinates.

Objects must satisfy dimension eligibility before they enter ranking.

## 6. Retrieval Pipeline

After query resolution, the retrieval pipeline is deterministic, filter-first, and proceeds through six stages:

1. apply hard dimension and scope eligibility filters, including caller isolation constraints supplied by orchestration
2. rank the remaining set with BM25 and other lexical signals
3. apply vector similarity inside that bounded set
4. rerank with confidence, freshness, and other governance signals
5. enforce token-budget and bundle-shape limits
6. construct a bounded bundle of typed knowledge objects, provenance, and conflict markers for orchestration

Eligibility precedes similarity. Embeddings are subordinate ranking signals inside the bounded set and never make an ineligible object eligible.

The injection contract is structured, typed, and inspectable, not transcript-shaped. Cortex returns knowledge bundles with enough provenance and governance metadata for orchestration to build audited prompt payloads without treating retrieval as prompt stuffing.

## 7. Ingestion Pipeline

Ingestion begins with runtime evidence capture and ends with indexed knowledge updates.

Intake sources may include live runtime evidence, external artifact import, and historical backfill, but all sources must pass through the same knowledge-authority model. Cortex does not read transcripts directly from runtime internals; transcript-derived evidence must arrive through explicit hooks, exports, or backfill jobs. On live runs, `tool_result_persist` is the capture boundary so structured outputs survive pruning, transcript compaction, and loss of prompt visibility.

1. persisted tool outputs, imported artifacts, or historical evidence are captured through runtime hooks or explicit import flows
2. evidence is parsed, chunked, and indexed for retrieval support
3. extraction produces candidate knowledge objects and candidate dimensions
4. Cortex applies create, update, merge, or retire operations against knowledge objects
5. affected objects are reindexed for retrieval and queued for later reconciliation when needed

The two primary write paths are:

- `/ingest` for deterministic structured tool or import capture, including low-confidence imported knowledge candidates when the source is already structured enough to mutate directly
- `/reflect` for direct post-turn reflection deltas and functional thread-memory compression

Ingestion and reflection both mutate Cortex state. They should be deterministic and idempotent by provenance key so retries do not duplicate knowledge.

Bootstrap ingestion is a first-class backfill path within this model. It reads historical transcript sources in read-only mode, extracts structured knowledge objects, builds relationships and dimension indexes, detects recurrence and contradiction signals, and initializes the knowledge base before or alongside live runtime evolution.

Bootstrap produces knowledge objects, continuity metadata, and other derived views such as memory-map projections. It must not rewrite source transcripts and must not bypass normal knowledge authority rules.

Bootstrap should prefer controlled Gateway, Forge, or OpenClaw-managed surfaces over raw runtime-store manipulation. Early migration work may still ingest existing memory or session files in read-only mode when that is the safest way to learn the data shape and seed onboarding.

Two future ingestion-oriented enhancement paths build on the same authority model:

- Artifact import: manually triggered ingestion of documents, repository snapshots, or other external artifacts that parses structure, extracts low-confidence candidates, and uses later review or user framing to adjust authority and confidence.
- Hydrate: historical conversation backfill that replays prior session history or external chat exports through reflection-oriented batch processing to initialize continuity and shorten time-to-value.

## 8. Reflection Model

Reflection is the near-line asynchronous extraction pass that runs after execution completes and after the user-visible response path is finished.

- trigger: `agent_end`
- input: bounded run evidence, tool results, and existing related knowledge
- output: candidate deltas such as add, revise, correct, weaken, strengthen, relate, retire, and propose-dimension

Reflection should be idempotent, incremental, and delta-based. It extracts facts, preferences, constraints, decisions, corrections, and candidate dimensions while updating the smallest necessary part of memory instead of regenerating a full memory snapshot. Reflection output is structured delta data, not a narrative summary.

Reflect runs directly after a chat turn. It may also emit functional process summaries or other dense thread-memory forms that can be retrieved later instead of replaying full chat history. New reflection outputs should be flagged for later Dream adjudication.

If the durable conversation layer is adopted, `agent_end` is also the natural update point for rolling conversation summaries and continuity metadata after execution completes.

## 9. Dream Model

Dream is the scheduled, system-wide reconciliation and consolidation layer, typically triggered by cron-driven background sessions.

Its responsibilities are:

- deduplicate overlapping knowledge objects
- detect and surface contradictions
- demote or retire weak knowledge
- form higher-order principles from repeated corroborated patterns
- promote stable candidate dimensions into canonical ones
- identify artifact-promotion candidates
- adjust confidence based on corroboration, recency, and conflict

Dream does not replace reflection. Reflection captures local deltas from a run; dream reconciles the global memory graph over time.

Dream is part of the target architecture. The MVP memory loop can be verified before full reconciliation logic is operationalized, but the storage and APIs should anticipate that later phase.

Dream is the nightly or scheduled adjudication pass. It looks harder at newly added memory, performs expanded retrieval and semantic separation, resolves conflicts, enriches context, and formalizes what reflection added quickly in the live path.

If conversation objects are adopted, dream may also become the place where stale summaries are compressed, overlapping conversations are reviewed for merge, and continuity prominence is recalibrated.

## 10. Artifact Promotion

Some knowledge should remain in Cortex only. Some knowledge should be promoted into durable human-managed artifacts.

Promotion is appropriate when a synthesized result is stable, reusable, reviewable, or needed outside runtime memory.

Promoted artifacts are Markdown projections of validated knowledge. They are derived outputs, not the canonical source of truth. The canonical memory record remains the knowledge object and its relationships inside Cortex.

Promoted artifacts should live in a local Git-backed artifact store, remain linked to their originating knowledge objects, and be reindexed back into Cortex as higher-authority document sources after creation or update.

The normal promotion flow is: knowledge candidate -> artifact draft -> diff and review in the App -> approval -> `/promote` -> commit or update -> reindex.

If the knowledge that points at a promoted artifact changes, Dream may redraft that document and commit a new version into the local artifact store so the full trail from source evidence to knowledge mutation to artifact revision remains traceable.

## 11. Runtime Integration

OpenClaw integration uses explicit runtime hooks plus scheduled background triggers:

- `before_model_resolve`: escalation and policy only; not a Cortex retrieval or mutation surface
- `before_prompt_build`: synchronous `/retrieve` of a bounded knowledge bundle
- `tool_result_persist`: capture of tool outputs and runtime evidence and enqueue `/ingest` before compaction
- `agent_end`: trigger reflection and `/reflect`
- cron-driven sessions or jobs: trigger `/dream`

OpenClaw and orchestration interact with Cortex through the service interface rather than through direct index or store access. The App reads Cortex through the API, and Gateway does not query knowledge directly.

In escalation flows, Cortex supplies structured recall. It does not assemble the final expert prompt, does not override system prompt authority, and does not decide whether external context should also be added.

If conversation objects are enabled, retrieval may also return dense conversation summaries with recency, prominence, and confidence metadata so orchestration can weight continuity without needing transcript history.

Sync boundaries should stay narrow around retrieval needed for prompt construction. Reflection, dream, and artifact promotion should run asynchronously unless an explicit workflow requires otherwise. Cortex retrieval failure returns an empty bundle and the run continues.

Prompt enhancement comes from layered retrieval at prompt-build time rather than from Dream mutating prompts directly. The old flat memory-file pattern should give way to structured layered retrieval.

Bootstrap ingestion is pre-runtime conditioning or a controlled maintenance path, not part of the normal live request latency path.

The runtime lifecycle is: interaction -> `tool_result_persist` capture -> `agent_end` reflection -> knowledge write -> future `before_prompt_build` retrieval.

## 12. Failure & Degradation

If Cortex is unavailable, runtime execution should continue in degraded mode with an empty knowledge bundle and without blocking the run. Evidence capture should be queued where possible rather than blocking execution.

If the search layer is unavailable, Cortex should prefer degraded metadata or direct-store retrieval over failure when possible, while suspending ranking quality and deferred reconciliation work that depends on the index.

Failures must be visible. Degradation should be explicit in logs, metrics, and returned status metadata.

## 13. Open Questions / Active Design Areas

- extraction strategy: always run reflection or gate it by heuristic
- reflection format: how granular structured deltas should be and what counts as a knowledge-worthy extraction
- prediction-based delta model: whether reflection should compare against expected memory changes before writing
- confidence math: exact scoring, decay, contradiction impact, and reinforcement weighting
- hybrid scoring: how BM25, vector similarity, confidence, and other weak signals should combine
- dimension promotion thresholds: what persistence and reuse signals qualify a candidate dimension for canonical promotion
- dimension explosion control: how candidate dimensions are introduced, validated, and retired
- entity normalization: how far the entity-collection model should go versus specialized object schemas
- deduplication strategy: when Cortex should update an existing object versus create, split, or merge
- bootstrap mode behavior: whether live injection should be disabled, reduced, or left pass-through while historical backfill is running
- historical backfill: how bootstrap ingestion should replay prior sessions and initialize confidence safely
- source-sensitive confidence: how `historical-session`, `external-artifact`, and live runtime evidence should differ in initial confidence and reinforcement rules
- external import: how document ingestion should balance low-confidence writes, review, and deduplication
- import review workflow: how post-analysis user framing should adjust authority, overrides, and evergreen status for imported knowledge
- import archive model: whether imported artifacts need searchable full-text storage outside canonical knowledge objects
- hydrate execution strategy: whether batch replay should be sequential or parallel, and whether hydrate defaults to full history or scoped ranges
- hydrate onboarding UX: which summary metrics and memory-map views best communicate "wake up to continuity" without overstating certainty
- durable conversation layer: whether conversation continuity should be modeled as first-class Cortex objects adjacent to knowledge objects or as derived retrieval views
- conversation assignment: whether attach, fork, and closure decisions belong in orchestration, Cortex, or a shared proposal flow
- migration sequencing: when Cortex can safely replace OpenClaw memory storage after a dual-run learning phase
- conversation compression: when continuity summaries should be compressed, archived, or pruned without losing identity
- conversation prominence: how inactive but important conversations should remain retrievable over time
- conversation merge policy: whether Dream may merge overlapping conversations and how user override interacts with that
- shared knowledge spaces: how explicit permissioned sharing should work without weakening local-first ownership
- prompt-assembly contract: how much provenance, confidence, and bundle structure orchestration needs for auditability without bloating prompt payloads
- injection strategy: what ordering, formatting, and grouping best turn retrieved knowledge into deterministic model influence
- memory map generation: what derived graph view best communicates initialized knowledge to users without pretending the visualization is canonical storage
- embedding strategy: which local or remote embedding path best fits sovereignty, cost, and ranking quality goals
- principle promotion: when recurring patterns become strong enough to elevate into explicit principles or artifact candidates
- behavioral verification: how to prove memory improved an outcome rather than merely persisting more data
- retention policy: what should remain stored long-term versus merely eligible for active retrieval
- vector index lifecycle: how reindexing, schema evolution, and dimension changes are managed safely
- bundle composition: how relevance, diversity, and confidence should be balanced in bounded retrieval
