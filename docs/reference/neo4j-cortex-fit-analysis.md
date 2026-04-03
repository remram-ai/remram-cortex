# Neo4j Cortex Fit Analysis

## Purpose

This document evaluates `Neo4j` under the same decision lens as the current primary-foundation work:

- one-builder implementation burden
- local and free base infrastructure
- fastest path to something usable
- lowest likelihood of replatforming stored data later
- strongest fit to a memory authority layer, not just a retrieval subsystem

Reviewed on `April 2, 2026`.

This is specifically an evaluation of **raw Neo4j as a Cortex anchor or storage-first wildcard**, not of `Graphiti`, which already uses graph backends such as `Neo4j`.

## Executive Take

`Neo4j` is more serious than `Qdrant` as a long-term Cortex substrate.

It is also more structurally aligned to Cortex than most plain vector databases because it naturally supports:

- explicit relationships
- provenance links
- graph traversal
- evolving typed entities and facts

But raw `Neo4j` still does **not** win the primary-foundation decision.

The blunt read is:

- better long-term wildcard than `Qdrant`
- more graph-native than `Weaviate`
- slower to first usefulness than `Weaviate`
- weaker than `Graphiti on Neo4j` as an actual memory-authority path

If you know you want `Neo4j`, the most credible route is usually:

**pick `Graphiti` and use `Neo4j` as its backend**

rather than:

**start from raw Neo4j and build the full memory layer yourself**

## What Neo4j Actually Is

From the current official docs, `Neo4j` Community Edition is a self-managed graph database you can run locally, including via the official Docker image.

Relevant capabilities for Cortex:

- nodes and relationships as first-class records
- Cypher query language
- full-text indexes
- vector indexes
- relationship vector indexes
- graph traversal and path queries

Important current details:

- vector indexes can index nodes or relationships
- as of `Neo4j 2026.01`, vector indexes can include extra properties for filtering
- full-text indexes use Lucene and are queried explicitly
- vector search remains approximate nearest-neighbor search

Those are meaningful capabilities, but they do not make Neo4j a memory platform by themselves.

## Strongest Mapping To Cortex

### 1. Links As Primary

This is Neo4j's biggest natural advantage.

Cortex already prefers:

- one object with many links
- derived views over bucket-first organization
- provenance relationships

That maps naturally to a graph database.

### 2. Provenance And Evidence

Neo4j is a very believable substrate for:

- artifact nodes
- evidence slice nodes
- knowledge-object nodes
- provenance edges
- contradiction and supersession edges

This is much richer than payload metadata stuffed into a vector store.

### 3. Relationship Expansion

Relationship expansion is almost a first-class Cortex retrieval move.

Neo4j is the strongest reviewed substrate for that specific pattern because traversal is native instead of bolted on.

### 4. Temporal And Versioned Memory

Neo4j does not give you temporal memory policy out of the box.

But it gives you a very believable place to model:

- valid-from and valid-to
- superseded-by
- contradicted-by
- derived-from

This means the stored model can evolve forward without feeling cramped.

## Where Neo4j Is Weaker Than It First Looks

### 1. It Is Not A Memory Engine

This is the main limiting fact.

Neo4j does **not** provide:

- extraction logic
- memory update policy
- merge rules
- Dream-like maintenance loops
- artifact intake discipline
- retrieval bundle shaping

So choosing Neo4j means choosing to build those yourself or choosing a framework above it.

### 2. Hybrid Retrieval Is More Manual

Neo4j has both vector and full-text search, but the retrieval ergonomics are not as turnkey as `Weaviate` or a search engine.

Important tradeoffs from the official docs:

- full-text indexes are queried explicitly rather than being automatically chosen by the Cypher planner
- vector search is ANN-based and approximate
- filtered vector search is newer

That means you can build strong retrieval, but you will build more of the score fusion and retrieval discipline yourself.

### 3. One-Builder Burden Is Higher

Raw Neo4j pushes more design burden onto you:

- graph schema decisions
- relationship semantics
- temporal modeling
- query tuning
- retrieval fusion

For one builder, that burden matters.

