# OpenSearch Service Capability Spec

## 1. Purpose

Provide the OpenSearch-backed indexing and query substrate Cortex uses for knowledge retrieval, bounded candidate search, and retrieval debugging.

This capability exists to make the locked Cortex retrieval model operational, not to turn Cortex into a raw document or vector store.

## 2. Capability Boundary

This capability is responsible for:

- bringing up one OpenSearch service usable by local Cortex development
- defining the OpenSearch indexes and mappings Cortex depends on for MVP retrieval
- storing knowledge documents, retrieval metadata, and retrieval traces
- supporting filter-first lexical retrieval with optional vector assist
- exposing enough diagnostics to debug schema and query behavior

This capability is not responsible for:

- storing raw artifact bytes
- reflection or merge decisions
- prompt assembly or chat UX
- choosing the embedding model itself

## 3. MVP Deliverable

The MVP deliverable for this capability is:

- one local single-node OpenSearch service that Cortex can reach reliably
- one idempotent bootstrap path that creates the required indexes and aliases
- one knowledge-document mapping aligned to governance-first, typed-signal-first retrieval
- one trace storage path for retrieval debugging
- one query path that works lexically even when vector assist is unavailable

The implementation should be practical to operate from Go and should not require OpenSearch-native complexity that the rest of the MVP does not yet need.

## 4. Service Requirements

### 4.1 Local Runtime Shape

The first implementation should assume:

- one local OpenSearch node
- persistence on a local development volume
- no high-availability behavior
- replica settings appropriate for a single-node deployment

The service must expose enough readiness information for Cortex startup checks to distinguish:

- service unreachable
- service reachable but unbootstrapped
- service bootstrapped and ready for reads and writes

### 4.2 Bootstrap Behavior

OpenSearch bootstrap must be idempotent.

Running bootstrap repeatedly must not corrupt existing mappings or require operators to delete indexes manually.

The practical MVP pattern should be:

- create a versioned knowledge index such as `cortex-knowledge-v1`
- create a stable alias such as `cortex-knowledge-current`
- create a versioned retrieval-trace index such as `cortex-retrieval-trace-v1`
- create a stable alias such as `cortex-retrieval-trace-current`

Versioned indexes plus stable aliases keep schema evolution possible without changing every Cortex caller.

## 5. OpenSearch Data Surfaces

### 5.1 Required Indexes

The MVP requires two OpenSearch data surfaces:

- a primary knowledge index for durable knowledge objects and retrieval fields
- a retrieval-trace index for persisted debug records

The knowledge index is mandatory.
The trace index is also part of the MVP because retrieval must remain inspectable.

### 5.2 Knowledge Document Contract

At minimum, each indexed knowledge document must contain:

- stable knowledge-object identity
- canonical statement and optional summary
- object kind
- governance fields
- typed signal fields
- semantic signature
- ranking metadata
- provenance
- typed links
- timestamps

A practical first-pass document shape is:

```json
{
  "knowledge_id": "ko_...",
  "statement": "Reseller network for trail lodging along hiking routes",
  "summary": "Partnership model for trail lodging inventory",
  "object_kind": "idea",
  "owner_ref": "person:jason",
  "audience": ["person:jason"],
  "knowledge_space": ["project:opentrails"],
  "lifecycle_state": "active",
  "valid_from": "2026-03-21T00:00:00Z",
  "valid_until": null,
  "domain": ["outdoors", "travel"],
  "activity": ["trip planning"],
  "need": ["find places to stay"],
  "object": ["trail lodging"],
  "mechanism": ["reseller network"],
  "semantic_signature": "8a31",
  "confidence": 0.81,
  "freshness_ts": "2026-03-21T00:00:00Z",
  "reinforcement_count": 2,
  "artifact_ids": ["art_..."],
  "provenance": [
    {
      "artifact_id": "art_...",
      "slice_id": "slice_...",
      "source_location": {
        "page": 3,
        "section": "Lodging"
      }
    }
  ],
  "links": [
    {
      "link_type": "relates_to",
      "target_ref": "project:opentrails"
    }
  ],
  "embedding": [0.12, 0.08, 0.44],
  "created_at": "2026-03-21T00:00:00Z",
  "updated_at": "2026-03-21T00:00:00Z"
}
```

