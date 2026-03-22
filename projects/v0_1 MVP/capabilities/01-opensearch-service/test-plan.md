# OpenSearch Service Capability Test Plan

## 1. Goal

Prove that Cortex has a working OpenSearch backend whose schema and behavior are compatible with the MVP retrieval model.

This capability is not finished just because OpenSearch starts.
It is finished when Cortex can index knowledge-object-shaped documents, query them safely, and inspect why retrieval behaved the way it did.

## 2. Required Test Areas

### 2.1 Service And Bootstrap

- OpenSearch service starts and is reachable from Cortex
- readiness checks can distinguish unreachable, reachable-but-unbootstrapped, and bootstrapped states
- bootstrap creates the required versioned indexes and stable aliases
- bootstrap is idempotent across repeated runs

### 2.2 Schema Compatibility

- the knowledge index mapping is created successfully
- the retrieval-trace index mapping is created successfully
- governance fields are exact-match or bounded field types
- typed signal fields are indexed as analyzed text
- typed signal fields expose exact subfields for debugging
- provenance and typed-link fields are accepted as structured objects
- vector-capable fields are accepted when vector support is enabled

### 2.3 Write And Read Behavior

- a knowledge document can be inserted by stable ID
- a knowledge document can be updated by stable ID without duplicate-write ambiguity
- a small bulk document set can be indexed successfully
- newly written documents become searchable after the expected refresh behavior
- a knowledge document can be fetched directly by ID
- provenance can be queried by `artifact_id`
- a retrieval trace document can be written and read back

### 2.4 Query Compatibility

- lexical queries over typed signal fields return the expected match
- lexical queries over `statement` and `summary` return the expected match
- governance filters exclude wrong-scope documents before ranking matters
- retrieval-path queries execute without schema errors
- lexical retrieval still works when vector input is omitted

### 2.5 Diagnostics

- current aliases can be inspected
- current mappings can be inspected
- raw query responses can be captured for debugging
- persisted retrieval traces can be inspected after a test query

## 3. Acceptance Scenario

1. start the local OpenSearch service
2. run the Cortex bootstrap path
3. confirm the knowledge and retrieval-trace aliases resolve to versioned indexes
4. index a small sample knowledge set containing:
   - one OpenTrails lodging idea in the correct governance scope
   - one unrelated document in the same owner scope
   - one similar document outside the allowed governance scope
5. index one retrieval-trace sample for the test query
6. run a governance-filtered lexical query such as `places to stay while hiking`
7. fetch the winning knowledge document by ID
8. query provenance by `artifact_id`

Expected result:

- the OpenTrails lodging idea is indexed and returned
- the wrong-scope document is excluded by governance filters
- the query executes without schema mismatch
- the winning document can be reopened by ID
- the trace record and provenance are inspectable

## 4. Optional Vector Scenario

If vector support is enabled in the local OpenSearch configuration:

- index sample embeddings for the same document set
- run the same query with vector assist enabled
- confirm the mapping accepts vector fields and the query still succeeds

Expected result:

- vector assist can contribute to retrieval
- lexical retrieval remains valid and queryable even without relying on vector-first behavior

## 5. Failure Conditions

- service is unreachable from Cortex
- bootstrap is not idempotent
- required indexes or aliases are missing
- mapping rejects governance, typed-signal, provenance, link, or ranking fields
- upsert behavior creates ambiguous duplicates for the same stable ID
- governance filters fail to exclude wrong-scope documents
- retrieval queries fail because the index shape is incompatible
- lexical retrieval depends on vector support to function at all
- retrieval traces cannot be persisted or inspected

## 6. Test Outputs

- service startup and readiness evidence
- alias-resolution evidence
- knowledge-index mapping sample
- retrieval-trace mapping sample
- sample indexed knowledge documents
- sample query request and result
- sample provenance lookup
- sample retrieval-trace record
