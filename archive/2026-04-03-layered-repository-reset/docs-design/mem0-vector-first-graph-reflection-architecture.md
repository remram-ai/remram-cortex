# Mem0 Vector-First Graph-Reflection Architecture

## Purpose

This memo captures a specific `Mem0` architecture path that emerged after the broader foundation review:

- `Mem0` remains the primary memory authority
- vector-backed memory remains the first retrieval surface
- graph is added later as a derived reflection layer
- graph does not replace the authority model unless it earns that role in practice

This is different from both:

- plain `Mem0` with no graph strategy
- graph-first `Graphiti` or `Neo4j`-style architectures

It is a deliberate middle path.

Reviewed on `April 3, 2026`.

## Why This Variant Matters

This pattern matches Cortex more closely than a pure record-only `Mem0` path, but without forcing a graph-first commitment.

It preserves the parts of the original Cortex direction that still seem solid:

- durable extracted memory over transcript dependence
- bounded retrieval
- artifact-backed provenance
- layered recall
- reflection and maintenance out of band
- promotion and synthesis as higher-order work

It also preserves one of the strongest practical lessons from the ecosystem review:

- first-pass memory retrieval should stay simple, inspectable, and proven

That leads to a clean split:

- vector memory for initial authority and recall
- graph as a derived structure for reflection, expansion, clustering, contradiction checks, and later promotion

## Core Architectural Decision

Treat `Mem0` as the only durable memory authority in phase 1.

Treat graph as a derived secondary structure built from authoritative `Mem0` memories out of process.

That means:

- the vector-backed `Mem0` record remains the write authority
- graph is projection, not source of truth
- graph can be rebuilt or lag temporarily without breaking core memory correctness
- graph earns its keep by improving reflection and expansion, not by being declared central in advance

This is the key rule that keeps the stack coherent.

## High-Level Shape

```text
Channels / CLI / Agents
        |
        v
OpenClaw Runtime
  - sessions
  - tools
  - hooks
  - Mem0 bridge
        |
        v
Mem0 Authority Layer
  - add / update / delete / none
  - memory records
  - metadata
  - history
  - vector-first recall
        |
        +--> Vector backend
        |
        +--> History / audit store
        |
        +--> Reflection event stream or poller
                  |
                  v
          Graph Reflection Worker
            - entity extraction
            - relation extraction
            - clustering
            - contradiction hints
            - promotion candidate detection
                  |
                  v
          Derived Graph Store
            - relationship neighborhoods
            - communities / clusters
            - reflection outputs
```

## Artifact Handling

`Mem0` is usable in this architecture for artifact-derived memory, but only if we are explicit about the boundary.

The right rule is:

- raw artifacts stay in provider-backed systems
- `Mem0` stores extracted durable memories plus artifact references in metadata
- graph reflection operates over canonical memories, not over raw files as the authority layer

That means this path is not "put all documents into Mem0."
It is:

1. ingest an artifact through an intake worker
2. extract text, images, or structured signals from the artifact
3. send the relevant material into `Mem0`
4. store artifact lineage and source references in the memory metadata
5. use those canonical memories as input to graph reflection

This fits Cortex well because it preserves the original artifact model:

- evidence lives outside the memory authority
- the memory authority stores what mattered
- source links remain inspectable

### What Mem0 natively helps with

Official docs show that `Mem0` can already:

- extract memories from text or conversation turns
- use custom fact extraction prompts to control what gets stored
- use custom update prompts to decide add or update or delete or none
- process images in multimodal mode and store the extracted information as standard memories

That means artifact intake can be stronger than a plain text-only chat memory loop.

For example:

- screenshots can become memories
- receipts or product photos can become memories
- scanned or image-based documents can become memories if the relevant details are extractable through the multimodal path

This is not full document lifecycle management by itself.
But it is enough to make artifact-derived memory real in phase 1.

### What should remain outside Mem0

`Mem0` should not become the raw artifact repository.

Keep these outside:

- full artifact bytes
- Git revisions
- Google Docs content storage
- large raw document corpora
- promoted artifact materialization

Instead, attach to each canonical memory:

- `artifact_id`
- `artifact_revision_id` when available
- `provider`
- optional location pointer or URI
- source kind such as `git`, `gdoc`, `image`, `receipt`, `note`

That gives Cortex the right contract without fighting the foundation.

## What Stays Canonical

The canonical object in this architecture is still the disciplined `Mem0` memory record.

Each canonical memory should carry:

- stable memory id
- memory text or canonical statement
- scope fields
- provenance fields
- artifact reference fields
- confidence or status fields where appropriate
- timestamps

The graph layer should never become the only place where a fact exists.

Instead, graph nodes and edges should point back to canonical memory ids and source artifact identifiers.

That gives us a strong invariant:

- if the graph is lost, delayed, or rebuilt, core memory still works

This same rule applies to artifacts:

- if the graph is rebuilt, canonical memories still retain artifact lineage
- if the source artifact changes, correction starts from the canonical memory layer, not from arbitrary graph state

## Retrieval Model

This pattern is intentionally layered.

### Phase-1 retrieval

Default retrieval path:

1. query `Mem0`
2. use vector recall plus filters plus reranking
3. return compact canonical memories

No graph dependency is required.

### Phase-2 retrieval enrichment

After the graph reflection layer exists:

1. run normal `Mem0` retrieval
2. inspect top memory ids
3. optionally ask the graph for nearby entities, relations, or cluster context
4. attach that as expansion context only when needed

That means graph improves retrieval without owning first-pass ranking.

This is closer to the original Cortex layered retrieval posture:

- fact first
- support and relationship context second
- raw artifact resolution last

## Reflection Model

