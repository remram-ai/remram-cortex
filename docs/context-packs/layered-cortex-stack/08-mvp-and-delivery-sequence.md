# MVP And Delivery Sequence

## Delivery Posture

The long-term architecture still includes `Mamba`.

The sequencing change is that `Mamba` is no longer required to prove the MVP spine, and the MVP should not read as if it is waiting on `Mamba` to become real.

Phase 1 proves the layered Cortex spine using boundary-triggered semantic processing.

## Phase 1: Prove The Core Spine Without Live Mamba

Phase 1 includes:

- `OpenClaw`
- Cortex policy layer
- `QMD` hot working memory
- notion storage in `QMD`
- turn-end and session-end semantic processing
- checkpoint-triggered semantic processing when needed
- session-end reconciliation
- `Graphiti + Neo4j` durable memory
- `Postgres` operational middle layer
- Layer 4 operational knowledge authority
- basic Layer 5 canonical artifact handling when applicable
- cross-thread concept linking through Layer 3
- reflection-driven `QMD` cleanup
- promotion readiness signals for eventual Layer 5 publication

Phase 1 does not require:

- live always-on `Mamba`
- continuous semantic checkpoint generation during the session

## Post-Phase-1 Decision Gate

After Phase 1, ask one simple question:

Is limited VRAM and local context pressure causing real continuity problems, prompt bloat, or poor live-session behavior?

- If yes, pull `Mamba` forward immediately as a Phase `1.5` spike.
- If no, keep the planned sequencing and add `Mamba` later as a supercharge.

This is a clear fork point, not an unresolved debate.

## Phase 2: Deepen Layer 4 And Layer 5

Phase 2 focuses on:

- richer Layer 4 workspace handling
- budding idea workspaces that span many threads
- stronger external reference handling
- stronger promotion lifecycle from Layer 4 to Layer 5
- better dirty-state and redraft flows
- cleaner operational knowledge organization driven by Layer 3 relationships
- clearer workspace and artifact category distinctions

This phase makes the Layer 4 and Layer 5 story feel real and usable.

## Phase 3: Add Mamba As Hardening And Optimization

Phase 3 introduces `Mamba` as the default always-on narrow high-signal listener.

At that point, `Mamba` improves:

- near-time continuity compression
- always-on high-signal capture
- lower-latency semantic awareness
- cleaner live-session handling for long-running work
- better directional signal for Reflection and Dream

At that point, Cortex can also add `Intuition` as a Mamba-side evaluator that queues opportunistic high-signal processing while GPU headroom exists.

`Mamba` still remains narrow.

It is not:

- a universal reasoning engine
- the reflection engine
- the document decomposition engine

## What Stays Locked

The core architecture decisions still stand:

1. `QMD` is the Layer 2 hot working-memory substrate and notion store.
2. Tentative cross-thread memory is allowed under tighter retrieval rules but is not silently authoritative before reconciliation.
3. `Postgres` remains the operational middle-layer authority.
4. `OpenSearch` is still deferred.
5. `Graphiti + Neo4j` remains the Layer 3 durable memory system.
6. Layer 4 remains the operational knowledge authority.
7. Layer 5 remains canonical publication truth only when canon is warranted.

## Bottom Line

The sequencing now reads:

- Phase 1 proves the layered spine with boundary-triggered semantic processing
- then there is a decision gate for a possible Phase `1.5` `Mamba` spike
- Phase 2 deepens workspaces and artifact lifecycles
- Phase 3 adds `Mamba` for optimization, hardening, and live-continuity supercharge by default
