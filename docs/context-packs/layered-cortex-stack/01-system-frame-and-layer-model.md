# System Frame And Layer Model

## Core System Statement

Cortex is a single knowledge authority coordinating multiple specialized layers.

The key phrase is:

**one authority, multiple memory surfaces**

This means the system has one semantic center, but not one storage substrate.

## The Five Layers

### Layer 1: Policy

Layer 1 defines how the system should behave.

It contains:

- role definitions
- mode packs
- tool-use rules
- approval rules
- escalation rules
- prompt-budget discipline
- mutable preference-policy through governed workflows

Layer 1 is not memory.

### Layer 2: Working Memory

Layer 2 supports active live work.

It contains:

- session continuity
- current task state
- rolling summaries
- recent tool outcomes
- handoff state
- temporary assumptions
- compact continuity objects

Layer 2 is fast and lossy.

It is not the durable source of truth.

### Layer 3: Durable Memory

Layer 3 stores long-lived semantic memory.

It contains:

- beliefs
- preferences
- constraints
- decisions
- relationships
- support references
- supersession and invalidation state

Layer 3 is where durable semantic truth compounds.

### Layer 4: Decomposed Artifact Knowledge

Layer 4 is the operational retrieval layer for artifacts.

It contains:

- typed slices
- extracted structures
- embeddings
- lexical fields
- source-linked offsets
- revision-aware retrieval payloads

Layer 4 is derived and allowed to move ahead of canonical artifacts during active work.

### Layer 5: Canonical Artifacts

Layer 5 is the ground-truth layer for artifacts.

It contains:

- reviewable documents
- revision history
- provider-backed authoritative artifacts
- approved redrafts and published outputs

## Authority By Layer

Each layer owns a different kind of truth.

Layer 1 owns behavioral truth.

Layer 2 owns live operational continuity.

Layer 3 owns durable semantic truth.

Layer 4 owns retrieval-ready operational artifact views.

Layer 5 owns canonical artifact truth.

## Why The Layers Exist

The architecture exists because these jobs conflict if forced into one store.

If policy lives in memory, behavior gets muddy.

If working memory becomes durable memory, noise becomes truth.

If durable memory stores whole artifacts, the graph becomes junk.

If decomposed knowledge replaces canonical artifacts, publication truth disappears.

The layered model prevents those failures.

## Stable Identity Across Layers

The same real-world thing should keep one stable Cortex identity across all layers.

That identity is the `anchor_id`.

Important consequences:

- the same artifact can have a Git revision, a Postgres decomposition, and a Graphiti representation without becoming three separate "things"
- memory can reference artifact anchors without owning artifact bodies
- publication and re-ingestion can update support cleanly

## Startup Stance

An agent should not boot from one giant prompt.

The startup stance is:

**policy + working memory snapshot + durable memory bundle + knowledge brief or pointers**

This means:

- policy shapes behavior
- working memory gives continuity
- durable memory gives orientation and learned context
- knowledge gives deeper evidence only when needed

## Retrieval Order

The intended retrieval order is:

1. durable-memory graph
2. linked anchor selection
3. decomposed artifact retrieval
4. canonical artifact body only when necessary

This keeps runtime retrieval bounded and prevents the system from dragging whole corpora into context too early.

## Cross-Layer Rules

The most important cross-layer rules are:

- working memory never becomes durable truth automatically
- artifact impacts can update Layer 4 immediately, but not silently rewrite Layer 5
- Layer 3 can reference artifacts, but not own their bodies
- Layer 4 can move ahead of Layer 5 only with explicit dirty-state tracking
- re-ingestion after publication must be able to reconcile stale support
- no layer should bypass Cortex contracts and write directly into another layer's store

## The Architecture In One Operational Sentence

Cortex uses policy to govern live OpenClaw sessions, compresses those sessions into a semantic checkpoint stream, promotes trusted meaning into Graphiti durable memory, keeps detailed artifact knowledge in Postgres, and preserves official source truth in Git.
