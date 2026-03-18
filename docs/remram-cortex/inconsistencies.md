# Cortex Inconsistency Tracker

This file tracks contradictions and boundary ambiguities discovered during thread ingestion.

Keep the canonical model clean in [architecture.md](architecture.md). Record unresolved conflicts here until they are explicitly resolved.

## Active

### 1. Conversation Object Ownership Split

- Conflicting signals:
  - the proposed durable conversation layer conceptually lives in Cortex as a durable semantic continuity object
  - the same thread places attach vs fork assignment logic in orchestration
- Why it matters:
  - this determines whether conversation continuity is a memory-owned object, an orchestration-owned routing view, or a split contract across both layers
- Current lean:
  - if conversation objects exist, Cortex stores them
  - orchestration may supply assignment hints at runtime
  - Cortex should remain the durable owner in the target state
- Resolve by:
  - deciding whether conversation assignment is purely orchestration policy, purely Cortex memory logic, or a proposal-and-commit flow between them

### 2. Bootstrap Transcript Access Boundary

- Conflicting signals:
  - bootstrap ingestion is described as operating over historical OpenClaw transcripts to initialize continuity
  - the stronger service-boundary model says Cortex does not access OpenClaw internals directly and should consume transcript-derived evidence through controlled hooks, exports, or backfill jobs
  - the migration plan may also ingest existing memory or session files directly in read-only mode during early learning phases
- Why it matters:
  - this determines whether bootstrap is a read-only import job over exported history, a Gateway or Forge-managed read path, or a deeper coupling to runtime storage internals
- Current lean:
  - bootstrap should prefer Gateway, Forge, or OpenClaw-managed control-plane surfaces
  - read-only direct file ingestion may still be acceptable in early low-risk migration work
  - Cortex still should not become directly coupled to mutable runtime internals
- Resolve by:
  - defining the exact bootstrap source contract and whether migration-phase file ingestion is an implementation detail or a supported path

### 3. Migration-Phase Memory Authority

- Conflicting signals:
  - the target architecture says Cortex is the single durable knowledge authority
  - the migration plan allows OpenClaw-native memory or memory files to continue existing while Cortex learns to capture the same continuity safely
- Why it matters:
  - this affects rollout sequencing, retrieval trust, cutover rules, and when OpenClaw memory features can actually be disabled
- Current lean:
  - target state remains Cortex as the durable authority
  - early phases may dual-run or import from OpenClaw-managed memory artifacts for learning and onboarding
- Resolve by:
  - defining phase boundaries, cutover criteria, and what "confidence that we're capturing what we need" means operationally

## Resolved

### 1. Gateway Execution Ownership

- Earlier signals blurred Gateway into the execution layer.
- Resolved model:
  - Gateway is the control plane for OpenClaw deployment, snapshots, and safe operational change
  - OpenClaw is the runtime execution layer
  - Gateway does not query knowledge directly

### 2. `/ingest` vs `/reflect` Mutation Boundary

- Earlier signals were inconsistent about which write path mutates durable memory.
- Resolved model:
  - `/ingest` and `/reflect` both mutate Cortex state
  - `/ingest` handles deterministic structured capture and may create low-confidence imported candidates
  - `/reflect` runs directly after a chat turn, compresses functional thread memory, emits structured deltas, and flags new outputs for Dream review

### 3. Promoted Artifact Authority Tier

- Earlier signals conflicted on whether promoted artifacts were merely derived or also authoritative.
- Resolved model:
  - knowledge objects remain canonical memory
  - promoted artifacts live in a local Git-backed artifact store as canonical document history
  - reindexed artifacts are higher-authority document sources, not replacements for knowledge-object storage

### 4. Dream vs Prompt-Policy Boundary

- Earlier signals risked implying Dream directly mutates prompts.
- Resolved model:
  - Dream adjudicates and enriches memory
  - prompt enhancement comes from layered retrieval at prompt-build time
  - orchestration still owns prompt policy and final prompt construction

### 5. Gateway Retrieval Consumer Boundary

- Earlier signals implied Gateway might directly consume retrieval bundles.
- Resolved model:
  - Orchestration calls Cortex for retrieval
  - the App reads Cortex through the API
  - Gateway does not query knowledge directly
