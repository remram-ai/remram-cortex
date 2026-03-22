# Retrieval Technical Spec

## Implementation Goal

Turn stored knowledge into bounded, inspectable retrieval bundles that satisfy the Cortex retrieval model.

## Design Summary

- retrieval is governance-first, not vector-first
- imported and captured knowledge are queried through the same retrieval pool
- output is a bounded bundle plus traceable evidence of why those results were selected
- OpenSearch is substrate; Cortex still owns retrieval semantics and trace shaping

## Implementation Surfaces

- project-local implementation and test plans in this epic folder
- capability reference in `product/capabilities/retrieval/spec.md`
- upstream dependency on OpenSearch readiness and knowledge-object shape

## Integration Boundaries

- consumes the OpenSearch dependency and Knowledge Extraction outputs
- feeds Chat Injection and later chat proof surfaces
- does not own provider behavior or chat UX

## Key Constraints

- keep retrieval inspectable rather than hidden ranking
- unify imported and captured knowledge
- stop at the retrieval-bundle boundary

## Definition Of Done

- governance-first, inspectable retrieval is working
- imported and captured knowledge can be retrieved from the same pool
- the project-local implementation and test plans are complete and consistent with this technical spec
