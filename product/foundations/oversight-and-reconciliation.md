# Oversight And Reconciliation

This document defines the stable product posture for oversight and reconciliation.

## Oversight

Oversight is a consumer of the semantic checkpoint stream.

Its responsibilities include:

- suspicious-memory detection
- policy violation flags
- review triggers
- confidence downgrades
- approval-oriented veto paths where required

## Reconciliation

Reconciliation is how tentative outputs become trusted durable memory.

It should run at:

- session end
- checkpoint boundaries
- nightly maintenance

## Product Rule

Fast cross-thread memory is allowed only as tentative memory.

Trusted memory requires reconciliation.
