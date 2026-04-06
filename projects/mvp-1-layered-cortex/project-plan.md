# Project Plan

## Framing

This is not just a build sequence.

It is a progressive activation of Cortex system loops:

1. `Phase 0` baseline
2. `Phase 1` evidence loop
3. `Phase 2` reference loop
4. `Phase 3` collaborative source-maintenance loop
5. `Phase 4` artifact loop
6. `Phase 5` optimization loop

Each phase:

- introduces a new kind of input or source
- activates a new transformation loop
- upgrades what the system can treat as source-of-record

## Current Execution Posture

The immediate build target is:

- `Phase 0` baseline
- then `Phase 1` chat-derived Cortex memory

Later phases remain part of the same project package so the implementation can be sequenced without architectural churn.

## Live Appliance Authority

When this project targets the live Moltbox appliance:

- `moltbox-gateway` is the source of truth for current appliance behavior
- older Cortex or `remram` docs do not override the Gateway repo for live appliance work
- `test` is the proving lane
- `prod` is a protected managed pet
- normal service-plane mutation uses `moltbox service ...`
- normal runtime mutation uses native `moltbox test|prod openclaw ...`
- routine validation should prefer `moltbox test verify runtime|browser|web` and `moltbox prod verify runtime`
- raw Docker, break-glass SSH, replay-era runtime ownership, and the old Playwright detour are not the intended baseline

This project can describe future Phase 1 services such as `Postgres`, `Neo4j`, `Graphiti`, and a Cortex service boundary, but those are future service-plane additions, not live-baseline facts.

Those service additions are allowed as part of this project.

The constraint is that they must land through the tracked Moltbox path:

- service definitions, baseline config, and service-local docs in `moltbox-services`
- promoted runtime-layer changes in `moltbox-runtime`
- official Gateway docs only when the operator contract or workflow changes
- deploy and validation through the normal `moltbox` operator surface

## Source-Of-Truth Evolution

| Phase | Primary Source Of Truth |
| --- | --- |
| `Phase 0` | OpenClaw runtime only |
| `Phase 1` | chat-derived meaning from runtime evidence |
| `Phase 2` | chat plus decomposed references |
| `Phase 3` | maintained owned source documents |
| `Phase 4` | authored artifacts in canon |
| `Phase 5` | same sources, with better live signal and efficiency |

## Phase 0: OpenClaw Baseline

### Goal

Stand up a safe, mostly vanilla OpenClaw baseline with a local model and public, out-of-the-box memory posture.

### New Loop Activated

No Cortex loop yet.

This is the baseline runtime and memory posture that Cortex will extend.

### System Change

Phase 0 gives the system:

- OpenClaw runtime
- local-model execution
- safe baseline config
- session pruning and compaction
- `QMD` enabled as baseline OpenClaw memory

### User-Visible Behavior

The assistant chats, uses tools, and has baseline OpenClaw memory and continuity.

It is useful, but it is not yet Cortex.

### Definition Of Done

- OpenClaw runs locally and reliably
- safe baseline config is checked in
- `QMD` is enabled
- compaction and pruning behave predictably
- the baseline can be demonstrated before Cortex-specific behavior is added
- if proven on the live appliance, the baseline is validated through the official `test` operator surfaces rather than host-only drift

### Non-Goals

- Graphiti durable memory
- Cortex reflection
- Layer 4 operational knowledge
- Layer 5 evidence system beyond baseline runtime behavior
- artifacts, dirty state, or Mamba

## Phase 1: Chat Memory Loop

### Goal

Prove the full Cortex loop from:

`chat -> evidence -> decomposition -> reflection -> durable meaning`

### New Loop Activated

The evidence loop.

### System Change

Phase 1 adds Cortex-owned behavior on top of the Phase 0 baseline:

- Layer 1 policy overlays
- Layer 5 chat-evidence store with a stable interface
- turn-end, session-end, and checkpoint-triggered semantic processing
- Layer 4 chat-derived support bodies
- Reflection and Dream over chat-derived evidence
- Layer 3 durable semantic memory in Graphiti

### Inputs

- chat transcripts only

### Layer Shape

- Layer 1 = basic Cortex policy
- Layer 2 = OpenClaw session surface plus `QMD`
- Layer 3 = Graphiti durable memory
- Layer 4 = real but narrow chat-derived operational bodies
- Layer 5 = filesystem-backed runtime evidence only

Layer 4 in Phase 1 should support:

- conversation-level and segment-level summaries
- concept support bodies
- fact and belief candidates
- retrieval and index records
- evidence pointers back to Layer 5
- lightweight clustering scaffolds when useful

### User-Visible Behavior

Cortex starts learning from conversation.

In practice, that means:

- it remembers important facts, preferences, and recurring concepts
- continuity improves across sessions
- important ideas from chat stop disappearing with compaction

### Definition Of Done

