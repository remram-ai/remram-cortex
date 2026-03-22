# Cortex v0.1 MVP Spec

## 1. Purpose

This document specifies the first Cortex MVP slice around:

- Artifact Storage dependency
- Artifact Intake
- Quick Capture
- general chat with Cortex knowledge injection
- retrieval over the resulting baseline knowledge base

It is intentionally narrower than the full architecture.

## 2. System Boundary

### 2.1 Included Runtime Surfaces

The MVP needs five functional surfaces:

1. artifact storage adapter
2. artifact intake submission and analysis
3. quick capture submission
4. retrieval
5. general chat retrieval injection

These may be exposed as dedicated APIs or as wrappers around the core Cortex surfaces such as `/ingest`, `/reflect`, and `/retrieve`.

### 2.2 External Dependency

Artifact Storage is treated as a Cortex-owned provider contract.

Cortex depends on it to:

- persist or register Cortex-managed imported artifacts
- persist lightweight capture artifacts
- return stable identifiers and deterministic internal paths

Cortex does not give artifact storage authority over knowledge metadata.

An implementation may later reuse or integrate with services from other repositories, but Cortex should not depend on that to define its artifact model.

## 3. MVP Architecture

The v0.1 loop is:

1. source artifact or quick capture enters Cortex
2. evidence is persisted as a Cortex-managed artifact through artifact storage
3. Cortex parses or normalizes the evidence into bounded source slices
4. reflection-style extraction produces knowledge-object deltas
5. OpenSearch indexes the resulting knowledge
6. retrieval returns bounded bundles against that seeded and updated knowledge base

Quick Capture should reuse this path rather than bypass it.

## 4. Functional Components

### 4.1 Artifact Storage Adapter

The MVP adapter must support:

- `store_import(original_bytes, filename, media_type, metadata) -> artifact_id, path`
- `store_capture(capture_text, metadata) -> artifact_id, path`
- `resolve(artifact_id) -> path, metadata`

The adapter may be implemented over a local Git-backed filesystem layout in v0.1.

The returned `path` is Cortex-internal. External file locations or source-system folders are provenance only.

Longer term, different providers may satisfy this contract, including local Git and Google Workspace-backed implementations.

### 4.2 Artifact Intake Worker

The intake worker must:

- accept an imported artifact reference
- extract text or structured content
- create bounded source slices
- attach source-location provenance
- emit candidate knowledge-object updates
- write resulting knowledge into OpenSearch

### 4.3 Quick Capture Worker

The quick capture worker must:

- accept a short text submission
- persist the raw capture as an artifact
- create a reflection job over that capture
- detect likely duplicates or related objects in the current knowledge base
- update or create knowledge objects accordingly

### 4.4 Retrieval Surface

Retrieval must operate over the same imported and captured knowledge pool using:

- governance filters
- semantic signature similarity boost
- typed signal field scoring
- vector assist
- relationship expansion

### 4.5 General Chat Injection Surface

The MVP must include one ordinary chat path that consumes Cortex retrieval before prompt build.

This surface does not need to prove a full app UX. It only needs to prove that:

- a live chat request can call Cortex retrieval
- Cortex returns a bounded bundle
- the bundle can be injected into chat context
- the resulting answer is observably better than the same chat without Cortex knowledge

## 5. Data Contracts

### 5.1 Artifact Record

Minimum record:

```json
{
  "artifact_id": "art_...",
  "artifact_kind": "imported|capture",
  "artifact_class": "evidence|working|official|operational",
  "editing_mode": "solo|collaborative",
  "media_family": "markdown|rich_doc|spreadsheet|deck|binary",
  "provider": "git_local|google_workspace|...",
  "authority_mode": "cortex_owned|external_authoritative|published_mirror|collaborative_mirror",
  "storage_path": "string",
  "media_type": "string",
  "original_name": "string",
  "created_at": "timestamp",
  "source_ref": "optional external source id",
  "source_uri": "optional external location"
}
```

This record may live partly in artifact storage and partly in Cortex metadata, but Cortex remains the knowledge authority.

These routing fields allow provider selection without making provider choice part of the memory model itself.

### 5.2 Import Slice

Minimum slice shape:

```json
{
  "artifact_id": "art_...",
  "slice_id": "slice_...",
  "content": "string",
  "summary": "string",
  "source_location": {
    "page": 3,
    "section": "Pricing",
    "offset_start": 120,
    "offset_end": 420
  }
}
```

