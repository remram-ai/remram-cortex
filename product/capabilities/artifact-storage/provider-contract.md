# Artifact Storage Provider Contract

## 1. Contract Role

This document defines the contract that concrete artifact-storage providers implement behind Cortex artifact storage.

The Cortex artifact-storage facade owns:

- `artifact_id`
- Cortex `version_ref`
- authoritative artifact records
- authoritative artifact-version records
- routing and policy decisions

Providers own:

- backing bytes, native documents, or resolvable provider handles
- provider-native revision handles when available
- provider-specific read and write mechanics
- provider-specific prune mechanics
- best-effort deep-link generation

Providers do not own knowledge-object metadata, retrieval metadata, or reflection state.

## 2. Required Provider Descriptor

Every provider should expose a descriptor with at least:

- `provider_id`
- `provider_kind`
- `display_name`
- `writable`
- `versioning_mode`
- `supports_open`
- `supports_write_version`
- `supports_prune`
- `supports_backlinks`

`versioning_mode` should distinguish at least:

- `provider_native`
- `cortex_emulated`

`cortex_emulated` means the provider itself does not expose useful native revision handles, so Cortex or the provider adapter must emulate version retention well enough to preserve the contract.

## 3. Provider Interface Shape

A Go-oriented interface may look like:

```go
type StorageProvider interface {
    Describe(ctx context.Context) (ProviderDescriptor, error)
    CreateArtifact(ctx context.Context, req CreateArtifactRequest) (CreateArtifactResult, error)
    ResolveArtifact(ctx context.Context, req ResolveArtifactRequest) (ResolveArtifactResult, error)
    OpenArtifact(ctx context.Context, req OpenArtifactRequest) (OpenArtifactResult, error)
    WriteArtifactVersion(ctx context.Context, req WriteArtifactVersionRequest) (WriteArtifactVersionResult, error)
    PruneArtifact(ctx context.Context, req PruneArtifactRequest) (PruneArtifactResult, error)
    BuildBacklink(ctx context.Context, req BuildBacklinkRequest) (BuildBacklinkResult, error)
}
```

Optional extensions may later include:

- `ListProviderVersions`
- `WatchChanges`
- `ExportArtifact`
- `ShareArtifact`
- `BackupSnapshot`

Those are optional extensions, not MVP requirements.
Service-level `list_versions(artifact_id)` is satisfied by Cortex artifact-version records and does not require `ListProviderVersions` for the MVP.

## 4. Required Operation Semantics

### 4.1 `CreateArtifact`

Create the initial provider-resident form of an artifact.

Input expectations:

- Cortex-assigned `artifact_id`
- Cortex-assigned initial `version_ref`
- artifact metadata and routing fields
- initial content bytes or provider-registration information

Provider rules:

- do not mint a new `artifact_id`
- return the provider storage location or handle
- return `provider_ref` when the provider needs one for later reopen
- return `provider_version_ref` when the provider exposes a native initial revision

### 4.2 `ResolveArtifact`

Return enough provider information to reopen or inspect the artifact later.

Resolve should not require the original external source path to remain unchanged.
It must work from the stable Cortex artifact record plus provider state.

### 4.3 `OpenArtifact`

Return a readable view of the artifact content or a provider-native open target.

Open rules:

- latest version is the default when `version_ref` is omitted
- a provider should honor a requested `version_ref` when it can map it to retained content
- if the artifact is pruned to reference-only, return an explicit pruned or unavailable status instead of pretending content still exists

### 4.4 `WriteArtifactVersion`

Persist a new content-bearing or retention-affecting version for an existing artifact.

Input expectations:

- stable `artifact_id`
- new Cortex `version_ref`
- prior `version_ref` when available
- `change_kind`
- new content or an explicit retention transition

Provider rules:

- keep the existing `artifact_id`
- write or register the new provider-side version
- return the new `storage_path` if it changed
- return `provider_version_ref` when available

