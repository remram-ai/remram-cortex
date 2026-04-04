# Epic 06 Test Plan

## Goal

Prove that imported artifacts become bounded, source-linked slices.

## Scenarios

- import Markdown or text artifacts
- confirm slices retain source linkage
- confirm extraction can consume the slices

## Failure Conditions

- slices lose source linkage
- supported imports are not bounded predictably
- extraction handoff is ambiguous

## Evidence

- slice samples
- source-link examples
- import result notes

## Test Artifacts

Store executed epic test results under `tests/` using run artifacts such as `001-test-result-ddmmyyyy.md`.
