# Layered Memory Architecture

## Purpose

This document defines the locked layered architecture for Remram Cortex.

The architecture is no longer trying to force runtime continuity, durable memory, operational knowledge, and canonical artifacts through one substrate.

It is now organized around five explicit layers with sharper authority boundaries and cleaner lifecycle rules.

The governing phrase remains:

**one authority, multiple memory surfaces**

More precisely:

**Cortex is one knowledge authority coordinating five layers that each own a different kind of truth.**

## Executive Summary

The active layer model is:

1. `Policy`
2. `Working Memory`
3. `Durable Memory`
4. `Operational Knowledge`
5. `Canonical Artifacts`

Those layers now have explicit authority boundaries:

- Layer 1 owns behavioral truth
- Layer 2 owns hot working continuity
- Layer 3 owns durable semantic truth
- Layer 4 owns operational knowledge truth
- Layer 5 owns canonical publication truth

This architecture is designed to support:

- live bounded runtime work
- cross-thread continuity without pretending it is already trusted truth
- durable semantic memory with lineage and supersession
- medium-horizon evolving workspaces that span many threads
- clean separation between operational knowledge and canonical publication
- fewer standing services and less architecture tax

## OpenClaw Selection Principle

`OpenClaw` was not chosen because Cortex compared orchestrators and decided it was the abstract best chat shell.

It was chosen because it is the agentic framework Remram intends to build around.

That means the architectural rule is:

- do things the OpenClaw way when that path is good enough
- extend OpenClaw cleanly before replacing it
- treat memory and knowledge as add-ons to the framework boundary, not as the reason to swap frameworks

## Layer Model

### Layer 1: Policy

Layer 1 is custom policy.

It is intentionally small compared with the broader operational knowledge surfaces.

It owns:

- role and mode composition
- tool-use rules
- approval and escalation posture
- prompt-budget discipline
- mutable preference-policy through governed workflows

Layer 1 is not a memory layer.

Hard runtime and workflow enforcement should stay as close as possible to OpenClaw agent or plugin configuration.

Cortex policy should focus on:

- composition
- routing
- approval posture
- preference-policy
- prompt-budget discipline

### Layer 2: Working Memory

Layer 2 is the hot working-memory layer.

It remains anchored on OpenClaw runtime sessions, transcript continuity, and execution mechanics.

The locked design change is:

- Layer 2 uses `QMD` as the hot working-memory retrieval substrate
- notions live in `QMD`
- `QMD` is part of the hot working-memory surface
- `QMD` must be kept lean through continuous cleanup

Layer 2 owns:

- live continuity
- hot retrieval over recent session and related thread context
- current task and handoff state
- transient working memory objects
- notions before they are reconciled into Layer 3

Layer 2 does not own durable truth.

It is allowed to be:

- fast
- lossy
- mutable
- aggressively pruned

#### QMD Role

`QMD` is not a giant second memory architecture.

It is the pragmatic hot-memory choice inside the OpenClaw-centered stack.

The reason to choose it explicitly is:

- it stays within the OpenClaw posture
- it gives a better working-memory retrieval surface than the builtin engine
- it is a natural home for notions and other hot continuity objects

#### Notions In Layer 2

A notion is a staged candidate durable memory.

In the locked design, notions are physically part of the Layer 2 hot working-memory surface through `QMD`.

They should be:

- fast to retrieve
- fast to expire
- fast to merge
- fast to invalidate
- visible cross-thread only under tighter rules

They are not silently authoritative durable memory.

#### Mamba In Layer 2

`Mamba` is narrow by design.

In the long-term architecture, it is:

- a small always-on listener
- a Layer 2-adjacent high-signal producer
- a stream that reads session activity and emits a typed high-signal channel

It is not:

- a universal reflection engine
- the document decomposition engine
- a broad semantic authority

Its job is to keep a narrow, continuous, high-signal stream available for downstream consumers.

Sequencing clarification:

- Phase 1 does not require live Mamba
- Phase 1 uses turn-end, session-end, and explicit-checkpoint semantic processing
- after Phase 1 there is a decision gate for a possible Phase `1.5` Mamba spike
- otherwise Mamba remains deferred until Phase 3

When Mamba arrives, it augments those hooks rather than replacing them.

#### Reflection And Layer 2 Cleanup

Reflection is allowed to maintain the health of Layer 2.

That includes:

- pruning notions
- merging notions
- demoting stale notions
- expiring low-value notions
- keeping `QMD` lean and fast

