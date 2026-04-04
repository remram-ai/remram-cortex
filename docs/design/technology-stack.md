# Technology Stack

This document records the active Cortex stack.

It is not a comparison memo.

It describes the technologies the repository is currently being organized around.

## Chosen Stack

- `OpenClaw` for runtime execution and Layer 2 working-memory mechanics
- Cortex-owned `Policy` layer above OpenClaw
- High-Signal `Mamba` stream for semantic checkpointing and rolling compression
- `Graphiti + Neo4j` for Layer 3 durable memory
- `Postgres + pgvector` for:
  - runtime evidence
  - control-plane state
  - Layer 4 decomposed knowledge
- `Git` for Layer 5 canonical artifacts

## Why This Stack

### OpenClaw

OpenClaw already owns:

- sessions
- hooks
- compaction
- context-engine surfaces
- runtime execution

That makes it the right Layer 2 base.

Cortex should augment it rather than replace it.

### Policy In Cortex

Policy remains custom because it is where Cortex-specific behavior lives:

- mode composition
- prompt-budget discipline
- approval rules
- mutable preference-policy
- routing logic

### High-Signal Mamba Stream

The Mamba stream is the main semantic checkpoint surface.

It exists to:

- keep smaller-window models viable
- avoid raw transcript replay as the normal consumer path
- stage notions for durable memory
- support oversight and nightly reconciliation

### Graphiti + Neo4j

This remains the chosen Layer 3 posture because it gives:

- temporal durable memory
- episode-backed provenance
- invalidation and supersession semantics
- graph-native retrieval over durable memory

`Neo4j` is the durable graph backend because it is disk-backed and better aligned with integrity than an in-memory primary graph store.

### Postgres + pgvector

This is the default Layer 4 substrate because it gives:

- typed relational control
- evidence storage
- revision-aware decomposition records
- vector search without introducing a second major platform
- lexical search through native Postgres full-text capabilities
- a credible hybrid-search posture inside one operational store

If later lexical retrieval requirements exceed what this posture handles well, a dedicated search layer can be added deliberately.

That is an intentional tradeoff:

- start with one operational Layer 4 platform
- measure where it breaks
- only then add a second search substrate

### Git

Git remains the canonical artifact truth because it gives:

- reviewable revisions
- explicit publication
- clear promotion boundaries
- inspectable history

## Stack Summary

The design rule is:

- let OpenClaw do Layer 2
- let Cortex own policy and semantic checkpointing
- let Graphiti own durable semantic memory
- let Postgres own evidence and decomposed operational knowledge
- let Git own publication truth