This contract is intentionally knowledge-object-shaped.
It must not degrade into transcript chunks or source-document blobs pretending to be durable memory.

### 5.3 Mapping Rules

The mapping must support the retrieval architecture already locked in the repo.

Required mapping rules:

- governance fields such as `owner_ref`, `audience`, `knowledge_space`, and `lifecycle_state` use exact-match or bounded field types such as `keyword`, `boolean`, and `date`
- typed signal fields `domain`, `activity`, `need`, `object`, and `mechanism` are multi-valued analyzed text fields
- typed signal fields should also expose exact subfields for debugging or exact-match use
- `statement` and `summary` remain searchable text fields
- `semantic_signature` is stored in a compact form such as `keyword` or integer-like representation
- ranking fields such as `confidence`, `freshness_ts`, and `reinforcement_count` use numeric or date-friendly types
- provenance and typed links are stored as structured objects that preserve their tuples
- the vector field uses an OpenSearch-supported vector type parameterized by the configured embedding dimensions

The signature field exists for soft routing bias, not as a hard eligibility gate.
The vector field exists for assistive similarity, not as the primary retrieval authority.

### 5.4 Retrieval Trace Contract

The retrieval-trace surface must preserve enough information to inspect what happened during retrieval.

At minimum, a trace record should be able to store:

- request identity and timestamp
- applied governance filters
- the raw query shape or a normalized query summary
- top candidate IDs returned from OpenSearch
- score contributors that Cortex or OpenSearch used
- suppression or truncation notes when the bundle was bounded

The exact trace schema may evolve, but the service must make persisted traces queryable and inspectable during the MVP.

## 6. Query Compatibility Requirements

This capability must support the query patterns required by the retrieval design.

At minimum, OpenSearch must be compatible with:

- `bool.filter` over governance fields before semantic ranking
- lexical scoring over typed signal fields
- lexical matching on `statement` and `summary`
- document fetch by `knowledge_id`
- provenance lookup by `artifact_id`
- optional vector assist inside an already governance-bounded candidate set

The first practical implementation does not need to compute semantic-signature distance inside OpenSearch.
That bias may be applied in Cortex after OpenSearch returns a bounded candidate set.

Relationship expansion also does not need graph-native infrastructure in this capability.
It only needs OpenSearch documents to preserve typed links clearly enough for Cortex to follow them after the primary match.

## 7. Write Requirements

The OpenSearch service must allow Cortex to:

- create indexes and aliases safely
- insert or upsert one knowledge document by stable ID
- bulk write knowledge documents during import or reflection jobs
- read a document back by ID
- refresh the index in a controlled way so new knowledge becomes queryable quickly enough for the MVP loop
- persist retrieval-trace documents

For the MVP, import and capture outputs should become searchable quickly after write completion.
Using explicit refresh behavior at the end of a write path is acceptable if it keeps the system predictable and debuggable.

## 8. Diagnostics And Debuggability

This capability must support operator inspection of:

- service health
- index existence
- alias resolution
- current mappings
- sample stored documents
- raw query responses
- persisted retrieval traces

If vector functionality is disabled, misconfigured, or temporarily unavailable, Cortex should still be able to perform lexical retrieval over the same knowledge index.
That degraded mode should be explicit in diagnostics rather than silently changing retrieval behavior.

## 9. Acceptance Requirements

The capability is acceptable for the MVP when all of the following are true:

- Cortex can connect to a local OpenSearch service reliably
- bootstrap creates the required indexes and aliases idempotently
- the knowledge mapping accepts all required governance, typed-signal, provenance, link, and ranking fields
- sample knowledge documents can be inserted, updated, and queried without schema mismatches
- lexical retrieval works over typed signals and canonical text
- vector-capable mappings are accepted when configured, but vector similarity is not required for basic retrieval success
- retrieval traces can be stored and inspected

## 10. Deferred

The following are deferred beyond this MVP capability:

- multi-node or high-availability deployment
- production-scale shard and index-lifecycle tuning
- graph-native relationship storage
- vector-first retrieval
- complex in-engine signature-distance scoring
