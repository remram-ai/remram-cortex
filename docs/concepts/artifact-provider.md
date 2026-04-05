# Artifact Provider

An artifact provider is the backend that stores or resolves a Layer 5 evidence body.

Layer 5 is defined by its role, not by one storage product.

That means Cortex should keep a stable Layer 5 contract even when the backing provider differs by evidence class or phase.

## Core Rule

The provider owns body storage and retrieval.

Cortex owns:

- stable identity
- provenance
- evidence class
- links into Layer 4 and Layer 3

The backend may vary.

The Cortex identity and authority boundaries should not.

## Evidence Classes

In the active architecture, providers serve three main Layer 5 evidence classes:

- `runtime_evidence`
- `reference_cache`
- `authored_artifact`

Those classes do not need the same retention or revision behavior.

## Provider Capabilities

Useful provider capabilities include:

- `ingest`
- `resolve`
- `exists`
- `metadata`
- `refresh` when the source is externally fetched
- `version_history` when the source is canon or revisioned
- `lifecycle` or retention support

Not every provider needs every capability.

## Current Posture

The current phased posture is:

- filesystem-backed Layer 5 runtime evidence early
- cache-like storage for retained references
- `Git` introduced later for the `authored_artifact` class

The important rule is not "which backend is fanciest."

It is:

- does this backend fit the evidence class
- does it preserve the right lifecycle behavior
- does it keep Layer 4 from becoming Layer 5's keeper

## Change Monitoring

If a provider exposes meaningful change signals, Cortex should be able to turn them into explicit reprocessing events.

That matters most for:

- owned maintained sources
- authored artifacts in canon

A source edit should become an explicit update path, not a silent hidden mutation.

## Related Concepts

- [Artifact Intake](artifact-intake.md)
- [Artifact Promotion](artifact-promotion.md)
- [Knowledge And Artifact Architecture](../design/knowledge-and-artifact-architecture.md)
