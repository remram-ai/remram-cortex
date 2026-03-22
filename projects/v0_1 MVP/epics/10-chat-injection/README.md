# Epic 10: Chat Injection

## Goal

Prove that Cortex retrieval can influence a live answer before prompt build.

## Stable Product References

- [Chat Injection Spec](../../../../product/capabilities/chat-injection/spec.md)
- [Retrieval Spec](../../../../product/capabilities/retrieval/spec.md)

## Definition Of Done

- a chat-facing path can call Cortex retrieval
- the bounded bundle is available for answer generation
- the epic implementation and epic tests are complete

## Depends On

- [09 Retrieval](../09-retrieval/README.md)

## Epic Documents

- [Requirements](chat-injection-requirements.md)
- [Technical Spec](chat-injection-spec.md)
- [Implementation Plan Data](implementation-plan.json)
- [Test Plan](test-plan.md)
- [Test Plan Data](test-plan.json)
- [Tests](tests/)

