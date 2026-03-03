# remram-cortex

Knowledge authority for the Remram system.

Remram Cortex is a Go service responsible for structured memory, semantic retrieval, and knowledge consolidation. It provides durable, queryable context to agents and client applications while remaining independent from runtime packaging and behavioral logic.

Cortex owns memory.
It does not own execution or agent behavior.

---

## Purpose

`remram-cortex` provides persistent, structured knowledge for the Remram ecosystem.

It is responsible for:

- Semantic indexing and retrieval
- Structured knowledge storage
- Memory consolidation and reflection routines
- Search schema management
- Exposing a service interface for agents and applications

Cortex is implemented as a standalone Go service.

---

## Project Structure (Go Service Layout)

This repository follows standard Go service conventions.

```
remram-cortex/
  README.md
  go.mod
  go.sum

  cmd/
    cortex/
      main.go

  internal/
    api/
    core/
    storage/

  migrations/
  config/
  scripts/
```

### Root Files

- `go.mod` / `go.sum` — Go module definition and dependencies.
- `README.md` — Repository documentation.

### `cmd/`

Entrypoint binaries.

- `cmd/cortex/main.go` — Application bootstrap, configuration loading, and server start.

### `internal/`

Core service logic (not intended for external reuse).

- `api/` — Transport layer (HTTP and/or future RPC surfaces).
- `core/` — Domain logic for indexing, retrieval, and memory operations.
- `storage/` — Persistence abstractions and OpenSearch integration.

Domain boundaries inside `core/` may evolve as Cortex matures.

### `migrations/`

Search index templates, mappings, and schema evolution.

### `config/`

Service configuration templates and environment bindings.

### `scripts/`

Operational utilities such as bootstrap or maintenance helpers.

---

## Interface Surface

Cortex will expose a service interface for:

- Agent memory queries
- Application-level knowledge access
- Structured ingestion and indexing

The transport mechanism (REST, RPC, or hybrid) is intentionally not fixed at this stage. The repository is structured to support evolution of the API layer without impacting core memory logic.

---

## Relationship to Other Repositories

- `remram-gateway` provisions and connects to Cortex.
- `remram-agents` query Cortex for structured memory.
- `remram-app` consumes Cortex data for user-facing experiences.
- `remram` documents the overall system.

Cortex remains isolated from runtime packaging and agent definitions.

---

## Design Principle

Cortex provides persistent, structured knowledge.

Agents interpret.
Gateway executes.
Cortex remembers.

