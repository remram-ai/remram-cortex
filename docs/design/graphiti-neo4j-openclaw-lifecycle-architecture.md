# Graphiti + Neo4j + OpenClaw Lifecycle Architecture

## Purpose

This memo evaluates an end-to-end Cortex path built on:

- `Graphiti` as the temporal memory lifecycle engine and durable memory authority
- `Neo4j Community` as the underlying local graph storage substrate
- `OpenClaw` as the runtime shell, session lifecycle owner, tool host, and automation surface

The question is not whether this stack already is Cortex.

The useful question is:

"If we let `Graphiti` solve temporal memory lifecycle, let `Neo4j` solve graph storage, and let `OpenClaw` solve runtime orchestration, what architecture is left, what works natively, and what still has to be custom?"

Reviewed on `April 2, 2026`.

## Executive Take

This is the strongest semantic fit to the Cortex direction of any external stack reviewed so far.

`Graphiti` is not just a retrieval layer. It already has several properties we actually want from a memory authority:

- episodic ingestion
- fact extraction into graph objects
- temporal validity and invalidation
- provenance through episodes
- hybrid semantic plus keyword plus graph retrieval
- customizable ontology
- maintenance primitives such as community building

Bluntly:

- this is a better authority-layer match than `Mem0 + OpenClaw`
- it is a heavier solo-builder lift than `Mem0 + OpenClaw`
- it has lower long-term data-model replatform risk if Cortex really wants graph-native, temporally-aware memory
- it is viable only if `Graphiti` remains the only durable write authority over the memory graph
- under the current AI-builder lens, this is the default favorite among the external foundation candidates

The strongest version of this stack is:

- `OpenClaw` as the runtime shell
- a thin custom `OpenClaw -> Graphiti` bridge
- `Graphiti` as the only durable authority for memory objects, corrections, and recall
- `Neo4j` as Graphiti's backing store
- optional `Graphiti` MCP or read-only Neo4j tooling for operator inspection

The wrong version is:

- OpenClaw writing its own parallel memory
- direct app writes to raw `Neo4j`
- Graphiti being used only for convenience search while some other app-layer model becomes the real source of truth

That would recreate split-brain memory almost immediately.

## Quick Assessment

| Criterion | Assessment | Why |
| --- | --- | --- |
| Memory authority fit | Very high | Graphiti already stores episodes, entities, facts, and fact lifecycles |
| Custom work remaining | Medium-high | The main missing piece is the OpenClaw bridge and Cortex-specific policy surfaces |
| Long-term migration risk | Low if graph-first is right | The stored model is already close to a plausible final Cortex authority |
| Stored data model forward fit | High | Temporal facts plus episode provenance are durable primitives, not throwaway chat memory |
| Fastest path to something usable | Medium | More setup than the Mem0 route, but still realistic |
| Solo operational burden | Medium-high | Python service plus Neo4j plus OpenClaw is heavier than a simpler vector-memory path |
| Path to Cortex vision | Strong | The biggest remaining work is policy, packaging, and integration, not rethinking the memory model |

## Why This Combination Is Different

`Graphiti` is already much closer to a knowledge authority than most "memory" products.

It does not merely store embeddings or summaries. It ingests episodes, extracts entities and facts, tracks temporal validity, invalidates contradicted edges, and retrieves facts through hybrid and graph-aware search.

That changes the shape of the problem.

With this stack, the missing system is not "how do we build memory lifecycle?"

The missing system is closer to:

- how OpenClaw should feed and query that authority
- how Cortex-specific policy should shape ingestion and retrieval
- how to expose operator inspection and artifact identity cleanly

That is a much narrower gap than a greenfield memory engine.

## The Most Important Architectural Rule

If we pursue this path, we should enforce one simple rule:

- `Graphiti` is the only durable write authority

That means:

- OpenClaw transcripts are evidence, not memory authority
- OpenClaw Markdown memory is projection or fallback, not authority
- raw `Neo4j` nodes and edges are Graphiti implementation storage, not an application-owned second schema
- direct `Cypher` writes should be treated as exceptional maintenance work, not normal product behavior

