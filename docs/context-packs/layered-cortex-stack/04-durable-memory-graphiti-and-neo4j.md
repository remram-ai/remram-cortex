# Durable Memory: Graphiti And Neo4j

## The Main Decision

Layer 3 remains one `Graphiti` memory system on `Neo4j`.

There is no second Graphiti and no separate concept-mapping graph.

## What Layer 3 Owns

Layer 3 owns:

- concepts
- identities
- relationships
- support
- supersession
- invalidation
- durable continuity across threads and sessions

## What Layer 3 Does Not Own

Layer 3 does not own:

- transcript bodies
- workspace bodies
- document bodies
- the full operational knowledge corpus

It stores concepts and semantic relationships, not whole content bodies.

## Why Graphiti Still Fits

Graphiti already provides what Cortex needs most:

- lineage
- support structure
- point-in-time semantics
- invalidation
- supersession

That means Graphiti can naturally express:

- same emerging idea
- related workspace
- supporting reference
- supersedes
- candidate for promotion

without inventing a second graph subsystem.

## Type Distinctions

Useful type distinctions include:

- `concept`
- `idea_cluster`
- `workspace_anchor`
- `artifact_anchor`
- `reference_anchor`

These are types inside one Layer 3 graph, not separate storage systems.

## Trust Model

The trust model on top of Graphiti should stay minimal.

Useful states include:

- `tentative`
- `low_confidence`
- `active`
- `superseded`
- `invalidated`
- `stale_support`

Do not build a giant second semantics system.

## How Layer 3 Helps Layer 4

Layer 3 helps Layer 4 organize itself by mapping concept relationships across:

- many threads
- many workspaces
- many references

Layer 4 may receive connector fields such as:

- `idea_cluster_id`
- `related_workspace_ids`
- `candidate_for_promotion`
- `promotion_readiness`

The bodies stay in Layer 4.
