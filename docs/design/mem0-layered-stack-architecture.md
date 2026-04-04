# Mem0 Layered Stack Architecture

## Purpose

This document describes the layered Cortex architecture with `Mem0` as the durable-memory base.

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
            +------------------------------+
            |                              |
            v                              v
OpenClaw Session Surface            Cortex Coordination Layer
  - transcripts                     - anchor identity
  - session evidence                - policy
  - native compaction               - publication workflow
            |                              |
            +--------------+---------------+
                           |
                           v
                   Context Compression
              - rolling summaries
              - Mamba-style continuity
              - open-loop state
                           |
                           v
                         Mem0
                 - extract / update / delete
                 - search memory
                 - runtime recall
                           |
                           v
                        Weaviate
           - Mem0 memory collections
           - knowledge decomposition collections
           - lexical + vector retrieval surfaces
                           |
                           v
                    Canonical Artifacts
                       - Git
                       - provider docs
```

## OpenClaw Extension Surface Mapping

In OpenClaw terms, this stack also resolves into four extension surfaces.

### 1. Context Engine

The context engine should assemble:

- policy
- working memory from the session surface
- compact `Mem0` recall

This keeps the runtime bounded and avoids using artifact corpora as prompt baggage.

### 2. Memory Engine

The memory-engine slot should use the official `Mem0` integration path where possible.

That slot owns:

- durable-memory writes through `Mem0`
- memory recall into runtime

### 3. Reflection Pipeline

Reflection should take runtime evidence and branch it into:

- `Mem0` durable-memory updates
- artifact and decomposition impacts
- context compression products
- governed preference-policy updates

This is also the right place for later graph-reflection experiments if desired.

### 4. Knowledge Tool Interface

Deeper knowledge access should be tool-based.

Tools should expose:

- decomposition search
- supporting slices
- canonical artifact fetch when needed

## Layer Contracts

### Working Memory

Owned by the OpenClaw session surface.

Cortex augments this layer through policy-aware assembly and Mamba-style semantic compression.

### Durable Memory

Owned by `Mem0` memory records and lifecycle logic.

### Knowledge

Owned by Cortex decomposition interfaces over separate `Weaviate` collections or schemas.

### Canonical Artifacts

Owned by `Git` or provider authority.

## Retrieval Flow

1. startup injects bounded policy, working memory, and `Mem0` recall
2. if deeper evidence is needed, resolve anchor and query decomposition collections on `Weaviate`
3. if publication truth is needed, fetch canonical artifact body

## Reflection Flow

1. evidence enters the session surface and evidence log
2. reflection proposes durable-memory updates for `Mem0`
3. reflection also proposes artifact impacts for decomposition
4. reflection produces context compression outputs
5. governed preference-policy updates are routed separately
6. publication later reconciles canonical artifacts

## Why This Architecture Is Clean

It keeps the durable-memory center simple:

- `Mem0` does memory

and lets the broader knowledge layer exist without overloading `Mem0`.
