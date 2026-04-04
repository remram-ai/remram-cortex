# Layered Memory Architecture

## Purpose

This document defines the layered memory architecture for Remram Cortex.

The goal is to stop forcing all memory, context, and knowledge behavior through one substrate or one mental model.

The system should instead operate as a coordinated stack of distinct layers under a single knowledge authority.

The core shift is:

- not one storage model
- not one memory product doing every job
- one authority coordinating multiple specialized layers

The correct framing is:

**one authority, multiple memory surfaces**

More precisely:

**Cortex is a single knowledge authority coordinating multiple specialized layers with different jobs**

## Executive Summary

The system should separate:

1. `policy`
2. `working memory`
3. `durable memory`
4. `decomposed artifact knowledge`
5. `canonical artifacts`

This gives the full stack:

**policy -> working memory -> durable memory -> decomposed artifact knowledge -> canonical artifacts**

This architecture is meant to support:

- low-latency live work during active sessions
- durable memory that compounds over time
- artifact-backed knowledge with clear temporal authority
- explicit separation between policy, working state, memory, and knowledge
- clean redraft and publication workflows for collaborative artifact evolution
- bounded runtime injection rather than prompt sprawl

## What This Document Does And Does Not Decide

This document defines the architecture and layer contracts.

It does not, by itself, lock the durable-memory substrate.

That choice remains inside the durable-memory layer and can still be evaluated across candidates such as:

- `Graphiti`
- `Mem0`
- `Cognee`
- a future Cortex-native authority implementation

The architecture should survive that choice.

## Design Principles

1. Do not force all layers into one substrate.
2. Keep policy separate from memory.
3. Keep working memory separate from durable memory.
4. Let durable memory own the reasoning graph.
5. Keep canonical artifacts authoritative and versioned.
6. Allow decomposed artifact knowledge to move ahead of canonical artifacts during active work.
7. Use one stable Cortex identity across all layers.
8. Do not make every decomposed object a graph node.
9. Run memory updates and artifact-impact updates from the same evidence feed.
10. Treat redraft and publication as a later pipeline, not as the source of live thought.
11. Re-ingest from canonical artifact revisions after publication.
12. Keep deep knowledge retrieval tool-based or deliberate rather than injected by default.

## Layer Overview

### Layer 1: Policy

Policy defines how the system should behave.

This is not memory. It is configuration, control, and guardrail logic.

It should contain:

- role definitions
- persona definitions
- tool-use rules
- escalation rules
- routing rules
- safety and permission rules
- mode packs such as coding mode, research mode, customer mode, or strategy mode
- prompt assembly discipline
- token budget policy
- reflection and artifact workflow policy

Policy is relatively stable compared with live context and learned memory.

It should remain in orchestration and configuration space.

Policy is not uniformly mutable.

It should be split conceptually into:

- stable access and safety policy
- mutable preference-policy and operating preferences

Mutable preference-policy can change through a governed reflection path.

Access policy should require explicit approval-oriented workflows.

### Layer 2: Working Memory

Working memory is the hot, temporary, low-latency runtime layer.

It exists to support live execution, active conversation continuity, and in-flight agent coordination.

It should contain:

- current task state
- active session continuity
- rolling summaries
- recent handoff notes
- temporary assumptions
- recent tool outcomes
- branch-local context
- in-progress planning state
- streamed compression products from chat or agent loops

Working memory is:

- fast
- mutable
- local to the active run or session
- low-latency
- allowed to be lossy
- optimized for runtime usefulness, not historical perfection

It is not the durable source of truth.

### Working Memory Posture

In OpenClaw terms, working memory should be anchored on the native session surface.

That means:

- the session transcript remains the evidence surface
- OpenClaw remains the primary working-memory implementation
- working continuity is session-scoped by default
- Cortex augments that layer through policy and semantic compression rather than replacing it

The system should not assume that raw session replay is the working-memory product.

Instead, the context engine should assemble bounded working memory from:

- recent session evidence
- rolling continuity summaries
- active runtime state
- compressed continuity objects

The raw session evidence should remain a journal, not the main consumer surface.

The main operational surface should be a derived semantic checkpoint stream built from that evidence.

An external hot store should not be assumed.

The default posture should be to let OpenClaw own working memory and to augment it through semantic compression and policy-aware assembly.

### Context Compression

Working memory quality should improve through rolling compression.

This is the best place for a Mamba-style or other compression-oriented model.

That compression layer should produce compact continuity objects such as:

- active goals
- open loops
- current assumptions
- recent decisions
- active entities and threads
- handoff state
- candidate notions
- artifact-impact hints
- oversight flags

This is how the system gets an effectively larger context window without pretending the model has infinite prompt budget.

### Raw Evidence And Semantic Checkpoint Model

The architecture should distinguish clearly between:

- raw evidence
- the semantic checkpoint stream

For runtime conversations and agent activity:

- raw evidence should close into an immutable evidence record, typically in `Postgres`
- the semantic checkpoint stream should be the primary operational consumer surface

For documents and other canonical artifacts:

- raw evidence should remain the canonical artifact body and revision history, typically in `Git`
- derived semantic checkpoints should still be the primary operational consumer surface

The best mental model is:

- raw evidence = journal or canonical source
- semantic checkpoint stream = materialized semantic checkpoint

Consumers should prefer the semantic checkpoint stream by default and escalate back to raw evidence only when exact verification is needed.

### Layer 3: Durable Memory

Durable memory is the real memory authority.

It stores the structured, evolving, long-lived knowledge that should persist beyond sessions, compaction, resets, and transient runtime noise.

It should contain:

- preferences
- constraints
- decisions
- corrections
- beliefs
- recurring patterns
- project truths
- customer posture summaries
- user operating profile
- relationship-bearing knowledge
- other durable memory objects

Durable memory is:

- structured
- persistent
- provenance-aware
- confidence-aware
- relationship-capable
- incrementally updated
- reconciled over time

This is where reflection and Dream-like maintenance belong.

### Layer 4: Decomposed Artifact Knowledge

This is the machine-usable derived layer built from canonical artifacts.

It is the operational knowledge layer the system can inspect, cite, retrieve from, and reason over at higher fidelity without pulling whole source artifacts into runtime.

It should contain:

- typed slices
- extracted structures
- sections
- entities
- fields
- embeddings
- lexical retrieval surfaces
- source-linked offsets and locators
- decomposition metadata
- retrieval-ready payloads

This layer is allowed to be mutable in near time and may temporarily move ahead of the canonical artifact during active work.

It is not the final published artifact truth.

It is derived working knowledge.

### Layer 5: Canonical Artifacts

Canonical artifacts are the official human-facing or system-facing source objects.

Examples:

- Markdown specs
- plans
- research notes
- CRM dossiers
- project records
- meeting notes
- source documents
- exported artifacts

Git is the preferred temporal authority for official artifacts when that storage posture fits.

Canonical artifacts are:

- versioned
- reviewable
- historically traceable
- human-manageable
- publication-oriented

## Unified Authority Model

The system still requires a single authority boundary.

That boundary remains Cortex.

But Cortex should be understood as a coordinating authority over multiple specialized memory and knowledge surfaces, not as one database or one index.

The correct statement is:

**Cortex is a single knowledge authority with multiple internal storage layers, not a single storage substrate.**

This allows:

- policy to remain stable and explicit
- working memory to remain fast and cheap
- durable memory to remain structured and graph-aware
- artifacts to remain versioned and authoritative
- decomposition to remain retrieval-optimized

without split-brain ownership.

## Layer Ownership Rules

Each layer must own a different class of truth.

### Policy Owns

- behavior rules
- routing rules
- mode overlays
- token and tool policy

### Working Memory Owns

- immediate continuity
- runtime coordination state
- hot summaries
- active execution state

### Durable Memory Owns