Graph is generated in reflection, not in the hot path.

That is the most important difference from a graph-first stack.

The reflection worker can run:

- after new memory writes
- on a schedule
- on demand for selected scopes or artifacts

Its responsibilities are:

- extract entities from authoritative memories
- derive relationship edges
- identify repeated co-occurrence or support patterns
- identify likely contradiction or supersession candidates
- build lightweight communities or clusters
- surface promotion candidates

This is the right place for graph because:

- it keeps the write path simple
- it keeps retrieval dependable even when reflection is behind
- it lets graph prove its value incrementally

## Why This Fits Cortex Better

This pattern matches Cortex more closely in three important ways.

### 1. Reflection stays out of the write path

Cortex always wanted higher-order maintenance to be bolt-on rather than a reason the whole base layer becomes fragile.

This does that cleanly.

### 2. Graph is used where graph is strongest

Graph is strongest for:

- expansion
- clustering
- neighborhood views
- contradiction discovery
- promotion candidates

It is not required to own initial recall just because it exists.

### 3. Provenance stays simple

The original Cortex provenance model was relatively simple and inspectable.

This architecture preserves that.

Graph can enrich provenance views later, but it does not force a more implicit episode-derived model on day 1.

## What To Do The Mem0 Way

If we choose this path, several things should remain explicitly `Mem0`-native:

- capture policy
- add or update or delete decisions
- core search
- metadata filtering
- reranking
- user or agent or run scoping
- history trail

Those are not the parts to rewrite early.

## Mem0 Extension Surface To Exploit

This path is only attractive if we actually use the extension seams Mem0 already gives us.

The important ones are:

- `custom_fact_extraction_prompt`
- `custom_update_memory_prompt`
- enhanced metadata filtering
- custom categories
- rerankers
- multimodal support
- graph memory
- REST and OpenAI-compatible APIs
- the official `OpenClaw` plugin

### Why these matter here

`custom_fact_extraction_prompt` is how we keep artifact-derived memory disciplined.

Instead of letting every file or conversation dump random facts into long-term memory, we can tell `Mem0` exactly what kinds of details count as durable memory for Cortex.

`custom_update_memory_prompt` is how we make revision behavior and correction safer.

That is especially important for artifact-backed memory because the hard problem is not only storing facts. It is deciding whether a new observation should:

- add a new memory
- update an existing memory
- delete an outdated memory
- do nothing

Enhanced metadata filtering and custom categories are the main way to keep Cortex policy visible in phase 1.

These should carry fields such as:

- artifact source
- artifact lineage
- provider
- confidence tier
- scope
- memory type
- promotion state

Rerankers matter because the whole point of vector-first authority is that first-pass recall stays strong and bounded.

Multimodal support matters because it gives us a better path for screenshot and image-derived memory than a text-only architecture.

Graph memory matters here mainly as an optional bridge or accelerator.

The docs describe it as:

- extracting entities, relationships, and timestamps
- returning graph relations alongside vector results
- not reordering vector hits by default

That is almost exactly the relationship we want between the authority layer and the graph layer.

### What not to assume

Do not assume the stock `OpenClaw` plugin exposes every Mem0 extension directly.

The official plugin clearly exposes:

- `customPrompt`
- `customCategories`
- backend configuration for embedder, vector store, and LLM

But the full Mem0 OSS surface is broader than the minimal plugin config.

So the likely path is:

- stock plugin first
- thin plugin fork or adapter later if we need richer update policy, reranking control, or more explicit artifact metadata handling

## What To Do In The Cortex Layer

The Cortex-owned layer should handle:

- metadata contract
- artifact identity
- artifact intake normalization
- provenance normalization
- retrieval tracing
- graph reflection job orchestration
- expansion policy
- contradiction review workflow
- promotion rules

This is where Cortex adds meaning without replacing the foundation.

## Graph Store Requirements

If graph is secondary and derived, the graph store should be chosen for:

- easy local Docker operation
- graph traversal and neighborhood queries
- optional vector and full-text support as a bonus, not a hard requirement
- rebuildability from authoritative memory

This is why a graph backend such as `FalkorDB` becomes interesting here.

It is not interesting because it becomes the authority.

It is interesting because it can host the derived graph layer without forcing the whole architecture to become graph-first.

## Why This Is Better Than Graph-First For The First Build

This architecture buys down the main early risks:

- you do not need to prove graph-first retrieval up front
- you do not need to rewrite provenance around graph semantics
- you do not need to depend on a thinner `OpenClaw + graph` integration ecosystem
- you still get a real path to test graph value in practice

That makes it a better learning architecture.

## Why This Is Better Than Plain Mem0 If Graph Matters

This architecture also buys down the main long-term risk of plain `Mem0`:

- graph does not stay forever hypothetical
- reflection and promotion can become structurally smarter over time
- contradiction review can use more than vector proximity
- emerging topic communities can become visible

So it preserves upside without forcing premature commitment.

## Risks

The main risks are:

- graph becomes a decorative sidecar and never earns operational complexity
- projection drift appears between canonical memories and graph reflection outputs
- artifact lineage becomes sloppy if metadata discipline is weak
- reflection jobs become too expensive or too vague if not scoped tightly
- the team starts treating graph output as authoritative without building the right correction rules

These are manageable if the authority line stays clean.

## Recommendation

If the question is "how do we keep `Mem0` as the first-build foundation while still respecting Cortex's graph-shaped ambitions?", this is the best architecture seen so far.

Bluntly:

- vector-first authority is the right phase-1 posture
- graph in reflection is the right phase-2 experiment
- graph should earn promotion into the critical path only after it proves value

That is both more practical than a graph-first stack and more faithful to Cortex than a plain record-only memory system.
