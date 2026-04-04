# Oversight

Oversight is the review and control consumer that watches semantic outputs for trust, policy, and approval concerns.

It is not the main knowledge authority.

## What Oversight Does

Oversight is responsible for:

- suspicious-memory detection
- policy violation flags
- confidence downgrades
- approval triggers
- review task creation
- veto paths for sensitive changes

## Default Input Surface

Oversight should consume the High-Signal Mamba Stream by default.

That gives it:

- better signal density
- lower cost than replaying raw evidence
- continuity across optimistic, on-demand, and nightly modes

## Escalation Path

Oversight should escalate to evidence packages or raw backing material when:

- impact is high
- confidence is low
- provenance is disputed
- approval is required

## What Oversight Is Not

Oversight is not:

- the durable-memory authority
- the policy author
- a replacement for reconciliation

It is a control and review lane that helps those systems stay trustworthy.

## Timing Modes

Oversight can run in:

- optimistic mode
- on-demand mode
- nightly mode

The same semantic stream can support all three.

## Related Concepts

- [Evidence Package](evidence-package.md)
- [High-Signal Mamba Stream](high-signal-mamba-stream.md)
- [Reflection](reflection.md)
- [Dream Cycle](dream-cycle.md)
