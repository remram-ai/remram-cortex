# Git Service Technical Spec

## Implementation Goal

Provide the local Git substrate that later provider work can rely on for repository-backed artifact storage and controlled mutation.

## Design Summary

- this epic owns the dependency posture for local Git access and repository mechanics
- it does not own artifact identity, provider routing, or collaborative-provider behavior
- the output should be a stable local Git service contract that the Git Provider epic can consume directly

## Implementation Surfaces

- project-local implementation and test plans in this epic folder
- dependency reference in `product/dependencies/git-service/spec.md`
- local repository or service posture documented well enough for later provider integration

## Integration Boundaries

- Artifact Storage consumes this as substrate, not as identity authority
- Git Provider consumes it as the concrete local backend
- this epic does not redesign provider behavior or artifact lifecycle semantics

## Key Constraints

- stay dependency-scoped rather than provider-scoped
- keep the local Git path explicit and reusable
- avoid provider-routing decisions here

## Definition Of Done

- the local Git service or repository foundation is stable enough for Cortex use
- the dependency contract is explicit
- the project-local implementation and test plans are complete and consistent with this technical spec
