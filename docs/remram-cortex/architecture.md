# Remram Cortex Architecture

## 1. Purpose

Remram Cortex is the knowledge authority layer for Remram.

It turns runtime evidence, tool outputs, and imported artifacts into durable knowledge, then returns bounded retrieval bundles to orchestration.

The core design rule is simple:

Reflection and Dream should do the hard work so retrieval can stay cheap, predictable, and inspectable.

Cortex is not:

- a transcript archive
- a vector-only memory store
- a prompt assembly system
- a replacement for runtime execution

OpenClaw executes.
Orchestration decides behavior.
Gateway governs the control plane.
Cortex remembers.

## 2. Architectural Rules

- Transcripts are evidence, not memory.
- Knowledge objects are the primary durable memory unit.
- One canonical object may have many retrieval paths.
- Links are primary; folders and clusters are derived views.
- Hard governance filters run before semantic scoring.
- Semantic signature is a soft routing signal, not a hard gate.
- Typed signal fields are the primary retrieval surface.
- Vector similarity is assistive, not authoritative.
- Reflection computes rediscovery paths; retrieval should mostly cash them in.
- Dream reconciles global memory quality without moving reasoning back into the live path.

## 3. Service Boundary And Stores

Cortex is a standalone Go service with explicit HTTP APIs.

It sits beside the runtime instead of inside it. Runtime clients do not read or write the OpenSearch index directly, and Cortex does not couple itself to mutable OpenClaw internals.

The implementation is expected to stay layered:

- `api/`: transport and request handling
- `core/`: memory, retrieval, reflection, and reconciliation logic
- `storage/`: OpenSearch and artifact-store integrations

The two core persistence surfaces are:

- OpenSearch for knowledge documents, retrieval indexes, ranking metadata, and traces
- a configurable artifact provider layer for imported artifacts and promoted artifacts

OpenSearch is the primary retrieval backend. It should own:

- governance field indexes
- typed signal fields
- canonical statement and summary text
- vector fields
- ranking metadata such as confidence and freshness

The artifact provider layer should own:

- backing artifact content or provider-native documents
- promoted human-readable artifacts
- provider-specific revision history where available
- optional local backup snapshots where policy requires them

Cortex should not create duplicate metadata files just to mirror state that already lives in OpenSearch or Git.

Different providers may back different artifact classes. A practical default is to use Google Workspace for collaborative human-readable artifacts and local Git for local-first, workflow-oriented, or backup-oriented artifacts.

## 4. Memory Model

Memory is the generic concept. The primary technical memory record inside Cortex is the knowledge object.

A knowledge object is a canonical durable statement or structured payload with stable identity over time. It may be reinforced, revised, superseded, contradicted, promoted, or retired, but it should not be duplicated merely because it can be rediscovered from multiple angles.

### 4.1 Knowledge Object Shape

Each knowledge object should carry at least:

- a canonical statement or structured payload
- an optional compact summary
- an object kind such as fact, preference, constraint, correction, decision, principle, procedure, or relation
- provenance back to runs, tools, artifacts, or promoted documents
- hard governance fields
- typed signal fields
- a semantic signature
- ranking metadata such as confidence, freshness, and reinforcement
- typed links to other objects, people, projects, or artifacts
- retention and promotion state

### 4.2 Canonical Objects, Not Buckets

Cortex should prefer:

- one object with many links
- one object with many retrieval cues
- one object with accumulated evidence

over:

- duplicate copies filed into multiple containers
- bucket-first clustering
- transcript chunk piles pretending to be knowledge

Clusters, project views, family views, and continuity summaries may all be derived later. They are views over the graph, not the source of truth.

### 4.3 Adjacent Continuity Objects

Conversation objects remain optional but plausible.

If adopted, a conversation object sits beside knowledge objects and stores bounded continuity such as:

- referenced `session_ids[]`
- a rolling semantic summary
- governance scope
- semantic signature
- recency and prominence metadata
- optional links to related artifacts or knowledge

