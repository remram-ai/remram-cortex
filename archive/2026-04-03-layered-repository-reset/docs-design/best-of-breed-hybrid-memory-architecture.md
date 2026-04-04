# Best-of-Breed Hybrid Memory Architecture

## Purpose

This memo answers a different question than the single-foundation evaluations:

"If we take the best pieces from the contenders reviewed so far, which pieces are actually best, can they work together cleanly, and what does the resulting Cortex build look like?"

The goal is not to maximize novelty.

The goal is to maximize leverage without creating a long-term maintenance trap.

Reviewed on `April 2, 2026`.

## Executive Take

Yes, a best-of-breed hybrid is possible.

But only one version of it is clean enough to recommend.

The best hybrid shape is:

- `OpenClaw` as the runtime shell and context assembly host
- `Graphiti + Neo4j` as the only durable memory authority
- `Microsoft GraphRAG` as a derived document-intelligence and synthesis sidecar
- optional `Weaviate` later only if document retrieval pressure justifies a stronger external search substrate than stock `LanceDB`

The important negative conclusion is just as important:

- do **not** run `Mem0`, `Cognee`, and `Graphiti` together as co-equal memory systems
- do **not** let `OpenClaw` Markdown memory remain a parallel authority
- do **not** add `Weaviate` on day 1 just because it is a good database

That would create split-brain memory and long-term migration pain immediately.

Bluntly:

- best runtime shell: `OpenClaw`
- best durable authority model: `Graphiti`
- best document memory / corpus synthesis layer: `GraphRAG`
- best optional retrieval substrate if external search becomes necessary: `Weaviate`
- best pattern source for fast capture and recall ergonomics: `Mem0`
- best pattern source for staged enrichment pipelines: `Cognee`

Only four of those should become live runtime dependencies, and only three should be live in phase 1.

## The Best Pieces

| Concern | Best piece | Why it wins | Use it live? |
| --- | --- | --- | --- |
| Runtime shell | `OpenClaw` | Clean plugin slots, `contextEngine`, hooks, tools, CLI, compaction, agent runtime | Yes |
| Durable memory authority | `Graphiti` | Best authority-model fit: episodes, entities, facts, temporal validity, invalidation | Yes |
| Graph storage | `Neo4j` | Best proven backing store for Graphiti's current strongest posture | Yes |
| Document-memory synthesis | `GraphRAG` | Best public implementation of community summaries, `Local`/`Global`/`DRIFT`, and Dream-lite corpus sensemaking | Yes |
| External search substrate | `Weaviate` | Strong hybrid search, named vectors, typed collections, filters, local/dockerized deployment | Later optional |
| Fast memory UX patterns | `Mem0` | Best auto-capture / auto-recall / plugin ergonomics | Borrow ideas only |
| Staged enrichment worldview | `Cognee` | Best "add -> enrich -> search -> memify" pattern among the platform kits | Borrow ideas only |

## Why This Hybrid Wins

This hybrid works because the components are not competing for the same job.

They divide cleanly:

- `OpenClaw` owns runtime orchestration
- `Graphiti` owns long-term authoritative memory
- `GraphRAG` owns derived corpus intelligence and higher-order summaries
- `Weaviate` only appears later if document retrieval outgrows stock GraphRAG storage

That is the key.

A hybrid only stays healthy when the boundaries are clean.

## The One Rule That Keeps It Sane

If this stack is built, there must be one hard rule:

- `Graphiti` is the only durable authority for memory objects used by the agent as truth

That means:

- `Graphiti` stores episodes, entities, facts, validity, and corrections
- `GraphRAG` stores derived document intelligence, summaries, communities, and retrieval structures
- `GraphRAG` outputs are evidence and synthesis aids, not the canonical source of truth for general memory
- `OpenClaw` session history and workspace memory files are runtime evidence, not long-term authority

Without that rule, the hybrid falls apart.

## What Each Piece Should Actually Do

### OpenClaw

Use `OpenClaw` for:

- channels and agent runtime
- tools and automation
- hooks
- session lifecycle
- custom `contextEngine`
- operator CLI and workflow ergonomics

