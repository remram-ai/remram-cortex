# High-Signal Mamba Stream

The High-Signal Mamba Stream is Cortex's always-on high-signal channel.

It is a narrow Layer 2-adjacent listener built from session activity.

## What It Is

The stream is:

- always-on
- typed
- source-linked
- narrow by design
- consumed by downstream systems

It is not the raw evidence log itself.

## What It Does

The stream reads session activity and emits a typed high-signal channel for:

- working-memory assembly
- notion updates
- oversight
- reflection

That is all.

## What It Does Not Do

The stream is not:

- a universal reasoning layer
- the broad reflection engine
- the document decomposition engine
- the full artifact interpretation engine

Do not describe it as doing broad magical system work.

## Implementation Pattern

The strongest implementation pattern is:

- a small always-on listener or sensor
- plus larger bounded downstream writers only when a high-signal window is worth further work

## Relationship To Layer 2

The stream is Layer 2-adjacent.

It helps:

- keep hot continuity usable
- feed notions in `QMD`
- support bounded context assembly

It does not replace `QMD`.

It does not replace OpenClaw sessions.

## Relationship To Reflection

Reflection may consume the stream.

That does not make the stream the reflection engine.

The stream produces signal.

Reflection decides what to do with it.

## Relationship To Artifacts

The stream may emit signal that later helps artifact-related workflows.

It should not itself be described as doing full document parsing or broad artifact decomposition.

## Design Principle

Keep Mamba narrow.

Let downstream systems consume the signal.

Do not let the architecture blur that boundary.