Conversation objects do not store full transcripts.

## 5. Retrieval Model

Retrieval in Cortex is not one search step.

It is a staged narrowing system designed to keep recall broad enough for quality while ensuring the expensive reasoning happened earlier during reflection and Dream.

### 5.1 Stage 0: Scope And Governance Filter

This is the hard gate.

Before scoring, Cortex applies exact or bounded filters such as:

- ownership and audience
- family, person, project, repository, or system scope
- lifecycle state such as active vs retired
- temporal validity or expiration rules
- caller visibility and isolation constraints from orchestration

If an object fails governance, it is not eligible.

This is Cortex's equivalent of hierarchical metadata gating in RAG systems. It maps most closely to filter-first and hierarchical retrieval patterns, and it is non-negotiable.

### 5.2 Stage 1: Semantic Signature Routing

Each object and query may carry a 16-32 bit semantic signature.

The signature is a compressed semantic routing layer that answers:

"What kind of thing is this?"

It should be used as:

- a score bias
- a cheap preselection hint
- a routing signal for later maintenance flows

It should not be used as:

- an exact equality filter
- the final decision surface

Practical scoring pattern:

`score_boost = 1 / (1 + hamming_distance(query_sig, object_sig))`

This is closest to a precomputed routing code than to a conventional vector embedding.

### 5.3 Stage 2: Typed Signal Retrieval

This is the primary retrieval surface.

Each knowledge object emits retrieval signals into a fixed set of fields:

- `domain`
- `activity`
- `need`
- `object`
- `mechanism`

The field set is fixed and intentionally small.
The values inside the fields remain open natural language.

Example:

```text
domain: ["outdoors", "travel"]
activity: ["hiking", "trip planning"]
need: ["find places to stay", "expand inventory"]
object: ["camping spots", "trail lodging"]
mechanism: ["reseller network"]
```

This is the Cortex equivalent of a structured multi-field semantic index. It replaces brittle taxonomies without collapsing everything into one untyped blob.

### 5.4 Stage 3: OpenSearch Lexical Scoring

OpenSearch should do the main retrieval work over the already-bounded candidate set.

The practical first-pass query shape is:

- `bool.filter` over governance fields
- `bool.should` or `multi_match` over typed signal fields
- lexical matching on canonical statement and summary
- optional keyword or phrase boosts where exact grounding matters

Recommended signal weighting:

- `need`: highest
- `object`: high
- `mechanism`: medium-high
- `activity`: medium
- `domain`: low

Those weights reflect what usually matters most for rediscovery:

- why it matters
- what it is about
- how it works
- what someone is doing
- what broad world it lives in

### 5.5 Stage 4: Vector Similarity

Vector similarity is assistive.

It helps when phrasing differs, when lexical overlap is weak, or when signal extraction was good but not exact.

It should operate only inside the governance-bounded candidate set.

This maps to hybrid search and vector backstop patterns from mainstream RAG systems, but Cortex explicitly rejects vector-first retrieval as the primary memory authority.

### 5.6 Stage 5: Relationship Expansion

After primary matching, Cortex may enrich the result set by following typed links such as:

- person to family
- project to related idea
- decision to constraint
- object to promoted artifact

Relationship expansion is not primary retrieval.

It is a second-pass enrichment step that adds nearby relevant context after the core match has already been established.

This is the practical RAG analogue of lightweight knowledge-graph augmentation without committing Cortex to graph-first infrastructure.

### 5.7 Stage 6: Final Ranking And Bundle Assembly

Final ranking may combine:

- OpenSearch lexical score
- signature similarity boost
- vector similarity contribution
- confidence
- freshness and temporal validity
- reinforcement or usage history
- relationship-expansion bonuses

The result should be a bounded knowledge bundle, not a raw result list.

Bundle assembly should:

- enforce token budgets
- preserve diversity instead of returning near duplicates
- surface conflict or supersession markers when relevant
- optionally carry a retrieval trace for inspection