Do not use it as the final long-term memory store.

### Graphiti + Neo4j

Use `Graphiti` as the only authority for:

- durable user memory
- project memory
- agent memory
- decisions
- heuristics
- temporal facts
- corrections and invalidation
- evidence episodes

This is the center of the system.

### GraphRAG

Use `GraphRAG` for:

- imported document corpora
- library-wide theme extraction
- community reports
- big-picture synthesis
- `Local` / `Global` / `DRIFT` retrieval over artifacts
- Dream-lite periodic summarization

This is not the authority layer.

It is a derived semantic intelligence layer over artifacts and exported evidence.

### Weaviate

Do not start with `Weaviate`.

Bring it in only if one or more of these become painful:

- filtered document retrieval across large corpora
- named-vector use cases
- stronger external hybrid search for documents
- wanting an inspectable external vector service instead of `LanceDB`

When that happens, `Weaviate` should back the document-intelligence side, not replace `Graphiti`.

## Recommended Hybrid Architecture

```text
Users / Channels / Agents
            |
            v
OpenClaw Gateway
  - runtime orchestration
  - custom Cortex context engine
  - tools / hooks / automation
  - optional explicit memory tools
            |
            +------------------------+
            |                        |
            v                        v
Graphiti Authority Service      GraphRAG Facade Service
  - add episodes                  - ingest artifacts
  - search facts                  - local/global/drift/basic query
  - search nodes                  - question generation
  - temporal invalidation         - update / reindex
  - ontology extensions           - community report refresh
            |                        |
            v                        v
        Neo4j                    GraphRAG Workspace
                                   - input/
                                   - output/ parquet
                                   - LanceDB

Optional later:
  GraphRAG -> Weaviate projection for stronger external document retrieval
```

## Query Flow

The right query behavior is not "search everything everywhere."

It is routed retrieval.

### Route To Graphiti When

- the question is about a person, project, agent, preference, rule, or known durable fact
- the answer depends on temporal truth or contradiction handling
- the answer should come from authoritative memory, not corpus synthesis

### Route To GraphRAG When

- the question is about themes across a document set
- the answer needs corpus synthesis
- the user wants a broad summary, comparison, or exploratory investigation
- the task looks like research over artifacts rather than direct personal or project memory

### Use Both When

- the model needs authoritative context plus corpus evidence
- a plan or answer should combine known durable facts with imported documentation

This is where the `OpenClaw` `contextEngine` becomes the key orchestration surface.

## Ingestion Flow

The hybrid should split writes deliberately.

### Write To Graphiti

- conversation episodes worth remembering
- user preferences
- durable decisions
- project rules
- tool outcomes that imply reusable heuristics
- corrections to prior memory

### Write To GraphRAG

- imported documents
- notes collections
- longform reports
- archived session summaries
- design artifacts
- project documentation

### Mirror Selectively

Some artifacts should hit both systems:

- important session summaries
- major decisions that should also become searchable in document synthesis
- exported Graphiti evidence bundles that improve GraphRAG's corpus view

But mirroring must be selective and explicit.

Do not mirror every turn into every system.

## What To Borrow Without Running It

The best hybrid is not just about active components.

We should also steal the best patterns from the contenders we are not running.

### Borrow From Mem0

- auto-recall before generation
- auto-capture after generation
- low-friction tool surfaces for add/search/update/delete
- simple scoping conventions

These are UX patterns worth copying into the `OpenClaw -> Graphiti` bridge.

### Borrow From Cognee

- staged lifecycle framing
- explicit background enrichment jobs
- clear separation between ingestion, enrichment, search, and maintenance

These are orchestration patterns worth copying into the hybrid maintenance loop.

## Why Not Run Mem0 Too

Because `Mem0` overlaps too heavily with `Graphiti`.

If both are live, you immediately create ambiguity around:

- where durable facts really live
- which system owns updates and deletions
- which result the agent should trust when the systems disagree

`Mem0` is a great primary foundation candidate.

It is not a good co-equal sidecar next to `Graphiti`.

## Why Not Run Cognee Too

