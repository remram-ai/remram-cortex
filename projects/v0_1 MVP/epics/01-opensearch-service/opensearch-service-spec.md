# OpenSearch Service Technical Spec

## Implementation Goal

Stand up the shared OpenSearch dependency in a way that later Cortex epics can treat as stable retrieval substrate instead of an evolving infrastructure experiment.

## Design Summary

- the service remains a Moltbox-managed appliance service, not a project-local runtime definition
- `remram-cortex` owns Cortex-side expectations such as readiness, bootstrap, index shape, and operator proof
- deployment, restart, and service health stay on the existing `moltbox gateway service ...` path
- Cortex bootstrap runs after service health and owns index and alias creation for Cortex data surfaces

## Implementation Surfaces

- project-local implementation and test plans in this epic folder
- product dependency reference in `product/dependencies/opensearch-service/spec.md`
- service definition in the shared Moltbox service surface outside this repo
- runtime operator evidence through Gateway and native OpenSearch inspection paths

## Integration Boundaries

- later retrieval work depends on this service being reachable, authenticated, and bootstrapped
- artifact storage and provider work may depend on the operator path and diagnostics posture, but not on bespoke service behavior
- this epic does not own retrieval scoring, knowledge extraction, or chat behavior

## Key Constraints

- no parallel service definition inside `remram-cortex`
- distinguish service health from Cortex bootstrap readiness
- keep the first implementation single-node and operator-debuggable

## Definition Of Done

- the Moltbox-managed OpenSearch service can be deployed and inspected
- the dependency posture is documented well enough for later Cortex epics to reuse directly
- the project-local implementation and test plans are complete and consistent with this technical spec
