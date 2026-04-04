# OpenClaw Integration

This document explains how Cortex integrates with OpenClaw.

## Boundary

OpenClaw remains the runtime shell.

Cortex integrates with it through:

- policy composition
- session-surface observation
- semantic checkpoint production
- durable-memory retrieval and writes
- knowledge tools

## Layer Mapping

### Layer 1: Policy

Cortex owns:

- role and mode selection
- tool policy
- approval and escalation rules
- prompt-budget discipline

OpenClaw consumes the resulting policy bundle.

### Layer 2: Working Memory

OpenClaw owns:

- sessions
- transcript continuity
- native compaction
- runtime execution state

Cortex augments Layer 2 through:

- policy-aware context assembly
- High-Signal Mamba stream production
- hooks that prepare compressed continuity ahead of compaction pressure

## High-Signal Mamba Integration

The Mamba stream should be produced from OpenClaw session evidence.

It should support:

- optimistic consumption
- on-demand consumption
- nightly consumption

It should be ready when OpenClaw needs compact continuity, rather than generated only after the prompt budget is already under stress.

## Hooks And Checkpoints

The main integration points are:

- turn-end or after-turn observation
- compaction boundaries
- `/stop`
- `/reset`
- explicit checkpoint flows

At those boundaries, Cortex should be able to:

- close the current evidence window
- emit semantic checkpoints
- stage notions
- reconcile high-signal tentative memory
- schedule slower maintenance work

## Runtime Retrieval Posture

OpenClaw should receive a bounded startup bundle:

- policy
- working-memory continuity
- compact durable-memory bundle
- knowledge pointers, not full corpora

Deeper artifact-backed knowledge should remain tool-driven.

## Implementation Rule

Do not replace OpenClaw Layer 2 mechanics unless OpenClaw itself becomes the blocker.

The default posture is:

- let OpenClaw do its thing
- hook into it cleanly
- add semantic compression and policy above it
