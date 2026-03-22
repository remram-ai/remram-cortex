# Git Service Dependency Regression Plan

## 1. Goal

Prove that the local Git foundation exists and is usable by Cortex as the base for the Git-backed provider.

## 2. Required Tests

- local Git-backed root exists
- repository can be initialized or validated
- stored artifacts land in deterministic locations
- the Git provider can use this foundation without path ambiguity

## 3. Failure Conditions

- no usable repository foundation exists
- provider storage depends on ad hoc paths
- local recovery history is unavailable
