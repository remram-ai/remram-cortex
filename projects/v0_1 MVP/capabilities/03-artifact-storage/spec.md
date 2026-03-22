# Artifact Storage Capability Spec

## 1. Purpose

Provide the Cortex-owned artifact-provider contract used by the MVP to assign stable artifact identity, persist or register artifact content, and resolve artifacts later by `artifact_id`.

## 2. Capability Boundary

This capability is responsible for:

- stable `artifact_id` assignment
- provider metadata capture
- import and capture persistence or registration
- later `resolve(artifact_id)` lookup
- deterministic provider routing inputs on the artifact record

This capability is not responsible for:

- knowledge extraction
- retrieval scoring
- chat behavior
- full provider-specific collaboration sync

## 3. MVP Contract

The capability must support:

- `store_import(original_bytes, filename, media_type, metadata) -> artifact_id, path`
- `store_capture(capture_text, metadata) -> artifact_id, path`
- `resolve(artifact_id) -> path, metadata`

Minimum artifact record fields:

- `artifact_id`
- `artifact_kind`
- `artifact_class`
- `editing_mode`
- `media_family`
- `provider`
- `authority_mode`
- `storage_path`
- `media_type`
- `original_name`
- `created_at`
- `source_ref`
- `source_uri`

## 4. Provider Policy Expectations

The MVP only needs one working provider implementation, but the contract must preserve room for routing by:

- artifact class
- editing mode
- media family
- authority mode

The first implementation may use local Git-backed storage. The model must not assume that all future providers are filesystem-backed.

## 5. Functional Requirements

- imported artifacts get stable Cortex identity
- captures get stable Cortex identity
- provider metadata is preserved on the artifact record
- artifact resolution works by Cortex ID even if the original source path changes
- external source references remain provenance, not canonical storage identity

## 6. Deferred

- provider-native change watching
- provider sync reconciliation loops
- multi-provider routing in production
- promotion-specific provider logic
