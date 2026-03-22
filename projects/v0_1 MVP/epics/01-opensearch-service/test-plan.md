# Epic 01 Test Plan

## Goal

Prove that OpenSearch is operationally ready for later Cortex MVP work.

## Scenarios

- deploy the service and confirm health
- confirm CLI reachability and smoke-index lifecycle
- confirm backup and restore smoke flow

## Failure Conditions

- service cannot be deployed cleanly
- CLI or health surface is missing
- backup posture exists only on paper and cannot be exercised

## Evidence

- service status output
- smoke-index create and delete proof
- snapshot and restore proof

## Test Artifacts

Store executed epic test results under `tests/` using run artifacts such as `001-test-result-ddmmyyyy.md`.
