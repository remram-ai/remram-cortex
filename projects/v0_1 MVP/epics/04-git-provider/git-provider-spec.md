# Git Provider Technical Spec

## Implementation Goal

Implement the local Git-backed provider as the safe default Cortex provider without diluting the artifact-storage contract.

## Design Summary

- the provider implements the Artifact Storage contract on top of the Git substrate
- it is the default local provider for MVP work because it gives deterministic local ownership and inspectability
- provider behavior stays adapter-scoped and does not redefine artifact identity

## Implementation Surfaces

- project-local implementation and test plans in this epic folder
- provider reference in `product/capabilities/git-provider/spec.md`
- contract source in the Artifact Storage epic and product spec

## Integration Boundaries

- consumes Git Service as substrate
- consumes Artifact Storage as the authoritative contract
- does not own collaborative-provider behavior, retrieval, or extraction logic

## Key Constraints

- keep default-provider logic explicit and reversible
- preserve Cortex-owned identity and versioning
- do not let Git-specific assumptions leak into the provider-neutral contract

## Definition Of Done

- the Git provider fits the artifact-storage contract
- it acts as the safe default local provider
- the project-local implementation and test plans are complete and consistent with this technical spec