When a query is genuinely ambiguous, Cortex should prefer:

- a composed multi-angle bundle
- or an explicit clarification hint

over silently forcing one false-precision answer.

## 6. OpenSearch-Practical Index Shape

The current design maps cleanly onto OpenSearch.

### 6.1 Governance Fields

Governance fields should be stored in exact-match or bounded forms such as:

- `keyword`
- `boolean`
- numeric ranges
- dates

These fields drive `filter`, not fuzzy ranking.

### 6.2 Typed Signal Fields

Typed signals should be stored as multi-valued text fields, ideally with exact subfields available where useful.

The main practical pattern is:

- analyzed text for `match`, `match_phrase`, and BM25 scoring
- optional keyword subfields for exact filtering or debugging

### 6.3 Canonical Text Fields

Canonical statement and summary should remain searchable.

They provide grounding for exact phrases, named entities, and natural language wording that should not be forced into rigid schema fields.

### 6.4 Vector Fields

The vector representation should be derived from the object's retrieval surface, not from raw transcripts.

A practical first pass is to embed some combination of:

- canonical statement
- compact summary
- typed signals

### 6.5 Signature Storage

The signature may be stored as a bitstring, integer, or another compact representation.

The first practical implementation may apply signature distance in Cortex after OpenSearch returns a bounded candidate set rather than forcing complex search-engine-native bit math on day one.

## 7. Write Model

### 7.1 Ingest

`/ingest` handles deterministic capture of already-structured evidence such as:

- tool outputs
- import parser outputs
- promoted artifact reindexing

It may create low-confidence knowledge candidates directly when the source is structured enough.

### 7.2 Reflection

`/reflect` is the near-line extraction pass triggered after execution completes.

Reflection is where Cortex earns cheap retrieval later.

For each candidate memory, reflection should:

1. find the most relevant existing objects inside the same governance scope
2. decide whether the candidate is new, reinforcing, refining, generalizing, specializing, superseding, or contradicting
3. produce or update the canonical statement
4. generate typed signal fields using the rediscovery question:
   "What phrases would someone use to find this later?"
5. compute the semantic signature
6. attach provenance and links
7. write structured deltas, not free-form summaries

Reflection output must be idempotent by provenance key so retries do not duplicate memory.

### 7.3 Reflection And Known RAG Patterns

Reflection is where Cortex absorbs the lessons from self-reflective RAG without paying that cost live at query time.

Rather than letting retrieval self-correct after poor search, Cortex tries to write better memory surfaces up front.

## 8. Dream Model

Dream is the scheduled reconciliation and consolidation layer.

Reflection is local and immediate.
Dream is global and slower.

Dream should:

- deduplicate overlapping objects
- surface and manage contradictions
- adjust confidence based on corroboration, conflict, and age
- normalize synonymous retrieval cues
- prune signal phrases that do not help retrieval
- form higher-order principles from recurring stable patterns
- identify promotion candidates
- compress stale continuity summaries

Dream may also surface pressure for schema changes, but it should not automatically invent new signal-field types in the hot path.

For this architectural phase:

- typed signal fields are fixed
- values inside those fields evolve freely

That keeps retrieval stable and OpenSearch queries understandable.

## 9. Artifact Intake And Bootstrap

### 9.1 Artifact Intake

Artifact intake is the multimodal import path for documents and images.

It should:

- store or register the artifact through the configured provider layer
- parse the artifact into source-linked slices
- use chunking only as an ingestion tactic
- create or reinforce knowledge objects from those slices
- preserve source locations for audit and later revision

Context-aware chunking, contextual enrichment, and late chunking are most relevant here. They improve document understanding before knowledge extraction without redefining the durable memory model.

### 9.2 Bootstrap Ingestion

Bootstrap ingestion is the historical backfill path.

It should consume:

- exports
- controlled backfill jobs
- other read-only operational sources

