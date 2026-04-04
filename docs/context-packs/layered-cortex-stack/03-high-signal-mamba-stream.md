# High-Signal Mamba Stream

## What It Is

The High-Signal Mamba Stream is the always-on high-signal channel for Cortex.

It sits next to Layer 2 and listens continuously to session activity.

## What It Does

It emits a typed signal stream for:

- working-memory assembly
- notion updates
- oversight
- reflection

## What It Does Not Do

It is not:

- a universal reasoning layer
- the broad reflection engine
- the document decomposition engine
- the operational knowledge authority

The architecture should keep it narrow.

## Recommended Implementation Pattern

The strongest pattern is:

- a small continuous listener or sensor
- plus larger downstream writers only when a bounded high-signal window justifies the cost

The stream is supposed to gate expensive downstream work, not absorb all of it.

## Why It Exists

The stream exists because:

- raw transcript replay is too expensive as the default path
- Layer 2 needs a continuous high-signal surface
- notions and oversight need fast input without rereading everything

## What It Feeds

The stream may be consumed by:

- working-memory assembly
- notion staging
- oversight
- reflection

That does not make the stream those systems.

It remains the narrow high-signal producer.
