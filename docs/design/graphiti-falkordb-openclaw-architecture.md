# Graphiti + FalkorDB + OpenClaw Architecture

## Purpose

This memo defines the lifecycle architecture for:

- `OpenClaw` as runtime shell
- `Graphiti` as memory authority
- `FalkorDB` as graph, vector, and full-text substrate

Reviewed on `April 3, 2026`.

## Executive Take

This is the cleanest graph-first architecture found so far.

It works because:

- `Graphiti` owns the authority model
- `FalkorDB` provides a backend posture that is more aligned with modern AI retrieval than the earlier `Neo4j` path
- `OpenClaw` still gives the runtime shell and lifecycle hooks we want

The architecture is coherent if one rule stays fixed:

- only Graphiti writes durable memory authority state

## Core Rule

Canonical memory lives in the Graphiti graph.

That means:

- raw artifacts stay external
- `OpenClaw` transcripts are evidence, not authority
- `FalkorDB` is Graphiti's implementation substrate, not an app-owned peer schema
- any Cortex overlay points into Graphiti, not around it

## High-Level Shape

```text
Channels / CLI / Apps
        |
        v
OpenClaw Runtime
  - sessions
  - hooks
  - tools
  - thin graphiti bridge plugin
        |
        v
Graphiti Service
  - episode ingestion
  - entity and edge extraction
  - temporal invalidation
  - hybrid search
  - community building
        |
        v
FalkorDB
  - graph storage
  - vector indexing
  - full-text indexing
  - range indexing
  - browser UI
        |
        +--> Optional Graphiti MCP server
        +--> Optional Cortex operator API
        +--> Optional GraphRAG / reflection sidecars
```

## Why This Is Different From Graphiti + Neo4j

The authority model is the same.

The backend attitude is different.

With FalkorDB:

- the backend already expects graph and vector and full-text to coexist
- local inspection is simpler because the browser ships in the container
- the backend is already documented in agent-memory and GraphRAG contexts

So the stack feels less like a pure graph bet and more like a graph-centered AI memory platform.

## Retrieval Model

Retrieval stays Graphiti-native.

That means:

- hybrid semantic + BM25 retrieval
- optional reranking recipes
- optional focal-node distance weighting
- graph-aware context expansion

The important difference from the `Mem0` path is:

- graph is allowed in the primary retrieval model
- we do not need a second retrieval facade later just to get lexical + vector hybrid behavior

## Artifact Model

Artifacts remain external.

Graphiti should store:

- episodes derived from artifacts
- source description
- source metadata
- artifact identity and revision metadata in episode or attached node properties
- links from facts back to evidence episodes

Graphiti should not store:

- raw Git repos as authority
- full artifact bodies as the only durable representation

This keeps the graph authoritative for knowledge, not for raw files.

## Why FalkorDB Matters Here

FalkorDB adds value in four places:

### 1. Full-text and vector live with the graph

This makes the graph path feel less detached from modern retrieval practice.

### 2. Browser-native inspection

The built-in browser is a real operator advantage.

### 3. Better local ergonomics

The Docker and persistence story is straightforward.

### 4. Optional GraphRAG upside

If later we want graph-native ingestion or ontology-driven retrieval experiments, FalkorDB already has adjacent GraphRAG tooling.

## What OpenClaw Needs To Do

`OpenClaw` should stay thin here.

Its job is:

- send episodes to Graphiti
- fetch memory context from Graphiti
- attach context to prompts
- expose a few inspection tools
- schedule or trigger maintenance jobs if useful

It should not:

- keep a peer durable memory model
- reshape Graphiti into flat memory rows

## What Cortex Needs To Own

Cortex should own:

- ontology contract
- artifact identity contract
- governance wrapper above `group_id`
- retrieval tracing
- operator inspection UX
- promotion and support-summary policy

That is the right custom layer for this path.

## Risks

The main risks are:

- committing to graph-first before the first build proves it is needed
- underestimating the bridge work to `OpenClaw`
- treating FalkorDB's broader AI posture as proof that the whole graph-first stack is automatically lower effort

## Recommendation

If the graph-first path stays alive, this should replace the old `Graphiti + Neo4j` baseline as the serious version of it.

Bluntly:

- Graphiti remains the authority
- FalkorDB makes the backend finally feel interesting
- OpenClaw remains the runtime shell

This is now the right graph-first reference architecture.
