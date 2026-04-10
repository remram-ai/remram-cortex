# Glossary

This glossary is the canonical terminology source for active Cortex docs.

If a term here conflicts with the architecture or concept docs, update them together.

## Preferred Language Rules

- Use `context` only for bounded runtime injection, not as a synonym for durable memory, operational knowledge, or Layer 2 as a whole.
- Use `Working Memory` for Layer 2, even when the runtime bundle being assembled is context.
- Use `authored_artifact` as the precise Layer 5 evidence-class term. `Authored canon` is acceptable shorthand for the publication-grade subset.
- Use `Dream` as the preferred short form. `Dream Cycle` remains an acceptable longer form.
- Treat `artifact` as an umbrella word only when precision does not matter. Prefer `runtime_evidence`, `reference_cache`, `authored_artifact`, `owned source`, or `workspace` when the exact class matters.
- Treat `Typed Signals`, `Semantic Signature`, and `Conversation Layer` as retained or deferred concepts unless a doc explicitly locks them for implementation.

## A

### Anchor

A stable Cortex identity used to connect related records across layers.

Anchors keep the same real-world thing linked across Layer 3 meaning, Layer 4 bodies, and Layer 5 evidence.

### Anchor ID

The stable identifier that carries an anchor across layers and revisions.

### Artifact

An umbrella term for a retained source or authored body.

It is intentionally imprecise. In active design docs, prefer the exact class when the distinction matters.

### Artifact Intake

The Layer 5 to Layer 4 intake path for non-runtime source material.

It stores source bodies in Layer 5, derives bounded operational forms into Layer 4, and leaves durable semantic conclusions to Layer 3.

### Artifact Promotion

The Layer 4 to Layer 5 publication path that turns stabilized operational work into an `authored_artifact`.

### Artifact Provider

The backend that stores or resolves a Layer 5 evidence body.

`Git` is one provider for `authored_artifact`, but Layer 5 is not defined by Git alone.

### Authored Artifact

The Layer 5 evidence class used for publication-grade, revisioned, intentionally retained authored output.

This is the precise term for the authored-canon subset of Layer 5.

### Authored Canon

Human shorthand for the publication-grade `authored_artifact` subset of Layer 5.

Use `authored_artifact` when the evidence-class contract matters.

## B

### Bounded Retrieval

The rule that runtime injection must stay small, deliberate, inspectable, and governance-bounded before ranking happens.

## C

### Chronicle

A longitudinal human-readable continuity body that summarizes a person, household, project, or topic over time.

Chronicles are typically Layer 4 operational bodies, with Layer 3 storing durable conclusions and Layer 5 storing supporting evidence.

### Context

The bounded information injected into a live runtime step.

Context is assembled from policy, hot continuity, durable-memory orientation, and Layer 4 knowledge pointers. It is not the same thing as memory.

### Conversation Layer

A retained deferred concept for a semantic continuity surface between sessions and durable memory.

It is not part of the locked MVP 1 architecture.

### Cortex

The Remram knowledge authority layer.

## D

### Dimension

A legacy Cortex umbrella term from earlier drafts.

It has been replaced by `Governance Fields`, `Typed Signals`, and `Semantic Signature`.

### Dream

The slower consolidation and maintenance path that revisits Layer 3 and Layer 4 state over longer horizons.

It deduplicates, hardens support, reconciles drift, and detects promotion readiness.

### Dream Cycle

Acceptable longer form of `Dream`.

Prefer `Dream` in active docs.

### Durable Memory

Layer 3 durable semantic memory that persists beyond sessions, compaction, and hot-memory pruning.

## E

### Evidence

Source material the system can learn from, such as transcripts, tool outputs, fetched references, files, photos, or authored artifacts.

### Evidence Layer

Layer 5, the source-of-record evidence layer.

Its main classes are `runtime_evidence`, `reference_cache`, and `authored_artifact`.

### Evidence Package

A closed, immutable, source-linked record used for audit, replay, reconciliation, and provenance.

### External Reference Material

Reference material the user does not necessarily own or intend to canonize, such as PDFs, articles, web snapshots, podcasts, or research sources.

### Reference Cache

The Layer 5 evidence class used to retain external reference bodies long enough for processing, reuse, and audit.

