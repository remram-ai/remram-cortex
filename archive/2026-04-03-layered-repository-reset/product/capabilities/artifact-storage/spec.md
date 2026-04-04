# Artifact Storage Capability Spec

## 1. Purpose

Provide the Cortex-owned artifact-storage foundation used by the MVP to assign stable artifact identity, route artifacts to storage providers, persist or register artifact content, version later changes, and resolve artifacts by `artifact_id`.

This capability exists to keep artifact identity and lifecycle inside Cortex even when the backing provider is external, collaborative, or later replaceable.

## 2. Capability Boundary

This capability is responsible for:

- stable `artifact_id` assignment
- stable Cortex-owned version references for artifact mutations
- artifact record and artifact-version record creation
- provider contract definition
- provider registry and routing configuration
- import and capture persistence or registration
- later artifact resolution by `artifact_id`
- best-effort backlink or deep-link generation from stored provenance locators
- prune behavior that can reduce stored content while retaining a stable Cortex artifact record

This capability is not responsible for:

- knowledge extraction
- retrieval scoring
- chat behavior
- full provider-specific collaboration sync
- provider-native watch-loop delivery in the MVP core
- artifact promotion policy

## 3. MVP Deliverable

The MVP deliverable for this capability is a provider foundation pack made of:

- one provider-neutral artifact-storage facade for Cortex
- one provider contract that downstream providers implement
- one provider configuration model and routing policy shape
- one implementation guide for creating new providers
- one artifact record model shared by imports and captures
- one versioning model that preserves change history for updates and pruning
- one backlink model that can navigate from knowledge provenance back toward the source artifact

The first concrete provider may be local Git-backed storage.
The contract must still leave room for providers that do not expose ordinary filesystem paths as their native storage model.

## 4. System Model

Artifact storage has two layers.

### 4.1 Cortex Artifact-Storage Facade

The facade is Cortex-owned.
It is responsible for:

- assigning `artifact_id`
- assigning Cortex `version_ref` values
- selecting a provider from routing policy
- persisting the authoritative artifact record
- persisting Cortex-owned artifact-version records
- exposing the public artifact-storage API to the rest of Cortex

The facade owns identity.
Providers do not mint `artifact_id`.

### 4.2 Storage Providers

A storage provider is a pluggable adapter behind the facade.
It is responsible for:

- storing bytes, native documents, or a resolvable provider handle
- returning provider-specific references such as revision IDs when available
- reopening artifact content later
- writing later versions when artifacts are updated or redrafted
- pruning provider-resident content when requested by policy
- generating best-effort backlinks from a source locator

Providers do not become a second metadata authority for knowledge objects, retrieval fields, or reflection state.

## 5. Public Artifact Activities

The design docs still require the minimum public MVP surface:

- `store_import(original_bytes, filename, media_type, metadata) -> artifact_id, path`
- `store_capture(capture_text, metadata) -> artifact_id, path`
- `resolve(artifact_id) -> path, metadata`

For provider-ready delivery, the artifact-storage capability must also define these lifecycle activities:

- `open(artifact_id, version_ref?)`
- `write_version(artifact_id, change_kind, content, metadata_delta?)`
- `list_versions(artifact_id)`
- `build_backlink(artifact_id, version_ref?, source_locator?)`
- `prune(artifact_id, prune_request)`

These lifecycle activities do not all need to be exposed as public HTTP endpoints on day one.
They do need to exist as concrete contracts because downstream providers cannot be implemented sanely without them.
`list_versions` is a facade-level activity backed by Cortex artifact-version records rather than a required provider-native enumeration method.

Hard delete is deferred.
For the MVP, prune is the supported reduction path.

## 6. Artifact Lifecycle Rules

### 6.1 Create

Imports and captures both create a Cortex artifact record.

Rules:

- Cortex assigns `artifact_id`
- provider is selected from routing policy
- the provider persists or registers the initial content
- Cortex writes an initial version record
- the returned `path` is a Cortex storage locator, not the external source path

### 6.2 Resolve And Open

`resolve(artifact_id)` returns the current artifact record and enough provider metadata to reopen the artifact later.

`open` is the content-access activity behind intake, inspection, and debugging.
It should be able to target the latest version by default and a specific `version_ref` when the provider can support it.

### 6.3 Update Or Redraft

Updating an artifact does not create a new `artifact_id`.

Instead:

- Cortex keeps the same `artifact_id`
- Cortex assigns a new `version_ref`
- the provider writes the new content or native revision
- Cortex writes a new version record with `change_kind` such as `update` or `redraft`

This covers:

- corrected imports
- normalized or cleaned copies
- redrafted human-facing documents
- mirror refreshes that materially change artifact content

### 6.4 Versioning

Every artifact-content mutation must create a new Cortex version record.

This includes:

- initial create
- update
- redraft
- prune transitions that materially change retained content
- restore from a prior retained state if such a flow is later added

Metadata-only changes that affect resolution, retention state, or user-visible navigation should also create a version record.
Pure bookkeeping changes such as retry timestamps do not need their own version.

Provider-native revision history is desirable, but Cortex version history is the canonical cross-provider surface.

### 6.5 Backlinks And Inner Navigation

Knowledge provenance should be able to point back to:

- the source `artifact_id`
- the specific `version_ref` when known
- a best-effort inner locator such as page, section, heading path, line range, sheet, slide, frame, or region

