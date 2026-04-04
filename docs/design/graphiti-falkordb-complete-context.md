# Graphiti + FalkorDB Complete Context Pack

## Purpose

This document is the full context pack for `Graphiti + FalkorDB` as a serious Cortex foundation path.

It is meant to answer:

- what `Graphiti + FalkorDB` actually is today
- why it feels materially different from the earlier `Graphiti + Neo4j` path
- what worldview we would need to accept if we choose it
- what still has to be custom for Cortex
- where the real risks are

Reviewed on `April 3, 2026`.

## Current Read

`Graphiti + FalkorDB` is the strongest version of the graph-first path reviewed so far.

Bluntly:

- it keeps the main reason `Graphiti` stayed interesting: a graph-native, temporally-aware memory authority
- it removes much of the specific `Neo4j` baggage that made that path feel heavier and less attractive
- it adds a backend that already thinks in graph, vector, full-text, agent-memory, and GraphRAG terms
- it still requires a stronger graph-first commitment than the favored `Mem0` path

This means the recommendation changes slightly:

- `Graphiti + Neo4j` was the strongest old graph path
- `Graphiti + FalkorDB` is the graph path that is actually tempting

It is still not automatically the better first build than `Mem0`.
But it is now much closer than the earlier `Neo4j` framing suggested.

## What This Stack Is Natively

### `Graphiti`

`Graphiti` is still the memory engine.

It natively gives:

- episodic ingestion
- extraction into entities and facts
- temporal validity and invalidation
- graph partitioning with `group_id`
- hybrid search
- configurable search recipes and reranking
- custom entity and edge types
- community building
- library, MCP, and service surfaces

So the authority model remains:

- evidence as episodes
- durable semantics as entities and edges
- time-aware truth as first-class state

### `FalkorDB`

`FalkorDB` is not just "a graph database instead of Neo4j."

Its current posture is broader:

- property graph database
- `openCypher` support
- vector indexing
- full-text indexing
- range indexing
- built-in browser UI
- documented Graphiti support
- documented GraphRAG-SDK support
- explicit agent-memory positioning

This is why it feels different.

`Neo4j` felt like a graph database we had to justify for AI memory.

`FalkorDB` feels like a graph-centered AI memory substrate that already expects graph, vector, full-text, and agent frameworks to coexist.

## What Changes Compared With Graphiti + Neo4j

This is the most important section.

The semantic model does not change.

What changes is the backend posture.

### What gets better

- the stack feels less like a pure graph play
- local Docker bring-up is simpler and more aligned with AI tooling
- full-text and vector indexing are clearly part of the product story
- Graphiti support is now documented from both sides
- the Graphiti MCP server quick start uses FalkorDB as the default database
- FalkorDB also opens a more plausible later path to GraphRAG-style ingestion and graph-native retrieval experiments

### What does not change

- Graphiti is still graph-first
- episodes are still the evidence model
- facts and edges are still the durable authority model
- you still need a custom `OpenClaw` bridge
- you still need to decide whether you are willing to accept graph-first authority from the beginning

So `FalkorDB` reduces backend and ecosystem discomfort.
It does not remove the graph-first architectural commitment.

## Why This Backend Is More Attractive

`FalkorDB` is attractive here for four reasons.

### 1. It is a blended AI substrate, not just a graph store

The docs explicitly position it around:

- graph
- vector
- full-text
- GraphRAG
- agentic memory frameworks

That makes the graph path feel less doctrinaire.

### 2. It has a cleaner local story

Current docs show:

- one Docker container
- port `6379` for the database
- port `3000` for the browser
- persistent volume support

That is a friendlier local posture than a lot of graph stacks.

### 3. Graphiti supports it directly

This is not a speculative adapter path.

Current Graphiti docs and repo show:

- `graphiti-core[falkordb]`
- a dedicated `FalkorDriver`
- FalkorDB as a documented supported backend
- Graphiti MCP quick start using FalkorDB by default

### 4. It creates optional upside for later

Because FalkorDB also has:

- `GraphRAG-SDK`
- agentic memory framework docs
- browser tooling

it offers more than just "persist the graph."

It also offers:

- better graph inspection
- possible later ingestion and reflection experiments
- a more interesting graph platform if the graph path earns its cost

## Native Durable Unit

The canonical durable unit is still the Graphiti graph, not a database row.

That means:

- `Episode` nodes remain evidence
- `Entity` nodes remain durable semantic things
- `EntityEdge` remains the closest durable fact unit
- temporal fields remain part of truth handling

This remains the main reason the graph path is appealing.

## Cortex Mapping

| Cortex concern | Closest `Graphiti + FalkorDB` equivalent | Read |
| --- | --- | --- |
| Durable memory authority | Episodes, entities, facts, temporal edges | Strong |
| Temporal correction | Native invalidation and validity windows | Strong |
| Relationship-aware expansion | Native graph search and reranking | Strong |
| Bounded retrieval | Hybrid search plus filters plus graph recipes | Strong |
| Artifact-backed provenance | Episode evidence plus custom metadata | Good, but still needs Cortex overlay |
| Promotion and clustering | Communities plus derived graph views | Good starting point |
| Local self-hosting | Dockerized FalkorDB plus Graphiti | Better than Neo4j path |
| Runtime shell integration | still custom via `OpenClaw` | Weaker than `Mem0` |