This is a first-class part of the architecture, not an afterthought.

### Layer 3: Durable Memory

Layer 3 is the durable semantic authority.

It is implemented as one `Graphiti` memory system on `Neo4j`.

There is no second Graphiti and no separate "concept mapping graph."

Layer 3 naturally owns:

- concepts
- identities
- relationships
- support
- supersession
- invalidation
- continuity across threads and sessions

Layer 3 stores:

- durable concepts
- stable relationships
- semantic continuity
- support and provenance links
- promotion readiness signals
- concept-level clustering and identity

Layer 3 does not store:

- transcript bodies
- workspace bodies
- document bodies
- full operational knowledge content

Hard rule:

**Layer 3 stores concepts and semantic relationships, not whole content bodies.**

#### One Graphiti Memory System

This means `Graphiti` can naturally represent:

- several threads belonging to one budding business idea
- several workspaces being related or merged
- one draft superseding another
- certain references supporting a concept
- a workspace becoming a candidate for promotion

Useful type distinctions inside Layer 3 may include:

- `concept`
- `idea_cluster`
- `workspace_anchor`
- `artifact_anchor`
- `reference_anchor`

These are not separate subsystems.

They are type distinctions inside one Layer 3 graph.

#### Trust Model

Graphiti gives the architecture:

- lineage
- support
- point-in-time semantics
- invalidation
- supersession

Cortex should keep a minimal trust overlay on top of that:

- `tentative`
- `low_confidence`
- `active`
- `superseded`
- `invalidated`
- `stale_support`

Do not build a giant second semantic system on top of Graphiti.

### Layer 4: Operational Knowledge

Layer 4 is the operational knowledge authority.

This is a major locked clarification.

Layer 4 is not merely a projection of Layer 5.

It is authoritative for operational content.

That means:

- if there is no Layer 5 artifact, Layer 4 is the authority for that content
- if there is a Layer 5 artifact, Layer 4 is still the operational authority for active work and retrieval
- Layer 5 is only the canonical publication authority when applicable

Layer 4 is authoritative for:

- evolving idea workspaces
- working synthesis bodies
- reference-derived knowledge bodies
- decomposed artifact knowledge
- active operational document state
- incubation workspaces that span many threads

Layer 4 is not authoritative for durable semantic conclusions about that content.

Those belong in Layer 3.

#### Classes Inside Layer 4

Layer 4 should explicitly support at least three operational content classes:

1. `working/incubation workspaces`
2. `external reference material`
3. `authored artifact knowledge`

Not all Layer 4 bodies have a Layer 5 counterpart.

That is expected.

#### Medium-Horizon Workspace

The architecture now treats the medium workspace as first-class.

A spark of an idea may begin as a sentence and evolve across many threads.

That medium-horizon body is:

- larger than Layer 3
- less formal than Layer 5
- incomplete
- unstable
- evolving

That space belongs in Layer 4.

Layer 3 helps identify that many threads belong to the same emerging concept.

Layer 4 holds the evolving workspace body for that concept.

Layer 5 only becomes relevant when the work is ready for canonical publication.

#### External Reference Material

External reference material is distinct from authored canonical artifacts.

Examples:

- podcast transcripts
- uploaded PDFs used as references
- external articles
- factual sources
- research materials the user does not own

These should not automatically become Git-backed canonical artifacts.

Instead:

- Layer 4 may hold summaries, linked reference records, extracted operational knowledge, and retrieval-ready material
- Layer 3 stores only durable meaning that actually matters
- the system may later ask whether a valuable reference should be retained more intentionally

This is a category distinction inside the operational knowledge model, not a sixth layer.

### Layer 5: Canonical Artifacts

Layer 5 is canonical publication truth when publication-grade authorship and revision are needed.

It is not the default destination for every useful idea.

It exists for:

- authored canonical artifacts
- reviewable revisions
- publication-grade bodies
- Git-backed or provider-backed canonical truth

Budding ideas do not jump straight to Git.

Layer 5 is only used when canonical publication is actually warranted.

## Authority Boundaries

The clean authority model is:

- Layer 1 = behavioral truth
- Layer 2 = hot working continuity
- Layer 3 = durable semantic truth
- Layer 4 = operational knowledge truth
- Layer 5 = canonical publication truth

This is the main architecture rule to protect.

### Cross-Layer Authority Rules

