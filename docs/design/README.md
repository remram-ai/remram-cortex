# Design

`docs/design/` holds the active architecture and implementation design for the current Cortex direction.

The active design set is intentionally small.

Historical comparisons, rejected stack options, and older MVP packages were moved to the archive.

The canonical authority order inside active docs is:

1. [../authority-map.md](../authority-map.md)
2. [../glossary.md](../glossary.md)
3. this folder
4. supporting summaries elsewhere in the repo

## Active Documents

- [Agent Tool Graph](agent-tool-graph.md)
- [Layered Memory Architecture](layered-memory-architecture.md)
- [Technology Stack](technology-stack.md)
- [OpenClaw Integration](openclaw-integration.md)
- [Graphiti + Neo4j Durable Memory](graphiti-neo4j-durable-memory.md)
- [Knowledge And Artifact Architecture](knowledge-and-artifact-architecture.md)
- [Deployment Plan](deployment-plan.md)

## How To Read This Folder

For live Moltbox appliance work, load the current Gateway guides and design docs first.

This folder describes the active Cortex architecture and intended integration shape, but it does not override `moltbox-gateway` on:

- live service inventory
- live CLI surfaces
- restricted-operator validation
- snapshot-first recovery behavior
- current web-tooling baseline

Repo authority split for live Moltbox work:

- `moltbox-gateway`: operator/control-plane behavior
- `moltbox-services`: baseline service definitions, baseline service config, service-local docs
- `moltbox-runtime`: final promoted runtime artifacts and overlays
- `remram-skills`: reusable skills/plugins

Do not treat this repo as the service-definition authority for the live appliance.

1. Start with [Layered Memory Architecture](layered-memory-architecture.md)
2. Read [Technology Stack](technology-stack.md)
3. Read [Agent Tool Graph](agent-tool-graph.md)
4. Read [OpenClaw Integration](openclaw-integration.md)
5. Read [Graphiti + Neo4j Durable Memory](graphiti-neo4j-durable-memory.md)
6. Read [Knowledge And Artifact Architecture](knowledge-and-artifact-architecture.md)
7. Use [Deployment Plan](deployment-plan.md) for implementation posture

Historical material now lives under [archive/](../../archive/README.md).
