# Mem0 Layered Stack Implementation Plan

## Purpose

This plan describes how to implement the layered stack with `Mem0` as the durable-memory base.

## Phase 0: Schema And Surface Separation

Goals:

- define separate logical surfaces for:
  - working memory
  - Mem0 durable memory
  - artifact decomposition
- define anchor and revision model

Exit criteria:

- clean ownership rules
- no ambiguity about what lives in Mem0 vs knowledge collections

## Phase 1: Working Memory Backbone

Goals:

- stand up bounded working-memory sidecar
- add evidence log and queue state

Exit criteria:

- low-latency continuity works
- evidence is replayable

## Phase 2: Mem0 Integration

Goals:

- enable official `OpenClaw` integration
- enforce durable-memory writes through `Mem0`
- define memory metadata for provenance and artifact support

Exit criteria:

- durable-memory recall works
- update lifecycle is observable

## Phase 3: Knowledge Plane On Weaviate

Goals:

- stand up decomposition collections
- add lexical and vector retrieval surfaces
- bind slices to anchors and revisions

Exit criteria:

- artifact-derived knowledge is retrievable separately from memory recall

## Phase 4: Reflection Split

Goals:

- send memory updates into `Mem0`
- send artifact impacts into decomposition
- keep canonical artifacts untouched until publication flow

Exit criteria:

- one evidence feed updates both surfaces cleanly

## Phase 5: Publication And Re-ingestion

Goals:

- mark dirty anchors
- redraft canonical artifacts
- publish to `Git`
- refresh decomposition
- reconcile memory support metadata

Exit criteria:

- revision-aware artifact lifecycle is working

## Phase 6: Optional Graph Reflection

Goals:

- test graph reflection over durable memory and anchors
- keep graph derived, not authoritative

Exit criteria:

- graph proves value or stays optional
