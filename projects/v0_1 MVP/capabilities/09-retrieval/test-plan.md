# Retrieval Capability Test Plan

## 1. Goal

Prove that the Cortex retrieval stack can find the right bounded knowledge bundle across multiple valid query framings.

## 2. Required Tests

- imported knowledge is retrievable
- capture-derived knowledge is retrievable
- linked imported plus captured knowledge can be retrieved together
- retrieval trace explains filters and ranking contributors
- one concept is reachable through multiple phrasings

## 3. Acceptance Scenario

After import and quick capture:

- query `find more camping spots`
- query `how could OpenTrails make money`
- query `places to stay while hiking`

Expected result:

- the same underlying concept remains discoverable from all three queries

## 4. Stretch Scenario

- run one ambiguous query where multiple relevant results should compose into a bundle instead of collapsing to one hit

## 5. Failure Conditions

- retrieval only works for exact wording
- ranking cannot explain why a result won
- near-duplicate objects crowd out diversity in the bundle

## 6. Test Outputs

- retrieval request samples
- retrieval trace samples
- ranked result comparison across multiple phrasings
