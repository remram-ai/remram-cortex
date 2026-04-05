# MVP 1 Seed Prompt

Use the locked layered Cortex architecture for implementation work.

Do not reopen major architecture decisions unless the codebase or current upstream docs prove that a locked assumption is no longer viable.

## Initial Context To Read

Read these first, in order:

1. `docs/context-packs/layered-cortex-stack/README.md`
2. `docs/context-packs/layered-cortex-stack/00-high-signal-debrief.md`
3. `docs/context-packs/layered-cortex-stack/08-mvp-and-delivery-sequence.md`
4. `projects/mvp-1-layered-cortex/README.md`
5. `projects/mvp-1-layered-cortex/project-plan.md`
6. `projects/mvp-1-layered-cortex/acceptance-test.md`

Then use these canonical architecture docs as needed:

- `docs/design/layered-memory-architecture.md`
- `docs/design/openclaw-integration.md`
- `docs/design/graphiti-neo4j-durable-memory.md`
- `docs/design/knowledge-and-artifact-architecture.md`
- `docs/design/technology-stack.md`
- `docs/design/deployment-plan.md`

## Locked Architecture Summary

Assume:

- `OpenClaw` is the chosen agentic framework.
- Layer 1 is Cortex policy.
- Layer 2 is OpenClaw sessions plus `QMD` hot working memory and notions.
- Layer 3 is `Graphiti + Neo4j`.
- Layer 4 is operational knowledge.
- Layer 5 is source-of-record evidence.
- `Postgres` is the operational middle-layer authority.
- `Git` is only for the `authored_artifact` evidence class later, not the default destination for early work.
- `Mamba` and `Intuition` are later optimization-phase additions, not prerequisites for Phase 0 or Phase 1.

## Immediate Build Target

The immediate target is:

- `Phase 0` baseline
- then `Phase 1` chat memory loop

Phase 0 means:

- local OpenClaw running reliably
- safe baseline config
- `QMD` enabled
- pruning and compaction behaving predictably
- no Cortex-specific reflection or durable-memory loop yet

Phase 1 means:

- Layer 5 runtime-evidence capture for chat transcripts
- turn-end, session-end, and checkpoint-triggered semantic processing
- Layer 4 chat-derived support bodies
- Reflection and Dream over chat-derived evidence
- Layer 3 durable semantic memory in Graphiti
- improved cross-session continuity over the Phase 0 baseline

## Phase 1 Layer Boundaries

Implement with these boundaries:

- Layer 1 owns policy composition and runtime behavior shaping.
- Layer 2 owns hot continuity, notions, and `QMD` retrieval.
- Layer 3 owns durable concepts, identities, relationships, support, supersession, and invalidation.
- Layer 4 owns chat-derived support bodies such as:
  - conversation and segment summaries
  - concept support bodies
  - fact and belief candidates
  - retrieval or index records
  - evidence pointers back to Layer 5
- Layer 5 owns runtime evidence bodies, not semantic meaning.

Do not let:

- Layer 3 become a body store
- Layer 4 become Layer 5's lifecycle owner
- QMD become a shadow durable-memory system
- Mamba creep into the initial proof surface

## Implementation Posture

Build the smallest real implementation that proves the loop end to end.

Prefer:

- real boundaries over mock abstractions
- filesystem-backed Layer 5 runtime evidence first
- boundary-triggered semantic processing before any always-on signal system
- explicit evidence pointers and inspectable staging surfaces

Avoid:

- introducing `OpenSearch`
- inventing a second graph system
- pushing ideas into `Git` early
- broadening scope into Phase 2+ document or artifact work unless needed for Phase 1 correctness

## Definition Of Done For The First Thread

The first implementation thread should leave the repo with a clear path toward:

- OpenClaw Phase 0 baseline working locally
- a Cortex-owned Phase 1 evidence loop design translated into code scaffolding or initial implementation
- inspectable Layer 5 runtime evidence
- initial Layer 4 support-body schema
- initial Layer 3 integration contract
- explicit hooks for Reflection and Dream

If tradeoffs are needed, preserve architecture boundaries first and defer polish second.