Read-only `Cypher` and Neo4j Browser inspection are fine.

Parallel writes are not.

## What This Architecture Looks Like After The Big Bites Are Taken

If we let `Graphiti` and `Neo4j` take the biggest bite out of memory authority, and let `OpenClaw` take the biggest bite out of runtime orchestration, the remaining architecture is relatively small:

```text
Users / Channels / Agents
            |
            v
OpenClaw Gateway + Agent Runtime
  - custom openclaw-graphiti memory plugin
  - lifecycle hooks: before_prompt_build, agent_end
  - optional compaction hooks
  - optional phase-2 context engine
            |
            v
Graphiti Service Boundary
  - ingest episodes/messages
  - search facts / get-memory
  - custom entity and edge types
  - maintenance triggers
            |
            v
Graphiti Core
  - episodic nodes
  - entity nodes
  - entity edges with fact + validity windows
  - search recipes / filters / rerankers
  - community building / invalidation
            |
            v
Neo4j Community
  - durable graph storage
  - full-text indexes
  - vector indexes
  - graph traversal / inspection

Optional sidecars:
  - Graphiti MCP server for operator tooling or external assistants
  - Neo4j Browser / Cypher-based inspection
  - export / audit / trace worker
```

After those three big components are in place, most of the custom work left is:

- adapter code
- policy code
- metadata discipline
- inspection surfaces

That is an encouraging architecture shape.

## Closest Cortex Equivalents Already In The Stack

This is the optimistic mapping that matters most.

| Cortex intent | Closest native equivalent | Read |
| --- | --- | --- |
| Raw evidence / source intake | `Graphiti` episodic nodes and episode ingestion | Strong native match |
| Durable memory statements | `EntityEdge.fact` plus temporal metadata | Strong native match |
| Memory correction and replacement | Edge invalidation instead of naive overwrite | Better than most contenders |
| Provenance | Episode references on extracted facts and entities | Strong native match |
| Typed knowledge objects | Entity nodes plus custom entity and edge types | Good enough early |
| Scoped memory partitions | `group_id` namespacing | Good early fit if used with discipline |
| Retrieval bundle inputs | Hybrid search, node-distance reranking, episode-aware reranking, filters | Strong fit |
| Maintenance / reconciliation | Sequential episode ingestion, invalidation, and `build_communities()` | Good Dream-lite equivalent |
| Tool and operator access | Graphiti FastAPI service, MCP server, Neo4j Browser | Strong fit |
| Document-oriented memory | Text and JSON episodes plus `Document`-style entity types | Workable, but needs import discipline |
| Runtime lifecycle orchestration | OpenClaw hooks, memory slot, context-engine slot, automation | Strong fit |
| Artifact / provider identity | Custom overlay | Weak native match |

The most important takeaway is this:

for the first time, the "native equivalent" column is strong almost all the way down.

## Inbuilt Extension Points To Exploit

### OpenClaw Native Seams

| OpenClaw seam | What it gives us | How to use it here |
| --- | --- | --- |
| `plugins.slots.memory` | One active memory plugin | Implement a thin `openclaw-graphiti` plugin instead of bending Graphiti into ad hoc tools |
| `plugins.slots.contextEngine` | Full control over assembly and compaction later | Stay on `legacy` early and only replace it if retrieval shaping becomes the bottleneck |
| `before_prompt_build` | Prompt-time dynamic injection | Recall Graphiti facts and inject them the OpenClaw way |
| `agent_end` | Post-turn persistence seam | Flush final messages into Graphiti as episodes |
| `before_compaction` / `after_compaction` | Compaction lifecycle | Attach continuity summaries or schedule graph maintenance |
| Automation hooks / cron / background tasks | Event and schedule driven maintenance | Rebuild communities, run exports, or run audits without inventing a separate scheduler |

### Graphiti Native Seams

