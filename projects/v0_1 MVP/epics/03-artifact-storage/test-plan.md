# Epic 03 Test Plan

## Goal

Prove that Cortex artifact identity and provider routing work as a stable foundation.

## Scenarios

- create or register artifact records with stable identity
- resolve artifacts by `artifact_id`
- verify provider metadata and routing behavior

## Failure Conditions

- artifact identity depends on source path
- provider routing is ambiguous
- import and capture flows would fork into different identity models

## Evidence

- sample artifact records
- route and resolution examples
- provider metadata examples

## Test Artifacts

Store executed epic test results under `tests/` using run artifacts such as `001-test-result-ddmmyyyy.md`.
