# Policy And Context

This document defines the stable product posture for Layers 1 and 2.

## Layer 1: Policy

Policy is custom.

It includes:

- role and mode composition
- tool-use policy
- approval and escalation rules
- prompt-budget discipline
- mutable preference-policy through governed workflows

Layer 1 is intentionally small.

It is behavioral truth, not a memory layer.

## Layer 2: Working Memory

OpenClaw still owns runtime sessions, transcript continuity, and execution mechanics.

Cortex augments that runtime with:

- `QMD` as the hot working-memory retrieval substrate
- notions stored directly in `QMD`
- policy-aware working-memory assembly
- a narrow High-Signal Mamba listener that emits typed high-signal events

The stable intent is:

- let OpenClaw own session continuity
- let `QMD` hold the hot notion and retrieval surface
- keep smaller-window runtime bundles viable without transcript replay by default
- keep the hot layer lean through reflection-driven cleanup

## Product Rule

The stable product contract is:

- OpenClaw owns runtime and workflow mechanics
- Cortex owns policy composition, hot-memory augmentation, and semantic continuity

That line should not be blurred casually.
