# Glossary

This glossary locks the baseline vocabulary for the current Cortex architecture.

If a term here conflicts with another document, update the architecture and glossary together instead of letting two definitions coexist.

## A

### Artifact

A human-readable durable output such as a design document, plan, or decision record. In Cortex, artifacts may be imported as evidence or promoted from knowledge, but they are not the primary memory unit.

### Artifact Promotion

The process of turning stabilized knowledge into a Git-backed artifact that can be reviewed, versioned, and reindexed.

## B

### Bootstrap Ingestion

The historical backfill path that reads prior conversations or other evidence in read-only mode and initializes Cortex with structured knowledge before live reflection becomes the main growth path.

### Bounded Retrieval

The rule that retrieval must be constrained by scope and dimensions before ranking. Cortex retrieves an inspectable knowledge bundle, not an unbounded memory dump.

## C

### Candidate Dimension

A proposed retrieval axis discovered during reflection or import that is not yet part of the canonical dimension set. Dream may later promote it.

### Confidence

A mutable score that expresses how strongly Cortex trusts a knowledge object. Confidence influences ranking, review, and reconciliation priority. It does not directly control execution.

### Conversation Object

A proposed Cortex continuity object that groups related sessions without storing transcripts. It carries dense summary and retrieval metadata adjacent to knowledge objects.

### Cortex

The Remram knowledge authority service. Cortex owns durable memory, retrieval, reflection, dream reconciliation, and artifact promotion workflows.

## D

### Dimension

A hard-bounding metadata field used to determine whether a knowledge object is eligible for retrieval before lexical or vector ranking begins.

### Dream

The scheduled reconciliation pass that reviews newly added memory, resolves conflicts, adjusts confidence, promotes stable patterns, and prepares artifact candidates.

## E

### Eligibility

The rule that a memory item must satisfy scope and dimension constraints before it can enter ranking. Eligibility precedes similarity.

### Evidence

The raw runtime material Cortex can learn from, such as transcripts, tool outputs, imported artifacts, or historical session files. Evidence is input to knowledge formation, not durable knowledge itself.

## F

### Functional Thread Memory

A dense, compressed summary of how a thread progressed and what operational state matters next. Reflection may emit this so later runs can retrieve process continuity without replaying full chat history.

## G

### Gateway

The OpenClaw control plane used for deployment, snapshotting, and safe operational change. Gateway is not a runtime execution surface and does not directly query Cortex for memory retrieval.

## H

### Hydrate

A future-oriented historical replay path that feeds prior sessions or chat exports through reflection-style processing to shorten time-to-value and initialize continuity.

## K

### Knowledge Authority

The layer that decides what counts as durable memory and is allowed to mutate it. In Remram, Cortex is the knowledge authority.

### Knowledge Bundle

The structured output of Cortex retrieval. A bundle contains bounded knowledge selected for a live run, along with enough metadata for orchestration to assemble prompts or user views intentionally.

### Knowledge Object

The primary durable memory unit in Cortex. A knowledge object is a structured claim, preference, constraint, decision, principle, procedure, or relation with provenance, dimensions, and confidence.

## L

### Local-first

The principle that Cortex should remain useful and durable on local infrastructure without depending on a remote control plane for ownership of memory.

## O

### OpenClaw

The Remram runtime execution system. OpenClaw owns sessions, transcripts, tool execution, and transcript compaction.

### Orchestration

The policy and prompt-assembly layer that decides when to retrieve from Cortex, what constraints to apply, and how retrieved knowledge influences runtime behavior.

## P

### Provenance

The traceable origin of a knowledge object or artifact, including the sessions, tools, imports, or documents that support it.

## R

### Reflection

The immediate post-run extraction pass that mutates Cortex memory with structured deltas, including new knowledge, corrections, and compressed functional thread memory.

## S

### Session

A runtime execution grouping owned by OpenClaw. Sessions are evidence sources and may belong to a longer-lived conversation, but they are not themselves durable knowledge objects.

## T

### Transcript

The append-only record of runtime interaction owned by OpenClaw. Transcripts are evidence, not knowledge, and Cortex must not become a second transcript store.
