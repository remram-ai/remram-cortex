# High-Signal Mamba Stream

The High-Signal Mamba Stream is Cortex's later always-on high-signal channel.

It is a narrow Layer 2-adjacent listener built from session activity.

The important posture is that Cortex does not need to wait for it to have a valid architecture.

The spine already works through OpenClaw sessions, `QMD`, notions, and boundary-triggered semantic processing.

Mamba arrives later as a supercharge to that same spine.

## Sequencing Clarification

`Mamba` is part of the long-term design, but it is not on the critical path for proving the architecture.

Phase 1 proves the architecture with boundary-triggered semantic processing:

- turn-end extraction
- session-end extraction
- explicit-checkpoint extraction when needed

After Phase 1, there is a simple decision gate:

- if local continuity pressure is real, Mamba can be pulled forward as a Phase `1.5` spike
- otherwise Phase 3 adds it as the default continuity supercharge

When Mamba does arrive, it augments those hooks rather than replacing them.

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
- Intuition
- reflection

That is all.

When it lands, it is valuable because it improves:

- infinite-context-like continuity for long-running work without claiming literal infinite recall
- near-time triggers
- better live memory quality
- better directional signal for Reflection and Dream

It also gives the system an infinite-context-like continuity effect for long-running work without pretending to provide literal infinite recall.

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

Reflection should still retain access to fuller evidence and evidence packages for deeper work.

That is the main boundary:

- Mamba improves salience, continuity, and trigger quality
- reflection still performs the deeper reasoning and reconciliation work

## Relationship To Intuition

Intuition is the later signal evaluator that can sit on top of the stream.

It decides when a bounded high-signal window should wake hotter layered ingestion.

That can include:

- faster notion updates
- hotter reflection triggers
- opportunistic GPU-backed processing while headroom exists
- later coding supervision hooks

Intuition is blocked by Mamba.

## Relationship To Artifacts

The stream may emit signal that later helps artifact-related workflows.

It should not itself be described as doing full document parsing or broad artifact decomposition.

Dream and deeper reconciliation passes still use fuller evidence and semantic state.

Mamba makes those passes more efficient and better directed later.

## Design Principle

Keep Mamba narrow.

Let downstream systems consume the signal.

Do not let the architecture blur that boundary.
