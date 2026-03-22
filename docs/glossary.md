# Glossary

This glossary locks the baseline Cortex vocabulary.

If a term here conflicts with the architecture or concept docs, update them together instead of letting parallel meanings survive.

## A

### Artifact

A durable file such as a document, image, plan, or decision record. When artifacts are imported, Cortex assigns them stable internal identity and resolves them through a configured provider. Artifacts may enter Cortex as evidence through import or leave Cortex as promoted outputs, but they are not the primary durable memory unit.

### Artifact Intake

The multimodal import path that reads external artifacts, creates a Cortex-managed artifact record, preserves source locations as provenance, and turns bounded evidence slices into source-linked knowledge updates.

### Artifact Provider

The configurable backend that stores or resolves artifact content for Cortex. Providers may include local Git, Google Workspace, or remote Git systems. Cortex keeps stable artifact identity and metadata above the provider layer.

### Artifact Promotion

The process of turning stabilized internal knowledge into a Cortex-managed human-facing artifact that can be reviewed, versioned, and reindexed through an artifact provider.

## B

### Bootstrap Ingestion

The historical backfill path that reads exported or otherwise controlled evidence in read-only mode and initializes Cortex before live reflection becomes the primary growth path.

### Bounded Retrieval

The Cortex rule that retrieval must be constrained by hard governance filters before semantic scoring. Cortex returns a small inspectable bundle, not an unbounded memory dump.

## C

### Confidence

A mutable ranking signal that expresses how strongly Cortex trusts a knowledge object right now. Confidence influences ranking, review priority, and reconciliation, but it does not itself grant execution authority.

### Conversation Object

A proposed continuity record that links related sessions without storing full transcripts. It lives beside knowledge objects and preserves semantic direction, recency, and continuity metadata.

### Cortex

The Remram knowledge authority service. Cortex owns durable memory, retrieval, reflection, Dream reconciliation, artifact intake, and artifact promotion.

## D

### Dimension

A legacy umbrella term from earlier drafts. The current model splits that older idea into harder [Governance Fields](#governance-field) and softer [Signal Fields](#signal-field).

### Dream

The scheduled reconciliation pass that reviews accumulated knowledge, resolves conflicts, normalizes retrieval cues, adjusts ranking signals, and identifies promotion candidates.

## E

### Eligibility

The rule that a memory item must satisfy scope, visibility, lifecycle, and other hard governance constraints before it may enter semantic ranking. Eligibility precedes similarity.

### Evidence

The raw material Cortex can learn from, such as transcripts, tool outputs, imported artifacts, or historical session exports. Evidence informs knowledge formation; it is not itself durable knowledge.

## F

### Functional Thread Memory

A dense operational summary of how a thread progressed and what state matters next. Reflection may emit this so later runs can retrieve continuity without replaying full chat history.

## G

### Gateway

The OpenClaw control plane used for deployment, snapshotting, and safe operational change. Gateway is not a runtime execution surface and does not query Cortex for retrieval.

### Governance Field

A hard-bounding field used to determine whether a knowledge object is even eligible for retrieval. Governance fields cover concerns such as ownership, audience, knowledge space, lifecycle state, and temporal validity. They are not open-ended semantic tags.

## H

### Hydrate

A historical replay mode that feeds prior sessions or chat exports through reflection-style processing to initialize useful continuity faster.

## K

### Knowledge Authority

The layer that decides what counts as durable memory and is allowed to mutate it. In Remram, Cortex is the knowledge authority.

### Knowledge Bundle

The structured output of Cortex retrieval. A bundle contains bounded knowledge chosen for a live run, along with enough provenance and ranking metadata for orchestration to use it deliberately.

### Knowledge Object

The primary technical durable memory unit in Cortex. A knowledge object is a structured claim, preference, constraint, decision, principle, procedure, or relation with provenance, governance fields, signal fields, ranking metadata, and links.

## L

### Local-first

The principle that Cortex should remain useful and durable on local infrastructure without depending on a remote control plane for ownership of memory.

## M

### Memory

The generic term for durable retained meaning in Remram. In Cortex, memory is stored primarily as knowledge objects plus any adjacent continuity objects such as conversation records.

## O

### OpenClaw

The Remram runtime execution system. OpenClaw owns sessions, transcripts, tool execution, and transcript compaction.

### Orchestration

The policy and prompt-assembly layer that decides when to retrieve from Cortex, what constraints to apply, and how retrieved knowledge influences runtime behavior.

## P

### Provenance

The traceable origin of a knowledge object or artifact, including the sessions, tools, imports, or documents that support it and any location metadata needed to get back to the source.

## R

### Reflection

The immediate post-run extraction pass that turns evidence into structured deltas. Reflection is where Cortex computes canonical statements, signal fields, links, and merge decisions so later retrieval can stay cheap.

### Relationship Expansion

The retrieval step that enriches a result set by following typed links between already-relevant knowledge objects. Relationship expansion augments primary retrieval; it does not replace it.

### Retrieval Trace

The inspectable debug record of how Cortex answered a retrieval request, including filters applied, score contributors, suppressed candidates, and final bundle composition.

## S

### Scope

The ownership and visibility boundary that determines which knowledge a caller is even allowed to see. Scope is part of governance, not a soft semantic hint.

### Semantic Signature

A compact 16-32 bit semantic routing code generated for both knowledge objects and queries. Signature similarity can bias retrieval or preselect candidates, but it is never the sole source of truth.

### Session

A runtime execution grouping owned by OpenClaw. Sessions are evidence sources and may belong to a longer-lived conversation, but they are not themselves durable knowledge objects.

### Signal Field

A fixed semantic channel used for primary retrieval scoring. Cortex currently centers retrieval around a small set of open-valued signal fields such as domain, activity, need, object, and mechanism.

### Statement

The canonical wording or structured payload Cortex stores for a knowledge object. Alternate wording may exist in provenance or retrieval cues, but the statement remains the canonical object surface.

## T

### Transcript

The append-only record of runtime interaction owned by OpenClaw. Transcripts are evidence, not knowledge, and Cortex must not become a second transcript store.

### Typed Signal Index

The OpenSearch retrieval surface formed by indexing each fixed signal field separately while allowing the values inside those fields to remain open natural language.