| Graphiti seam | What it gives us | How to use it here |
| --- | --- | --- |
| `add_episode(...)` | Main ingestion primitive | Use this as the default path for all durable observations |
| Sequential per-group ingestion guidance | Correct temporal and invalidation behavior | Respect it; do not parallelize writes recklessly |
| `add_episode_bulk(...)` | Higher-throughput batch imports | Use for imports only when its weaker invalidation behavior is acceptable |
| `group_id` | Namespacing and query isolation | Map users, agents, workspaces, or domains onto it carefully |
| Custom entity and edge types | Domain ontology without a second schema | Encode Cortex categories here first |
| Custom extraction instructions | Domain-specific extraction control | Push Cortex memory quality rules into the extractor before building post-processors |
| Search recipes and filters | Multiple out-of-the-box retrieval strategies | Start with native hybrid search before inventing a custom retrieval pipeline |
| Node distance and episode mention reranking | Better context-sensitive recall | Useful for agent-centric or artifact-centric retrieval |
| `build_communities(...)` | Graph maintenance and summarization clusters | Treat as Dream-lite before building a separate Dream system |
| FastAPI service | Clean service boundary for non-Python callers | Preferred OpenClaw bridge |
| MCP server | Assistant-facing tool surface | Great operator sidecar; probably not the primary OpenClaw runtime bridge |

### Neo4j Native Seams

| Neo4j seam | What it gives us | Why it matters here |
| --- | --- | --- |
| Community Edition | Local and free deployment | Fits the local-base-system requirement |
| Docker and Desktop options | Easy local bring-up | Reduces solo setup friction |
| Full-text indexes | Keyword retrieval over graph content | Supports Graphiti's hybrid search posture |
| Vector indexes | Approximate semantic retrieval over graph objects | Gives the graph store a real modern search surface |
| Native traversal and Cypher | Rich graph inspection and debugging | Useful for read-only operator tooling and later custom views |

The main thing `Neo4j` gives this architecture is not "graph coolness."

It gives `Graphiti` a durable store whose native shape already matches the facts-and-relationships model we would otherwise try to invent later.

## What The Official Stack Already Gives Us For Free

With the current upstream stack, we already get:

- `Graphiti` core on `Neo4j`
- hybrid semantic plus BM25 plus graph-aware retrieval
- explicit temporal metadata on facts
- contradiction handling through invalidation
- episode-based provenance
- custom entity and edge types
- a Graphiti FastAPI service with message ingest and search endpoints
- a Graphiti MCP server for assistant-facing tooling
- OpenClaw plugin slots, context-engine slots, and lifecycle hooks
- OpenClaw automation primitives for scheduled or event-driven maintenance
- local `Neo4j Community` deployment

That means phase 0 does not need to start from bare metal.

A believable phase-0 stack already exists:

- `OpenClaw`
- one small `Graphiti` bridge plugin
- `Graphiti` server or service wrapper
- `Neo4j Community`

There is also a plausible fully local model path:

- `Neo4j` local
- `Graphiti` local
- `OpenClaw` local
- `Ollama` or another OpenAI-compatible local endpoint for LLM calls

I would still treat local-model plumbing as a day-1 smoke-test item, not something to assume blindly.

## The Key Integration Nuance

This stack is strong because `Graphiti` is already close to the authority role.

It is weaker because the `OpenClaw` integration is not turnkey the way the `Mem0` integration is.

There is no official `Graphiti + OpenClaw` memory plugin that I could find.

That means we still need a bridge.

The main architectural question is what that bridge should target:

- Graphiti core directly
- Graphiti MCP server
- Graphiti FastAPI service

My recommendation is:

- use the Graphiti FastAPI service as the primary runtime bridge
- use the Graphiti MCP server as an optional operator or external-assistant sidecar

Why:

- OpenClaw's memory slot wants a deterministic plugin contract, not free-form assistant tool calls
- the FastAPI service is a cleaner language boundary for a likely TypeScript OpenClaw plugin talking to Python Graphiti
- the current service already exposes useful ingestion and retrieval endpoints
- MCP remains useful, but more as a tool surface than as the core authority boundary