- learned long-lived memory objects
- relationship-bearing memory structures
- corrections and supersession
- the reasoning graph

### Canonical Artifacts Own

- official document body
- reviewable revision history
- publication truth

### Decomposed Artifact Knowledge Owns

- retrieval-ready machine views of artifacts
- typed slices and extracted structure
- embeddings and lexical surfaces
- source-linked derived payloads

## Cross-Layer Identity Model

### Core Rule

One real-world thing gets one stable Cortex identity even if it has multiple storage representations.

The identity is not:

- the Git path
- the graph node id
- the vector row id
- the provider-native file id

Instead, Cortex assigns a stable anchor identity.

### Anchor Identity

A top-level anchor object represents the smallest cross-layer unit worthy of stable identity.

Examples:

- a document
- a repo
- a customer dossier
- a conversation thread summary object
- a meeting bundle
- a workspace page
- a ticket
- a project artifact

Suggested fields:

- `anchor_id`
- `anchor_kind`
- `provider_kind`
- `provider_ref`
- `canonical_uri`
- `current_revision`
- `title`
- `scope`
- `status`

### Child Decomposition Objects

Decomposition objects point back to the anchor.

Suggested fields:

- `decomposition_id`
- `anchor_id`
- `revision_id`
- `kind`
- `source_locator`
- `typed_payload`
- `embedding_ref`
- `lexical_index_fields`
- `extraction_version`

### Memory Objects

Memory objects may reference one or more anchors without becoming the anchors themselves.

Suggested fields:

- `memory_id`
- `statement`
- `kind`
- `anchor_ids[]`
- `confidence`
- `freshness`
- `provenance`
- `graph_links`

### Identity Principle

Every anchor gets identity.

Some anchors get graph nodes.

Children inherit linkage.

Not every decomposed object becomes a graph node.

## Layer Interfaces

The architecture only stays clean if the interfaces are explicit.

The following interfaces are the minimum layer contracts Cortex must own.

### 1. Policy Interface

This interface assembles runtime behavior overlays.

Core responsibilities:

- resolve base role
- resolve mode packs
- resolve safety and routing policy
- expose bounded startup overlays

Suggested operations:

- `resolve_policy(run_context) -> policy_bundle`
- `resolve_mode_overlays(run_context) -> overlays[]`
- `resolve_tool_policy(run_context) -> tool_policy`
- `resolve_prompt_budget(run_context) -> token_budget_policy`

Write authority:

- human editors
- system configuration workflows

Direct writes from memory or artifact layers are not allowed.

### 2. Working Memory Interface

This interface owns hot session continuity and active runtime coordination.

Core responsibilities:

- store active continuity state
- expose recent high-signal runtime context
- maintain queue and handoff state
- support bounded hot retrieval

Implementation note:

- this interface should be anchored on the OpenClaw session surface
- OpenClaw should remain the primary working-memory implementation
- Cortex should contribute policy overlays and Mamba-style semantic compression
- external hot storage is not assumed

Suggested operations:

- `append_event(session_id, event)`
- `get_hot_window(session_id, limit) -> events[]`
- `get_working_snapshot(session_id) -> working_snapshot`
- `put_working_summary(session_id, summary)`
- `put_runtime_state(session_id, state_patch)`
- `get_runtime_state(session_id) -> state`
- `ack_graphization(cursor_or_event_id)`

Write authority:

- runtime orchestrator
- compression sidecar
- reflection queue handlers

Durable-memory systems must not treat this layer as canonical truth.

### 3. Raw Evidence Interface

Raw evidence is the canonical recovery and audit surface.

It is not the main subscribeable bus.

Core responsibilities:

- append immutable evidence records
- support replay and audit
- support checkpoint close and evidence packaging
- support exact verification when semantic outputs are disputed

Suggested operations:

- `append_evidence(event)`
- `close_evidence_window(scope_id) -> evidence_record`
- `get_evidence(evidence_id) -> evidence_record`
- `fetch_evidence(range_or_filter) -> evidence[]`
- `replay(range_or_filter) -> events[]`