Backlinking is best-effort, not guaranteed-perfect deep linking.

The rule is:

- if a provider can generate a precise deep link, return it
- if it can only get close, return the closest stable navigation target
- if inner navigation is unsupported, fall back cleanly to the artifact root

Failure to generate a deep link must not break provenance.
It only reduces navigation precision.

### 6.6 Prune

Prune exists for cases where Cortex no longer wants to retain the full stored artifact but must keep stable identity and provenance.

The MVP prune posture is:

- `artifact_id` remains valid
- the artifact record remains resolvable
- retained provenance such as `source_ref`, `source_uri`, `provider_ref`, and prior version metadata remains available
- the record may shift to a reference-only retention state
- a compact summary or summary reference may remain so the system preserves why the artifact mattered after bytes are removed

Typical prune case:

- Cortex imported a large web article or reference document
- durable knowledge was extracted already
- Cortex decides not to keep the full artifact copy
- the artifact record remains as a reference with source link and summary

Prune is not silent deletion.
It is an explicit lifecycle transition.

## 7. Core Data Contracts

### 7.1 Artifact Record

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
- `updated_at`
- `source_ref`
- `source_uri`
- `provider_ref`
- `latest_version_ref`
- `version_count`
- `retention_state`
- `summary_ref`
- `pruned_at`

Rules:

- `artifact_id` is opaque and Cortex-owned
- `storage_path` is a Cortex locator, not a claim that the provider is filesystem-native
- `provider_ref` is optional for filesystem-backed providers and expected for provider-native systems
- `retention_state` should support at least `full_copy`, `provider_only`, `reference_only`, and `missing`
- `summary_ref` is optional and should point to a Cortex-managed summary or retained abstract when pruning occurs

### 7.2 Artifact Version Record

Each artifact version record should preserve at least:

- `artifact_id`
- `version_ref`
- `version_index`
- `change_kind`
- `provider_version_ref`
- `storage_path`
- `content_sha256`
- `byte_size`
- `created_at`
- `summary_ref`

Rules:

- `version_ref` is Cortex-owned
- `provider_version_ref` stores the provider-native revision handle when available
- `change_kind` should support at least `create`, `update`, `redraft`, `mirror_sync`, and `prune`

### 7.3 Source Locator And Backlink

Knowledge provenance should store:

- `artifact_id`
- `version_ref` when available
- `source_locator`

`source_locator` is a best-effort normalized object that may contain any relevant subset of:

- `page`
- `section`
- `heading_path`
- `sheet`
- `slide`
- `frame`
- `line_start`
- `line_end`
- `char_start`
- `char_end`
- `region`
- `fragment_id`
- `provider_hint`

Artifact storage must define a backlink result shape that can return:

- the resolved `artifact_id`
- the resolved `version_ref` when applicable
- the provider name
- the Cortex `storage_path`
- a provider URI or local open target when available
- a best-effort navigation target
- the achieved precision such as `artifact`, `page`, `section`, `line_range`, or `provider_native`

## 8. Provider Routing And Configuration

Provider choice is routed by artifact policy, not by source path.

At minimum, routing must be able to consider:

- `artifact_class`
- `editing_mode`
- `media_family`
- `authority_mode`

Configuration must support:

- a provider registry keyed by provider ID
- one default provider
- deterministic routing rules
- provider-specific configuration payloads
- optional fallback-to-default behavior
- prune and retention defaults when policy needs them

Rule evaluation should be deterministic.
The MVP should use ordered first-match routing with fallback to the configured default provider when no rule matches.

The full configuration shape lives in [provider-configuration.md](provider-configuration.md).

## 9. Provider Contract And Guidance

Downstream providers must implement the contract defined in:

- [provider-contract.md](provider-contract.md)
- [provider-configuration.md](provider-configuration.md)
- [provider-implementation-guide.md](provider-implementation-guide.md)

These documents are part of the capability output for Artifact Storage.

## 10. Functional Requirements

This capability is acceptable for the MVP only if all of the following are true:

- imports and captures share one artifact identity model
- providers are configured and selected by explicit policy rather than source path parsing
- providers implement a concrete contract for create, resolve, open, write-version, prune, and backlink behavior
- every content mutation results in a new Cortex version record
- artifact provenance can point back to an artifact and a best-effort inner locator
- artifact resolution works by Cortex ID even if the original source path changes
- pruning can reduce retained content without breaking `artifact_id`
- the contract remains usable for both filesystem-backed and provider-native backends

## 11. Acceptance Requirements

The capability is acceptable when all of the following are true:

- the provider contract is concrete enough for Git and Google-backed providers to implement against
- the provider configuration model is concrete enough to register and route more than one provider
- storing one imported artifact returns a stable `artifact_id` and current `version_ref`
- storing one capture returns a stable `artifact_id` and current `version_ref`
- resolving either artifact returns stable provider metadata and retention state
- writing an updated version preserves `artifact_id` and creates a new `version_ref`
- provider or service logic can return a best-effort backlink for an artifact plus inner locator
- pruning leaves a resolvable reference-only artifact instead of silently deleting identity

## 12. Deferred

The following are deferred beyond this MVP capability:

- hard-delete lifecycle as a normal operator surface
- provider-native watch loops in the MVP core
- automatic provider-to-provider migration workflows
- production multi-provider routing policy tooling
- collaboration conflict resolution beyond provider-native capabilities
- full artifact-promotion policy