## What To Accept The Graphiti Way

If we choose this path, we should accept five things directly.

### 1. Accept graph-first authority

Do not try to preserve a flat canonical memory row model under Graphiti.

If this stack is chosen, the graph is the authority.

### 2. Accept episodes as provenance

The original Cortex provenance model was simpler.

This path only works if we accept that provenance becomes richer and more graph-shaped through episode linkage.

### 3. Accept hybrid retrieval as native

One of the strongest reasons to choose this stack is that Graphiti already exposes hybrid search as a first-class capability instead of asking us to build it later through a facade.

### 4. Accept graph maintenance as normal

Communities, re-indexing, and derived graph views are not bolt-ons in the same way they are on a vector-first stack.

They become part of the normal lifecycle.

### 5. Accept that graph is allowed to matter in the hot path

This is the biggest philosophical split from the `Mem0` path.

With `Graphiti`, graph is not just reflection output.
It is part of primary retrieval and authority semantics.

## Why This Stack Might Actually Be Better Than Mem0

This is the strongest possible case for it.

If Cortex really does want:

- linked facts as the primary memory unit
- temporal correction as native behavior
- graph-aware expansion by default
- native hybrid search
- communities as first-class maintenance surfaces

then this stack may be the lowest-regret path.

The case is stronger now than it was with `Neo4j` because the backend no longer feels like the wrong kind of graph database.

The real bet becomes simpler:

- do we want graph-first semantics enough to justify early commitment?

If the answer is yes, this is the best graph-first option seen so far.

## Why This Stack Still Might Not Be The First Build

The main restraints remain:

- `OpenClaw` integration is still not first-party and turnkey the way `Mem0` is
- the authority model is more opinionated than the original Cortex implementation sketch
- provenance, inspection, and artifact handling still need more adaptation than on the `Mem0` path

So this is still a stronger architectural bet.

It is just a much more appealing one than before.

## Built-In Extension Surfaces Worth Using

### Graphiti

- `FalkorDriver`
- hybrid search
- low-level search recipes
- entity and edge customization
- `group_id` namespacing
- community building
- MCP server

### FalkorDB

- vector indexes
- full-text indexes
- range indexes
- browser UI
- persistence on Docker
- GraphRAG-SDK
- official MCP server

### OpenClaw

- memory plugin slot
- context engine slot
- lifecycle hooks
- tools
- services

## What Still Has To Be Custom

Even on the optimistic read, we still need:

- an `OpenClaw -> Graphiti` bridge
- Cortex ontology contract
- artifact and provider identity
- ingestion policy
- retrieval tracing
- operator inspection surfaces
- promotion policy
- governance wrapper above `group_id`

The difference is that this work is now more integration and policy work than backend discomfort work.

## Main Risks

The real risks are:

- graph-first turns out to be more commitment than the first build needed
- the custom `OpenClaw` bridge becomes more work than expected
- provenance becomes richer but harder to reason about operationally
- FalkorDB-specific limitations matter in areas Graphiti or Cortex actually depend on

## FalkorDB-Specific Caveats

These should be kept explicit.

- the docs mark Bolt support as experimental and recommend official client libraries for production use
- FalkorDB documents known `openCypher` limitations
- GraphRAG toolkit support exists, but FalkorDB’s backend there currently does not support traversal-based search

These are not dealbreakers for the Graphiti path because:

- Graphiti uses its own Falkor driver over Redis protocol, not Bolt
- the core Graphiti path does not depend on the AWS GraphRAG toolkit

But they are still worth remembering.

## Blunt Recommendation

If we reopen the graph-first path seriously, this is now the right version of it.

Bluntly:

- `Graphiti + FalkorDB` is the first graph-first stack that feels truly aligned and practically appealing
- it is still a stronger architecture bet than `Mem0`
- but it is now close enough that it deserves equal serious consideration, not just “wildcard” status

## Source Map

- https://help.getzep.com/graphiti/graphiti/overview
- https://help.getzep.com/graphiti/working-with-data/searching
- https://help.getzep.com/graphiti/configuration/falkor-db-configuration
- https://help.getzep.com/graphiti/getting-started/mcp-server
- https://github.com/getzep/graphiti
- https://docs.falkordb.com/agentic-memory/graphiti.html
- https://docs.falkordb.com/agentic-memory/
- https://docs.falkordb.com/cypher/indexing/
- https://docs.falkordb.com/operations/persistence.html
- https://docs.falkordb.com/browser/
- https://docs.falkordb.com/genai-tools/graphrag-sdk.html
- https://docs.falkordb.com/integration/bolt-support.html
- https://docs.falkordb.com/cypher/known-limitations.html

