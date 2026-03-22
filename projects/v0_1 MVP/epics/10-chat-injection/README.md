# Epic 10: Chat Injection

## Goal

Prove that Cortex retrieval can influence a live answer before prompt build.

## Product References

- [Chat Injection Spec](../../../../product/capabilities/chat-injection/spec.md)
- [Retrieval Spec](../../../../product/capabilities/retrieval/spec.md)

## Definition Of Done

- a chat-facing path can call Cortex retrieval
- the bounded bundle is available for answer generation
- the epic implementation and epic tests are complete

## Depends On

- [09 Retrieval](../09-retrieval/README.md)

## Epic Documents

- [Implementation Plan](implementation-plan.md)
- [Test Plan](test-plan.md)
- [Tests](tests/)
