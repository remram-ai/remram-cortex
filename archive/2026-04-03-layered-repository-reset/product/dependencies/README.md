# Product Dependencies

This folder holds dependencies that Cortex relies on but does not fully own as native product behavior.

## Current Dependencies

- [opensearch-service](opensearch-service/README.md)
- [git-service](git-service/README.md)

Start at each dependency `README.md`. That file is the entry point for ownership, promotion status, and the local document set.

## Dependency Rules

- the stable local dependency bundle should normally include `README.md`, `spec.md`, and `regression-plan.md`
- when a dependency regression plan is under active implementation or validation, add `regression-plan.json` as the structured execution companion
- if the dependency is already a platform item in `remram/platform/`, prefer a local pointer plus only the minimum Cortex-specific overlay needed
- if the dependency has not yet been promoted into the platform registry, local dependency docs may stay here temporarily
- project execution sequencing and rollout proof still belong under [../../projects/](../../projects/README.md)
- when changing a stable local dependency, update the specific `spec.md` and `regression-plan.md` together
