# Repo Orientation

## What Cortex Is

Cortex is the Remram knowledge authority layer.

It coordinates five layers:

1. `Policy`
2. `Working Memory`
3. `Durable Memory`
4. `Operational Knowledge`
5. `Evidence`

The architecture rule is:

`one authority, multiple memory surfaces`

## What Problem It Solves

Cortex exists so the system does not collapse into:

- transcript as memory
- prompt state as truth
- retrieval indexes as semantic authority
- operational workspaces jumping to canon too early

## What Is Active

The active stack direction is:

- `OpenClaw` at the runtime center
- Cortex-owned Layer 1 policy composition
- `QMD` for Layer 2 hot retrieval and notions
- `Graphiti + Neo4j` for Layer 3 durable memory
- `Postgres` for the operational middle of the stack
- Layer 5 evidence classes: `runtime_evidence`, `reference_cache`, `authored_artifact`

## What Is Deferred

- `Mamba` and `Intuition` until Phase 5
- `OpenSearch`
- treating every useful idea as a Git destination
- any second graph or second Graphiti pattern

## Canonical Docs

When you need exact wording, use:

- [../../authority-map.md](../../authority-map.md)
- [../../glossary.md](../../glossary.md)
- [../../design/layered-memory-architecture.md](../../design/layered-memory-architecture.md)
- [../../design/technology-stack.md](../../design/technology-stack.md)
- [../../design/knowledge-and-artifact-architecture.md](../../design/knowledge-and-artifact-architecture.md)
- [../../design/deployment-plan.md](../../design/deployment-plan.md)
