# Artifact Storage Capability Test Plan

## 1. Goal

Prove that Cortex artifact identity is stable and that artifact content can be persisted or registered without making external source layout canonical.

## 2. Required Tests

- import artifact gets an `artifact_id`
- capture artifact gets an `artifact_id`
- `resolve(artifact_id)` returns stable metadata
- provider metadata is recorded correctly
- a filesystem-backed implementation stores artifacts in predictable locations
- artifact resolution still works after the original source file is renamed or moved

## 3. Acceptance Scenario

1. import one document
2. confirm artifact record exists
3. confirm provider metadata exists
4. resolve artifact by ID
5. rename or move the original source reference outside Cortex
6. resolve artifact by ID again

Expected result:

- Cortex still resolves the artifact through its own identity

## 4. Failure Conditions

- source path is treated as canonical identity
- provider metadata is missing
- capture artifacts take a different identity path from imports
- `resolve` depends on the original external file still existing in place

## 5. Test Outputs

- sample import artifact record
- sample capture artifact record
- sample resolve output
