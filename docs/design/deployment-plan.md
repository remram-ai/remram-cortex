# Deployment Plan

This document records the active delivery posture for the locked Cortex architecture.

The long-term architecture still includes `Mamba`.

The important sequencing clarification is that Cortex is already valid without it.

## Long-Term Stack

The long-term stack remains:

- `OpenClaw`
- Cortex policy and integration layer
- `QMD` as the Layer 2 hot working-memory substrate
- `Graphiti`
- `Neo4j`
- `Postgres`
- `Git` when canonical artifact publication is warranted
- a narrow High-Signal `Mamba` listener added later as a real-time supercharge layer

## Phase 1: Prove The Core Spine Without Live Mamba

Phase 1 focuses on the minimum architecture needed to prove the layered model and core lifecycle.

Phase 1 includes:

- `OpenClaw`
- Cortex policy and integration layer
- `QMD` for hot working-memory retrieval and notion storage
- turn-end, session-end, and explicit-checkpoint semantic processing
- session-end reconciliation
- `Graphiti + Neo4j` for Layer 3 durable semantic memory
- `Postgres` for runtime evidence and Layer 4 operational knowledge
- basic Layer 5 canonical artifact handling when applicable
- reflection-driven `QMD` cleanup
- Layer 3 relationship-building and promotion readiness signals

Phase 1 does not require:

- live always-on `Mamba`
- continuous in-session semantic checkpoint generation

The Phase 1 rule is:

- prove the spine with boundary-triggered semantic processing first
- keep clean interfaces so `Mamba` can plug in later without architectural churn

Phase 1 should read as a complete proof surface in its own right.

## Post-Phase-1 Decision Gate

After Phase 1, evaluate whether local continuity pressure is becoming a meaningful problem.

If limited VRAM and local context pressure are causing:

- real continuity loss
- prompt bloat
- poor long-running session behavior

then `Mamba` may be pulled forward immediately as a Phase `1.5` spike.

If not, keep the planned sequencing and add `Mamba` later as a supercharge.

This is a clear fork point, not an unresolved debate.

## Phase 2: Deepen Operational Knowledge And Artifact Lifecycles

Phase 2 expands the Layer 4 and Layer 5 story.

Phase 2 includes:

- richer Layer 4 workspace handling
- budding idea workspaces spanning many threads
- stronger external reference handling
- clearer workspace and artifact category distinctions
- stronger dirty-state, redraft, and promotion flows
- Layer 3-assisted organization of Layer 4 operational work

This phase makes the Layer 4 and Layer 5 story feel real and usable.

## Phase 3: Add Mamba As Hardening And Optimization

Phase 3 introduces `Mamba` as the default always-on Layer 2-adjacent listener.

At that point, `Mamba` becomes:

- a small always-on high-signal listener
- a producer of a typed semantic channel
- an optimization layer for continuity and live-session quality
- a lower-latency signal source for working memory, notion staging, Intuition, and reflection

`Mamba` still remains narrow.

It is not:

- the general reflection engine
- the document decomposition engine
- a universal semantic subsystem

## Service Roles

### OpenClaw

- runtime shell
- sessions
- transcript continuity
- hooks
- compaction
- tool execution

### Cortex Integration Layer

- policy composition
- bounded context assembly
- turn-end and session-end semantic processing
- notion staging and cleanup rules
- Layer 3 and Layer 4 orchestration
- reflection and Dream orchestration

### QMD

- hot working-memory retrieval
- notion storage
- short-horizon cross-thread continuity under tighter retrieval rules

`QMD` must stay lean.

### Graphiti + Neo4j

- Layer 3 durable semantic memory
- concept relationships
- support
- supersession
- invalidation

### Postgres

- runtime evidence authority
- Layer 4 operational knowledge bodies
- reference summaries and links
- decomposed artifact knowledge where canonical artifacts exist
- retrieval metadata
- workflow and dirty-state fields
- retention metadata for later cold-storage migration

### Git

- canonical publication truth when canon is warranted

### Mamba Later

When Phase 3 arrives, `Mamba` adds:

- always-on Layer 2-adjacent high-signal listening
- typed semantic event production
- bounded routing into more expensive downstream work
- stronger infinite-context-like continuity for long-running sessions
- better near-time triggers and live memory quality
- better directional signal for Reflection and Dream

It does not replace deeper evidence-backed maintenance passes.

Reflection, Dream, and reconciliation still retain access to fuller evidence and evidence packages when they need real depth.

## Evidence Retention

Runtime evidence should stay hot only for a bounded recent window.

Active posture:

- keep full transcripts hot for roughly `90` to `120` days since last access
- then move them to cold storage
- keep compact metadata and semantic checkpoints hot much longer

## Bring-Up Order

### Phase 1 Bring-Up

1. `OpenClaw`
2. `Postgres`
3. `Neo4j`
4. `Graphiti`
5. Cortex integration layer
6. `QMD`
7. Git-backed canonical artifact flow when applicable

### Phase 3 Add-On

8. narrow `Mamba` listener

## MVP Simplicity Rule

The architecture should avoid unnecessary service sprawl.

That means Phase 1 explicitly excludes:

- `OpenSearch`
- a second graph system
- a second Graphiti usage pattern
- a giant separate external working-memory service
- live always-on `Mamba` by default

## Bottom Line

The deployment shape is intentionally smaller in Phase 1:

- OpenClaw at the framework center
- QMD for hot Layer 2 memory
- Graphiti + Neo4j for Layer 3
- Postgres for the operational middle
- Git only when canonical artifact publication is warranted
- boundary-triggered semantic processing instead of live Mamba

`Mamba` remains part of the long-term design, but as a later supercharge to an already-working spine unless the post-Phase-1 gate pulls it forward.