Because `Cognee` overlaps with both `Graphiti` and `GraphRAG`.

It would add:

- a second graph-ish memory worldview
- a second enrichment pipeline worldview
- more stores
- more policy surfaces

That is exactly the kind of hybrid complexity we should reject.

## Phase Buildout

### Phase 1: Core Hybrid

Run:

- `OpenClaw`
- `Graphiti`
- `Neo4j`

Build:

- custom `OpenClaw -> Graphiti` context engine
- authority-first memory loop
- basic operator tools

Do not add `GraphRAG` yet unless you already have a real document corpus waiting.

### Phase 2: Document Intelligence

Add:

- `GraphRAG` facade
- `GraphRAG` indexer
- shared workspace volume

Use it for:

- imported docs
- design docs
- notes collections
- archive synthesis

### Phase 3: Unified Context Routing

Build:

- one query router in the `OpenClaw` context engine
- Graphiti-first retrieval for authority questions
- GraphRAG-first retrieval for corpus questions
- blended context for mixed questions

### Phase 4: Maintenance Loop

Add:

- scheduled Graphiti maintenance jobs
- GraphRAG `update` and report refresh jobs
- session-summary export jobs
- inspection surfaces and provenance traces

### Phase 5: Optional Search Upgrade

Only if needed, add:

- `Weaviate` as an external document retrieval projection for GraphRAG outputs or document chunks

Do not use it to replace `Graphiti`.

## What The Full Build Looks Like

At maturity, the stack should feel like this:

- `OpenClaw` runs the agent and chooses what kind of memory it needs
- `Graphiti` answers "what do we know and what is currently true?"
- `GraphRAG` answers "what do these documents and archives mean at local and global scales?"
- `Neo4j` persists the authority graph
- `Weaviate`, if added, improves externalized document retrieval without changing the authority layer

That is a coherent hybrid.

## Main Risks

The main risks are not code difficulty.

The main risks are architectural discipline.

### Risk 1. Split-Brain Memory

This happens if:

- OpenClaw files remain authoritative
- Graphiti and GraphRAG are both treated as truth stores
- extra frameworks get added "just because they are good"

### Risk 2. Over-Mirroring

If every event is copied to every system, maintenance cost explodes and trust drops.

### Risk 3. Over-Optimizing Search Early

Adding `Weaviate` or another external substrate too early will slow the build without proving value.

## Blunt Recommendation

If you want the strongest best-of-breed buildout so far, build this:

- `OpenClaw` for runtime
- `Graphiti + Neo4j` for authority memory
- `GraphRAG` for document intelligence and Dream-lite summarization

Then stop.

Only add `Weaviate` later if document retrieval scale or filtering clearly demands it.

Do not run `Mem0` or `Cognee` alongside this stack as live memory systems.

Steal their best ideas instead of their runtime complexity.

## Sources

- OpenClaw Context Engine: <https://docs.openclaw.ai/concepts/context-engine>
- OpenClaw Plugins: <https://docs.openclaw.ai/tools/plugin>
- OpenClaw Memory Overview: <https://docs.openclaw.ai/concepts/memory>
- Graphiti Quick Start: <https://help.getzep.com/graphiti/getting-started/quick-start>
- Graphiti MCP Server: <https://help.getzep.com/graphiti/getting-started/mcp-server>
- Graphiti Graph Namespacing: <https://help.getzep.com/graphiti/graphiti/graph-namespacing>
- Microsoft GraphRAG docs: <https://microsoft.github.io/graphrag/>
- GraphRAG CLI: <https://microsoft.github.io/graphrag/cli/>
- GraphRAG Bring Your Own Graph: <https://microsoft.github.io/graphrag/index/byog/>
- GraphRAG Outputs: <https://microsoft.github.io/graphrag/index/outputs/>
- Weaviate Hybrid Search: <https://docs.weaviate.io/weaviate/search/hybrid>
- Weaviate Vector Search: <https://docs.weaviate.io/weaviate/concepts/search/vector-search>
- Mem0 OpenClaw integration: <https://docs.mem0.ai/integrations/openclaw>
