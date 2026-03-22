# Chat Injection Technical Spec

## Implementation Goal

Prove that Cortex retrieval can influence a live answer before prompt build without hiding the retrieval bundle or its effect.

## Design Summary

- a chat-facing path calls Retrieval first
- the bounded retrieval bundle is made available to answer generation
- the injection path stays inspectable enough to demonstrate that Cortex improved the result
- this epic proves the integration boundary before any broader UI work

## Implementation Surfaces

- project-local implementation and test plans in this epic folder
- capability reference in `product/capabilities/chat-injection/spec.md`
- upstream dependency on the Retrieval bundle contract

## Integration Boundaries

- consumes Retrieval
- feeds the later Chat Interface proof surface
- does not own retrieval semantics or a full chat product UI

## Key Constraints

- preserve the bounded retrieval bundle contract
- keep the injected context inspectable
- avoid growing into a full agent or UI framework

## Definition Of Done

- a chat-facing path can call Cortex retrieval
- the bounded bundle is available for answer generation
- the project-local implementation and test plans are complete and consistent with this technical spec
