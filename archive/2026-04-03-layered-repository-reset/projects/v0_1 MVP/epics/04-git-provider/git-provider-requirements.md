# Git Provider Requirements

## Source

Derived from:

- ../../project-charter.md
- ../../project-plan.md
- the stable product references listed below

Owned by:

- project manager for epic-level scope shaping and definition of done

## Epic Intent

Make the local Git provider the safe default Cortex provider.

## Primary User Need

- As a Cortex implementer, I want this epic goal realized so later MVP work can rely on it without reopening the same scope questions.

## Definition Of Done

- the Git provider fits the artifact-storage contract
- it acts as the safe default local provider
- the epic implementation and epic tests are complete

## Stable Product References

- [Git Provider Spec](../../../../product/capabilities/git-provider/spec.md)
- [Artifact Storage Spec](../../../../product/capabilities/artifact-storage/spec.md)

## Depends On

- [02 Git Service](../02-git-service/README.md)
- [03 Artifact Storage](../03-artifact-storage/README.md)

## Acceptance Notes

- this requirements slice should stay aligned to the project charter and project plan
- the technical spec must respond to these requirements without silently expanding scope
- the implementation plan and test plan must trace back to this epic requirements file
