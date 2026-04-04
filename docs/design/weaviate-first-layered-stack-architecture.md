# Weaviate-First Layered Stack Architecture

## Purpose

This document describes the layered Cortex architecture built directly on `Weaviate` as the primary hybrid retrieval platform.

## Architecture Summary

```text
Users / Channels / Agents
            |
            v
OpenClaw Runtime
  - tools
  - prompts
  - lifecycle hooks
            |
            +-------------------------------+
            |                               |
            v                               v
Working Memory Sidecar               Cortex Authority Layer
  - hot continuity                   - anchor registry
  - queue state                      - memory lifecycle rules
  - task state                       - publication workflow
            |                               |
            +---------------+---------------+
                            |
                            v
                        Weaviate
         - durable memory object collections
         - anchor collections
         - decomposition collections
         - lexical + vector search
         - cross references
                            |
                            v
                     Canonical Artifacts
                        - Git
                        - provider docs
```

## Layer Contracts

### Working Memory

Separate and bounded.

### Durable Memory

Implemented by Cortex on top of explicit `Weaviate` collections for:

- memory objects
- memory supports
- major entities
- anchor references

### Knowledge

Implemented through separate decomposition collections with revision-aware records.

### Canonical Artifacts

Remain outside `Weaviate`.

## Retrieval Flow

1. startup injects policy, working snapshot, and compact durable-memory bundle
2. hybrid retrieval over `Weaviate` resolves:
   - durable-memory objects
   - decomposition slices
3. canonical bodies are fetched only when needed

## Why This Architecture Is Distinct

It is the only option here where:

- the retrieval substrate is first
- the memory lifecycle semantics are custom

That makes it the most flexible and the most custom at the same time.