### 4. Semantic Checkpoint Stream Interface

This is the main operational stream for downstream consumers.

It is derived from raw evidence and rebuildable from it.

Core responsibilities:

- emit typed semantic checkpoints
- preserve source references back to raw evidence
- support optimistic, on-demand, and nightly consumption
- support notion staging and lightweight oversight

Suggested operations:

- `append_checkpoint(checkpoint) -> checkpoint_id`
- `read_checkpoints(cursor, filters) -> checkpoints[]`
- `get_checkpoint(checkpoint_id) -> checkpoint`
- `mark_checkpoint_state(checkpoint_id, state)`

Suggested checkpoint states:

- `captured`
- `continuity_available`
- `notion_staged`
- `artifact_impact_applied`
- `oversight_reviewed`
- `reconciled`
- `verified`
- `rejected`

### 5. Durable Memory Interface

This is the primary memory authority contract.

Core responsibilities:

- ingest staged notions and durable memory candidates
- update or supersede prior memory objects
- store provenance and support references
- expose graph-shaped retrieval and navigation
- support maintenance and reconciliation

Suggested operations:

- `stage_notion(notion) -> notion_result`
- `upsert_memory(memory_delta) -> memory_result`
- `invalidate_memory(memory_id, reason)`
- `search_memory(query, scope, filters) -> memory_bundle`
- `get_memory(memory_id) -> memory_object`
- `get_related_memory(memory_id, depth, filters) -> related_bundle`
- `reconcile_support(anchor_id, revision_id) -> reconciliation_result`
- `run_maintenance(scope) -> maintenance_result`

Write authority:

- reflection pipeline
- approved correction workflows
- controlled maintenance routines

Direct runtime writes are not allowed unless they pass through the durable-memory contract.

High-signal cross-thread writes may be staged in near time, but they should be marked as:

- `tentative`
- `low_confidence`
- `unreconciled`

Only reconciliation should promote them to trusted Layer 3 memory.

### 6. Artifact Registry Interface

This interface manages stable artifact anchors and canonical revisions.

Core responsibilities:

- register anchors
- map provider references to anchor ids
- track canonical revisions
- expose artifact state

Suggested operations:

- `register_anchor(anchor_descriptor) -> anchor_id`
- `resolve_anchor(provider_ref_or_uri) -> anchor_id`
- `record_revision(anchor_id, revision_descriptor) -> revision_id`
- `set_anchor_state(anchor_id, state)`
- `get_anchor(anchor_id) -> anchor_record`

Write authority:

- intake workflows
- publication workflows
- provider sync jobs

### 7. Knowledge Decomposition Interface

This interface owns machine-usable derived views of artifacts.

Core responsibilities:

- decompose canonical revisions
- maintain typed slices
- maintain vector and lexical retrieval surfaces
- support revision-aware lookup

Suggested operations:

- `decompose_revision(anchor_id, revision_id) -> decomposition_result`
- `apply_artifact_impacts(anchor_id, impact_set) -> impact_result`
- `search_decomposition(query, anchor_scope, filters) -> decomposition_bundle`
- `get_slice(slice_id) -> decomposition_record`
- `replace_revision_projection(anchor_id, revision_id) -> refresh_result`

Write authority:

- artifact intake
- reflection artifact-impact branch
- re-ingestion after publication

### 8. Publication Interface

This interface handles redraft and canonical publication.

Core responsibilities:

- gather dirty anchors
- synthesize redrafts
- request or perform review
- publish canonical updates
- trigger re-ingestion

Suggested operations:

- `queue_redraft(anchor_id)`
- `build_redraft(anchor_id) -> redraft_candidate`
- `publish_revision(anchor_id, body, metadata) -> revision_id`
- `finalize_publication(anchor_id, revision_id)`

Write authority:

- scheduled consolidation jobs
- explicit user-initiated publication flows

### 9. Runtime Context Assembly Interface

