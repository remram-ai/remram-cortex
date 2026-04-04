# Epic 07 Test Plan

## Goal

Prove that extraction turns evidence into structured, retrievable knowledge-object deltas.

## Scenarios

- extract knowledge from imported slices
- confirm typed signals and provenance are attached
- confirm obvious duplicate noise is reduced through merge discipline

## Failure Conditions

- extraction outputs blobs instead of structured knowledge
- provenance is missing
- retrieval signals are absent or unusable

## Evidence

- sample knowledge deltas
- signal examples
- provenance examples

## Test Artifacts

Store executed epic test results under `tests/` using run artifacts such as `001-test-result-ddmmyyyy.md`.
