# Stack And Service Posture

## Active Stack

- `OpenClaw` for runtime execution and session mechanics
- Cortex policy composition
- `QMD` for Layer 2 hot retrieval and notion storage
- `Graphiti + Neo4j` for Layer 3 durable memory
- `Postgres` for Layer 4 and operational state
- Layer 5 evidence contract with multiple classes

## Current Service Posture

For the intended Phase 1 deployment shape:

- `cortex` is a separate service
- `graphiti` is a separate service
- `neo4j` is a separate backing database
- `postgres` is the operational store

## Important Posture Rules

- `Postgres` is the operational middle-layer authority.
- `pgvector` may live inside that same Postgres surface when vector similarity helps.
- `Git` is introduced later for `authored_artifact`, not for every useful idea.
- `Mamba` is later and narrow by design.
- `OpenSearch` is not in the active stack.

## What Not To Assume

- no second graph system
- no second Graphiti pattern
- no giant separate working-memory service
- no default authored-canon destiny for Layer 4 work