This interface is how the orchestrator composes bounded startup and prompt context from the layers.

Core responsibilities:

- assemble the startup stance
- inject bounded continuity
- include compact memory bundles
- include knowledge briefs or pointers instead of full corpora by default

Suggested operations:

- `assemble_startup_stance(run_context) -> stance_bundle`
- `assemble_turn_context(run_context) -> context_bundle`
- `request_deep_knowledge(run_context, target) -> knowledge_bundle`

## Cross-Layer Write Rules

These rules are mandatory.

### Rule 1

Working memory can influence durable memory, but it cannot become durable memory by existing long enough.

Promotion must be explicit through reflection.

### Rule 2

Artifact-derived working updates can mark anchors dirty and update decomposition immediately, but they do not silently replace canonical artifact truth.

### Rule 3

Durable memory can reference artifacts and revisions, but it does not own the artifact body.

### Rule 4

Decomposition can outrun canonical artifacts temporarily, but only under explicit dirty-state tracking.

### Rule 5

Re-ingestion from a new canonical revision must be allowed to supersede stale derived decomposition and trigger memory support reconciliation.

### Rule 6

No layer is allowed to write directly into another layer's storage implementation while bypassing Cortex contracts.

### Rule 7

Cross-thread memory can appear before reconciliation only as tentative staged memory.

Layer 1 and Layer 2 may publish high-signal notions into the shared pipeline, but Layer 3 remains the authority that confirms, merges, rejects, or supersedes them.

## Assembled Startup Stance

An agent should not boot from one giant monolithic prompt.

It should boot from an assembled context stack.

The startup stance should be composed from multiple layers.

### Startup Formula

**startup stance = policy + working memory snapshot + durable memory bundle + knowledge brief/pointers**

More concretely:

1. base role profile
2. policy and mode overlays
3. retrieved operating profile and durable memory
4. subject or entity brief such as customer or project context
5. live working continuity block

### Injection Rule

Only bounded memory should be injected by default.

Broader knowledge should usually be accessed via tools or deliberate retrieval calls.

By default, inject:

- policy
- working-memory continuity
- durable-memory bundle
- compact knowledge brief or pointers

By default, do not inject:

- full artifact bodies
- full decomposition records
- full CRM-style corpora
- large knowledge warehouses

## Graph Strategy

The graph should primarily live in the durable-memory layer.

The decomposition layer should remain typed and retrieval-optimized rather than fully graph-native.

This gives the system the benefits of graph reasoning without forcing every storage layer to carry graph semantics.

### Likely Graph-Worthy Objects

- durable memory objects
- major entities
- artifact anchors
- projects
- customers
- users
- repositories
- important continuity objects if promoted
- promoted or consolidated knowledge structures

### Usually Off-Graph Unless Promoted

- every chunk
- every section
- every extracted field
- every decomposition record
- every temporary working slice

### Graph Principle

The graph is a reasoning index over knowledge, not a duplication of all knowledge internals.

## Reflection Split: Four Products Plus Oversight

Reflection should not produce only memory deltas.

It should branch the same evidence stream into four output types:

1. memory updates
2. artifact impacts
3. context compression
4. governed instructions or policy updates

Oversight should consume the same semantic checkpoint stream in parallel, but it is not itself a normal write branch.

### Memory Updates

These should usually begin as staged notions derived from the semantic checkpoint stream.

Examples:

- new preference
- changed decision
- new customer posture
- updated operating belief
- new constraint

By default, durable memory should be reconciled at:

- session end
- checkpoint hooks
- nightly maintenance

Near-time durable writes should happen only for high-signal items, and those writes should remain tentative until later reconciliation.

### Artifact Impacts

These update the decomposed artifact-knowledge layer immediately and mark the relevant anchor dirty.

Examples:

- affected artifact id
- likely changed sections
- suggested section-level edits
- confidence
- urgency
- whether a redraft should be queued now

### Context Compression

