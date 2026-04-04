# High-Signal Debrief

## Cortex In One Sentence

Cortex is a five-layer knowledge architecture built around OpenClaw, QMD hot working memory, a narrow always-on Mamba signal stream, Graphiti plus Neo4j durable memory, Postgres operational knowledge, and Git-backed canon only when canonical publication is actually warranted.

## The Main Architectural Move

The architecture is no longer trying to force all context, memory, and artifacts through one substrate.

It now separates:

1. `Policy`
2. `Working Memory`
3. `Durable Memory`
4. `Operational Knowledge`
5. `Canonical Artifacts`

The clean authority model is:

- Layer 1 = behavioral truth
- Layer 2 = hot working continuity
- Layer 3 = durable semantic truth
- Layer 4 = operational knowledge truth
- Layer 5 = canonical publication truth

## The Chosen Stack

- `OpenClaw` is the chosen agentic framework.
- Cortex owns Layer 1 policy composition.
- `QMD` is the Layer 2 hot working-memory substrate and notion store.
- a narrow High-Signal `Mamba` listener emits a typed high-signal stream from session activity.
- `Graphiti + Neo4j` is Layer 3 durable memory.
- `Postgres` is the operational middle-layer authority.
- `Git` is used only when canonical artifact publication is warranted.

## The Biggest Locked Clarifications

- Layer 2 explicitly uses `QMD`.
- notions live in Layer 2, not in a separate Postgres-first or Graphiti-first ledger.
- Mamba is narrow by design and should not absorb broad reflection or artifact parsing work.
- Layer 3 remains one Graphiti memory system.
- Layer 4 is the operational knowledge authority.
- Layer 5 is only canonical publication truth when applicable.
- `OpenSearch` is not part of the active stack.

## The Main Runtime Story

1. OpenClaw runs the session.
2. QMD supports hot working-memory retrieval and notion storage.
3. the Mamba listener continuously emits typed high-signal events from session activity.
4. those signals can update notions, oversight, and bounded continuity.
5. reflection uses Layer 3 relationships to help organize Layer 4 workspaces.
6. high-value meaning promotes into Graphiti durable memory when warranted.
7. Dream does slower consolidation and promotion readiness work.

## The Main Workspace Story

A budding idea can span many threads.

That is not a bug to hand-wave away.

The architecture solves it like this:

- Layer 3 identifies that many threads belong to the same emerging concept
- Layer 4 holds the evolving workspace body for that concept
- Layer 5 only becomes relevant if the work is ready for canonical publication

This is the medium-horizon operational space that earlier versions of the architecture underdefined.

## The Main Artifact Story

Not all operational knowledge bodies are canonical artifacts.

Layer 4 can hold:

- working or incubation workspaces
- external reference material
- authored operational artifact bodies

Layer 5 only exists when publication-grade canon is warranted.

External references do not automatically become Git-backed canonical artifacts.

## What Layer 3 Does For Layer 4

Layer 3 helps Layer 4 organize itself.

It can represent:

- same emerging idea
- related workspace
- supporting reference
- supersedes
- candidate for promotion

The bodies remain in Layer 4.

The conceptual relationship network remains in Layer 3.

## Why QMD Matters

QMD is the pragmatic hot-memory choice inside the OpenClaw-centered stack.

It gives Cortex:

- hot retrieval
- notion storage
- tentative cross-thread continuity under tighter rules
- a Layer 2 memory surface that can be kept lean through reflection cleanup

## Why Mamba Matters

Mamba is not a broad semantic engine.

It is:

- a small always-on listener
- a high-signal producer
- a bounded trigger surface for downstream systems

It should stay narrow.

## Why Postgres Matters

Postgres is not just a decomposition database.

It is the operational middle-layer authority for:

- runtime evidence
- Layer 4 bodies
- reference records and summaries
- decomposed artifact knowledge where canonical artifacts exist
- metadata
- workflow state

This is why the architecture avoids `OpenSearch` for now.

## The Most Important Exclusions

The active design explicitly avoids:

- OpenSearch in the near-term stack
- a second Graphiti usage pattern
- pushing budding ideas into Git too early
- treating external references like authored canonical artifacts
- making Mamba a universal reasoning engine

## Bottom Line

The architecture is now cleaner:

- OpenClaw at the framework center
- QMD for hot working continuity and notions
- Graphiti for durable semantic truth
- Postgres for operational knowledge truth
- Git only for canonical publication when that is actually needed
