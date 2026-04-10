# OpenClaw Integration

This document explains how Cortex integrates with OpenClaw after design lock.

## Boundary

OpenClaw remains the runtime shell and the chosen agentic framework.

Cortex integrates with it through:

- Layer 1 policy composition
- Layer 2 hot working-memory augmentation
- boundary-triggered semantic processing in early phases
- Layer 3 durable-memory retrieval and promotion
- Layer 4 and Layer 5 knowledge tooling

The architectural rule is:

- do things the OpenClaw way when that path is good enough
- extend OpenClaw cleanly before replacing it

## Live Appliance Authority

For live Moltbox appliance behavior, `moltbox-gateway` is the source of truth.

That means:

- the managed service inventory
- the public `moltbox` CLI contract
- restricted-operator verification surfaces
- snapshot-first recovery behavior
- the current web baseline

should be taken from the Gateway repo, not inferred from older Cortex notes.

In practice:

- `test` is the proving lane
- `prod` is a protected managed pet
- normal service-plane mutation uses `moltbox service ...`
- normal runtime mutation uses native `moltbox test|prod openclaw ...`
- routine validation should prefer `moltbox test verify runtime|web` and `moltbox prod verify runtime`
- raw Docker and break-glass SSH are not the normal path when the operator surface can do the job
- the intended web baseline is `web_search` + built-in `web_fetch`
- native `memory-core` is disabled in the default local lane
- the old Playwright detour is not the intended baseline

The current service inventory is the live baseline, not a permanent ceiling.

If Cortex needs additional services such as `Postgres`, `Neo4j`, `Graphiti`, or a Cortex service boundary, those services should be introduced through:

- tracked baseline service-definition changes in `moltbox-services`
- promoted runtime-layer changes in `moltbox-runtime` when runtime behavior changes
- official Gateway documentation updates only when the operator-facing contract or workflow changes
- normal `moltbox` deployment and validation paths

This document can still describe the intended Cortex integration seam, but it does not override the current live appliance contract.

## Layer Mapping

### Layer 1: Policy

Cortex owns:

- role and mode composition
- approval and escalation posture
- prompt-budget discipline
- mutable preference-policy

OpenClaw should own:

- hard runtime-safe defaults
- hard workflow mechanics
- hard tool-use enforcement where possible

This split should stay hard.

### Layer 2: Working Memory

OpenClaw still owns:

- sessions
- transcript continuity
- compaction
- runtime execution state

Cortex augments Layer 2 with:

- `QMD` as the hot working-memory retrieval substrate
- notion storage in `QMD`
- policy-aware bounded context assembly
- semantic processing hooks that run at turn end, session end, and explicit checkpoints

That is the post-baseline Cortex posture.

It replaces the earlier passive "OpenClaw-native only" wording without requiring live Mamba on day one.

The key posture is that this Layer 2 design is already real and useful before `Mamba` exists, and even before Cortex adds its own loops on top of the Phase 0 baseline.

#### QMD Role

`QMD` is part of the hot working-memory surface.

It is used for:

- retrieving hot working continuity
- storing notions
- supporting tentative cross-thread continuity
- supporting reranking and query expansion in the OpenClaw memory surface
- supporting optional session-transcript indexing when that experimental posture is deliberately enabled
- staying lightweight and fast through continuous cleanup

`QMD` should not become a shadow durable-memory system.

Phase 0 should treat `QMD` as a real baseline component rather than a later optimization.

That means:

- enable `QMD`
- keep pruning and compaction on
- use the OpenClaw-native fallback posture rather than inventing a second working-memory stack on day one
- treat session-transcript indexing as an explicit choice rather than silently assuming it in baseline config

## Semantic Processing Before Mamba

Phases 1 through 4 still need semantic outputs.

It just produces them at boundaries instead of through a continuously running listener.

The main OpenClaw integration points remain:

- turn-end or after-turn observation
- compaction boundaries
- `/stop`
- `/reset`
- explicit checkpoints

At those boundaries, Cortex should be able to:

- emit typed semantic outputs
- stage and clean notions in `QMD`
- reconcile candidate durable memory
- update Layer 4 operational workspaces
- schedule slower Dream work

These hooks should remain even after Mamba arrives.

## High-Signal Mamba Integration Later

The High-Signal Mamba stream is still part of the long-term architecture.

It is:

- narrow
- always-on
- Layer 2-adjacent

It is not:

- a general reflection engine
- the document decomposition engine
- the broad artifact interpreter

The preferred implementation pattern is:

- a small continuous sensor
- plus a larger writer or reasoning model only when bounded high-signal windows justify it

Delivery posture:

- Phase 0 establishes vanilla OpenClaw with `QMD`
- Phases 1 through 4 use boundary-triggered semantic processing
- Mamba lands in Phase 5 as hardening, optimization, and continuity supercharge

When it arrives, it improves:

- infinite-context-like live continuity
- near-time triggers
- live memory quality
- directional signal for Reflection and Dream

When `Mamba` exists, Cortex can add `Intuition` as a narrow evaluator on top of the stream.

Its role is to queue opportunistic high-signal processing while GPU headroom exists instead of waiting only for session-end or batch windows.

It does not replace fuller evidence in deeper maintenance passes.

Reflection, Dream, and reconciliation still retain access to fuller evidence and evidence packages when deeper work is required.

## Runtime Retrieval Posture

OpenClaw should receive a bounded startup bundle:

- policy
- Layer 2 hot continuity
- compact Layer 3 durable-memory orientation
- Layer 4 knowledge pointers or briefs

It should not receive:

- full transcript replay by default
- whole workspace bodies by default
- full artifact bodies by default

Deeper knowledge remains tool-driven or deliberate.

## Dreaming And Other OpenClaw Memory Features

OpenClaw features like `Dreaming` are relevant as adjacent concepts and may inform cadence or UX.

They are not the center of Cortex durable memory.

Cortex still treats:

- `QMD` as the hot Layer 2 working-memory substrate
- Graphiti as the Layer 3 durable-memory center

## Bottom Line

OpenClaw owns runtime mechanics.

Cortex adds:

- policy
- `QMD`-backed hot working memory
- boundary-triggered semantic processing in early phases
- durable-memory promotion
- operational knowledge organization

Mamba arrives later as a narrow supercharge layer, not as the prerequisite for proving the architecture.

For live appliance work, Cortex should fit itself into the current Moltbox operator contract first and only broaden that contract through explicit Gateway changes when necessary.