Only the location fields relevant to the source need to be present.

### 5.3 Quick Capture Submission

Minimum capture input:

```json
{
  "capture_text": "Reseller network for trail lodging along hiking routes",
  "owner_ref": "person:jason",
  "audience": ["person:jason"],
  "knowledge_space": ["project:opentrails"]
}
```

Voice transcription, follow-up clarification, and deeper feasibility analysis are deferred.

### 5.4 Knowledge Object Subset For MVP

The MVP object subset must include:

- canonical statement
- object kind
- provenance
- governance fields
- typed signals
- semantic signature
- ranking metadata
- typed links

## 6. Storage Layout

### 6.1 Artifact Storage Layout

If the selected provider is filesystem-backed, the MVP may use a simple predictable layout such as:

```text
artifacts/
  imports/
    <artifact-id>/
      original/<filename>
  captures/
    <artifact-id>/
      capture.md
```

Promoted artifacts are out of scope for this MVP slice.

The layout should stay predictable, but Cortex should avoid duplicating authoritative metadata into extra sidecar files unless truly needed for storage operation.

This layout is only one valid provider implementation. It is not the human inspection hierarchy and should not be derived from the original source folder tree.

### 6.2 OpenSearch Document Shape

At minimum, the OpenSearch knowledge document must contain:

- `statement`
- `summary`
- `object_kind`
- governance fields such as `owner_ref`, `audience`, `knowledge_space`, `lifecycle_state`
- typed signals: `domain`, `activity`, `need`, `object`, `mechanism`
- `semantic_signature`
- `confidence`, `freshness_ts`, `reinforcement_count`
- provenance fields including `artifact_id` and `source_location`
- typed links

## 7. Required Flows

### 7.1 Baseline Import Flow

1. user submits an artifact
2. artifact storage saves or registers the artifact and returns `artifact_id`
3. Cortex intake parses the artifact into bounded slices
4. Cortex extracts and writes knowledge objects
5. Cortex indexes those objects for retrieval
6. import status and object counts are visible

The stored artifact should remain resolvable by Cortex artifact ID even if the original external source is later renamed, moved, or removed.

### 7.2 Quick Capture Flow

1. user submits a short text capture
2. Cortex stores the raw capture as a capture artifact
3. reflection evaluates the capture against existing knowledge
4. Cortex decides whether to reinforce, refine, link, or create
5. resulting objects become retrievable immediately

### 7.3 Retrieval Proof Flow

1. user asks a question related to imported or captured knowledge
2. Cortex filters by governance
3. Cortex scores typed signals
4. Cortex applies vector assist and relationship expansion
5. Cortex returns a bounded bundle and optional trace

### 7.4 General Chat Injection Flow

1. user asks an ordinary chat question
2. orchestration calls Cortex `/retrieve` before prompt build
3. Cortex returns a bounded bundle
4. orchestration injects that bundle into the live chat prompt
5. the runtime produces an answer informed by seeded and captured knowledge

## 8. MVP Acceptance Requirements

The implementation is acceptable when all of the following are true:

- at least one imported document creates usable knowledge objects with source-linked provenance
- at least one quick capture updates the same knowledge area without duplicating blindly
- the same knowledge can be rediscovered through more than one query framing
- at least one ordinary chat scenario clearly benefits from Cortex knowledge injection
- the original source artifact and the resulting knowledge object remain linked
- the Cortex-managed artifact copy remains resolvable without depending on the original source-system path
- retrieval traces show which filters and scores produced the final result

## 9. Deferred Requirements

The following are intentionally deferred:

- image-native extraction guarantees
- voice-first capture
- dormant idea resurfacing
- auto-feasibility analysis
- aggressive Dream-time normalization
- artifact pruning
- artifact promotion
- family-scale sharing UX
- provider-specific collaboration monitoring and reconcile loops

## 10. Recommended First Public Shapes

The exact API surface can change, but a practical first public shape is:

- `POST /artifacts/import`
- `POST /captures`
- `POST /retrieve`
- `GET /artifacts/{artifact_id}`

Those may fan into internal Cortex operations such as ingest and reflect.

The chat surface may remain external to Cortex as long as it uses Cortex retrieval in the runtime path.

## 11. Design Constraint

The MVP must not split into:

- imported artifact memory on one path
- quick notes on a separate path
- retrieval trying to unify them later

That would recreate the very memory fragmentation Cortex is supposed to solve.
