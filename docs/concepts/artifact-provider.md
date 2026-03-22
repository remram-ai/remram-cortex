# Artifact Provider

Artifact storage in Cortex should be provider-backed and configurable.

Cortex needs a stable artifact model, but it should not hardcode one storage backend forever. Different users and artifact types want different operational tradeoffs.

## Core Rule

Cortex always owns the artifact record:

- stable `artifact_id`
- provider type
- authority mode
- provenance
- links to knowledge objects

The backing provider may vary. The Cortex artifact record does not.

## Provider Capabilities

Providers may support different capabilities.

Important capabilities include:

- `store`
- `resolve`
- `version_history`
- `share`
- `watch_changes`
- `export`
- `backup_snapshot`

Not every provider needs every capability.

## Authority Modes

Each artifact should declare an authority mode.

Suggested starting modes:

- `cortex_owned`
- `external_authoritative`
- `published_mirror`
- `collaborative_mirror`

These modes matter more than where the bytes happen to live.

## Routing Policy

Provider choice should be routed from artifact policy rather than hardcoded by file path.

A practical first routing policy uses:

- `artifact_class`: `evidence | working | official | operational`
- `editing_mode`: `solo | collaborative`
- `media_family`: `markdown | rich_doc | spreadsheet | deck | binary`
- `authority_mode`

Example first-pass behavior:

- default to local Git for unconfigured or system-oriented artifacts
- use Google Workspace for collaborative rich docs, sheets, and decks
- keep imported evidence in a provider that preserves the original form
- allow official artifacts to remain Git-canonical and optionally mirror outward

The right question is not "is it human readable?"
The right question is "how does this artifact live, who edits it, and which provider best serves that lifecycle?"

## Human And System Split

The provider line often follows who actually uses the artifact:

- collaborative human-facing plans, ideas, and business artifacts often fit Google Workspace best
- markdown, system-authored artifacts, prompts, exported HTML, and workflow-facing outputs often fit Git better
- provider-native tools such as design systems may be the source of truth for their own artifact classes while still exporting linked derivatives

## Change Monitoring

If a provider supports change watching, Cortex should be able to monitor artifact edits and trigger re-ingestion or reconciliation.

This should remain explicit. A watched external edit should become an update path, not an invisible silent mutation.

## Related Concepts

- [Artifact Intake](artifact-intake.md)
- [Artifact Promotion](artifact-promotion.md)
- [Knowledge Object](knowledge-object.md)
- [Architecture](../remram-cortex/architecture.md)
