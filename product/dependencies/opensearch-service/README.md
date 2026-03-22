# OpenSearch Service Dependency

OpenSearch is a platform-owned dependency for Cortex, not a Cortex-native capability.

The canonical service bundle lives in the main `remram` repository:

- [Platform README](../../../../remram/platform/services/opensearch/README.md)
- [Platform Spec](../../../../remram/platform/services/opensearch/spec.md)
- [Platform Operator Guide](../../../../remram/platform/services/opensearch/operator-guide.md)
- [Platform Test Plan](../../../../remram/platform/services/opensearch/test-plan.md)

## Local Role

Cortex still depends on this service for MVP retrieval and indexing readiness.

The local files in this folder are transitional Cortex dependency notes and should not drift away from the platform-owned service contract.

Local documents:

- [spec.md](spec.md)
- [regression-plan.md](regression-plan.md)
- [regression-plan.json](regression-plan.json)

When the platform item fully captures the needed posture, this folder can collapse to this README alone.