1. Layer 2 may surface tentative continuity and notions, but it does not become durable truth automatically.
2. Layer 3 may organize and connect workspaces, but it does not own their bodies.
3. Layer 4 may move fast and be operationally authoritative, but it does not silently replace Layer 5 when canonical publication exists.
4. Layer 5 is canonical only when there is a publication-grade artifact to own.

## Storage And Service Posture

The long-term stack is:

- `OpenClaw`
- Cortex policy layer
- `QMD` for Layer 2 hot working memory and notions
- narrow High-Signal `Mamba` stream
- `Graphiti + Neo4j` for Layer 3
- `Postgres` for the operational middle of the stack
- `Git` when canonical artifact publication is warranted

## Implementation Sequencing

### Phase 1

Phase 1 proves the layered spine without live Mamba.

It uses:

- turn-end semantic processing
- session-end semantic processing
- explicit-checkpoint semantic processing when needed

### Post-Phase-1 Decision Gate

After Phase 1, evaluate whether local continuity pressure is becoming a real problem.

If limited VRAM and local context pressure are causing continuity loss, prompt bloat, or poor live-session behavior, Mamba may be pulled forward as a Phase `1.5` spike.

If not, Mamba remains deferred.

### Phase 2

Phase 2 deepens Layer 4 workspaces, external reference handling, and Layer 4 to Layer 5 lifecycle behavior.

### Phase 3

Phase 3 adds Mamba as the default always-on narrow high-signal listener.

### Postgres As Middle-Layer Authority

`Postgres` remains the practical operational substrate for the middle of the stack.

It should cover:

- Layer 1 policy and control data
- runtime evidence authority
- Layer 4 operational knowledge bodies
- incubation workspaces
- reference summaries and links
- decomposed artifact knowledge
- retrieval metadata
- dirty-state and workflow fields

No `OpenSearch` for now.

That is explicit.

Do not design around a standing `OpenSearch` service.

The architecture should center on fewer moving pieces.

## Identity And Relationship Model

One stable Cortex identity should still exist across layers.

That identity usually begins with an `anchor_id`.

Useful anchor and concept distinctions now include:

- `concept`
- `idea_cluster`
- `workspace_anchor`
- `artifact_anchor`
- `reference_anchor`

Layer 3 may use these distinctions to express:

- same emerging idea
- related workspace
- supporting reference
- supersedes
- candidate for promotion

Layer 4 may receive lightweight connector fields from that process, for example:

- `idea_cluster_id`
- `related_workspace_ids`
- `candidate_for_promotion`
- `promotion_readiness`

The bodies remain in Layer 4.

The conceptual relationship network remains in Layer 3.

## Lifecycles

### Flow 1: Live Session To Layer 2

1. OpenClaw runs the session.
2. The transcript and runtime events remain the evidence surface.
3. `QMD` provides hot working-memory retrieval and notion storage.
4. turn-end, session-end, and explicit-checkpoint processing emit typed semantic outputs.
5. Layer 2 continuity is assembled from session state, `QMD`, and those outputs.
6. later, Mamba can improve this same flow by providing a better always-on signal source.

### Flow 2: Layer 2 To Layer 3

1. boundary-triggered semantic processing contributes to a notion in `QMD`
2. the notion is queryable for continuity and cross-thread use under tighter rules
3. reflection evaluates the notion against evidence and current semantic structure
4. high-value meaning is promoted into Layer 3 when warranted
5. stale or low-value notions are pruned or demoted

### Flow 3: Many Threads To One Emerging Idea

1. several chat threads contain fragments of one emerging concept
2. Layer 3 identifies that they belong to the same idea cluster or concept relationship network
3. Layer 4 holds the evolving workspace body for that idea
4. reflection and Dream use Layer 3 relationships to keep that workspace organized
5. if the workspace matures, it may become a candidate for canonical publication

This is a core problem the architecture is explicitly designed to solve.

### Flow 4: External Reference Material

1. an external source is introduced
2. Layer 4 stores summaries, linked reference records, extracted operational knowledge, and retrieval-ready material
3. Layer 3 stores only durable meaning that matters
4. the reference may later be retained more intentionally, but it does not automatically become a canonical artifact

### Flow 5: Working Workspace To Canonical Artifact

1. a Layer 4 workspace matures
2. Layer 3 relationships and support indicate promotion readiness
3. a redraft or publication workflow is initiated
4. Layer 5 receives the canonical artifact only when publication-grade authorship is warranted
5. once promoted, Layer 5 becomes the canonical source for that artifact
6. later meaningful Layer 5 revisions can trigger re-ingestion back into Layer 4
7. Layer 3 support, summaries, and semantic links are then reconciled as needed