There is one more practical nuance:

- the stock Graphiti service exposes a useful but narrower surface than the full core library

That is acceptable.

It just means phase 1 might need one small service extension or a thin local fork if we want richer metadata, retrieval traces, or more explicit maintenance controls.

## Recommended Architecture

The strongest architecture for this stack is:

```text
1. OpenClaw owns session lifecycle, tool hosting, and user interaction.
2. OpenClaw calls Graphiti through a thin plugin or service adapter.
3. Graphiti owns all durable memory writes and recall semantics.
4. Neo4j stores Graphiti's graph and stays behind Graphiti.
5. Optional MCP and Cypher surfaces are read-oriented operator tools.
```

Minimal module split:

- `openclaw-graphiti`
  - custom memory plugin
  - recall on `before_prompt_build`
  - writeback on `agent_end`
  - optional inspect tools
- `graphiti-service`
  - mostly stock upstream service
  - maybe one small extension for richer search or metadata
- `neo4j`
  - stock local Community instance
- optional `graphiti-mcp`
  - operator-facing sidecar

This keeps the long-term authority line clean while keeping the custom surface area tolerable.

## Best "Do It The Graphiti Way" Moves

- Treat episodes as the atomic evidence unit. Ingest conversations, documents, and events as episodes first.
- Treat facts on edges as the primary durable memory statements. Do not immediately invent a separate parallel "memory record" model.
- Use invalidation for correction and contradiction instead of manual delete-and-reinsert workflows wherever possible.
- Start with Graphiti's custom entity and edge types before adding a second schema layer for Cortex concepts.
- Use `group_id` as the first namespace and isolation seam. Add more complex scope machinery only if needed later.
- Start with native hybrid search and built-in reranking strategies before writing a bespoke retrieval bundle engine.
- Use `build_communities()` and maintenance jobs as Dream-lite. Dream is not the reason to reject this stack.
- When importing documents, chunk them into disciplined episodes with stable source metadata instead of bypassing Graphiti with a separate document store on day 1.

## Best "Do It The OpenClaw Way" Moves

- Keep the built-in `legacy` context engine at first. Replace it only if assembly quality becomes the real bottleneck.
- Use the memory plugin slot and lifecycle hooks first. They are the lighter extension seam.
- Use `before_prompt_build` for dynamic recall injection instead of hard-coding retrieval into prompts elsewhere.
- Use `agent_end` for writeback so ingestion follows the actual turn lifecycle.
- Use OpenClaw automation for periodic graph maintenance, exports, and audit tasks.
- Add read-oriented inspection tools before adding any write-oriented direct graph tools.

## What Still Has To Be Custom

Even with this stack, several Cortex-specific pieces still have to be built:

- the `OpenClaw -> Graphiti` bridge plugin
- scope mapping between OpenClaw identities and Graphiti `group_id` strategy
- artifact and provider identity if Cortex wants first-class artifact objects
- explicit governance and retrieval-boundary policy
- inspection surfaces that are friendlier than raw Cypher or generic MCP tools
- document import discipline and source metadata conventions
- optional service extensions if the stock Graphiti API is too thin

The encouraging part is what does not need to be custom immediately:

- temporal fact lifecycle
- contradiction handling
- episode provenance
- hybrid fact retrieval
- graph-native storage
- Dream-like maintenance basics

## Data Model Posture And Migration Risk

This is where the stack looks unusually good.

`Graphiti` stores:

- episodes as source evidence
- entities as graph nodes
- facts as edges
- temporal validity on those facts
- references back to episodes

That is already close to a plausible long-term Cortex authority model.

So the primary risk is not:

- "Will we need to throw away the stored data model later?"

The primary risk is:

- "Will we accept the operational and integration complexity required to keep this stack clean?"

That is a much better kind of risk.

If Cortex eventually remains graph-first and provenance-first, this stack has low replatform pressure.

