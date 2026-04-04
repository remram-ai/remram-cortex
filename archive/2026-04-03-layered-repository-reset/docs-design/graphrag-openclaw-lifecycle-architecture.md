# GraphRAG + OpenClaw Lifecycle Architecture

## Purpose

This memo evaluates an end-to-end Cortex path built on:

- `Microsoft GraphRAG` as the corpus-memory lifecycle engine and durable semantic document authority
- `OpenClaw` as the runtime shell, session lifecycle owner, tool host, and automation surface
- built-in `LanceDB` plus GraphRAG output tables as the default local storage posture

The useful question is:

"If we let GraphRAG take the biggest bite out of document-memory indexing, graph formation, summarization, and multi-scale retrieval, and let OpenClaw take the biggest bite out of runtime orchestration, what architecture is left, what can be done the GraphRAG way, and what still has to be custom?"

Reviewed on `April 2, 2026`.

## Executive Take

This stack is a real contender, but only if we accept what it naturally is.

`GraphRAG` is strongest as:

- a durable semantic index over imported artifacts
- a graph-shaped document memory
- a theme and synthesis engine
- a multi-scale retrieval system with `Local`, `Global`, and `DRIFT`
- a Dream-lite summarization substrate through community reports

It is weaker as:

- a transactional memory authority for tiny live updates
- a canonical mutable object store
- a fine-grained governance-first runtime database

The strongest version of this stack is:

- `OpenClaw` as the runtime shell
- a thin custom `OpenClaw -> GraphRAG` plugin, with a `contextEngine` role first and a `memory` role second
- `GraphRAG` as the only durable authority for corpus-derived long-term memory
- OpenClaw session state as short-term runtime context and evidence, not parallel long-term authority
- non-document durable memory represented as small synthetic artifacts so it can stay inside the same GraphRAG authority instead of forcing a second durable store

Bluntly:

- this is a stronger contender than a storage-only stack
- this is a stronger document-memory contender than a plain vector memory plugin
- this is more corpus-native than `Mem0 + OpenClaw`
- this is less authority-native than `Graphiti + OpenClaw`
- this is viable if we accept batch-ish indexing, coarse partitioning, and artifact-first memory modeling

## Quick Assessment

| Criterion | Assessment | Why |
| --- | --- | --- |
| Memory authority fit | Medium | Strong for artifact memory, weaker for live canonical memory objects |
| Custom work remaining | Medium-high | Needs a real OpenClaw bridge and a thin service boundary |
| Long-term migration risk | Medium | Better if Cortex becomes corpus-first; worse if Cortex becomes highly transactional |
| Stored data model forward fit | Medium | Entities, relationships, communities, and reports are useful durable artifacts, but they are derived artifacts |
| Fastest path to something usable | Medium | Faster than a custom build, slower than stock Mem0 |
| Solo operational burden | Medium | A couple of containers and a shared workspace, but no large database is required in phase 1 |
| Path to Cortex vision | Plausible with compromises | Strong on document memory and synthesis, weaker on governance-first mutable memory |

## The Most Important Architectural Rule

If we pursue this path, we should enforce one simple rule:

- `GraphRAG` is the only durable authority for long-term artifact memory

That means:

- imported docs, notes, decisions, heuristics, and session summaries become GraphRAG inputs
- OpenClaw session persistence is runtime evidence, not final authority
- OpenClaw `MEMORY.md` and daily notes should be disabled, minimized, or treated as a temporary cache during transition
- raw parquet tables and `LanceDB` files are GraphRAG implementation storage, not an app-owned second schema

## The Key OpenClaw Insight

For this stack, the most important OpenClaw seam is probably not the `memory` plugin slot.

It is the `contextEngine`.

Why:

- GraphRAG is not just a search backend
- it has multiple retrieval modes with different purposes
- it naturally assembles structured context from graph artifacts and text units

If we integrate only as a memory-search plugin, we flatten GraphRAG into one more retrieval tool.

If we integrate through a context engine, OpenClaw can:

- choose `Local`, `Global`, or `DRIFT` based on the question type
- inject richer recall blocks into prompt assembly
- own compaction behavior that writes durable session summaries back into the GraphRAG workspace
- keep recent session turns hot while GraphRAG stays the long-term store

## What This Architecture Looks Like After The Big Bites Are Taken

```text
Users / Channels / Agents
            |
            v
OpenClaw Gateway
  - custom openclaw-graphrag plugin
  - context engine for ingest / assemble / compact / afterTurn
  - optional memory plugin surface for CLI + explicit search
            |
            v
GraphRAG Facade Service
  - ingest artifact API
  - query API: local / global / drift / basic
  - question generation API
  - update / reindex control
  - coarse policy checks
            |
            v
GraphRAG Workspace
  - input/
  - prompts/
  - settings.yaml
  - cache/
  - output/ parquet tables
  - LanceDB embeddings
            ^
            |
GraphRAG Index Worker
  - prompt-tune
  - index / update
  - standard vs fast method selection
  - scheduled maintenance / report refresh
```