- chat transcripts are captured into Layer 5 through a stable interface
- semantic processing yields usable Layer 4 chat-derived bodies
- Reflection can stage and clean notions
- Dream can consolidate chat-derived memory on a slower cadence
- Graphiti stores durable concepts and relationships without becoming a body store
- cross-session continuity is observably better than Phase 0
- if proven on the live appliance, the change is safe to keep in `test` and can be validated without bypassing the Gateway operator contract

### Non-Goals

- external reference ingestion
- owned document sync
- dirty-state dual-version semantics
- Git-backed authored canon
- Mamba or Intuition

## Phase 2: Reference Decomposition Loop

### Goal

Introduce one-way outside material so Cortex can reason over decomposed references, not only chat.

### New Loop Activated

The reference loop.

### System Change

Phase 2 adds reference intake and decomposition on top of the chat-memory spine.

### Inputs

- uploaded reference documents
- web links and fetched page snapshots

Both inputs use the same decomposition spine.

### User-Visible Behavior

You can attach a document or hand Cortex a link, and the system can later reason over the useful structure instead of treating it as one-off context.

### Definition Of Done

- uploaded references are ingestible
- web links can be fetched into one-way snapshots
- references decompose into Layer 4 knowledge bodies
- Layer 3 keeps only durable meaning that survives decomposition
- retrieved reference knowledge can ground later chat

### Non-Goals

- source ownership semantics
- dirty-state dual-state maintenance
- authored artifact promotion
- Git-backed canon

## Phase 3: Collaborative Source Maintenance Loop

### Goal

Turn owned high-signal documents into living maintained sources instead of one-way ingested material.

### New Loop Activated

The collaborative source-maintenance loop.

### Inputs

- owned high-signal "file cabinet" documents such as:
  - business plans
  - ideas
  - scripts
  - budgets
  - structured personal documents

Explicit exclusions:

- code
- ephemeral notes
- most external references

### System Change

Phase 3 introduces dirty state as a real data model expansion.

It is not just a flag.

The system now tracks:

- current version
- derived version
- diff and reconciliation surface

### User-Visible Behavior

Owned documents become maintainable working sources.

In practice, that means:

- Cortex can help keep important source documents current
- derived knowledge no longer drifts silently away from owned source material
- source updates can trigger reprocessing and semantic reconciliation

### Definition Of Done

- owned documents ingest through the Layer 5 evidence system
- dirty-state dual-version tracking exists
- source changes trigger reprocessing into Layer 4
- Layer 3 reconciles against those updates cleanly
- maintained documents feel like living sources, not static uploads

### Non-Goals

- promotion of new authored canon from idea clusters
- Mamba and Intuition

## Phase 4: Artifact Promotion Loop

### Goal

Turn accumulated Layer 3 and Layer 4 work into authored artifacts in canon.

### New Loop Activated

The artifact loop.

### System Change

Phase 4 introduces:

- promotion candidate detection
- artifact drafting
- Git-backed canonical authored artifacts
- bottom-up reprocessing from authored canon back into Layer 4 and Layer 3

### User-Visible Behavior

The system starts producing maintainable assets, not just memories and decomposed knowledge.

In practice, that means:

- ongoing work can be promoted into authored outputs
- promoted artifacts become the canonical source for that body
- later artifact edits flow back down into the working and semantic layers

### Definition Of Done

- Layer 3 and Reflection can identify promotion candidates
- authored artifacts can be drafted and stored in Git
- authored artifacts re-ingest back into Layer 4
- Layer 3 support, summaries, and relationships reconcile from artifact updates
- promoted outputs are maintainable over time

### Non-Goals

- always-on Mamba optimization
- Intuition-driven opportunistic processing

## Phase 5: Optimization Loop

### Goal

Improve signal quality, latency, and processing efficiency without changing the fundamental architecture.

### New Loop Activated

The optimization loop.

### System Change

Phase 5 introduces:

- Mamba as a narrow always-on signal layer
- Intuition as a later signal evaluator on top of Mamba
- better near-time wake-ups for expensive downstream work
- performance and hardening work across the stack

### User-Visible Behavior

The system behaves more like it has persistent context without brute-force replay.

In practice, that means:

- smoother long-running sessions
- better timing on what gets noticed and processed
- lower latency for high-value memory updates
- more efficient downstream reflection and Dream targeting

### Definition Of Done

- Mamba produces useful high-signal outputs without becoming a reasoning engine
- Intuition can trigger bounded opportunistic processing when headroom exists
- reflection and Dream are measurably better targeted
- the same architecture runs more efficiently and with less drift

### Non-Goals

- redefining layer boundaries
- replacing reflection
- replacing Dream
- turning Mamba into a universal semantic subsystem

## Why This Order

- Phase 0 establishes a baseline that proves what OpenClaw already gives us.
- Phase 1 proves the full Cortex memory loop using chat-derived evidence only.
- Phase 2 adds one-way decomposition before ownership and sync complexity.
- Phase 3 introduces real source maintenance only when the system can already decompose and retrieve well.
- Phase 4 adds authored canon after source-sync and decomposition are already stable.
- Phase 5 optimizes an already-working system instead of becoming a hidden dependency.
