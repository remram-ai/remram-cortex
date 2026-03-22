# Chat Interface Capability Test Plan

## 1. Goal

Prove that there is a usable end-to-end chat surface for the MVP, not just backend retrieval components.

## 2. Required Tests

- chat harness accepts a user question
- Cortex retrieval is invoked before answer generation
- retrieved bundle is inspectable
- answer output differs meaningfully from the same path without Cortex retrieval

## 3. Acceptance Scenario

1. seed the corpus with imports and one relevant quick capture
2. ask a chat question through the harness
3. inspect the retrieval bundle used
4. compare against a no-Cortex baseline

Expected result:

- the Cortex-backed answer uses project-specific knowledge the baseline misses

## 4. Failure Conditions

- no real chat surface exists
- retrieval is not wired into the read path
- answer quality does not improve with Cortex enabled

## 5. Test Outputs

- example chat transcript or harness output
- bundled retrieval sample
- baseline versus Cortex-enabled answer comparison
