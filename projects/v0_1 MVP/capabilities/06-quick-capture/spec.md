# Quick Capture Capability Spec

## 1. Purpose

Provide the low-friction write surface for adding new knowledge into Cortex and proving that captured thoughts use the same durable model as imported artifacts.

## 2. Capability Boundary

This capability is responsible for:

- accepting short text captures
- normalizing them into capture artifacts
- sending them through reflection
- updating or creating knowledge objects

This capability is not responsible for:

- voice-first UX
- dormant idea resurfacing
- feasibility analysis

## 3. MVP Contract

Minimum capture input:

- `capture_text`
- `owner_ref`
- `audience`
- `knowledge_space`

Each capture must become:

1. a capture artifact
2. a reflection input
3. one or more knowledge-object deltas

## 4. Functional Requirements

- capture uses the same provenance model as imports
- capture can reinforce existing objects
- capture can refine or link to imported knowledge
- capture can create a new object when no strong match exists
- resulting knowledge is retrievable immediately

## 5. Merge Expectations

The capability should support the reflection decision set:

- reinforce
- refine
- link
- create

It should avoid obvious duplicate object creation in known knowledge areas.

## 6. Deferred

- voice capture
- multi-step clarification UX
- capture-time agentic analysis
