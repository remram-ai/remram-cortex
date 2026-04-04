# Runtime And Data Lifecycles

## Why This Document Exists

The architecture is easier to understand when viewed as flows rather than only as layers.

This document explains the main flows.

## Flow 1: Live Session To Durable Memory

1. OpenClaw runs the live session.
2. The session transcript acts as the base evidence surface.
3. Cortex policy shapes runtime behavior and context assembly.
4. The High-Signal Mamba Stream emits semantic checkpoints from the session evidence.
5. High-signal checkpoints may emit tentative notions.
6. Some notions may be written early as tentative cross-thread memory.
7. At session end or checkpoint, the evidence window closes into an immutable evidence package.
8. Reconciliation checks tentative notions against evidence, oversight, existing memory, and artifact support.
9. Confirmed outputs become trusted Layer 3 memory in Graphiti.

Clarification:

- the semantic checkpoint stream is always-on infrastructure
- checkpoints and nightly passes can revisit full evidence plus summaries plus staged notions

## Flow 2: Cross-Thread Memory

1. A checkpoint emits a strong notion.
2. The system writes it as tentative cross-thread memory.
3. Another thread can see it under tighter retrieval rules.
4. Reconciliation later upgrades, merges, downgrades, or rejects it.

The key idea is:

- cross-thread continuity is allowed
- false certainty is not

## Flow 3: Session Closure

1. A natural boundary happens such as session end, checkpoint, `/stop`, `/reset`, or compaction-triggered closure.
2. Cortex closes the evidence window.
3. The raw evidence package is persisted, usually in Postgres.
4. A compact semantic package is prepared for Graphiti.
5. Notions are reconciled.
6. Oversight signals are applied.
7. Durable memory is updated.

Later, older evidence packages should migrate out of hot Postgres into colder storage while retaining lookup metadata.

This is the main quality-control point for Layer 3.

## Flow 4: Artifact Ingestion

1. A canonical artifact exists in Git or another approved provider.
2. Cortex assigns or resolves its anchor identity.
3. The artifact revision is decomposed into Layer 4 knowledge.
4. Layer 4 gains slices, embeddings, lexical fields, and source-linked structures.
5. Layer 3 receives only compact summary plus pointer plus Layer 3 appropriate beliefs or support.

This is how artifacts become usable without shoving whole documents into durable memory.

## Flow 5: Artifact Change During Active Work

1. The user or system updates the operational understanding of an artifact.
2. Layer 4 changes ahead of Layer 5.
3. The anchor is marked dirty.
4. Layer 3 may update support relationships or semantic beliefs as appropriate.
5. A later redraft process gathers the latest Layer 4 and Layer 3 state.
6. The canonical artifact is updated in Layer 5.
7. The new revision is re-ingested.

This is how the system supports live change without collapsing publication truth.

## Flow 6: Retrieval

1. The system starts from policy and the active task.
2. Layer 3 durable memory provides semantic orientation.
3. Linked anchors identify relevant artifacts or knowledge sources.
4. Layer 4 decomposition provides precise retrieval-ready evidence.
5. Layer 5 canonical artifacts are consulted only when publication-grade source material is actually needed.

The intended retrieval order is:

1. Layer 3
2. anchor selection
3. Layer 4
4. Layer 5 on demand

## Flow 7: Nightly Maintenance

1. The system reprocesses the High-Signal Mamba Stream more deeply.
2. Oversight checks suspicious outputs.
3. Reconciliation confirms or rejects tentative memory.
4. Contradictions and stale support can be analyzed.
5. Dirty artifacts can be queued for redraft.
6. Layer 3 maintenance or Dream-style work can consolidate memory.

Nightly work is where the architecture cashes in slower, higher-quality processing.

## The Big Picture

Every flow follows the same principle:

- capture raw evidence
- create semantic checkpoints
- stage semantic outputs
- reconcile before trusting
- keep canonical truth separate from operational derived views

That recurring pattern is what makes the whole stack coherent.
