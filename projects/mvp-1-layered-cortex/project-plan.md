# Project Plan

## Delivery Phases

### Phase 1: Prove The Core Spine Without Live Mamba

Phase 1 proves the layered Cortex spine using boundary-triggered semantic processing.

It includes:

- policy and OpenClaw integration
- `QMD` hot working memory and notion storage
- turn-end, session-end, and explicit-checkpoint semantic processing
- `Graphiti + Neo4j` durable memory
- `Postgres` as the operational middle layer
- basic Layer 4 workspace handling
- basic Layer 5 canonical artifact handling when applicable
- reflection-driven `QMD` cleanup
- session-end reconciliation
- Layer 3 concept linking and promotion readiness signals

### Post-Phase-1 Decision Gate

After Phase 1, decide whether local continuity pressure justifies pulling `Mamba` forward.

If limited VRAM and local context pressure are causing real prompt bloat, continuity loss, or poor live-session behavior, run a Phase `1.5` `Mamba` spike.

If not, continue with the planned sequencing and leave `Mamba` deferred.

### Phase 2: Deepen Layer 4 And Layer 5

Phase 2 focuses on:

- richer Layer 4 workspace handling
- multi-thread idea incubation
- stronger external reference handling
- stronger dirty-state and redraft flows
- cleaner Layer 3-assisted organization of operational knowledge
- more complete promotion behavior toward Layer 5

### Phase 3: Add Mamba As Hardening And Optimization

Phase 3 adds `Mamba` as the default always-on high-signal listener.

It improves:

- near-time continuity compression
- always-on high-signal capture
- lower-latency semantic awareness
- cleaner live-session handling for long-running work

## Epic Mapping

- Epic 01 is Phase 1
- Epic 03 is Phase 1
- Epic 04 starts in Phase 1 and deepens in Phase 2
- Epic 05 starts in Phase 1 and deepens in Phase 2
- Epic 02 is Phase 3 by default, with an optional Phase `1.5` spike if the decision gate says it is needed

## Why This Order

- Layer 1 and Layer 2 must be stable before the system can feed good durable memory.
- Phase 1 proves the architecture with boundary-triggered semantic processing rather than live-stream elegance.
- Operational knowledge and artifact lifecycles are more valuable in the near term than early always-on Mamba.
- Layer 3 must be stable before it can help organize Layer 4.
- Phase 2 makes the Layer 4 and Layer 5 story real.
- Phase 3 optimizes and hardens the live runtime once the core spine already works.
