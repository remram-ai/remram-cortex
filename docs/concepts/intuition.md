# Intuition

Intuition is the future Mamba-side signal evaluator for Cortex.

It watches the High-Signal Mamba Stream and decides when a bounded high-signal window is worth waking hotter layered ingestion.

Its main job is to queue opportunistic processing when GPU cycles are free instead of waiting only for session-end or batch schedules.

It is not part of the base Phase 1 spine.

## What Intuition Does

Intuition is responsible for:

- evaluating high-signal windows from the Mamba stream
- deciding when hotter notion work should run
- deciding when reflection should be pulled into a hotter path
- queuing bounded opportunistic processing while GPU headroom exists
- later emitting coding-supervision or off-track-correction triggers

## Default Input Surface

Intuition is blocked by `Mamba`.

That means:

- in Phase 1 and Phase 2, Cortex uses boundary-triggered semantic processing without Intuition
- once `Mamba` lands, Intuition can consume the High-Signal Mamba Stream as its default near-time feed

This gives Intuition:

- better signal density
- lower cost than replaying fuller evidence all the time
- a narrow trigger surface for hot-memory and reflection wake-ups

## Escalation Path

Intuition should escalate to richer downstream work only when the signal warrants it.

That may include:

- notion updates in `QMD`
- reflection on a bounded evidence window
- deeper evidence-package review
- later coding-supervision or off-track correction workflows

## What Intuition Is Not

Intuition is not:

- the durable-memory authority
- the policy author
- the general reflection engine
- a replacement for reconciliation

It is a signal evaluator and wake-up surface that supercharges reflection once Mamba exists.

## Timing Modes

Intuition can eventually run in:

- optimistic mode
- on-demand mode
- nightly hint mode

The same signal contract should support all three.

## Related Concepts

- [Evidence Package](evidence-package.md)
- [High-Signal Mamba Stream](high-signal-mamba-stream.md)
- [Reflection](reflection.md)
- [Dream Cycle](dream-cycle.md)
