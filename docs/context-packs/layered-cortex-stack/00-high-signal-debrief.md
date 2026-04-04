# High-Signal Debrief

## Cortex In One Sentence

Cortex is a layered knowledge authority built around custom policy, OpenClaw-native working memory, Graphiti plus Neo4j durable memory, Postgres plus pgvector decomposed knowledge, and Git-backed canonical artifacts.

## The Main Architectural Move

The system is no longer trying to force all memory, knowledge, and runtime context through one substrate.

Instead, it separates five layers:

1. `Policy`
2. `Working Memory`
3. `Durable Memory`
4. `Decomposed Artifact Knowledge`
5. `Canonical Artifacts`

The entire stack is organized around one rule:

**one authority, multiple memory surfaces**

That means Cortex is still the authority, but different kinds of truth live in different places.

## The Chosen Stack

- `OpenClaw` is the runtime shell and the default Layer 2 working-memory engine.
- Cortex owns `Policy` above OpenClaw.
- A High-Signal `Mamba` stream turns noisy runtime evidence into a semantic checkpoint stream.
- `Graphiti + Neo4j` is Layer 3 durable memory.
- `Postgres + pgvector` is the operational substrate for runtime evidence, control-plane state, and Layer 4 decomposed knowledge.
- `Git` is the preferred Layer 5 canonical artifact truth.

## The Most Important Runtime Story

The runtime model is:

1. OpenClaw runs the live session.
2. The session transcript is the evidence surface.
3. Cortex observes that session and produces a High-Signal Mamba stream.
4. That stream is the main semantic consumer surface.
5. The stream emits candidate notions for durable memory.
6. High-signal notions may appear early as tentative cross-thread memory.
7. Reconciliation at session end, checkpoints, or nightly maintenance decides what becomes trusted Layer 3 memory.

This is the key compromise:

- fast enough for cross-thread continuity
- conservative enough to protect memory integrity

## The Most Important Artifact Story

Artifacts follow the same pattern as sessions:

- keep the raw source in the canonical layer
- build a decomposed operational layer separately
- only send compact summary plus pointer plus Layer 3 appropriate beliefs into durable memory

For documents, that means:

- Layer 5 keeps the canonical body and revision history
- Layer 4 keeps slices, embeddings, lexical fields, and typed extracted structures
- Layer 3 only gets what belongs in semantic memory

## Why This Stack

This stack exists because each layer solves a different real problem:

- `Policy` is custom because Cortex behavior is custom.
- `OpenClaw` already solves the runtime and session problem well enough that Cortex should not replace it casually.
- the High-Signal `Mamba` stream exists because smaller-window models make raw transcript replay expensive and brittle.
- `Graphiti + Neo4j` is the hardest part to replace because Cortex wants temporal lineage, invalidation, provenance, and graph-native durable memory.
- `Postgres + pgvector` gives a practical substrate for evidence and decomposed operational knowledge without adding another large platform.
- `Git` remains the best default for canonical artifact truth and publication history.

## What The System Explicitly Avoids

The active posture avoids:

- one giant universal memory bucket
- a separate external working-memory store in phase 1
- storing raw transcripts inside durable memory
- storing full artifact bodies inside durable memory
- forcing every decomposed slice into the graph
- making Layer 4 and Layer 5 compete for authority

## The Main Idea Behind The High-Signal Mamba Stream

The High-Signal Mamba stream is a semantic checkpoint stream built from raw evidence.

It is:

- typed
- compressed
- source-linked
- rebuildable
- the default consumer surface for most downstream systems

It is not:

- the raw evidence log
- a second authority
- a freeform summary layer

Most of the stack should read the Mamba stream, not raw evidence.

## The Main Idea Behind Durable Memory

Durable memory is where long-lived semantic truth lives.

It owns:

- durable beliefs
- preferences
- constraints
- decisions
- support relationships
- temporal lineage
- invalidation and supersession

It does not own:

- the working transcript
- the evidence log
- the full artifact corpus

## The Main Idea Behind Reflection

Reflection is not just "write memory."

It branches one evidence feed into multiple products:

1. memory updates
2. artifact impacts
3. context compression
4. governed preference-policy updates

Oversight watches the same semantic products in parallel.

## The Main Build Order

The delivery order is:

1. policy and OpenClaw integration
2. High-Signal Mamba stream
3. Graphiti plus Neo4j durable memory
4. knowledge plane and artifacts
5. oversight and reconciliation

That order matters because the system should not write durable memory before it has a stable semantic checkpoint surface.

## The Most Important Risks

- working-memory prompt bloat if the Mamba stream is weak
- bad notion quality if compression is noisy
- durable-memory corruption if tentative writes are treated as trusted truth
- artifact drift if Layer 4 outruns Layer 5 without dirty-state tracking and redraft discipline
- split-brain authority if layers write into each other directly instead of through Cortex contracts

## Bottom Line

The stack is now clear:

- OpenClaw handles runtime execution and session mechanics
- Cortex adds policy and semantic checkpointing
- Graphiti plus Neo4j handles durable semantic memory
- Postgres plus pgvector handles operational evidence and decomposed knowledge
- Git handles canonical artifact truth

The whole architecture is designed so the system can think live, remember durably, and reason over grounded artifacts without pretending one store can do every job.
