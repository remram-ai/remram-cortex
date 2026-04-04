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

The preferred Layer 2 memory posture inside OpenClaw is:

- keep sessions and compaction OpenClaw-native
- prefer the `QMD` memory engine over the builtin engine if local resources and ops posture allow
- treat `Honcho` and `Dreaming` as informative reference points, not the main Cortex durable-memory center

### Policy In Cortex

Policy remains custom because it is where Cortex-specific behavior lives:

- mode composition
- prompt-budget discipline
- approval rules
- mutable preference-policy
- routing logic

But the split inside Layer 1 should be sharper than before:

- hard runtime and tool-use enforcement should stay as close as possible to OpenClaw agent or plugin configuration
- Cortex policy should focus on composition, preference-policy, routing, approval posture, and prompt-budget discipline

### High-Signal Mamba Stream

The Mamba stream is the main semantic checkpoint surface.

It exists to:

- keep smaller-window models viable
- avoid raw transcript replay as the normal consumer path
- stage notions for durable memory
- support oversight and nightly reconciliation

`Mamba` here is an architectural role, not yet a locked implementation choice.

The important commitment is:

- rolling semantic compression
- typed checkpoints
- source-linked rebuildability

The exact model or library can still change as long as it preserves that contract.

The compute posture should also be clearer:

- semantic checkpoint production should run continuously
- optimistic GPU offload should be spent on embeddings, graphizing, chunking, and near-time enrichment
- checkpoint and nightly passes should be allowed to revisit full evidence plus semantic checkpoints plus staged notions

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
- JSON and JSONB document support for transcript and evidence packaging

If later lexical retrieval requirements exceed what this posture handles well, a dedicated search layer can be added deliberately.

That is an intentional tradeoff:

- start with one operational Layer 4 platform
- measure where it breaks
- only then add a second search substrate

The first escalation path, if Layer 4 retrieval pressure outgrows this posture, is `OpenSearch`.

That would be justified when:

- transcript or document retrieval becomes a dominant workload
- Postgres relevance tuning becomes too bespoke
- operational filters, hybrid ranking, or corpus scale clearly exceed the one-store posture

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