## Reflection And Dream

### Reflection

Reflection is the near-time path.

It is allowed to:

- stage and update notions
- prune and merge notions in `QMD`
- demote stale notions
- keep Layer 2 lean
- update Layer 4 operational workspaces
- use Layer 3 concept relationships to organize Layer 4 workspaces
- detect early promotion candidates

### Dream

Dream is the slower consolidation path.

It is allowed to:

- revisit Layer 3 concept relationships more deeply
- consolidate or merge idea clusters
- identify whether multiple workspaces should merge
- identify whether a workspace is ripening into a promotion candidate
- harden support, supersession, and invalidation

Both Reflection and Dream use Layer 3 to help organize Layer 4.

Neither should turn Layer 3 into a shadow document store.

## Service Simplicity

Reducing unnecessary service count is an explicit design goal.

That is why:

- `OpenSearch` is excluded for now
- the architecture does not assume a standing extra projection service
- the operational middle of the stack stays centered on `Postgres`

## Hot And Cold Evidence

Runtime evidence should stay hot only for a bounded recent window.

Locked retention posture:

- keep full transcripts hot for roughly `90` to `120` days since last access
- then move them to cold storage
- keep compact metadata and semantic checkpoints hot much longer

Layer 3 durable memory and Layer 4 operational knowledge should not depend on raw transcript bodies staying hot forever.

## What The Architecture Explicitly Avoids

The revised architecture explicitly avoids:

- passive Layer 2 with no chosen hot-memory substrate
- using Mamba as a broad semantic engine
- treating Layer 4 as only a projection of Layer 5
- pushing budding ideas into Git too early
- treating external references like authored canonical artifacts
- introducing `OpenSearch` into the near-term stack
- creating a second Graphiti usage pattern or shadow graph

## The 10 Design-Lock Answers

### 1. Do we explicitly choose QMD as the Layer 2 memory engine for MVP 1, or keep it as preferred if needed?

Choose `QMD` explicitly for Layer 2 hot working memory and notions.

### 2. Where does the notion ledger live physically?

In `QMD` as part of the Layer 2 hot working-memory surface.

It is not a separate Postgres-first ledger and not a separate Graphiti-first ledger.

### 3. What are the exact retrieval rules for tentative cross-thread memory?

Tentative cross-thread memory is allowed under tighter retrieval rules, but it is not silently authoritative before reconciliation.

It may guide continuity, but high-impact conclusions still depend on reconciliation and stronger evidence.

### 4. Is Layer 4 staying Postgres + pgvector first, with OpenSearch additive later, or do we want to start with both now?

No `OpenSearch` for now.

`Postgres` remains the operational middle-layer authority for MVP.

Do not introduce `OpenSearch` into the active stack yet.

### 5. What is the hot-to-cold evidence retention policy?

Keep full transcripts hot only for a bounded recent window, roughly `90` to `120` days since last access, then move them to cold storage.

Keep compact metadata and semantic checkpoints hot much longer.

### 6. How explicit do we want the Cortex trust model to be on top of Graphiti?

Keep the trust model minimal.

Use the established memory states and avoid inventing a giant second semantics system.

Optional per-edge or per-support confidence signals are acceptable if they stay lightweight.

### 7. What is the canonical artifact lineage schema in Graphiti?

Use stable anchor identity and pointer-based relationships.

Graphiti should represent concept relationships, support, supersession, and links to workspaces or artifacts, but not become a document body store.

### 8. How hard is the split between OpenClaw config and Cortex policy?

Keep the split hard.

OpenClaw owns runtime and workflow mechanics.

Cortex owns memory, policy composition, reconciliation, and governed preference-policy behavior.

### 9. What exactly is “Mamba” in implementation terms?

Mamba is a narrow always-on Layer 2 listener that emits a high-signal stream from session activity.

It is not a general artifact parser or universal semantic subsystem.

It is deferred by default for sequencing reasons, not removed from the architecture.

### 10. What is in MVP 1 versus intentionally deferred?

MVP 1 includes:

- `OpenClaw`
- Cortex policy layer
- `QMD` hot working memory
- boundary-triggered semantic processing
- `Graphiti + Neo4j` durable memory
- `Postgres` operational middle layer
- `Git` canonical artifacts when applicable

`OpenSearch` is deferred.

`Mamba` is deferred by default and may be pulled forward as a Phase `1.5` spike if the post-Phase-1 gate says continuity pressure justifies it.

Additional service expansion is deferred.