### 4.5 `PruneArtifact`

Transition an artifact to a lighter retention posture while preserving identity and provenance.

Prune rules:

- do not delete the Cortex artifact record
- preserve enough provider and provenance metadata for later audit
- return the new retention state
- return a `provider_version_ref` if the provider records the prune as a revision
- if the provider cannot retain content after prune, return an explicit reference-only or unavailable status

### 4.6 `BuildBacklink`

Return a best-effort navigation target from:

- `artifact_id`
- optional `version_ref`
- optional `source_locator`

Backlink rules:

- prefer a precise deep link when the provider supports it
- otherwise return the nearest stable target
- otherwise fall back to the artifact root
- never fail the entire artifact lookup merely because a deep link could not be produced

## 5. Core Request And Result Fields

### 5.1 `CreateArtifactRequest`

Should include at least:

- `artifact_id`
- `version_ref`
- `artifact_kind`
- `artifact_class`
- `editing_mode`
- `media_family`
- `authority_mode`
- `media_type`
- `original_name`
- `content`
- `source_ref`
- `source_uri`

### 5.2 `CreateArtifactResult`

Should include at least:

- `storage_path`
- `provider_ref`
- `provider_version_ref`
- `byte_size`
- `content_sha256`
- `retention_state`

### 5.3 `WriteArtifactVersionRequest`

Should include at least:

- `artifact_id`
- `new_version_ref`
- `base_version_ref`
- `change_kind`
- `content`
- `summary_ref`

`summary_ref` matters most for prune and redraft flows where the compact retained meaning should remain visible even if full content is reduced.

### 5.4 `BuildBacklinkRequest`

Should include at least:

- `artifact_id`
- `version_ref`
- `source_locator`

### 5.5 `BuildBacklinkResult`

Should include at least:

- `artifact_id`
- `version_ref`
- `provider`
- `storage_path`
- `open_target`
- `navigation_target`
- `precision`

`open_target` may be a local path, provider URI, or another provider-native handle that Cortex can expose for inspection.

## 6. Versioning Expectations

Every provider must behave as if every meaningful artifact change is versioned.

At minimum, that includes:

- create
- update
- redraft
- prune

Recommended posture:

- return a provider-native revision handle when the provider has one
- preserve enough information for Cortex to reopen the latest version
- preserve enough information for Cortex to reference older versions when supported

If the provider lacks useful native versioning, the adapter must still preserve Cortex version records and enough retained content to avoid version ambiguity.

## 7. Source Locator Contract

`source_locator` is intentionally flexible.

It may contain any useful subset of:

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

Example:

```json
{
  "page": 3,
  "section": "Pricing",
  "heading_path": ["Go To Market", "Pricing"],
  "line_start": 120,
  "line_end": 142,
  "char_start": 4211,
  "char_end": 4870
}
```

Providers may ignore unsupported locator fields.
They should still use what they can.

## 8. Prune Contract

Prune should support at least the reference-only posture:

- full artifact content no longer retained for ordinary reopen
- artifact record remains resolvable
- source provenance remains available
- summary or summary reference remains available

A practical prune result should preserve:

- `artifact_id`
- latest `version_ref`
- `retention_state=reference_only`
- `source_ref`
- `source_uri`
- `provider_ref`
- `summary_ref`
- `pruned_at`

Hard delete is not part of the normal MVP contract.

## 9. Error Expectations

Providers should fail explicitly for:

- unknown `artifact_id`
- invalid or unsupported `version_ref`
- pruned content reopened as if it were still resident
- unsupported write or prune operations
- malformed provider configuration

Providers should not fall back silently to source-path guessing.

## 10. Non-Negotiable Rules

- Never mint or reinterpret `artifact_id`.
- Never make the original source path canonical identity.
- Never drop version history for a content mutation without an explicit contract reason.
- Never hide prune as silent deletion.
- Never require deep-link precision to preserve artifact provenance.
