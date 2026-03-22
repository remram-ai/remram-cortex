# Git Provider Capability Test Plan

## 1. Goal

Prove that the first concrete local artifact provider works for Cortex-owned artifacts.

## 2. Required Tests

- import artifact is stored in the local Git-backed layout
- capture artifact is stored in the local Git-backed layout
- artifact can be resolved by Cortex ID
- local Git history is available for stored artifacts or containers

## 3. Acceptance Scenario

1. store one imported artifact
2. store one capture artifact
3. resolve both by Cortex ID
4. inspect the local Git-backed layout

Expected result:

- both artifacts are persisted, addressable, and locally recoverable

## 4. Failure Conditions

- storage layout is nondeterministic
- artifacts cannot be resolved later
- local provider is not usable as the default fallback

## 5. Test Outputs

- sample local artifact paths
- sample resolve output
- sample Git status or history evidence
