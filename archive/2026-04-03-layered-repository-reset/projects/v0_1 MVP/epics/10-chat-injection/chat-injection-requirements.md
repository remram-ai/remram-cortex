# Chat Injection Requirements

## Source

Derived from:

- ../../project-charter.md
- ../../project-plan.md
- the stable product references listed below

Owned by:

- project manager for epic-level scope shaping and definition of done

## Epic Intent

Prove that Cortex retrieval can influence a live answer before prompt build.

## Primary User Need

- As a Cortex implementer, I want this epic goal realized so later MVP work can rely on it without reopening the same scope questions.

## Definition Of Done

- a chat-facing path can call Cortex retrieval
- the bounded bundle is available for answer generation
- the epic implementation and epic tests are complete

## Stable Product References

- [Chat Injection Spec](../../../../product/capabilities/chat-injection/spec.md)
- [Retrieval Spec](../../../../product/capabilities/retrieval/spec.md)

## Depends On

- [09 Retrieval](../09-retrieval/README.md)

## Acceptance Notes

- this requirements slice should stay aligned to the project charter and project plan
- the technical spec must respond to these requirements without silently expanding scope
- the implementation plan and test plan must trace back to this epic requirements file
