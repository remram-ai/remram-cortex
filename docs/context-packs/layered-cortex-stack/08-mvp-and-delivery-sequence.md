# MVP And Delivery Sequence

## Delivery Posture

The architecture is now delivered as a progressive activation of system loops.

The key sequencing move is that the baseline comes first, then Cortex proves itself on chat, then on references, then on maintained sources, then on authored canon, and only later on optimization.

## Phase 0: OpenClaw Baseline

Goal:

- prove the vanilla OpenClaw baseline with a local model, safe config, compaction, pruning, and `QMD`

User-visible behavior:

- the assistant chats and uses tools
- baseline OpenClaw memory works
- there is no Cortex-specific reflection, Graphiti memory, or Layer 5 evidence loop yet

## Phase 1: Chat Memory Loop

Goal:

- prove the full Cortex loop from chat into memory

System change:

- Layer 5 runtime evidence for chat transcripts
- boundary-triggered semantic processing
- Layer 4 chat-derived support bodies such as summaries, concept support bodies, and fact or belief candidates
- Reflection and Dream over chat-derived evidence
- Layer 3 durable memory

User-visible behavior:

- Cortex starts remembering important facts, preferences, and recurring concepts from conversation
- continuity improves across sessions

## Phase 2: Reference Decomposition Loop

Goal:

- make one-way outside material usable

Inputs:

- uploaded reference documents
- web-link snapshot fetches

This phase is still one-way.

It does not yet add source-sync or dirty-state semantics.

User-visible behavior:

- attached documents and links become usable knowledge in later conversations

## Phase 3: Collaborative Source Maintenance Loop

Goal:

- maintain owned high-signal documents as living sources

System change:

- dirty-state dual-version semantics
- source-sync and reprocessing
- Layer 4 and Layer 3 alignment against owned-source updates

This is the phase where "file cabinet" documents become living maintained sources rather than static uploads.

User-visible behavior:

- important owned documents stop being static uploads and become maintainable working sources

## Phase 4: Artifact Promotion Loop

Goal:

- promote clustered work into authored canon

System change:

- promotion candidate detection
- artifact drafting
- Git-backed authored artifacts
- bottom-up reprocessing from canon back into Layer 4 and Layer 3

User-visible behavior:

- the system can turn ongoing work into maintained authored outputs

## Phase 5: Optimization Loop

Goal:

- improve signal quality, efficiency, and live-session behavior

System change:

- `Mamba` as the narrow always-on signal layer
- `Intuition` as the later signal evaluator on top of Mamba

User-visible behavior:

- the system feels more responsive and more continuous without brute-force replay

## What Stays Locked

The core architecture decisions still stand:

1. `QMD` is the Layer 2 hot working-memory substrate and notion store.
2. Tentative cross-thread memory is allowed under tighter retrieval rules but is not silently authoritative before reconciliation.
3. `Postgres` remains the operational middle-layer authority.
4. `OpenSearch` is still deferred.
5. `Graphiti + Neo4j` remains the Layer 3 durable memory system.
6. Layer 4 remains the operational knowledge authority.
7. Layer 5 remains the source-of-record evidence layer, with authored canon as one special class when publication is warranted.

## Bottom Line

The sequencing now reads:

- Phase 0 proves the vanilla OpenClaw baseline
- Phase 1 learns from chat
- Phase 2 understands references
- Phase 3 maintains owned sources
- Phase 4 promotes authored artifacts
- Phase 5 optimizes the same system
