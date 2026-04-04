# Oversight And Reconciliation

This document defines the stable product posture for oversight and reconciliation.

## Oversight

Oversight is a control consumer of semantic outputs and related staged state.

Its responsibilities include:

- suspicious-memory detection
- policy violation flags
- review triggers
- confidence downgrades
- approval-oriented veto paths where required

Oversight should consume boundary-triggered semantic outputs in early phases, notion activity by default, and later the Mamba stream when available.

It should escalate to evidence packages only when fidelity or approval requirements demand it.

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
