# Chat Injection Capability Test Plan

## 1. Goal

Prove that ordinary chat visibly improves when Cortex retrieval is injected before prompt build.

## 2. Required Tests

- chat path calls Cortex retrieval before prompt construction
- returned bundle is bounded and inspectable
- final answer uses imported or captured knowledge
- no-Cortex baseline is materially weaker on the same question

## 3. Acceptance Scenario

Seed state:

- imported artifacts and at least one related quick capture exist

Action:

- ask an ordinary chat question in the relevant knowledge area

Expected result:

- Cortex retrieval runs
- the bundle is injected
- the final answer reflects project-specific knowledge the baseline path would miss

## 4. Failure Conditions

- retrieval is not called
- injected bundle is unbounded or opaque
- final answer shows no meaningful difference from the no-Cortex path

## 5. Test Outputs

- baseline chat answer sample
- Cortex-injected chat answer sample
- retrieval bundle sample used for the injected answer
