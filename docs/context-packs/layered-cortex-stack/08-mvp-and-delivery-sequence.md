# MVP And Delivery Sequence

## MVP Goal

The first MVP is not "stand up a search backend."

The first MVP is to prove the layered Cortex spine.

The system is considered successful when it demonstrates:

- custom policy on top of OpenClaw
- OpenClaw-native working memory with bounded context assembly
- a usable High-Signal Mamba Stream
- tentative notion staging and later reconciliation
- Graphiti plus Neo4j durable memory
- Postgres plus pgvector decomposed knowledge
- Git-backed canonical artifact flow
- inspectable oversight and acceptance surfaces

## Epic Order

The current build order is:

1. policy and OpenClaw integration
2. High-Signal Mamba Stream
3. Graphiti plus Neo4j durable memory
4. knowledge plane and artifacts
5. oversight and reconciliation

## Why The Build Order Looks Like This

The order is driven by dependency logic.

Policy and OpenClaw integration come first because the system needs a stable Layer 1 and Layer 2 posture before it can feed good semantic checkpoints.

The Mamba Stream comes second because durable memory and oversight depend on it.

Durable memory comes third because semantic checkpoints need somewhere trustworthy to land.

Knowledge and artifacts come fourth because their flows depend on the layer contracts already being stable.

Oversight and reconciliation come fifth because they harden the system after the main data flows exist.

## Phase 1 Deployment Shape

The base deployment includes:

- OpenClaw
- Cortex policy and integration layer
- High-Signal Mamba stream worker
- Graphiti
- Neo4j
- Postgres plus pgvector
- Git working repository or provider-backed artifact source

## What Phase 1 Explicitly Excludes

Phase 1 explicitly excludes:

- a separate external working-memory store beside OpenClaw Layer 2
- a second graph system beside Layer 3
- a separate search platform unless Layer 4 proves it needs one
- broad candidate-comparison work

## Proof Surface

The runtime proof surface should demonstrate:

- OpenClaw session flow
- policy injection points
- semantic checkpoint generation
- tentative notion staging
- reconciliation checkpoints
- artifact intake
- redraft and publication loop

## What Success Looks Like

Success looks like a system where:

- live sessions stay bounded
- continuity survives smaller context windows
- high-signal memory can cross threads tentatively
- trusted memory emerges through reconciliation
- artifacts are operationally usable before publication
- canonical truth remains clean

## The Most Important Implementation Pressure

The most important implementation pressure is not "how many features exist."

It is whether the semantic checkpoint stream is good enough to support:

- working-memory compression
- notion staging
- oversight
- artifact impacts
- reconciliation

If that layer is weak, the rest of the stack becomes noisy.

If that layer is strong, the rest of the stack becomes tractable.
