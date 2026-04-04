# High-Signal Mamba Stream

## What It Is

The High-Signal Mamba Stream is the primary semantic checkpoint stream for Cortex.

It is:

- derived from raw evidence
- typed
- compressed
- source-linked
- rebuildable
- the default downstream consumer surface

It is not the raw evidence log itself.

## Why It Exists

The stream exists because raw replay is too expensive as the normal path.

Without it, the system would have to keep leaning on:

- large transcript replay
- oversized context windows
- expensive prompt bloat
- weak cross-thread continuity

The stream solves those problems by turning raw runtime activity into compact semantic checkpoints.

## Raw Evidence Versus Semantic Checkpoints

The architecture separates two things:

- the raw evidence log
- the semantic checkpoint stream

The raw evidence log is the audit and recovery surface.

The semantic checkpoint stream is the normal operational surface.

Most consumers should subscribe to the semantic checkpoint stream.

Very few consumers should read raw evidence directly.

## The Best Mental Model

The best model is:

- raw evidence = journal or canonical source
- High-Signal Mamba Stream = materialized semantic checkpoint stream

That means the stream should be regenerable if the compression logic improves later.

## Typical Payload

A checkpoint item may include:

- active goals
- open loops
- current assumptions
- recent decisions
- current entities or threads
- handoff state
- candidate notions
- artifact-impact hints
- oversight flags
- source references back to the evidence log or canonical artifact revision

The payload should be typed, not generic prose.

## The Three Consumption Modes

The same stream supports three timing modes:

### Optimistic

Near-time and cheap.

Used when the system wants quick semantic output and spare compute is available.

### On-Demand

Pulled when a thread, tool, or workflow actually needs more continuity or interpretation.

### Nightly

Slower and deeper.

Used for consolidation, reconciliation, contradiction checks, and cleanup.

## The Stream As Shared Semantic Bus

The stream is more than a context-summary trick.

It is a shared semantic bus for multiple consumers:

- working-memory assembly
- notion staging for durable memory
- oversight
- artifact-impact detection
- nightly maintenance

That is how the system gets maximum value from live compression.

## Relationship To Working Memory

The stream improves Layer 2 by giving OpenClaw and Cortex compact continuity objects.

This reduces dependence on raw transcript replay.

The stream does not replace OpenClaw sessions.

It sits above them as the main semantic consumer surface.

## Relationship To Durable Memory

The stream is the default staging surface for Layer 3 durable memory.

It produces:

- candidate notions
- tentative beliefs
- support hints

These do not become trusted memory automatically.

They enter a staged path first.

## Cross-Thread Memory

The stream enables fast cross-thread continuity through tentative memory.

The intended model is:

1. a checkpoint emits a high-signal notion
2. that notion may be written early as tentative cross-thread memory
3. it is marked `tentative`, `low_confidence`, and `unreconciled`
4. later reconciliation confirms, merges, downgrades, or rejects it

This gives the system speed without pretending speed equals truth.

## Relationship To Oversight

Oversight should consume the stream by default because it is cheaper and higher signal than raw evidence.

Oversight should escalate to raw evidence only when:

- confidence is low
- impact is high
- provenance is disputed
- approval is required

## Relationship To Artifacts

Artifacts follow the same pattern.

The stream can carry compact semantic checkpoints for artifact ingestion and change interpretation, while canonical source material remains in Layer 5.

## Bottom Line

The High-Signal Mamba Stream is the core semantic middle layer of the entire stack.

It is how Cortex turns raw runtime and artifact evidence into bounded continuity, tentative memory, oversight input, and reconciliation-ready semantic products.
