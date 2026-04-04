# Epic 11 Test Plan

## Goal

Prove that the chat harness is a usable proof surface for the end-to-end Cortex read path.

## Scenarios

- submit a question through the Cortex-backed path
- inspect the retrieved bundle or trace
- confirm the harness can support the final MVP demo

## Failure Conditions

- no usable proof surface exists
- the harness hides the retrieval behavior completely
- later OpenClaw integration would require redefining Cortex semantics

## Evidence

- harness walkthrough notes
- bundle or trace visibility proof
- end-to-end demo notes

## Test Artifacts

Store executed epic test results under `tests/` using run artifacts such as `001-test-result-ddmmyyyy.md`.
