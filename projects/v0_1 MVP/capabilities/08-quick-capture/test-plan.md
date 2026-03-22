# Quick Capture Capability Test Plan

## 1. Goal

Prove that low-friction captures become real Cortex memory instead of a separate notes lane.

## 2. Required Tests

- capture text becomes a capture artifact
- reflection produces knowledge deltas
- capture can reinforce an existing concept
- capture can create a new concept when appropriate
- capture-derived knowledge is retrievable

## 3. Acceptance Scenario

Seed state:

- imported OpenTrails project documents already exist

Action:

- submit capture: `Reseller network for trail lodging along hiking routes`

Expected result:

- capture artifact is created
- related project knowledge is updated or linked
- no obvious duplicate object is introduced if the idea already exists nearby

## 4. Failure Conditions

- capture bypasses artifact/provenance creation
- capture always creates a new object
- capture is not visible in retrieval immediately after processing

## 5. Test Outputs

- capture request sample
- capture artifact sample
- before/after object comparison for one refine or reinforce case
