# Deployment Plan

This document records the active deployment posture after design lock.

## Base Deployment Shape

The near-term stack includes:

- `OpenClaw`
- Cortex policy and integration layer
- `QMD` as the Layer 2 hot working-memory substrate inside the OpenClaw posture
- a narrow always-on High-Signal `Mamba` listener
- `Graphiti`
- `Neo4j`
- `Postgres`
- `Git` when canonical artifact publication is warranted

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
- notion staging rules
- Layer 3 and Layer 4 orchestration
- reflection and Dream orchestration

### QMD

- hot working-memory retrieval
- notion storage
- short-horizon cross-thread continuity under tighter retrieval rules

`QMD` must stay lean.

### Mamba Listener

- always-on Layer 2-adjacent high-signal listening
- typed high-signal stream production
- bounded routing into more expensive downstream work

This listener should remain narrow.

It is not the broad document decomposition engine.

### Graphiti + Neo4j

- Layer 3 durable semantic memory
- concept relationships
- support
- supersession
- invalidation

### Postgres

- runtime evidence authority
- Layer 4 operational knowledge bodies
- reference summaries and links
- decomposed artifact knowledge
- retrieval metadata
- workflow and dirty-state fields
- retention metadata for later cold-storage migration

### Git

- canonical publication truth when canon is warranted

## Evidence Retention

Runtime evidence should stay hot only for a bounded recent window.

Active posture:

- keep full transcripts hot for roughly `90` to `120` days since last access
- then move them to cold storage
- keep compact metadata and semantic checkpoints hot much longer

## Bring-Up Order

1. `OpenClaw`
2. `Postgres`
3. `Neo4j`
4. `Graphiti`
5. Cortex integration layer
6. `QMD`
7. narrow Mamba listener
8. Git-backed canonical artifact flow when applicable

## MVP Simplicity Rule

The architecture should avoid unnecessary service sprawl.

That means MVP explicitly excludes:

- `OpenSearch`
- a second graph system
- a second Graphiti usage pattern
- a giant separate external working-memory service

## Bottom Line

The deployment shape is intentionally smaller and more opinionated now:

- OpenClaw at the framework center
- QMD for hot Layer 2 memory
- Graphiti + Neo4j for Layer 3
- Postgres for the operational middle
- Git only when canonical artifact publication is warranted
