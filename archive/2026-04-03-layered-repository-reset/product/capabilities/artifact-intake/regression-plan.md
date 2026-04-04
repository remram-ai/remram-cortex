# Artifact Intake Capability Regression Plan

## 1. Goal

Prove that imported artifacts can become source-linked Cortex knowledge without bypassing the main memory model.

## 2. Required Tests

- Markdown import creates source-linked slices
- text import creates source-linked slices
- PDF import creates source-linked slices when text is extractable
- knowledge objects are created or updated from those slices
- provenance links back to the source artifact and location

## 3. Acceptance Scenario

1. import a small OpenTrails document
2. inspect emitted slices
3. inspect resulting knowledge objects
4. retrieve one concept from the imported corpus
5. trace it back to the source location

Expected result:

- the concept is retrievable and auditable back to the artifact

## 4. Failure Conditions

- slices are unbounded or lose source location
- intake produces opaque blobs instead of knowledge updates
- imported content is not retrievable after indexing

## 5. Test Outputs

- import job sample
- example slice payload
- resulting knowledge object sample
- provenance trace sample
