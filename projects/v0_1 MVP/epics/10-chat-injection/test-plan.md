# Epic 10 Test Plan

## Goal

Prove that chat answers can improve because Cortex retrieval ran first.

## Scenarios

- ask a question that should benefit from stored knowledge
- inspect the injected bundle
- compare with a no-Cortex baseline

## Failure Conditions

- retrieval is never called before answer generation
- injected bundle is not inspectable
- answer quality does not improve meaningfully

## Evidence

- bundle examples
- before and after answer comparison
- orchestration notes

## Test Artifacts

Store executed epic test results under `tests/` using run artifacts such as `001-test-result-ddmmyyyy.md`.
