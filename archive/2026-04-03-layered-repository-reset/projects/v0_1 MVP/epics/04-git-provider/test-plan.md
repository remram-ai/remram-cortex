# Epic 04 Test Plan

## Goal

Prove that the Git provider is usable as the default local provider.

## Scenarios

- persist artifacts through the Git provider
- resolve stored artifacts through the provider
- confirm fallback behavior is coherent

## Failure Conditions

- provider does not fit the artifact-storage contract
- default local behavior is unclear
- provider state depends on hidden path conventions

## Evidence

- provider persistence examples
- provider resolution examples
- default-provider notes

## Test Artifacts

Store executed epic test results under `tests/` using run artifacts such as `001-test-result-ddmmyyyy.md`.
