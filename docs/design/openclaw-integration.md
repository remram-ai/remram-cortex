# OpenClaw Integration

This document explains how Cortex integrates with OpenClaw after design lock.

## Boundary

OpenClaw remains the runtime shell and the chosen agentic framework.

Cortex integrates with it through:

- Layer 1 policy composition
- Layer 2 hot working-memory augmentation
- high-signal listening
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

Cortex now augments Layer 2 with:

- `QMD` as the hot working-memory retrieval substrate
- notion storage in `QMD`
- high-signal continuity and notion inputs from the Mamba stream
- policy-aware bounded context assembly

This is the locked Layer 2 posture.

It replaces the earlier passive "OpenClaw-native only" wording.

#### QMD Role

`QMD` is part of the hot working-memory surface.

It is used for:

- retrieving hot working continuity
- storing notions
- supporting tentative cross-thread continuity
- staying lightweight and fast through continuous cleanup

`QMD` should not become a shadow durable-memory system.

## High-Signal Mamba Integration

The High-Signal Mamba stream should read session activity continuously and emit a typed high-signal channel.

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

## Hooks And Boundaries

The main OpenClaw integration points remain:

- turn-end or after-turn observation
- compaction boundaries
- `/stop`
- `/reset`
- explicit checkpoints

At those boundaries, Cortex should be able to:

- emit high-signal continuity objects
- stage and clean notions in `QMD`
- reconcile candidate durable memory
- update Layer 4 operational workspaces
- schedule slower Dream work

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

- QMD as the hot Layer 2 working-memory substrate
- Graphiti as the Layer 3 durable-memory center

## Bottom Line

OpenClaw owns runtime mechanics.

Cortex adds:

- policy
- QMD-backed hot working memory
- a narrow Mamba listener
- durable-memory promotion
- operational knowledge organization

That is the clean framework-first integration posture.
