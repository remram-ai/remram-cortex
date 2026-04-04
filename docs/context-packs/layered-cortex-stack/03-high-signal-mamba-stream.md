# High-Signal Mamba Stream

## The Main Sequencing Clarification

`Mamba` is part of the long-term design, but the architecture is already valid without it.

Phase 1 and Phase 2 still use semantic processing, but they do it through:

- turn-end extraction
- session-end extraction
- explicit-checkpoint extraction when needed

After Phase 1, there is a decision gate:

- if local continuity pressure is already painful, pull `Mamba` forward as a Phase `1.5` spike
- otherwise add it in Phase 3 as a supercharge to the same spine

## What Mamba Is

The High-Signal Mamba Stream is the later always-on high-signal channel for Cortex.

It is:

- a small always-on listener
- a Layer 2-adjacent signal producer
- a narrow optimization and continuity-improvement layer

It is not the thing that makes the architecture finally work.

It improves an already-valid runtime.

## What Mamba Does

It emits a typed signal stream for:

- working-memory assembly
- notion updates
- Intuition
- reflection

Later, that same signal helps give the system an infinite-context-like continuity effect for long-running work without pretending to offer literal infinite recall.

## What Mamba Does Not Do

It is not:

- a universal reasoning layer
- the broad reflection engine
- the document decomposition engine
- the operational knowledge authority

The architecture should keep it narrow.

## Why Mamba Still Matters

When it lands, Mamba improves:

- infinite-context-like continuity for long-running work
- near-time continuity compression
- always-on high-signal capture
- lower-latency semantic awareness
- cleaner live-session handling for long-running work

It also provides:

- better near-time triggers
- better directional context for Reflection
- better directional context for Dream

## Important Boundary

The Phase 1 hooks should survive after Mamba arrives.

Mamba augments:

- turn-end processing
- session-end processing
- checkpoint-triggered processing

It does not invalidate that implementation work.

It also does not replace full evidence in deeper passes.

Reflection and Dream still use fuller evidence and evidence packages when doing real consolidation or reconciliation.

Mamba just helps them get there faster, with better direction, and with better live continuity.

## Intuition On Top Of Mamba

When Mamba exists, Cortex can add Intuition as a narrow signal evaluator on top of the stream.

Intuition decides when a high-signal window should wake hotter layered ingestion.

That can include:

- faster notion updates
- hotter reflection triggers
- opportunistic GPU-backed processing while headroom exists
- later coding supervision hooks
