# Git Provider Capability Spec

## 1. Purpose

Provide the first concrete artifact provider implementation for Cortex using a local Git-backed store.

## 2. Capability Boundary

This capability is responsible for:

- local artifact persistence in a Git-backed layout
- stable path resolution for Cortex-owned artifacts
- basic version history via Git
- local-first fallback behavior for unconfigured artifacts

This capability is not responsible for:

- provider routing policy definition in the abstract
- Google Workspace integration
- artifact promotion policy

## 3. MVP Requirements

- local provider implementation for imports and captures
- deterministic storage layout
- ability to resolve artifacts by Cortex artifact ID
- Git-backed history for stored artifacts or artifact containers

## 4. Functional Requirements

- imported artifacts can be written locally
- capture artifacts can be written locally
- local provider can resolve stored content later
- Markdown and system-oriented artifacts have a safe default provider path

## 5. Deferred

- remote Git sync
- GitHub-specific collaboration flows
- encryption-at-rest workflows beyond host or volume configuration
