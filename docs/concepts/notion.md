# Notion

A notion is a staged candidate memory derived from semantic checkpoints.

It is the main object that sits between runtime evidence and trusted durable memory.

## What A Notion Is

A notion is:

- provisional
- source-linked
- confidence-bearing
- reconcilable
- eligible for promotion into Layer 3

It is not yet trusted durable memory just because it exists.

## Why Notions Exist

They let Cortex separate:

- fast semantic interpretation
- cross-thread continuity
- trusted durable memory

without forcing every useful signal to wait until nightly maintenance.

## Typical Lifecycle

The normal notion lifecycle is:

1. semantic checkpoints suggest a candidate
2. Cortex stages it as a notion
3. high-signal notions may be exposed early as tentative cross-thread memory
4. reconciliation confirms, merges, downgrades, rejects, or supersedes it

## Typical Status Values

Common notion and memory-adjacent states include:

- `candidate`
- `tentative`
- `low_confidence`
- `active`
- `rejected`
- `superseded`
- `invalidated`

The exact schema can evolve, but the architectural rule should not:

- early exposure is allowed
- trust must still be earned

## Minimum Shape

A notion should usually carry:

- a stable id
- a statement or compact claim
- source references
- support references when available
- confidence
- timestamps
- scope or anchor references
- current lifecycle state

## Relationship To Durable Memory

Layer 3 should usually ingest reconciled notions, not raw transcript fragments.

That keeps durable memory:

- more trustworthy
- more inspectable
- easier to supersede later

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Evidence Package](evidence-package.md)
- [High-Signal Mamba Stream](high-signal-mamba-stream.md)
- [Reflection](reflection.md)
- [Oversight](oversight.md)
