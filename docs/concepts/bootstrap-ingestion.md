# Bootstrap Ingestion

Bootstrap ingestion is the historical backfill path that initializes Cortex from prior conversations and other historical evidence.

It is a conditioning pipeline for waking up the knowledge base, not a replacement for live reflection.

## What It Does

Bootstrap ingestion should:

- read historical transcript sources in read-only mode
- extract structured knowledge objects, recurrence signals, and durable continuity cues
- build dimensions, relationships, and retrieval indexes
- surface contradictions and candidate principles
- initialize derived continuity views such as memory-map projections

It must not rewrite transcripts or store them as durable Cortex memory.

Where possible, it should use controlled Gateway, Forge, or OpenClaw-managed surfaces rather than ad hoc raw runtime-store manipulation. Early migration work may still ingest existing memory or session files in read-only mode when that is the lowest-risk way to learn the source format.

## Why It Exists

Without bootstrap, a new Cortex instance starts structurally empty even when long conversation history already exists. Bootstrap ingestion turns that history into usable continuity without forcing the user to manually replay or re-prompt everything.

## Bootstrap Versus Reflection

Bootstrap ingestion is historical and batch-oriented.

Reflection is post-run and incremental.

Both produce structured knowledge, but bootstrap initializes the base while reflection evolves it over time.

## Boundary Reminder

Bootstrap ingestion does not change the authority model:

- OpenClaw still owns transcripts and session history
- Cortex still owns only structured durable knowledge
- orchestration still controls retrieval use and runtime injection

## Related Concepts

- [Knowledge Authority](knowledge-authority.md)
- [Reflection](reflection.md)
- [Dream Cycle](dream-cycle.md)
- [Memory Versus Context](memory-vs-context.md)
- [Architecture](../remram-cortex/architecture.md)
