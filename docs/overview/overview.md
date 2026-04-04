# Cortex Overview

Remram Cortex is the knowledge authority layer for Remram.

It coordinates policy, hot working continuity, durable semantic memory, operational knowledge, and canonical publication without collapsing them into one storage model.

The architecture is now centered on five layers:

1. `Policy`
2. `Working Memory`
3. `Durable Memory`
4. `Operational Knowledge`
5. `Canonical Artifacts`

The clean authority model is:

- Layer 1 = behavioral truth
- Layer 2 = hot working continuity
- Layer 3 = durable semantic truth
- Layer 4 = operational knowledge truth
- Layer 5 = canonical publication truth

## Chosen Stack

The active stack direction is:

- `OpenClaw` as the chosen agentic framework
- Cortex-owned Layer 1 policy
- `QMD` for Layer 2 hot working memory and notions
- a narrow High-Signal `Mamba` stream as a later always-on optimization layer
- `Graphiti + Neo4j` for Layer 3 durable memory
- `Postgres` for the operational middle of the stack
- `Git` for Layer 5 canonical artifacts when canonical publication is warranted

## What Cortex Owns

Cortex owns:

- policy composition
- Layer 2 notion and high-signal lifecycle rules
- Layer 3 durable-memory contracts
- Layer 4 operational knowledge authority rules
- the split between operational knowledge and canonical publication
- reflection, Dream, oversight, and promotion behavior

## OpenClaw Principle

`OpenClaw` was not chosen because Cortex benchmarked orchestrators and decided it was the abstract best shell.

It was chosen because it is the framework Remram intends to build around.

That means the architectural rule is:

- do things the OpenClaw way when that path is good enough
- extend OpenClaw cleanly before replacing it
- add memory and knowledge behavior around the framework boundary

## What Changed In The Locked Design

The biggest clarifications now are:

- Layer 2 explicitly uses `QMD`
- Mamba is narrow by design
- Mamba is deferred by default until Phase 3 unless the post-Phase-1 gate pulls it forward
- Layer 3 stays one Graphiti memory system
- Layer 4 is the operational knowledge authority
- Layer 5 is only canonical publication truth when canon is warranted
- `OpenSearch` is not part of the near-term stack

## Repository Direction

The repository now aims to describe one coherent architecture rather than a stack-comparison process.

Historical alternatives and superseded packages live in the top-level archive.