This branch should continuously distill noisy session evidence into compact working-memory objects.

This is the natural home for:

- rolling continuity summaries
- open-loop compression
- active-thread distillation
- Mamba-style continuity products

These outputs improve working memory.

They do not become durable memory just by existing.

They are also the default input surface for:

- oversight
- notion staging
- artifact-impact hints
- low-cost ongoing monitoring

### Governed Instructions Or Policy Updates

Some policy-like state is mutable and should be learned over time.

Examples:

- user preferences
- preferred operating style
- stable formatting tendencies
- mode bias adjustments

These should not share a write path with access control or safety-critical rules.

Access-policy changes should require explicit approval-oriented workflows.

### Oversight Consumer

Oversight should consume the semantic checkpoint stream by default.

It should be able to escalate back to raw evidence when:

- confidence is low
- impact is high
- approval is required
- provenance is disputed
- memory reconciliation needs exact verification

Oversight responsibilities include:

- flag suspicious memory writes
- detect policy violations
- open review tasks
- downgrade confidence
- veto sensitive updates when required
- maintain audit traces

### Reflection Principle

Use one evidence feed.

Branch it into:

- durable-memory updates
- knowledge and artifact updates
- working-memory compression products
- governed preference-policy updates

Let oversight observe the same semantic products in parallel.

## Artifact Lifecycle And Collaboration Model

### Canonical Truth

Git-backed artifacts remain the canonical temporal truth for official artifacts.

A document can evolve through collaboration, and Git preserves the authoritative body and revision history.

### Near-Time Derived Working Knowledge

Decomposed artifact knowledge is allowed to move ahead of Git during active work.

Once a business plan or similar artifact is ingested, the user should be able to say:

- "I had an idea on the business plan."
- "Update the assumptions section."
- "This changes our market posture."

The system should update derived artifact knowledge immediately so reasoning and retrieval stay current.

Document artifacts should be indexed into the durable-memory layer with the same restraint used for session evidence:

- one compact summary node or episode-level representation
- a pointer back to the canonical artifact revision
- only extracted Layer 3 appropriate standalone facts, beliefs, or support relationships

The full artifact body should remain outside the durable-memory layer.

### Dirty State

When the decomposed artifact layer changes ahead of Git, the artifact anchor should be marked with states such as:

- `dirty`
- `pending_redraft`
- `unsynced_to_canonical`
- `redraft_ready`

### Consolidation And Redraft

A slower consolidation process can then:

1. gather all dirty anchors
2. collect latest derived knowledge and related durable-memory context
3. reconcile contradictions
4. generate a coherent redraft of the canonical artifact
5. request review if required
6. commit to Git or publish through the canonical provider
7. re-ingest the new revision

This process can run:

- nightly by default
- on demand when explicitly requested

### Artifact Principle

Artifact-derived working knowledge may move first.

Canonical artifact publication catches up later.

## Revision-Aware Knowledge Model

A collaborative artifact lifecycle only works if decomposition and support are revision-aware.

The system needs to know not just which anchor a decomposed record came from, but which revision.

### Decomposition Requirements

Decomposition records should carry:

- `anchor_id`
- `revision_id`
- `slice_id`
- `source_locator`
- typed extracted payload

### Durable Memory Support Requirements

Memory objects that depend on artifacts should also know which revisions support them.

This enables:

- confidence adjustment
- stale support detection
- contradiction analysis
- clean re-ingestion from Git after redraft

## Evidence Packaging And Graph Ingestion

At session end or other reconciliation checkpoints, the system should:

1. close the session evidence window
2. persist the evidence package as immutable runtime evidence, typically in `Postgres`
3. reconcile staged notions against:
   - existing durable memory
   - oversight outcomes
   - artifact support
   - the closed evidence package
4. ingest a compact evidence package into the durable-memory graph

For `Graphiti`, that evidence package should usually contain:

- a compact summary
- source pointers to the evidence record
- timestamps and thread identifiers
- selected extracted beliefs or support only when they are Layer 3 appropriate

