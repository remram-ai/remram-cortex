# Intuition And Reconciliation

This document defines the stable product posture for Intuition and reconciliation.

## Intuition

Intuition is the future Mamba-side signal evaluator for Cortex.

Its responsibilities include:

- evaluating high-signal windows from Mamba
- deciding when hotter layered ingestion should wake
- emitting stronger notion or reflection triggers
- leaving the deeper reasoning to reflection and reconciliation
- later supporting coding-supervision triggers when that capability exists

Intuition is blocked by `Mamba`.

It is therefore not part of the base Phase 1 architecture.

## Reconciliation

Reconciliation is how tentative outputs become trusted durable memory.

It should run at:

- session end
- checkpoint boundaries
- nightly maintenance

Session-end reconciliation is the primary trust boundary for fast cross-thread memory.

Reflection is also allowed to:

- prune notions
- merge notions
- demote stale notions
- expire low-value notions
- keep `QMD` lean and fast

Reflection and Dream may both use Layer 3 semantic relationships to help organize Layer 4 workspaces, but they do not turn Layer 3 into a body store.

## Product Rule

Fast cross-thread memory is allowed only as tentative memory.

Trusted memory requires reconciliation.
