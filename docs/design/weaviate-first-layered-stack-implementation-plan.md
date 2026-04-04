# Weaviate-First Layered Stack Implementation Plan

## Purpose

This plan describes how to validate and implement a Cortex-native layered stack on top of `Weaviate`.

## Phase 0: Prove The Retrieval Core

Goals:

- stand up `Weaviate`
- validate hybrid retrieval over test memory and artifact slices
- define collection strategy

Exit criteria:

- retrieval quality is strong enough to justify the custom-lifecycle cost

## Phase 1: Working Memory And Control Plane

Goals:

- stand up bounded working-memory sidecar
- stand up small control-plane store if needed
- define anchor and revision registry

Exit criteria:

- layer boundaries are explicit

## Phase 2: Durable-Memory Service MVP

Goals:

- implement Cortex durable-memory object schema
- implement add, update, supersede, invalidate rules
- implement provenance and support references

Exit criteria:

- durable-memory lifecycle works without external memory platform

## Phase 3: Knowledge Decomposition Plane

Goals:

- add artifact decomposition collections
- add lexical and vector retrieval
- bind decomposition to anchors and revisions

Exit criteria:

- fine-grained evidence retrieval works

## Phase 4: Reflection Split And Publication

Goals:

- branch evidence into memory updates and artifact impacts
- support dirty anchors
- redraft and republish canonical artifacts

Exit criteria:

- layered artifact cycle is complete

## Phase 5: Evaluate Custom Semantic Burden

Goals:

- measure whether owning memory semantics directly is still worth it
- compare effort against `Mem0` and `Graphiti`

Exit criteria:

- continue only if custom semantics are proving to be an advantage, not just work
