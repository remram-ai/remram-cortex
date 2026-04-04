# Git Service Dependency Spec

## 1. Purpose

Provide the concrete local Git repository or service foundation used by the Git-backed artifact provider.

## 2. Capability Boundary

This capability is responsible for:

- initializing or managing the local Git-backed storage root
- providing a stable repository context for artifact persistence
- supporting local history and recovery for Cortex-owned artifacts

This capability is not responsible for:

- provider routing policy
- knowledge extraction
- retrieval

## 3. MVP Requirements

- one usable local Git-backed storage root
- basic repository initialization or validation
- deterministic location for stored artifact content
- compatibility with the Git provider capability

## 4. Deferred

- remote sync
- GitHub workflows
- advanced repo maintenance automation