If Cortex later pivots to a document-first or generic vector-memory architecture, then this stack may look over-specialized.

## Phased Path

### Phase 0: Stock Core, Thin Bridge

- Run `Neo4j Community` locally.
- Run the stock `Graphiti` service.
- Build a minimal `openclaw-graphiti` plugin that:
  - queries Graphiti before prompt build
  - writes new messages to Graphiti on agent end
- Keep `OpenClaw` on the `legacy` context engine.
- Use stock entity types and disciplined `group_id` naming.

This phase should be enough to get something usable.

### Phase 1: Better Ontology And Recall Discipline

- Add custom entity and edge types aligned to Cortex concepts.
- Add custom extraction instructions.
- Add source metadata conventions for documents and external systems.
- Add read-oriented inspection tools in OpenClaw.
- Schedule periodic `build_communities()` jobs.

This phase turns the stack from "interesting" into "credible."

### Phase 2: Cortex Overlay, Not Cortex Rewrite

- Add a lightweight Cortex overlay for artifact identity and governance policy.
- Add retrieval traces and richer filters if the stock service surface is too thin.
- Add optional context-engine logic only if recall shaping or compaction quality demands it.

This phase should still avoid building a second authority model.

### Phase 3: Optional Maintenance And Projection

- Add Dream-like maintenance only if community rebuilding is not enough.
- Add exports or projections for human inspection.
- Add richer auditing and promotion workflows if they prove valuable.

This phase is bolt-on, not foundational.

## Recommendation

This is a serious wildcard and a real contender.

If the goal is:

- the absolute fastest path to something working

then `Mem0 + OpenClaw` is still easier.

If the goal is:

- the strongest external foundation for a long-lived Cortex memory authority with the lowest chance of a future data-model rebuild

then `Graphiti + Neo4j + OpenClaw` is probably the best wildcard reviewed so far.

My blunt recommendation for this stack is:

- use `Graphiti` as the authority
- use `Neo4j Community` as the local durable store
- use `OpenClaw` as the shell
- bridge them with one thin custom OpenClaw plugin
- prefer the Graphiti FastAPI service as the runtime boundary
- treat the Graphiti MCP server as optional operator tooling, not the primary runtime bridge

For the concrete deployment and rollout path, the implementation details now live in [Graphiti on Moltbox to OpenClaw to Cortex Implementation Plan](graphiti-moltbox-openclaw-implementation-plan.md).

If this stack fails, I do not think it will fail because it is a poor conceptual fit for Cortex.

I think it would fail because the solo-builder integration and operational weight are higher than you want to carry.

That is a meaningful but much more respectable failure mode.

## Sources

- https://help.getzep.com/graphiti/graphiti/overview
- https://help.getzep.com/graphiti/getting-started/quick-start
- https://help.getzep.com/graphiti/working-with-data/searching
- https://help.getzep.com/graphiti/graphiti/graph-namespacing
- https://help.getzep.com/graphiti/graphiti/custom-entity-and-edge-types
- https://help.getzep.com/graphiti/getting-started/mcp-server
- https://github.com/getzep/graphiti/blob/main/graphiti_core/graphiti.py
- https://github.com/getzep/graphiti/blob/main/graphiti_core/edges.py
- https://github.com/getzep/graphiti/blob/main/graphiti_core/search/search_config_recipes.py
- https://github.com/getzep/graphiti/blob/main/server/README.md
- https://github.com/getzep/graphiti/blob/main/server/graph_service/routers/ingest.py
- https://github.com/getzep/graphiti/blob/main/server/graph_service/routers/retrieve.py
- https://neo4j.com/product/community-edition/
- https://neo4j.com/docs/operations-manual/current/docker/introduction/
- https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/
- https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/full-text-indexes/
- https://docs.openclaw.ai/plugins/manifest
- https://docs.openclaw.ai/concepts/context
- https://docs.openclaw.ai/concepts/context-engine
- https://docs.openclaw.ai/concepts/agent-loop
- https://docs.openclaw.ai/automation
