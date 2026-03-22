# Artifact Storage Technical Spec

## Implementation Goal

Define the Cortex-owned artifact identity, versioning, and provider-routing model that every later storage provider and intake path must obey.

## Design Summary

- Cortex owns `artifact_id`, version references, and retained artifact metadata
- providers sit behind the facade and store bytes or provider-native handles
- routing is policy-driven and provider-neutral
- prune, backlink, and resolve behavior are explicit parts of the contract, not ad hoc follow-on features

## Implementation Surfaces

- project-local implementation and test plans in this epic folder
- capability reference in `product/capabilities/artifact-storage/spec.md`
- later provider epics consume this contract rather than defining their own artifact semantics

## Integration Boundaries

- Git Service provides substrate but not identity
- Git Provider and Google Drive Provider implement this contract
- knowledge extraction and retrieval consume artifact records but do not own them

## Key Constraints

- stay provider-neutral
- keep Cortex as the single identity authority
- do not leak retrieval or chat concerns into the artifact contract

## Definition Of Done

- stable `artifact_id` handling exists
- provider routing and record shape are explicit
- the project-local implementation and test plans are complete and consistent with this technical spec
