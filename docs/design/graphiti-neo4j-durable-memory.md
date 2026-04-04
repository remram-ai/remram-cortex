# Graphiti + Neo4j Durable Memory

This document defines the active Layer 3 posture after design lock.

## Role

Layer 3 is the durable semantic authority.

It owns:

- concepts
- identities
- relationships
- support
- supersession
- invalidation
- durable semantic continuity across threads and sessions

It is implemented as one `Graphiti` memory system on `Neo4j`.

## What Layer 3 Stores

Layer 3 stores:

- durable concepts
- idea clusters
- workspace relationships
- artifact and reference anchors
- support relationships
- promotion readiness signals
- semantic supersession and invalidation

Layer 3 does not store:

- transcript bodies
- workspace bodies
- document bodies
- full operational knowledge records

Hard rule:

**Layer 3 stores concepts and semantic relationships, not whole content bodies.**

## Why Graphiti

`Graphiti` remains the Layer 3 center because it already aligns with Cortex needs:

- episode-backed provenance
- temporal validity
- invalidation rather than blind overwrite
- durable graph-native relationships
- continuity across threads and sessions

That means Cortex does not need a second concept-mapping graph.

The same Layer 3 system can naturally represent:

- that several threads belong to one budding idea
- that two workspaces are related or merged
- that one workspace supersedes another
- that references support a concept
- that a workspace is becoming a promotion candidate

## Useful Type Distinctions

Useful type distinctions inside Layer 3 may include:

- `concept`
- `idea_cluster`
- `workspace_anchor`
- `artifact_anchor`
- `reference_anchor`

These are not separate memory systems.

They are type distinctions inside one Layer 3 graph.

## Why Neo4j

`Neo4j` remains the backend because it is:

- durable
- disk-backed
- aligned with long-lived memory integrity

The architecture is optimizing Layer 3 for durable semantic truth, not for RAM-heavy graph speed.

## Confidence And Trust

Graphiti clearly provides:

- temporal lineage
- support structure
- invalidation
- supersession

It does not need a giant second semantics layer on top of it.

The Cortex trust model should stay minimal.

Use lightweight states such as:

- `tentative`
- `low_confidence`
- `active`
- `superseded`
- `invalidated`
- `stale_support`

Optional per-edge or per-support confidence signals are acceptable if they remain lightweight.

## Layer 3 And Layer 4

Layer 3 helps Layer 4 organize itself.

It may represent:

- same emerging idea
- related workspace
- supporting reference
- supersedes
- candidate for promotion

Layer 4 may receive lightweight connector fields from this process, for example:

- `idea_cluster_id`
- `related_workspace_ids`
- `candidate_for_promotion`
- `promotion_readiness`

The bodies remain in Layer 4.

The conceptual relationship network remains in Layer 3.

## Artifact And Reference Lineage

Artifact and reference lineage should both exist in Layer 3.

The clean pattern is:

- represent the artifact or reference as an anchor entity
- keep pointer-based links back to Layer 4 or Layer 5
- connect concepts, support, and supersession through those anchors

Graphiti should not become a body store.

It should remain a semantic relationship system with stable pointers outward.

## Promotion Model

Layer 3 promotion should happen from:

- reconciled notions from Layer 2
- stable semantic conclusions from Layer 4 operational workspaces
- durable meaning extracted from external references

Layer 3 should not receive raw transcript or workspace bodies as its normal representation.

## Non-Goals

Layer 3 is not:

- the hot notion ledger
- the transcript archive
- the workspace body store
- the artifact body store
- a second document management system

## Bottom Line

Layer 3 remains one Graphiti memory system.

It owns durable semantic truth and the concept relationship network that helps Layer 4 organize operational content.
