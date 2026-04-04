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

That is the Phase 1 posture.

It replaces the earlier passive "OpenClaw-native only" wording without requiring live Mamba on day one.

The key posture is that this Layer 2 design is already real and useful before `Mamba` exists.

#### QMD Role

`QMD` is part of the hot working-memory surface.

It is used for:

- retrieving hot working continuity
- storing notions
- supporting tentative cross-thread continuity
- staying lightweight and fast through continuous cleanup

`QMD` should not become a shadow durable-memory system.

## Semantic Processing Before Mamba

Phase 1 still needs semantic outputs.

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

- Phase 1 proves the spine without Mamba
- after Phase 1 there is a decision gate for a possible Phase `1.5` spike
- otherwise Mamba lands in Phase 3 as hardening, optimization, and continuity supercharge

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
