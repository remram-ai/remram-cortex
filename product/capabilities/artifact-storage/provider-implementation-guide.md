# Artifact Storage Provider Implementation Guide

## 1. Purpose

This guide explains how to create a new artifact-storage provider that fits Cortex artifact storage cleanly.

Use this before implementing the next provider capabilities.

## 2. What A Provider Must Respect

The provider must respect these invariants:

- Cortex owns `artifact_id`
- Cortex owns the authoritative artifact record
- Cortex owns the authoritative Cortex `version_ref`
- provider choice comes from routing policy, not source path
- knowledge and retrieval metadata do not belong in the provider
- prune is an explicit lifecycle transition, not silent deletion

## 3. Provider Build Checklist

### 3.1 Choose The Provider Identity

Define:

- provider ID used in configuration, such as `git_local`
- provider kind used to load the adapter, such as `git_local` or `google_workspace`
- display name for diagnostics

### 3.2 Define The Provider Descriptor

Declare:

- whether the provider is writable
- whether it supports native versioning
- whether it can open content directly
- whether it can prune
- whether it can build deep links or only artifact-root links

### 3.3 Implement The Required Operations

Implement:

- `CreateArtifact`
- `ResolveArtifact`
- `OpenArtifact`
- `WriteArtifactVersion`
- `PruneArtifact`
- `BuildBacklink`

Keep the write set inside the provider.
Do not reach outward and mutate Cortex knowledge records.

### 3.4 Decide How Versioning Maps

Map provider-native history to Cortex versioning.

Recommended posture:

- return `provider_version_ref` whenever the provider has a native revision handle
- let Cortex keep the stable cross-provider `version_ref`
- for providers without useful native revisions, emulate retained versions clearly enough that `version_ref` does not become ambiguous

### 3.5 Define `storage_path`

`storage_path` is the Cortex locator written to the artifact record.

Rules:

- it must be deterministic
- it must not mirror the original source tree blindly
- it may be a file path for filesystem-backed providers
- it may be a Cortex locator string for provider-native backends

### 3.6 Implement Backlink Best Effort

Your provider must try to navigate as close to the source location as it can.

Examples:

- Git local may use file path plus line range or anchor-like hints when possible
- Google Workspace may use provider URIs plus page, sheet, slide, or provider-native fragment hints when possible

If exact deep linking is impossible, fall back to the artifact root.

### 3.7 Implement Prune Explicitly

Prune should preserve:

- `artifact_id`
- source references
- provider references
- prior version metadata
- summary or summary reference

Do not let prune erase the audit trail.

## 4. Versioning Guidance

Every meaningful content change should create a new version.

At minimum:

- create
- update
- redraft
- prune

If your provider does not expose native revision IDs, you still need a coherent retained-version story.
Git and Google providers both have native version concepts, so use them.

## 5. Backlink Guidance

Backlink precision should degrade gracefully:

1. exact provider-native deep link
2. page, sheet, slide, or section target
3. artifact-root link

Good backlink behavior is about inspectability, not perfection.
The provenance survives even when the deep link is approximate.

## 6. Prune Guidance

Prune is appropriate when:

- the durable knowledge has already been extracted
- the full artifact no longer needs to remain resident
- a source reference and summary are enough for future audit

Reference-only prune is the required MVP posture.
Hard delete is not.

## 7. Testing Expectations

A new provider is not done when it can merely write one file.

It should pass:

- the shared Artifact Storage test plan
- its provider-specific test plan
- explicit checks for create, resolve, versioning, backlink behavior, and prune behavior

## 8. Common Failure Modes

Avoid these mistakes:

- minting provider IDs or version IDs as if they were Cortex identity
- deriving storage layout from source paths
- hiding missing deep-link support behind fake precision
- dropping version history on updates
- treating prune as an ordinary delete
- storing duplicate knowledge metadata in the provider

## 9. Guidance For The Next Two Providers

### 9.1 Git Provider

Expected strengths:

- local-first fallback
- deterministic storage layout
- strong native version history
- straightforward path-based open targets

### 9.2 Google Drive Provider

Expected strengths:

- collaborative document authority
- provider-native document references
- provider-native revision handles
- provider-native deep-link opportunities for some document classes

Expected caution:

- do not let Drive file IDs or folder layout become Cortex identity
- do not assume all Google-native inner locations are stable enough for perfect deep links