## What GraphRAG Natively Takes Off Our Plate

If we stay close to the framework, GraphRAG already solves a surprising amount:

- graph extraction into entities, relationships, and optional claims
- multi-scale memory views through text units, communities, and community reports
- different retrieval styles for different question classes
- Dream-lite summarization through community report generation
- incremental maintenance through `standard-update` and `fast-update`
- extension seams through prompt tuning, workflow selection, custom vector stores, and `BYOG`

## What To Accept The GraphRAG Way

If this path is chosen, several Cortex ideas should be implemented the `GraphRAG` way.

| Cortex intent | GraphRAG-native equivalent | Decision |
| --- | --- | --- |
| Imported artifact memory | documents + text units + extracted graph | Accept directly |
| Durable semantic memory | entities + relationships + community reports | Accept as derived authority |
| Dream / condensation | community report generation and refresh | Accept directly as Dream-lite |
| Big-picture recall | `Global Search` | Accept directly |
| Specific recall | `Local Search` | Accept directly |
| Multi-hop exploration | `DRIFT Search` | Accept directly |
| Memory follow-up suggestions | question generation | Accept directly |
| Domain ontology control | prompt tuning + entity type control | Accept with prompt discipline |
| Retrieval backend | `LanceDB` first, custom store later if needed | Accept in phase 1 |
| Corpus partitioning | separate workspaces or coarse dataset boundaries | Accept with modification |

The biggest worldview shift is:

- Cortex durable memory becomes artifact-first and graph-derived
- not row-first and mutation-first

## Built-In Extension Points That Matter

The official GraphRAG docs expose useful seams:

- prompt tuning
- custom vector store registration
- workflow subsetting
- `BYOG`
- `LiteLLM`-based model integration

OpenClaw also exposes the right host seams:

- `contextEngine`
- `systemPromptAddition`
- `memory` plugin slot
- hooks
- tools and plugin routes

That is enough to build a serious `openclaw-graphrag` integration without forking either project.

## The Main Hard Differences From Graphiti Or Mem0

This is where the stack loses points as a primary foundation.

- GraphRAG wants to derive graph structure from artifacts, not maintain tiny hand-edited authority records.
- It is more comfortable with periodic runs and updates than per-turn transactional mutation.
- Its natural partition boundary is closer to a workspace or corpus than to fine-grained governance filters.
- Community reports and extracted graph artifacts are generated artifacts, not clean app-owned records.

## The Minimum Custom Modules Still Needed

If we want this to grow toward Cortex without turning into a custom rewrite, the minimum custom additions are:

### 1. `openclaw-graphrag`

A plugin that:

- registers a context engine
- optionally registers memory search tools
- calls the GraphRAG facade
- chooses query modes
- persists post-turn summaries as ingestable artifacts

### 2. `graphrag-facade`

A thin service wrapper around the CLI and/or library that exposes:

- `ingest`
- `query/local`
- `query/global`
- `query/drift`
- `query/basic`
- `question-generation`
- `update`

### 3. Artifact Normalization

A tiny layer that turns runtime events into durable artifacts such as:

- session summaries
- user preference notes
- durable decisions
- tool lessons
- imported documents

## Bottom Line

`GraphRAG + OpenClaw` is a credible contender.

The honest framing is:

- not the best general long-term memory authority
- one of the best document-memory and sensemaking architectures in the field
- viable as a Cortex path if we accept artifact-first durable memory, GraphRAG-owned derived structure, and a context-engine-first OpenClaw integration

The best phase-1 posture is:

- `GraphRAG` with built-in `LanceDB`
- one GraphRAG workspace per major corpus or agent boundary
- a thin `OpenClaw` context engine plugin
- scheduled or event-batched updates instead of per-message full indexing

## Sources

- Microsoft GraphRAG docs: <https://microsoft.github.io/graphrag/>
- GraphRAG Outputs: <https://microsoft.github.io/graphrag/index/outputs/>
- GraphRAG Indexing Methods: <https://microsoft.github.io/graphrag/index/methods/>
- GraphRAG Bring Your Own Graph: <https://microsoft.github.io/graphrag/index/byog/>
- GraphRAG Prompt Tuning Overview: <https://microsoft.github.io/graphrag/prompt_tuning/overview/>
- GraphRAG CLI: <https://microsoft.github.io/graphrag/cli/>
- GraphRAG Detailed Configuration: <https://microsoft.github.io/graphrag/config/yaml/>
- GraphRAG paper: <https://arxiv.org/abs/2404.16130>
- OpenClaw Context Engine: <https://docs.openclaw.ai/concepts/context-engine>
- OpenClaw Memory Overview: <https://docs.openclaw.ai/concepts/memory>
- OpenClaw Plugins: <https://docs.openclaw.ai/plugins>
- OpenClaw Hooks: <https://docs.openclaw.ai/automation/hooks>