For document artifacts, the comparable raw evidence surface remains the canonical artifact revision in `Git` or the provider source, not `Postgres`.

## Retrieval Order

A good retrieval order is:

1. durable-memory graph first
2. linked anchor selection second
3. decomposition retrieval third
4. canonical artifact body only when needed

This means the graph gives the system fast orientation, and the decomposition layer provides fine-grained evidence only when the query requires it.

### Example

For a business-plan revision question:

- durable memory may know the plan is shifting toward enterprise positioning
- an anchor node identifies the business-plan artifact
- the decomposition layer returns relevant sections and updated typed assumptions
- the canonical Git artifact is consulted or redrafted only when publication-level output is needed

## State Models

### Artifact Anchor States

Suggested artifact states:

- `canonical`
- `derived_current`
- `dirty`
- `pending_redraft`
- `redraft_ready`
- `published`
- `stale`

These make it possible to reason clearly about:

- whether the derived layer is ahead of the canonical artifact
- whether a redraft is needed
- whether re-ingestion is pending
- whether working knowledge is currently trustworthy

### Evidence Pipeline States

Suggested evidence states:

- `captured`
- `continuity_available`
- `notion_staged`
- `artifact_impact_applied`
- `oversight_reviewed`
- `reconciled`
- `verified`
- `rejected`

### Durable Memory States

Suggested durable-memory status fields:

- `active`
- `tentative`
- `superseded`
- `invalidated`
- `stale_support`

These states should be explicit, not inferred only from timestamps.

## Suggested Implementation Posture By Layer

### Policy

Likely implementation surfaces:

- orchestration config
- mode packs
- role profiles
- routing rules
- tool policy

### Working Memory

Likely implementation surfaces:

- OpenClaw session surface
- native compaction and session continuity
- runtime continuity objects
- streaming compression sidecar

Implementation note:

- working memory should stay OpenClaw-native by default
- Cortex should augment it through semantic checkpoint production and policy-aware assembly
- the append-only evidence log may be disk-backed
- working memory should be treated as operational infrastructure, not durable authority

### Durable Memory

Likely implementation surfaces:

- graph-oriented memory substrate
- structured memory objects
- reflection and Dream-style maintenance
- graph for reasoning and navigation

### Canonical Artifacts

Likely implementation surfaces:

- Git
- provider-backed authoritative documents
- source records with revision history

### Decomposed Artifact Knowledge

Likely implementation surfaces:

- typed database
- vector index
- lexical search fields
- source-linked slices
- revision-aware decomposition records

## Guardrails And Failure Modes

### Failure Mode 1: Split-Brain Authority

This happens if:

- durable memory and decomposition both try to own the same truth
- working memory starts acting like durable memory
- direct storage writes bypass Cortex contracts

Guardrail:

- enforce layer write interfaces
- require provenance and revision references

### Failure Mode 2: Graph Inflation

This happens if every decomposed slice becomes a node.

Guardrail:

- graph only durable memory, anchors, and promoted high-value structures

### Failure Mode 3: Artifact Drift Without Redraft Discipline

This happens if decomposition outruns canonical artifacts with no dirty-state and publication process.

Guardrail:

- explicit artifact states
- explicit redraft queue
- required re-ingestion after publication

### Failure Mode 4: Prompt Bloat

This happens if full corpora or full decomposition records are injected by default.

Guardrail:

- bounded startup stance
- deliberate deep retrieval only

## Bottom Line

The system should not behave like one giant memory bucket.

It should behave like a coordinated layered architecture where:

- policy governs behavior
- working memory supports live thought
- durable memory compounds learned understanding
- canonical artifacts preserve official temporal truth
- decomposed artifact knowledge supports fine-grained reasoning and retrieval
- reflection branches one evidence stream into multiple update products
- redraft and publication happen later without blocking live learning

This architecture is cleaner, more honest about the jobs the system actually has, and more likely to scale without turning memory into a junk drawer.
