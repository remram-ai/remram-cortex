# Artifact Storage Capability Regression Plan

## 1. Goal

Prove that Cortex artifact identity is stable, that provider behavior is governed by one explicit contract, and that artifacts can be created, versioned, linked back to, and pruned without making external source layout canonical.

This capability is not complete just because one provider can write bytes somewhere.
It is complete when downstream providers have a concrete contract to implement and Cortex can preserve identity, version history, provenance navigation, and prune behavior across provider types.

## 2. Required Test Areas

### 2.1 Provider Contract Completeness

- provider contract defines required operations for create, resolve, open, write-version, prune, and backlink generation
- the contract clearly assigns `artifact_id` ownership to Cortex rather than providers
- the contract clearly assigns Cortex `version_ref` ownership to Cortex rather than providers
- provider-native revision handles have a defined place in the contract

### 2.2 Provider Configuration And Routing

- provider registry shape is defined
- default provider behavior is defined
- routing rules are policy-based rather than source-path-based
- configuration validation rules are defined
- fallback-to-default behavior is defined explicitly rather than implicitly

### 2.3 Identity And Record Creation

- import artifact gets an opaque `artifact_id`
- capture artifact gets an opaque `artifact_id`
- import and capture both produce the same core artifact record shape
- artifact records preserve routing fields such as `artifact_class`, `editing_mode`, `media_family`, and `authority_mode`
- artifact records preserve provider fields such as `provider`, `provider_ref`, `latest_version_ref`, and `retention_state`

### 2.4 Versioning

- initial create produces a first Cortex `version_ref`
- updating or redrafting an artifact preserves `artifact_id` and creates a new `version_ref`
- prune transitions create a version record rather than silently deleting content
- artifact version records preserve `change_kind` and `provider_version_ref` when available

### 2.5 Resolution And Open Behavior

- `resolve(artifact_id)` returns stable metadata for an imported artifact
- `resolve(artifact_id)` returns stable metadata for a capture artifact
- artifact resolution still works after the original source file is renamed or moved
- `open` semantics are defined for latest version and specific version targets
- unknown `artifact_id` lookups fail explicitly

### 2.6 Backlinks And Source Locators

- the source-locator contract is defined clearly enough for intake and provenance to use
- backlink results can return artifact-root links when inner navigation is unavailable
- backlink results can carry best-effort precision such as page, section, sheet, slide, or line range
- failure to produce a precise deep link does not break artifact-level provenance

### 2.7 Prune And Reference-Only Retention

- prune behavior preserves `artifact_id`
- prune behavior preserves source references and summary reference
- prune behavior leaves the artifact resolvable in `reference_only` state
- prune is clearly distinct from hard delete

### 2.8 Provider-Neutral Contract

- filesystem-backed providers fit the contract cleanly
- provider-native document systems fit the same contract cleanly
- `storage_path` is treated as a Cortex locator rather than the original external path

## 3. Acceptance Scenario

1. configure artifact storage with `git_local` as the default provider and at least one additional provider entry in the registry
2. store one imported document with source provenance from an external location
3. confirm the stored artifact record contains `artifact_id`, provider data, routing fields, `latest_version_ref`, and a Cortex `storage_path`
4. write one updated or redrafted version of that artifact
5. confirm `artifact_id` stayed stable and a new `version_ref` was created
6. build a backlink using the artifact plus a source locator such as page and section
7. rename or move the original source file outside Cortex
8. resolve the imported artifact by ID again
9. prune the artifact to a reference-only posture with a retained summary reference
10. resolve the pruned artifact by ID
11. store one text capture and confirm it uses the same identity and versioning model

Expected result:

- both artifacts are addressable by Cortex ID
- provider metadata, version history, and provenance remain inspectable
- source-path drift does not break artifact resolution
- backlink generation degrades gracefully if exact deep linking is unavailable
- prune leaves a resolvable reference-only artifact instead of silently deleting identity

## 4. Optional Provider-Future Scenario

If the implementation team wants an explicit preflight before building the Google provider:

- create a mock resolve result whose provider metadata includes `provider_ref` and a non-filesystem `storage_path`
- create a mock backlink result that returns provider-native precision weaker than exact section navigation
- confirm the contract still holds without changing `artifact_id` or Cortex `version_ref`

Expected result:

- the artifact model remains valid for provider-native documents
- deep-link precision may vary without breaking provenance

## 5. Failure Conditions

- source path is treated as canonical identity
- providers are expected to mint `artifact_id` or authoritative version IDs
- routing depends on source path naming instead of policy inputs
- capture artifacts take a different identity path from imports
- versioning is undefined for updates or prune transitions
- `resolve` depends on the original external file still existing in place
- backlink behavior is missing or assumes perfect deep-link precision
- prune behaves like a silent hard delete
- the contract assumes every provider returns a direct filesystem path

## 6. Test Outputs

- sample provider registry configuration
- sample import artifact record
- sample capture artifact record
- sample artifact version history
- sample backlink output
- sample prune result
- sample evidence that external source rename or move did not break resolution