It should not depend on a permanent direct coupling to mutable runtime internals.

Migration-phase direct file ingestion may still exist as one-time operational tooling, but that is not the desired long-term service contract.

## 10. Conversation Continuity

If conversation objects are adopted, Cortex should own their durable storage and lifecycle.

Orchestration may still provide runtime hints such as:

- continue prior thread
- fork to new thread
- prefer one related thread over another

But durable attachment, continuity storage, merge, and archival should remain Cortex responsibilities.

During migration, OpenClaw-native memory artifacts may continue to exist as evidence or operational fallback, but they do not become peer authorities once Cortex retrieval is in use.

## 11. Runtime Integration

OpenClaw integration should use explicit hooks and jobs:

- `before_prompt_build`: synchronous `/retrieve`
- `tool_result_persist`: capture evidence and enqueue `/ingest`
- `agent_end`: trigger `/reflect`
- scheduled jobs: trigger `/dream`

OpenClaw and orchestration should talk to Cortex through service APIs rather than direct storage access.

Prompt assembly remains outside Cortex.

Retrieval is synchronous because the live run needs it.
Reflection, Dream, and promotion should remain asynchronous unless a specific workflow says otherwise.

## 12. RAG Strategy Alignment

The Cortex design aligns with several known RAG strategies, but it translates them into a knowledge-authority system instead of copying a generic RAG stack.

### 12.1 Direct Fits

- Hybrid search:
  governance filters plus BM25 plus vector scoring are central to Cortex and map cleanly to OpenSearch.
- Reranking:
  Cortex should rerank with confidence, freshness, reinforcement, signature bias, and relationship context after primary search.
- Hierarchical retrieval using metadata:
  this maps directly to governance-first filtering.
- Context-aware chunking:
  most relevant for artifact intake and bootstrap ingestion.

### 12.2 Constrained Fits

- Query expansion:
  useful for low-confidence or underspecified queries, but it should be fallback behavior rather than the normal retrieval path.
- Multi-query RAG:
  may improve recall in ambiguous cases, but it increases latency and should be used selectively.
- Contextual retrieval:
  useful when imported artifact slices need more document-level context; it is less central for canonical knowledge objects.

### 12.3 Translated Rather Than Adopted

- Self-reflective RAG:
  Cortex pushes that logic into Reflection and Dream instead of query-time self-correction loops.
- Knowledge graphs:
  Cortex uses typed links and relationship expansion today. A graph-first backend is deferred.
- Agentic RAG:
  orchestration may decide when to call Cortex or fetch full artifacts, but Cortex retrieval itself should stay predictable rather than fully agentic.

### 12.4 Deferred Or Open

- Fine-tuned embeddings:
  relevant later if local or domain-specific embeddings materially improve ranking quality.
- Late chunking:
  promising for intake and bootstrap, but not required to lock the core architecture.

## 13. Failure, Degradation, And Observability

If Cortex is unavailable, runtime execution should continue in degraded mode with an empty knowledge bundle.

If OpenSearch is degraded, Cortex should prefer reduced-quality retrieval over total failure where possible, while clearly marking that degraded state.

Cortex should expose enough observability to make retrieval debuggable:

- filter decisions
- signature contribution
- signal-field matches
- vector contribution
- relationship-expansion steps
- final bundle composition

Without retrieval traces, the system will be difficult to tune and hard to trust.

## 14. Open Questions

- exact signature bit layout and whether the first practical size is 16, 24, or 32 bits
- the best place to compute signature distance: OpenSearch script scoring or Cortex-side rerank
- whether signal alias normalization belongs entirely in Dream or partly in reflection
- how much ambiguity Cortex should resolve automatically versus return as clarification hints
- the exact object-kind taxonomy for the first implementation
- whether conversation objects are part of the initial build or a later adjacent layer
- which embedding path best fits local-first constraints without degrading ranking quality
- whether query expansion lives inside Cortex retrieval, orchestration, or both
