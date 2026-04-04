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
Working Memory Sidecar              Cortex Coordination Layer
  - hot continuity                  - anchor identity
  - task state                      - policy
  - evidence queue                  - publication workflow
            |                              |
            +--------------+---------------+
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

## Layer Contracts

### Working Memory

Owned by the hot sidecar only.

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

1. evidence enters working memory and evidence log
2. reflection proposes durable-memory updates for `Mem0`
3. reflection also proposes artifact impacts for decomposition
4. publication later reconciles canonical artifacts

## Why This Architecture Is Clean

It keeps the durable-memory center simple:

- `Mem0` does memory

and lets the broader knowledge layer exist without overloading `Mem0`.
