# Graphiti + FalkorDB + OpenClaw Implementation Plan

## Purpose

This document is the implementation plan for the `Graphiti + FalkorDB + OpenClaw` path.

It covers the full path from local container bring-up through runtime integration and later Cortex-specific overlay work.

Reviewed on `April 3, 2026`.

## Blunt Read

This is the right implementation plan if we decide the graph-first path is worth the extra commitment.

The right order is:

1. stand up `FalkorDB` and `Graphiti`
2. prove ingestion and search with FalkorDB as backend
3. connect `OpenClaw` through a thin bridge
4. add artifact and provenance discipline
5. add operator inspection and maintenance flows

Do not start by writing a big custom Cortex service first.

## Planning Assumptions

- one builder, heavily AI-assisted
- Dockerized external services are acceptable
- model APIs are acceptable if they reduce risk
- `Graphiti` remains the only memory authority
- `FalkorDB` replaces `Neo4j` as the backend assumption

## Target End State

```text
OpenClaw
  - runtime orchestration
  - graphiti bridge plugin
  - hooks and tools
        |
        v
Graphiti service boundary
  - ingestion
  - search
  - graph maintenance
        |
        v
FalkorDB
  - graph storage
  - vector index
  - full-text index
  - browser
        |
        +--> optional Graphiti MCP server
        +--> optional operator tooling
        +--> optional GraphRAG sidecars later
```

## Phase 0: Backend Bring-Up

Goal:

- prove `Graphiti` runs cleanly on `FalkorDB`

Containers:

- `falkordb`
- `graphiti` service or direct local Graphiti runtime

Recommended baseline:

- run FalkorDB with persistence
- use `graphiti-core[falkordb]`
- connect via `FalkorDriver`
- disable telemetry if desired

Verification:

- build indices and constraints
- add sample episodes
- run `graphiti.search(query)`
- inspect graph in FalkorDB browser

Exit criteria:

- Graphiti ingest and search work end to end on FalkorDB

## Phase 1: Service Boundary

Goal:

- create a stable runtime boundary for `OpenClaw`

Recommended posture:

- prefer a small Graphiti service boundary over direct in-process OpenClaw integration

Why:

- `OpenClaw` is likely TypeScript-facing
- `Graphiti` is Python-first
- a service boundary keeps the plugin thin

Implementation options:

- extend Graphiti’s FastAPI service
- or wrap Graphiti core in a small Cortex-owned Python service

Recommendation:

- start with Graphiti’s own service surface where possible
- fork or extend only when needed

## Phase 2: OpenClaw Bridge

Goal:

- make Graphiti usable as an OpenClaw memory backend

Build a thin plugin that:

- stores post-turn interactions as episodes
- retrieves memory through Graphiti search
- injects compact context into prompts
- exposes a few inspection tools

Suggested tools:

- `graphiti_search_facts`
- `graphiti_search_nodes`
- `graphiti_get_recent_episodes`
- `graphiti_clear_group` for admin only

Exit criteria:

- OpenClaw can use Graphiti-backed memory in normal runtime flow

## Phase 3: Artifact And Provenance Discipline

Goal:

- align the graph path with Cortex artifact expectations

Add:

- artifact identity fields
- provider fields
- artifact revision fields
- consistent `source_description`
- episode metadata normalization

Important rule:

- artifacts stay external
- Graphiti stores extracted knowledge plus evidence links

Exit criteria:

- artifact-derived episodes and facts are inspectable and traceable

## Phase 4: Retrieval Shaping

Goal:

- tune Graphiti’s native retrieval instead of replacing it

Work:

- choose default search recipes
- decide when to use plain hybrid vs focal-node reranking
- define `group_id` strategy
- add governance wrapper rules around query compilation

This is one of the biggest advantages of the stack:

- hybrid retrieval is already native

So this phase should be mostly policy and tuning, not plumbing.

## Phase 5: Inspection And Maintenance

Goal:

- make the graph path operable

Add:

- read-only inspection tools
- retrieval traces
- browser-based graph inspection workflow
- maintenance jobs for community building or graph cleanup
- optional Graphiti MCP server for operator or IDE access

Exit criteria:

- we can explain why a fact was returned
- we can inspect supporting episodes and graph neighborhoods

## Phase 6: Promotion And Higher-Order Cortex Logic

Goal:

- add Cortex-specific support and promotion behavior on top of the graph authority

Add:

- support-summary generation
- promotion candidate detection
- artifact proposal flows
- contradiction review workflows

This is where the stack becomes recognizably Cortex-like.

## Recommended Container Layout

Baseline:

- `falkordb`
- `graphiti-service`

Phase 2 onward:

- `openclaw`

Phase 5 onward:

- `graphiti-mcp` optional
- `cortex-operator-api` optional

Phase 6 onward:

- `promotion-worker`

## Repo Landing Zones

Suggested implementation boundaries:

- `deploy/moltbox/graphiti-falkordb/compose.yml`
- `plugins/openclaw-graphiti/`
- `services/graphiti-service/`
- `services/cortex-operator-api/`
- `packages/cortex-ontology-contract/`

## What Not To Build Early

Do not build these first:

- direct raw FalkorDB writes from app code
- parallel file-based memory authority
- a custom search stack replacing Graphiti hybrid retrieval
- a custom graph engine beside Graphiti
- GraphRAG sidecars before the main graph loop works

## FalkorDB-Specific Notes

Use FalkorDB the supported way:

- connect through Graphiti’s Falkor driver over Redis protocol
- do not depend on Bolt for primary production behavior
- use the browser for inspection
- enable persistence from day 1

Keep two cautions visible:

- Bolt support is experimental
- FalkorDB documents known Cypher limitations

Neither should block the Graphiti path if we stay within the supported driver path.

## Time Estimate

AI-assisted, realistic rough estimate:

- FalkorDB + Graphiti baseline: `2 to 5 days`
- OpenClaw bridge prototype: `1 week`
- artifact and provenance discipline: `1 to 2 weeks`
- inspection and maintenance surfaces: `1 to 2 weeks`
- credible Cortex-like v1 on this stack: `5 to 8 weeks`

## Blunt Recommendation

If we choose the graph-first path, this is now the right implementation plan.

Bluntly:

- replace `Neo4j` with `FalkorDB`
- keep Graphiti authoritative
- keep OpenClaw thin
- tune native hybrid search before building custom retrieval
- let FalkorDB’s broader AI posture help, but do not confuse that with reduced conceptual commitment

This is the strongest graph-first implementation plan we have so far.

## Source Map

- https://help.getzep.com/graphiti/configuration/falkor-db-configuration
- https://help.getzep.com/graphiti/working-with-data/searching
- https://help.getzep.com/graphiti/getting-started/mcp-server
- https://github.com/getzep/graphiti
- https://docs.falkordb.com/agentic-memory/graphiti.html
- https://docs.falkordb.com/agentic-memory/
- https://docs.falkordb.com/operations/persistence.html
- https://docs.falkordb.com/browser/
- https://docs.falkordb.com/cypher/indexing/
- https://docs.falkordb.com/integration/bolt-support.html
- https://docs.falkordb.com/cypher/known-limitations.html
- https://docs.falkordb.com/genai-tools/graphrag-sdk.html

