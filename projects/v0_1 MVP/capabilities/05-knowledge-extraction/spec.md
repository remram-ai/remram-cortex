# Knowledge Extraction Capability Spec

## 1. Purpose

Turn imported and captured evidence into structured knowledge-object deltas through the Cortex reflection path.

## 2. Capability Boundary

This capability is responsible for:

- reflection-driven extraction
- merge discipline against existing knowledge
- typed signal generation
- semantic signature generation
- provenance and link attachment

This capability is not responsible for:

- raw artifact persistence
- OpenSearch service operations
- chat UX

## 3. MVP Requirements

- candidate memory is evaluated against existing knowledge in the same governance scope
- extraction can decide whether to reinforce, refine, link, or create
- typed signals are generated consistently
- semantic signature is generated consistently
- resulting deltas are written in a structured form

## 4. Functional Requirements

- write path is idempotent by provenance key where practical
- obvious near-duplicates do not create duplicate object noise
- extracted knowledge remains linked to source evidence
- resulting objects are immediately eligible for retrieval

## 5. Deferred

- full Dream-time reconciliation
- large-scale principle promotion
- advanced contradiction adjudication workflows
