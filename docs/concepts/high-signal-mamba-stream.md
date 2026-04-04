# High-Signal Mamba Stream

The High-Signal Mamba Stream is Cortex's primary semantic checkpoint stream.

It is a derived, typed, source-linked stream built from raw evidence.

It is not the raw evidence log itself.

## Purpose

The stream exists so Cortex does not need to replay large raw session logs or artifact histories every time a downstream consumer needs continuity.

It gives the system one compact semantic surface for:

- working-memory assembly
- tentative cross-thread memory staging
- oversight
- artifact-impact hints
- nightly reconciliation

## What It Is

The stream should be treated as:

- high signal
- compressed
- typed
- rebuildable
- source-linked
- operational

The best mental model is:

- raw evidence = journal or canonical source
- High-Signal Mamba Stream = materialized semantic checkpoint stream

## What It Is Not

It is not:

- a second authority
- a freeform prose summary layer
- a replacement for canonical artifacts
- a replacement for raw runtime evidence

If the compression logic changes, the stream should be regenerable from the underlying evidence.

## Inputs

The stream is primarily derived from:

- OpenClaw session evidence
- tool results and agent actions
- checkpoint or compaction boundaries
- canonical artifact revisions when they are ingested or updated

Raw runtime evidence will usually be retained in `Postgres`.

Canonical document evidence will usually remain in `Git` or the provider source.

## Typical Payload

A High-Signal Mamba Stream item may contain:

- active goals
- open loops
- current assumptions
- recent decisions
- entities and threads in focus
- handoff state
- candidate notions
- artifact-impact hints
- oversight flags
- source references back to raw evidence or canonical revisions

These payloads should be typed rather than treated as generic summary text.

## Consumption Modes

The same stream should support multiple service levels:

- optimistic
  - near-time, best effort, cheap
- on-demand
  - pulled when a thread or workflow needs it
- nightly
  - slower, deeper, consistency-oriented

This lets Cortex use one semantic bus instead of inventing separate systems for each timing mode.

## Relationship To Working Memory

Working memory should remain anchored on the OpenClaw session surface.

The High-Signal Mamba Stream improves that layer by giving the context engine compact continuity objects instead of forcing raw transcript replay.

## Relationship To Durable Memory

The stream is the default staging surface for Layer 3 memory.

It should usually produce:

- candidate notions
- tentative beliefs
- support signals

These should not become trusted durable memory just by existing.

By default, they should be reconciled at:

- session end
- checkpoint hooks
- nightly maintenance

High-signal items may be written early for cross-thread continuity, but they should be marked as:

- `tentative`
- `low_confidence`
- `unreconciled`

## Relationship To Oversight

Oversight should consume the High-Signal Mamba Stream by default.

It can escalate to raw evidence when:

- confidence is low
- impact is high
- approval is required
- provenance is disputed

## Relationship To Artifacts

Document artifacts should follow the same high-signal pattern.

The durable-memory layer should usually receive:

- one compact summary node or episode-level representation
- a pointer to the canonical artifact revision
- only extracted Layer 3 appropriate standalone facts or beliefs

The full document body should remain in the canonical artifact layer.

## Design Principle

Most consumers should subscribe to the High-Signal Mamba Stream.

Very few consumers should read raw evidence directly.

That keeps Cortex efficient on smaller-window models while preserving a path back to exact evidence when it matters.
