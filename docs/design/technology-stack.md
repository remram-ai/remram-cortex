# Technology Stack

This document records the active Cortex stack after design lock.

It is not a comparison memo.

It describes the stack the repository is being organized around and the sequencing posture for implementing it.

## Long-Term Stack

The long-term stack is:

- `OpenClaw` as the chosen agentic framework
- Cortex-owned Layer 1 policy composition
- `QMD` for Layer 2 hot working memory and notions
- a narrow High-Signal `Mamba` stream as a later Layer 2 supercharge
- `Graphiti + Neo4j` for Layer 3 durable semantic memory
- `Postgres` as the operational middle-layer authority
- `Git` for Layer 5 canonical artifacts when publication-grade canon is actually warranted

## Delivery Sequencing

The base architecture is complete without live `Mamba`.

The sequencing choice is:

- Phase 1 proves the spine without live `Mamba`
- Phase 1 uses turn-end, session-end, and explicit-checkpoint semantic processing
- after Phase 1 there is a simple decision gate for a possible Phase `1.5` `Mamba` spike
- otherwise Phase 3 adds `Mamba` as a supercharge rather than a missing dependency

This is a sequencing choice, not an architecture reversal and not a sign that the stack is waiting to become valid later.

## Why This Stack

### OpenClaw

`OpenClaw` is the chosen agentic framework for Remram.

That means the selection logic is:

- build around OpenClaw as the framework center
- prefer native OpenClaw patterns when they are good enough
- add Cortex memory and knowledge behavior around that boundary

OpenClaw remains responsible for:

- runtime execution
- sessions
- transcript continuity
- hooks
- compaction

### Policy In Cortex

Layer 1 remains custom because Cortex-specific behavior lives there.

It owns:

- role and mode composition
- approval posture
- escalation posture
- prompt-budget discipline
- mutable preference-policy

Hard runtime and tool-use enforcement should remain as close as possible to OpenClaw agent or plugin configuration.

### QMD In Layer 2

`QMD` is now the explicit Layer 2 hot working-memory substrate.

It is used for:

- hot working-memory retrieval
- notion storage
- fast cross-thread continuity under tighter retrieval rules
- short-horizon continuity around the OpenClaw session surface

This is not a giant new memory architecture.

It is the pragmatic hot-memory choice inside an OpenClaw-centered stack.

### Semantic Processing Before Mamba

Phase 1 still needs semantic processing.

It just does not need an always-on listener yet.

Phase 1 uses:

- turn-end extraction
- session-end extraction
- explicit-checkpoint extraction when needed

Those hooks should survive into later phases.

When `Mamba` arrives, it augments those hooks instead of replacing them.

### High-Signal Mamba Stream Later

The Mamba stream remains narrow by design.

It is:

- a small always-on listener
- a typed high-signal channel
- a Layer 2-adjacent signal producer

It is not:

- a universal reflection engine
- the document decomposition engine
- a general-purpose semantic authority

Its role is to supercharge:

- infinite-context-like continuity without claiming literal infinite recall
- near-time continuity compression
- always-on high-signal capture
- lower-latency semantic awareness
- cleaner live-session handling for long-running work

It also gives Reflection and Dream better directional signal and better candidate surfaces.

It does not change the authority model.

Reflection and Dream still retain access to fuller evidence and evidence packages for deeper passes.

When `Mamba` exists, Cortex can add `Intuition` on top of that stream.

`Intuition` is the later signal evaluator that decides when high-signal windows should wake hotter layered ingestion or opportunistic GPU-backed processing.

The important line is:

- the spine already works without `Mamba`
- `Mamba` improves the quality and timeliness of signal flowing through that same spine
- deeper reflection, Dream, and reconciliation still use fuller evidence when needed

### Graphiti + Neo4j

Layer 3 stays centered on `Graphiti + Neo4j` because it gives:

- durable semantic memory
- temporal lineage
- support relationships
- invalidation and supersession
- concept and identity relationships across threads and workspaces

There is only one Graphiti memory system.

It is used for normal durable-memory behavior, including concept clustering and workspace relationship mapping.

### Postgres

`Postgres` remains the practical operational middle-layer authority.

It covers:

- policy and control data
- runtime evidence
- Layer 4 operational knowledge bodies
- incubation workspaces
- reference summaries and links
- decomposed artifact knowledge where canonical artifacts exist
- retrieval metadata
- workflow and dirty-state fields

This is not being justified as the final winner for document retrieval in the abstract.

It is being chosen because it keeps the near-term service count lower and covers the mixed operational middle of the stack well enough.

### Git

`Git` remains the Layer 5 canonical publication surface when publication-grade artifacts are warranted.

It should not be treated as the default destination for every useful idea or every external reference.

## What Is Not In The Active Stack

The active stack explicitly excludes:

- `OpenSearch`
- a second graph system
- a second Graphiti usage pattern
- a separate giant external working-memory service

`OpenSearch` may remain a future option if artifact retrieval becomes dominant enough to justify it, but it is not part of the current architecture or MVP.

## Stack Summary

The active rule is:

- let OpenClaw own runtime mechanics
- let `QMD` own hot working-memory retrieval and notions
- let Phase 1 prove the spine with boundary-triggered semantic processing
- let `Mamba` arrive later as a narrow supercharge to an already-working design
- let Graphiti own durable semantic memory
- let Postgres own the operational middle
- let Git own canonical publication only when canon is warranted
