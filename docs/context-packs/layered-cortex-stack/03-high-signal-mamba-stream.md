# High-Signal Mamba Stream

## The Main Sequencing Clarification

`Mamba` is deferred, not removed.

Phase 1 and Phase 2 still use semantic processing, but they do it through:

- turn-end extraction
- session-end extraction
- explicit-checkpoint extraction when needed

After Phase 1, there is a decision gate:

- if local continuity pressure is already painful, pull `Mamba` forward as a Phase `1.5` spike
- otherwise leave it deferred until Phase 3

## What Mamba Is

The High-Signal Mamba Stream is the later always-on high-signal channel for Cortex.

It is:

- a small always-on listener
- a Layer 2-adjacent signal producer
- a narrow optimization and continuity-improvement layer

## What Mamba Does

It emits a typed signal stream for:

- working-memory assembly
- notion updates
- oversight
- reflection

## What Mamba Does Not Do

It is not:

- a universal reasoning layer
- the broad reflection engine
- the document decomposition engine
- the operational knowledge authority

The architecture should keep it narrow.

## Why Mamba Still Matters

When it lands, Mamba improves:

- near-time continuity compression
- always-on high-signal capture
- lower-latency semantic awareness
- cleaner live-session handling for long-running work

## Important Boundary

The Phase 1 hooks should survive after Mamba arrives.

Mamba augments:

- turn-end processing
- session-end processing
- checkpoint-triggered processing

It does not invalidate that implementation work.
