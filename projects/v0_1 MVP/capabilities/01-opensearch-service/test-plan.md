# OpenSearch Service Capability Test Plan

## 1. Goal

Prove that Cortex has a working OpenSearch backend capable of supporting the MVP retrieval model.

## 2. Required Tests

- OpenSearch service starts and is reachable
- Cortex index can be created successfully
- sample documents can be indexed
- lexical queries return expected matches
- vector-capable fields are accepted by the mapping
- retrieval path can read from the index without schema errors

## 3. Acceptance Scenario

1. start the local OpenSearch service
2. create the Cortex knowledge index
3. write a small sample document set
4. run a retrieval query through Cortex or a direct harness

Expected result:

- documents are indexed and queryable with the expected mapping

## 4. Failure Conditions

- service is unreachable
- mapping rejects required fields
- sample indexing fails
- retrieval queries fail because the index shape is incompatible

## 5. Test Outputs

- service startup evidence
- index mapping sample
- sample query result
