# Quick Capture Technical Spec

## Implementation Goal

Provide a low-friction path for new thoughts to enter the same evidence-to-knowledge system as imported artifacts.

## Design Summary

- quick capture reuses Artifact Storage for identity and persistence
- captured content flows through the same intake and extraction model instead of becoming a sidecar notes system
- the path is intentionally narrow: create artifact, normalize input, and reinforce or extend knowledge

## Requirements Inputs

This technical spec responds to:

- [Quick Capture Requirements](quick-capture-requirements.md)
- [Project Charter](../../project-charter.md)
- [Project Plan](../../project-plan.md)

## Implementation Surfaces

- project-local implementation and test plans in this epic folder
- capability reference in `product/capabilities/quick-capture/spec.md`
- upstream dependency on artifact-storage and knowledge-extraction contracts

## Integration Boundaries

- consumes Artifact Storage and Knowledge Extraction
- later Retrieval should see captures in the same pool as imported knowledge
- this epic does not own retrieval ranking or chat interface behavior

## Key Constraints

- no separate memory subsystem for captures
- keep the write path simple and inspectable
- treat capture as another evidence source, not a different product

## Definition Of Done

- a short capture becomes a stored artifact
- the capture reinforces or extends existing knowledge through the same model
- the project-local implementation and test plans are complete and consistent with this technical spec

