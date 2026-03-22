# OpenSearch Service Requirements

## Source

Derived from:

- ../../project-charter.md
- ../../project-plan.md
- the stable product references listed below

Owned by:

- project manager for epic-level scope shaping and definition of done

## Epic Intent

Stand up the OpenSearch dependency so Cortex has a usable retrieval substrate for later MVP work.

## Primary User Need

- As a Cortex implementer, I want this epic goal realized so later MVP work can rely on it without reopening the same scope questions.

## Definition Of Done

- the Moltbox-managed OpenSearch service can be deployed and inspected
- the dependency posture is documented well enough for later Cortex epics to reuse directly
- the epic implementation and epic tests are complete

## Stable Product References

- [OpenSearch Service Dependency](../../../../product/dependencies/opensearch-service/README.md)
- [Retrieval Capability](../../../../product/capabilities/retrieval/spec.md)

## Depends On

- none

## Acceptance Notes

- this requirements slice should stay aligned to the project charter and project plan
- the technical spec must respond to these requirements without silently expanding scope
- the implementation plan and test plan must trace back to this epic requirements file
