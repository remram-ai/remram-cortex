# Cortex Inspection Surfaces

## 1. Purpose

This design note captures the human inspection surfaces that should exist around Cortex memory and artifacts.

These surfaces are not the canonical storage model and not the primary retrieval mechanism. They are derived projections built so a human can browse, inspect, debug, and search Cortex-owned memory.

## 2. Core Rule

Cortex remains graph-first:

- knowledge objects are canonical
- artifacts have stable Cortex-owned identity after intake
- links are many-to-many

Any tree, map, or hierarchy shown to a user is a projection over that graph.

It must not become:

- the source of truth for memory organization
- a replacement for typed retrieval signals
- a dependency on the original source-system folder tree

## 3. Canonical Inputs

The inspection layer should project over Cortex-owned records:

- knowledge objects
- Cortex-managed imported artifacts
- Cortex-promoted artifacts
- typed links between them
- governance scope such as person, family, project, and system

External origin information such as Drive folder, chat attachment source, or local import path should remain provenance only.

## 4. Primary Surfaces

### 4.1 Tree View

Tree View is the simplest human-browsing surface.

It should allow a chosen root such as:

- `person:jason`
- `group:family`
- `project:opentrails`
- `artifact:art_...`

The tree is not a physical storage tree. It is a deterministic browsing projection.

Practical first-pass grouping can use:

- scope root
- linked projects or knowledge spaces
- artifacts
- knowledge objects

Where multiple parents are possible, Tree View may choose a primary display path for browsing convenience while preserving full link visibility in the detail pane.

### 4.2 Graph View

Graph View shows the actual many-to-many neighborhood around a selected node.

It is the right surface for:

- exploring linked concepts
- seeing why one fact touches multiple projects or contexts
- understanding artifact-to-object and object-to-object relationships

Graph View should remain bounded around a chosen root or search result. It does not need to render the whole memory graph at once.

### 4.3 Search And Inspect View

Search View is the primary debugging surface.

A user should be able to:

- search for a suspected fact or assumption
- open the matching object or artifact
- inspect its statement or summary
- inspect its provenance
- inspect its links
- inspect retrieval signals and, when relevant, retrieval traces

This is the best surface for debugging bad assumptions, duplicate memories, or suspicious retrieval behavior.

## 5. Mind Map Projection

The "mind map" feature should be treated as a specialized projection, not a different storage model.

A practical model is:

1. choose a root such as a person, project, or artifact
2. expand a bounded neighborhood by typed links
3. render that neighborhood as either:
   - a tree-like mind map for human readability
   - a graph when link density matters more than hierarchy

This can be built deterministically from stored structure.

It does not require sending the entire memory graph to an LLM. LLM help may later improve labels or summaries, but the projection itself should be computable locally from Cortex data.

## 6. Relationship To Retrieval

The inspection hierarchy should not be reused as the retrieval facet system.

Retrieval remains:

- governance-first
- signature-biased
- typed-signal-driven
- OpenSearch-scored

Inspection is for human understanding after or alongside retrieval, not the primary search engine.

## 7. MVP Boundary

Full Tree View and Graph View are beyond the v0.1 MVP.

The MVP should still preserve the prerequisites for them:

- stable Cortex artifact IDs
- source-linked provenance
- typed links
- retrieval traces

The minimum v0.1 inspection surface is:

- search by object or artifact
- open provenance
- inspect why a result was retrieved

That is enough to debug the memory model before a richer visualization layer exists.
