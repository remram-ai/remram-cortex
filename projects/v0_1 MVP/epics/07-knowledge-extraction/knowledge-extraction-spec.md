# Knowledge Extraction Technical Spec

## Implementation Goal

Turn bounded intake slices into structured knowledge objects with provenance and retrieval-ready signals.

## Design Summary

- extraction consumes source-linked slices from Artifact Intake
- outputs are structured knowledge-object deltas rather than raw summaries or retrieval bundles
- typed signals, semantic signature, and provenance remain first-class explicit fields
- the extraction contract is shaped so Retrieval can consume it directly without reinterpretation

## Requirements Inputs

This technical spec responds to:

- [Knowledge Extraction Requirements](knowledge-extraction-requirements.md)
- [Project Charter](../../project-charter.md)
- [Project Plan](../../project-plan.md)

## Implementation Surfaces

- project-local implementation and test plans in this epic folder
- capability reference in `product/capabilities/knowledge-extraction/spec.md`
- upstream dependency on the slice contract from the Artifact Intake epic

## Integration Boundaries

- consumes Artifact Intake outputs
- feeds Retrieval and Quick Capture reinforcement paths
- does not own retrieval scoring, provider routing, or chat behavior

## Key Constraints

- preserve provenance end to end
- keep typed signals explicit and inspectable
- output knowledge objects, not retrieval-time bundles

## Definition Of Done

- knowledge-object deltas are produced from imported evidence
- typed signals, provenance, and signature are attached
- the project-local implementation and test plans are complete and consistent with this technical spec

