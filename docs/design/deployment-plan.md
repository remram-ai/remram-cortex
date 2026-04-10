# Deployment Plan

This document records the active delivery posture for the locked Cortex architecture.

The architecture is being delivered as a progressive activation of system loops rather than one flat implementation sprint.

## Live Appliance Authority

For live Moltbox appliance work, `moltbox-gateway` is the source of truth for:

- the current managed service inventory
- the public `moltbox` CLI contract
- the restricted-operator verification surfaces
- the snapshot-first recovery model
- the current web-tooling baseline

This deployment plan describes the intended Cortex bring-up shape.

It does not mean those future services already exist on the live appliance.

Current live-baseline facts must still come from the Gateway repo until the service plane is intentionally extended.

That extension is allowed as part of Cortex delivery.

The rule is that new services must be introduced the Moltbox way:

- define and track baseline service artifacts and service-local docs in `moltbox-services`
- use `moltbox-runtime` for final promoted runtime artifacts and runtime-baseline changes
- update official Gateway docs only when the operator contract, workflow, verification surface, or recovery behavior changes
- deploy and validate through the official CLI and service-plane path

Current Phase 1 deployment decision:

- `cortex` is a separate service
- `graphiti` is a separate service
- `neo4j` remains the backing graph database
- `postgres` remains the Layer 4 operational store

## Long-Term Stack

The long-term stack remains:

- `OpenClaw`
- Cortex policy and integration layer
- `QMD` as the Layer 2 hot working-memory substrate
- `Graphiti`
- `Neo4j`
- `Postgres`
- a Layer 5 evidence system, with `Git` used for authored artifacts when publication-grade canon is warranted
- a narrow High-Signal `Mamba` listener added later as a real-time supercharge layer

## Phase 0: OpenClaw Baseline

Phase 0 establishes the vanilla baseline.

It includes:

- `OpenClaw`
- local-model execution
- safe baseline config
- session pruning and compaction
- `QMD` enabled in the public OpenClaw posture

It does not yet include Cortex-specific reflection, durable memory, or Layer 5 evidence orchestration.

## Phase 1: Chat Memory Loop

Phase 1 is the first full Cortex loop.

It includes:

- Cortex policy and integration layer
- Layer 5 runtime-evidence capture for chat transcripts
- turn-end, session-end, and explicit-checkpoint semantic processing
- Reflection and Dream over chat-derived evidence
- `Graphiti + Neo4j` for Layer 3 durable semantic memory
- `Postgres` for narrow Layer 4 chat-derived support bodies and the operational middle layer
- reflection-driven `QMD` cleanup
- session-end reconciliation

Phase 1 does not require:

- reference ingestion
- owned-source sync
- Git-backed authored canon
- live always-on `Mamba`

## Phase 2: Reference Decomposition Loop

Phase 2 introduces one-way outside material.

It includes:

- uploaded reference documents
- web-link snapshot fetches
- a shared decomposition spine for those reference inputs
- Layer 4 reference-derived knowledge bodies
- Layer 3 meaning extraction from those decomposed references

This phase makes outside material usable without yet introducing source ownership or dirty-state complexity.

## Phase 3: Collaborative Source Maintenance Loop

Phase 3 introduces owned high-signal documents as living maintained sources.

It includes:

- owned "file cabinet" documents
- dirty-state as a dual-state model
- current-version and derived-version tracking
- diff and reconciliation surfaces
- source reprocessing back into Layer 4 and Layer 3

This is the phase where source-sync becomes real.

## Phase 4: Artifact Promotion Loop

Phase 4 introduces authored canon.

It includes:

- promotion candidate detection
- artifact drafting
- Git as the canonical backend for authored artifacts
- bottom-up reprocessing from authored canon into Layer 4 and Layer 3

This is the phase where the system begins producing maintained authored assets, not just memory and decomposition.

## Phase 5: Optimization Loop

Phase 5 introduces optimization and hardening.

It includes:

- `Mamba` as the narrow always-on Layer 2-adjacent listener
- `Intuition` as a later signal evaluator on top of Mamba
- bounded routing into more expensive downstream work
- performance and reliability hardening

`Mamba` remains narrow.

It is not:

- the general reflection engine
- the document decomposition engine
- a universal semantic subsystem

## Service Roles

### OpenClaw

- runtime shell
- sessions
- transcript continuity
- hooks
- compaction
- tool execution

### Cortex Integration Layer

- policy composition
- bounded context assembly
- boundary-triggered semantic processing
- notion staging and cleanup rules
- Layer 3 and Layer 4 orchestration
- reflection and Dream orchestration

Default Phase 1 deployment shape:

- one separate `cortex` service
- not folded into the UI process
- not folded into the `graphiti` service

On the live appliance, this layer should fit into the current operator model:

- prove changes in `test` first
- keep `prod` protected
- use `moltbox service ...` for service-plane changes
- use native `moltbox test|prod openclaw ...` for runtime mutation
- prefer `moltbox test verify runtime|web` and `moltbox prod verify runtime` for routine validation

### QMD

- hot working-memory retrieval
- notion storage
- short-horizon cross-thread continuity under tighter retrieval rules

`QMD` must stay lean.

### Graphiti + Neo4j

- Layer 3 durable semantic memory
- concept relationships
- support
- supersession
- invalidation

Default Phase 1 deployment shape:

- one separate `graphiti` service
- backed by `neo4j`
- not folded into the `cortex` service

### Postgres

- Layer 4 operational knowledge bodies
- reference summaries and links
- decomposed artifact knowledge
- workflow and dirty-state fields
- retention metadata for later cold-storage migration
- operational evidence-control state where needed by the implementation

### Git

- Layer 5 `authored_artifact` backend in the artifact-promotion phase and later

### Mamba Later

When Phase 5 arrives, `Mamba` adds:

- always-on Layer 2-adjacent high-signal listening
- typed semantic event production
- bounded routing into more expensive downstream work
- stronger infinite-context-like continuity for long-running sessions
- better near-time triggers and live memory quality
- better directional signal for Reflection and Dream

It does not replace deeper evidence-backed maintenance passes.

## Bring-Up Order

### Phase 0 Bring-Up

1. `OpenClaw`
2. local model
3. safe baseline config
4. `QMD`

### Phase 1 Bring-Up

5. Layer 5 runtime-evidence store
6. `Postgres`
7. `Neo4j`
8. `Graphiti`
9. Cortex integration layer
10. Reflection and Dream hooks

For live appliance work, steps `6` through `9` are explicit service-plane additions beyond the current baseline.

They should be introduced through tracked Moltbox repo changes, with baseline service definitions in `moltbox-services`, promoted runtime artifacts in `moltbox-runtime`, and Gateway doc changes only when the operator-facing contract actually changes, then deployed through the official service-plane path rather than treated as host-only drift.

The current intended Phase 1 service set for that expansion is:

- `postgres`
- `neo4j`
- `graphiti`
- `cortex`

### Later Bring-Up

11. reference-decomposition workers
12. owned-source sync and dirty-state machinery
13. `Git`-backed artifact flow
14. narrow `Mamba` listener
15. `Intuition`

## MVP Simplicity Rule

The architecture should avoid unnecessary service sprawl in the early phases.

That means the early phases explicitly exclude:

- `OpenSearch`
- a second graph system
- a second Graphiti usage pattern
- a giant separate external working-memory service
- live always-on `Mamba`

## Bottom Line

The deployment shape is intentionally progressive:

- Phase 0 establishes vanilla OpenClaw
- Phase 1 proves the chat-derived Cortex loop
- Phase 2 adds one-way references
- Phase 3 adds maintained owned sources
- Phase 4 adds authored canon
- Phase 5 optimizes the whole system with Mamba and Intuition

For live appliance delivery, that progression must still respect the current Moltbox operator contract until it is intentionally broadened.
