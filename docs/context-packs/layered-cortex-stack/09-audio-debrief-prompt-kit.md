# Audio Debrief Prompt Kit

## Purpose

These prompts are meant for NotebookLM or another synthesis system that already has this context pack loaded.

Use them to generate an audio-style deep briefing on the chosen Cortex stack.

## Prompt 1: Full Executive Debrief

Give me a detailed audio briefing on the current Remram Cortex stack.

Explain:

- what Cortex is
- the five-layer model
- why the stack uses OpenClaw, High-Signal Mamba, Graphiti plus Neo4j, Postgres plus pgvector, and Git
- how runtime evidence becomes durable memory
- how artifacts move through decomposed knowledge and canonical publication
- the major implementation risks

Assume I want a thorough architectural walkthrough, not a short summary.

## Prompt 2: Layer-By-Layer Walkthrough

Walk me through Cortex layer by layer in order.

For each layer, explain:

- what it owns
- what it does not own
- why it is separated from the other layers
- which technology currently implements it
- what failures happen if the boundary is violated

## Prompt 3: Session-To-Memory Narrative

Give me a narrative walkthrough of one live Cortex session.

Start with OpenClaw runtime and end with trusted durable memory.

Make sure to explain:

- the raw evidence log
- the High-Signal Mamba Stream
- tentative notions
- session-end reconciliation
- Graphiti evidence packaging
- when oversight intervenes

## Prompt 4: Artifact Pipeline Deep Dive

Explain the artifact side of Cortex in detail.

Cover:

- Layer 4 versus Layer 5
- why Postgres and Git are separate
- anchor identity
- dirty-state tracking
- redraft and publication
- how Graphiti receives only compact artifact memory, not full documents

## Prompt 5: Why This Stack And Not A Monolith

Explain why Cortex deliberately does not use one universal memory system for everything.

Contrast:

- policy
- working memory
- durable memory
- decomposed knowledge
- canonical artifacts

Focus on the actual failure modes the layered design is trying to avoid.

## Prompt 6: Implementation Readiness Review

Based on this context pack, give me a detailed implementation-readiness review.

Tell me:

- what is already architecturally clear
- what the biggest open implementation risks are
- what the MVP sequence should validate first
- which parts of the stack are most likely to cause rework

## Prompt 7: Long-Form Audio Outline

Create a 30 to 45 minute audio-debrief outline on the Cortex stack.

Break it into sections with estimated time per section.

Include:

- system framing
- layers
- data flows
- memory model
- artifact model
- reflection and oversight
- deployment and MVP sequence

End with the top architectural watchpoints.
