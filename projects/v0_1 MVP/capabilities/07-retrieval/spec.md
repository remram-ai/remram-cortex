# Retrieval Capability Spec

## 1. Purpose

Return bounded, inspectable knowledge bundles over the combined imported and capture-derived memory pool.

## 2. Capability Boundary

This capability is responsible for:

- governance filtering
- semantic signature bias
- typed signal scoring
- vector assist
- relationship expansion
- final bundle assembly
- retrieval trace output

This capability is not responsible for:

- reflection-time merge decisions
- prompt assembly

## 3. MVP Retrieval Stack

Retrieval should apply:

1. governance filters
2. semantic signature similarity boost
3. typed signal field scoring
4. vector assist
5. relationship expansion
6. final ranking and bundle assembly

## 4. Functional Requirements

- imported and capture-derived knowledge are retrieved from the same pool
- the same concept can be rediscovered through multiple framings
- retrieval remains bounded and inspectable
- retrieval traces show filters and ranking contributors
- relationship expansion enriches but does not replace primary matching

## 5. Acceptance Bar

The MVP should prove at least one concept is discoverable from multiple angles, such as:

- `find more camping spots`
- `how could OpenTrails make money`
- `places to stay while hiking`

## 6. Deferred

- query expansion by default
- multi-query retrieval
- advanced reranker models