It follows different retention and promotion rules than authored artifacts.

### Runtime Evidence

The Layer 5 evidence class derived from sessions, transcripts, tool outputs, and other runtime activity.

## G

### Governance Fields

Hard-bounding fields that decide whether something is eligible before semantic ranking begins.

They carry exact or bounded scope rules such as ownership, audience, person, household, family, provider, project, or lifecycle boundaries.

### Governance Scope

The stable scope boundary expressed through governance fields.

Examples include person, household, family, project, organization, provider, or system scope.

## H

### High-Signal Mamba Stream

The later always-on, narrow, Layer 2-adjacent high-signal channel built from live session activity.

It is deferred until the optimization phase.

## I

### Idea Cluster

A Layer 3 grouping that links related threads, workspaces, or concepts belonging to the same emerging idea or continuity line.

### Incubation Workspace

A Layer 4 workspace that is still evolving, incomplete, and operationally authoritative without yet warranting publication-grade canon.

### Intuition

A future Mamba-side signal evaluator that decides when high-signal windows should wake hotter layered ingestion or opportunistic downstream work.

It is blocked by `Mamba` and is not part of the base Phase 1 architecture.

## K

### Knowledge Authority

The authority allowed to decide what becomes durable semantic truth.

In Remram, that authority is Cortex.

### Knowledge Object

A durable memory record such as a belief, preference, constraint, correction, decision, principle, or procedure.

It is the concrete stored record Cortex uses to hold memory.

## M

### Mamba

The implementation-family shorthand for the later always-on high-signal sensing role in Cortex.

In active docs, `Mamba` refers to the narrow Layer 2-adjacent signal producer role, not a commitment to one exact checkpoint family or model release.

## N

### Notion

A hot staged candidate durable memory stored in Layer 2 as part of the `QMD` working-memory surface.

It is provisional, source-linked, and eligible for reconciliation into Layer 3.

## O

### Operational Knowledge

Layer 4 operationally authoritative knowledge bodies, including workspaces, reference-derived knowledge, chronicle bodies, needs workspaces, and decomposed artifact knowledge.

### Owned Source

Source material the user intentionally retains as part of their evidence corpus and expects to maintain over time.

Owned sources have stronger retention and source-maintenance posture than generic references.

## P

### Policy

Layer 1 behavior and control logic, including modes, tool policy, approval rules, escalation posture, and mutable preference-policy.

### Provenance

The support and source trail that explains where memory or operational knowledge came from.

## Q

### QMD

The explicit Layer 2 hot working-memory substrate in the active Cortex stack.

`QMD` supports hot retrieval, notion storage, and bounded cross-thread continuity under tighter rules. It is not a second durable-memory system.

## R

### Reconciliation

The trust-boundary process that decides whether tentative working-memory outputs become trusted durable memory.

It runs at checkpoints such as session end and slower maintenance windows.

### Reflection

The near-time interpretation and maintenance path that updates notions, keeps Layer 2 lean, updates Layer 4 operational bodies, and contributes to promotion readiness.

### Reference Material

External or retained source material introduced for operational use, learning, or grounding.

Depending on posture, it may land as `reference_cache` or as stronger owned-source evidence.

## S

### Semantic Checkpoint

A typed, source-linked continuity object emitted by boundary-triggered semantic processing in early phases and later by the High-Signal Mamba Stream.

### Semantic Signature

A retained deferred retrieval concept for coarse semantic routing.

It is not a locked Phase 1 implementation commitment.

### Source Of Record

The layer role that owns persisted evidence bodies without owning their semantic meaning.

In Cortex, this is Layer 5.

## T

### Typed Signals

A retained deferred retrieval concept for structured semantic retrieval fields.

It is not a locked Phase 1 implementation commitment.

## W

### Working Memory

Layer 2 hot working continuity.

In the active design, it is OpenClaw-centered, uses `QMD` for hot retrieval and notions, and is augmented by Cortex rather than replaced.

### Workspace

A medium-horizon Layer 4 operational body that may span many threads and evolve before publication-grade authorship is warranted.

Workspaces may be idea bodies, chronicle bodies, needs workspaces, coordination dossiers, or other operational knowledge surfaces.