## Evaluation Under The Current Decision Lens

### Memory Authority Fit

`Neo4j` as a raw database is a **medium** fit for the memory authority role.

Why not higher:

- it is still a substrate, not a memory framework
- authority behavior must be designed above it

Why not lower:

- the stored model can genuinely represent Cortex-like knowledge and provenance better than most vector-first stores

If paired with `Graphiti`, the effective fit rises substantially.

### Custom Work Still Required

Custom work required is **high**.

You would still need to build:

- extraction and update policy
- artifact and provenance contracts
- retrieval traces and bundle shaping
- lifecycle and governance logic
- review and maintenance flows

That is why raw Neo4j does not beat `Mem0` or `Graphiti`.

### Long-Term Migration Risk

Migration risk is **low-medium**.

Why relatively good:

- graph entities and relationships are not a dead-end shape
- provenance and typed links can be modeled honestly
- temporal upgrades are plausible

Why not simply low:

- if you later decide you do **not** want graph-first memory, then moving out of Neo4j could still be painful

So Neo4j is a strong storage commitment, not a neutral temporary store.

### Stored Data Model Evolvability

This is `Neo4j`'s best score.

Stored-model evolvability is **high**.

You can model:

- knowledge objects
- artifacts
- evidence slices
- people and projects
- typed links
- provenance chains
- conflict and version relationships

That is a strong long-term data posture.

### Path Toward Final Cortex

`Neo4j` keeps you on a believable path toward final Cortex **if**:

- you accept graph-first durable memory
- you are comfortable building more of the service semantics yourself

That is a real path.

It is just a heavier path than the better-ranked options.

## Neo4j Versus The Current Field

### Versus Weaviate

`Neo4j` is better for:

- relationship-rich memory
- provenance modeling
- graph traversal
- explicit contradiction and supersession structures

`Weaviate` is better for:

- faster initial usefulness
- easier hybrid retrieval
- lower one-builder retrieval complexity
- object-plus-vector storage without full graph commitment

For the current decision lens, `Weaviate` still edges out raw `Neo4j` as the storage-first wildcard because it gets to a usable system faster.

### Versus Qdrant

`Neo4j` is stronger than `Qdrant` as a long-term Cortex wildcard.

Why:

- richer evolvable model
- real relationships
- provenance is more natural
- lower odds of future data-shape regret

`Qdrant` is still easier if you only want fast local retrieval.

But on the memory-authority axis, Neo4j wins.

### Versus Graphiti

This is the most important comparison.

If you are drawn to `Neo4j` because:

- links matter
- provenance matters
- temporal facts matter
- graph-native memory feels right

then raw Neo4j is usually the **wrong** way to act on that instinct.

The better move is:

- choose `Graphiti`
- run it on `Neo4j`

because `Graphiti` already supplies the memory semantics raw Neo4j does not.

That is why Neo4j is not promoted into the top three by itself.

## Recommendation

`Neo4j` should stay in the field, but as a **storage-first wildcard**, not as the recommended primary foundation.

My practical recommendation is:

- do not replace `Mem0` with raw `Neo4j` as the top recommendation
- do rank `Neo4j` above `Qdrant` as a long-term custom-storage option
- if the real attraction is graph-native memory, prefer `Graphiti on Neo4j` over raw Neo4j

## Blunt Conclusion

Raw `Neo4j` is:

- more serious than `Qdrant`
- more structurally aligned than `Weaviate`
- less practical than `Weaviate` for a fast one-builder start
- less compelling than `Graphiti` as an actual memory-authority path

So the net call is:

**evaluate Neo4j as a worthwhile wildcard, but do not promote it above Graphiti or Mem0 as the primary foundation.**

## Sources

- Neo4j Community Edition: https://neo4j.com/product/community-edition/
- Neo4j Docker getting started: https://neo4j.com/docs/operations-manual/current/docker/introduction/
- Neo4j vector indexes: https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/
- Neo4j full-text indexes: https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/full-text-indexes/
- Neo4j vector search with filters overview: https://neo4j.com/blog/developer/vector-search-with-filters-in-neo4j-v2026-01-preview/
