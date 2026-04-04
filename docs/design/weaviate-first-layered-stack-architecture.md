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
OpenClaw Session Surface            Cortex Authority Layer
  - transcripts                     - anchor registry
  - session evidence                - memory lifecycle rules
  - native compaction               - publication workflow
            |                               |
            +---------------+---------------+
                            |
                            v
                    Context Compression
              - rolling summaries
              - Mamba-style continuity
              - task and thread distillation
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

## OpenClaw Extension Surface Mapping

In OpenClaw terms, this stack also resolves through four extension surfaces.

### 1. Context Engine

The context engine should assemble:

- policy
- working memory from the session surface
- compact durable-memory bundle

It should keep knowledge retrieval out of the default startup path.

### 2. Memory Engine

The memory-engine slot would front a Cortex-native durable-memory service on top of `Weaviate`.

That means this slot is custom, not inherited from a third-party memory product.

### 3. Reflection Pipeline

Reflection should branch evidence into:

- durable-memory updates
- artifact impacts
- context compression products
- governed preference-policy updates

This is where the system would implement update, supersession, and support reconciliation rules.

### 4. Knowledge Tool Interface

Deep knowledge and artifact access should come through tools.

That tool surface should expose:

- hybrid retrieval over decomposition
- anchor resolution
- canonical artifact fetch when needed

## Layer Contracts

### Working Memory

Owned by the OpenClaw session surface.

Cortex augments this layer through policy-aware assembly and Mamba-style semantic compression.

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
