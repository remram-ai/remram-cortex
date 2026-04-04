# Policy, OpenClaw, And Working Memory

## The Main Decision

Layer 1 remains custom.

Layer 2 now explicitly uses `QMD`.

OpenClaw remains the chosen framework and still owns runtime sessions, transcript continuity, compaction, and execution mechanics.

## Layer 1

Layer 1 owns:

- role and mode composition
- tool-use rules
- approval posture
- escalation posture
- prompt-budget discipline
- mutable preference-policy

The split with OpenClaw should stay hard:

- hard runtime-safe and workflow enforcement in OpenClaw config
- policy composition and preference-policy in Cortex

## Layer 2

Layer 2 is hot working continuity.

Its substrate is:

- OpenClaw sessions
- `QMD`

QMD now explicitly owns:

- hot working-memory retrieval
- notion storage
- tentative continuity across threads under tighter rules

## Why QMD

QMD is the practical hot-memory choice because it stays within the OpenClaw-centered posture while giving Cortex a better Layer 2 retrieval surface.

It should stay:

- light
- fast
- continuously cleaned up

It should not become a shadow durable-memory system.

## Notions

Notions live in QMD.

They are:

- hot candidate durable memories
- source-linked
- fast to merge
- fast to prune
- not silently authoritative

They are allowed to support continuity and tentative cross-thread retrieval, but they still need reconciliation before becoming Layer 3 truth.

## Mamba In This Layer

Mamba is the always-on high-signal listener.

It is:

- narrow
- typed
- continuous

It is not:

- the reflection engine
- the artifact parser
- the broad semantic engine

## Cleanup

Reflection is explicitly allowed to keep QMD healthy.

That includes:

- pruning notions
- merging notions
- demoting stale notions
- expiring low-value notions

This is a designed part of Layer 2, not just operational hygiene.
