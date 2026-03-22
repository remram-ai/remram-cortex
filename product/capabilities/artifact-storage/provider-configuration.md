# Artifact Storage Provider Configuration

## 1. Purpose

This document defines the configuration shape for registering artifact-storage providers and routing artifacts to them.

The goal is to let Cortex support multiple providers without making source paths or provider-native IDs the canonical memory model.

## 2. Top-Level Shape

A practical first-pass shape is:

```yaml
artifact_storage:
  default_provider: git_local
  providers:
    git_local:
      kind: git_local
      enabled: true
      writable: true
      allow_fallback_target: true
      config:
        repo_root: /var/lib/cortex/artifacts-repo
        working_root: /var/lib/cortex/artifacts
    google_workspace_main:
      kind: google_workspace
      enabled: true
      writable: true
      allow_fallback_target: false
      config:
        drive_root_id: 123456
        export_markdown: true
  routing_rules:
    - match:
        artifact_class: [evidence]
        authority_mode: [cortex_owned, external_authoritative]
      provider: git_local
    - match:
        artifact_class: [official]
        editing_mode: [collaborative]
        media_family: [rich_doc, spreadsheet, deck]
      provider: google_workspace_main
      allow_fallback_to_default: true
  prune_defaults:
    require_summary_ref: true
    default_retention_state: full_copy
```

## 3. Provider Registry Entries

Each provider entry should define at least:

- `kind`
- `enabled`
- `writable`
- `allow_fallback_target`
- `config`

Rules:

- registry keys are the provider IDs used in artifact records
- `kind` identifies the adapter implementation to load
- `enabled=false` keeps the provider registered but not routable for writes
- `writable=false` allows read or resolve-only postures later if needed
- provider-specific details stay under `config`

Examples:

- Git local config may include repo roots and commit behavior
- Google Workspace config may include Drive root IDs, export defaults, and auth references

## 4. Routing Rules

Routing must be policy-driven.

Supported match fields for the MVP:

- `artifact_class`
- `editing_mode`
- `media_family`
- `authority_mode`

Rules are evaluated in order.
The first matching rule wins.
If no rule matches, Cortex uses `default_provider`.

`allow_fallback_to_default` controls whether a matching provider may fall back to the default provider when the target provider is unavailable or disabled at runtime.

## 5. Validation Rules

Configuration is invalid if:

- `default_provider` is missing
- `default_provider` does not exist in `providers`
- `default_provider` is disabled
- a routing rule references an unknown provider
- a routing rule references a disabled provider for normal write traffic
- two providers share the same registry key

Configuration warnings should be emitted if:

- a provider is registered but never routable
- a routing rule is shadowed completely by an earlier rule
- a provider is writable but not marked as an allowed fallback target where policy likely expects it

## 6. Fallback Behavior

The safe default and fallback provider for the MVP is local Git.

Recommended posture:

- unmatched artifacts go to the default provider
- evidence and capture flows may allow fallback to the default provider
- provider-specific collaborative flows may choose to fail explicitly instead of silently rerouting

Fallback is a policy decision.
It should not happen implicitly without configuration.

## 7. Prune And Retention Defaults

Configuration may also define prune defaults.

Useful first-pass keys:

- `require_summary_ref`
- `default_retention_state`

Recommended posture:

- pruning to `reference_only` should require a retained summary or summary reference
- imported evidence should default to `full_copy` until Cortex explicitly chooses to prune

## 8. Example Policy Guidance

Recommended initial routing posture:

- default all unconfigured artifacts to `git_local`
- default captures to `git_local`
- default imported evidence to `git_local` unless a stronger rule says otherwise
- route collaborative rich docs, sheets, and decks to a Google provider when configured
- do not route by source path prefixes, file trees, or provider-native URLs

## 9. Notes For Downstream Providers

- Git provider should assume it is the MVP fallback target.
- Google provider should assume it is selected only by explicit policy.
- Both providers should treat the registry key as the provider ID written into artifact records.
