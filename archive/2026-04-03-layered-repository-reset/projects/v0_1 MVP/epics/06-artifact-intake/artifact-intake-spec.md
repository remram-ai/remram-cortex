# Artifact Intake Technical Spec

## Implementation Goal

Turn imported artifacts into bounded, source-linked slices that the extraction stage can consume directly.

## Design Summary

- imported artifacts resolve through Artifact Storage first
- intake normalizes supported source shapes into bounded slices
- every slice preserves enough source linkage to support provenance and backlinking later
- the output of this epic is the slice handoff contract, not the final knowledge object

## Requirements Inputs

This technical spec responds to:

- [Artifact Intake Requirements](artifact-intake-requirements.md)
- [Project Charter](../../project-charter.md)
- [Project Plan](../../project-plan.md)

## Implementation Surfaces

- project-local implementation and test plans in this epic folder
- capability reference in `product/capabilities/artifact-intake/spec.md`
- upstream dependency on artifact-storage and provider surfaces

## Integration Boundaries

- Knowledge Extraction consumes slices from this epic
- provider and artifact identity behavior stay upstream of this stage
- retrieval and chat work stay downstream

## Key Constraints

- preserve source linkage
- keep slices bounded and inspectable
- stop at the slice boundary rather than absorbing extraction logic

## Definition Of Done

- supported artifacts can be turned into source-linked slices
- the slice handoff to extraction is clear
- the project-local implementation and test plans are complete and consistent with this technical spec

