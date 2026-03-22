# Knowledge Extraction Capability Test Plan

## 1. Goal

Prove that Cortex can turn evidence into structured knowledge updates without relying on retrieval-time reasoning to compensate for weak write-path logic.

## 2. Required Tests

- extraction creates knowledge objects from imported evidence
- extraction creates or updates knowledge objects from capture evidence
- merge discipline avoids obvious duplicate objects
- typed signals are present on resulting objects
- semantic signature is present on resulting objects
- provenance and links are attached

## 3. Acceptance Scenario

1. import one document containing a known concept
2. quick-capture a related phrasing of the same concept
3. inspect the resulting object set

Expected result:

- Cortex reinforces, refines, or links the existing knowledge area instead of creating blind duplicate noise

## 4. Failure Conditions

- extraction emits unstructured blobs
- duplicate objects proliferate in one knowledge area
- typed signals or signature are missing
- provenance links are broken

## 5. Test Outputs

- sample extraction delta
- before/after object comparison
- sample object with signals, signature, and provenance
