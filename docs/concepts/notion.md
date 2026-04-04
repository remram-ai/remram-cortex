# Notion

A notion is a hot staged candidate durable memory.

It lives in Layer 2 as part of the `QMD` working-memory surface.

## What A Notion Is

A notion is:

- provisional
- fast to retrieve
- fast to prune
- source-linked
- reconcilable
- eligible for promotion into Layer 3

It is not trusted durable memory just because it exists.

## Why Notions Exist

Notions let Cortex separate:

- live working continuity
- medium-confidence semantic candidates
- trusted durable semantic memory

without forcing every useful signal to wait until nightly maintenance.

## Physical Home

In the locked design, notions live in `QMD`.

They are part of the Layer 2 hot working-memory surface.

They are not:

- a separate Postgres-first ledger
- a separate Graphiti-first ledger

## Typical Lifecycle

The normal notion lifecycle is:

1. turn-end, session-end, or explicit-checkpoint processing emits semantic outputs
2. a notion is created or updated in `QMD`
3. the notion may be retrieved for continuity or tentative cross-thread use
4. reflection may merge, prune, demote, or expire it
5. reconciliation may promote it into Layer 3 durable memory

When `Mamba` arrives later, it becomes an additional near-time signal source for the same lifecycle.

## Retrieval Rule

Tentative cross-thread retrieval is allowed under tighter rules.

It may guide continuity.

It is not silently authoritative before reconciliation.

## Cleanup Rule

Reflection is allowed to:

- prune notions
- merge notions
- demote stale notions
- expire low-value notions

This is necessary to keep Layer 2 lean and fast.

## Relationship To Layer 3

Layer 3 consumes reconciled meaning from notions.

Layer 3 does not need to store notions as its normal hot staging surface.

The boundary is:

- Layer 2 stores hot candidate durable memory
- Layer 3 stores trusted durable semantic truth

## Related Concepts

- [High-Signal Mamba Stream](high-signal-mamba-stream.md)
- [Reflection](reflection.md)
- [Evidence Package](evidence-package.md)
- [Knowledge Object](knowledge-object.md)
