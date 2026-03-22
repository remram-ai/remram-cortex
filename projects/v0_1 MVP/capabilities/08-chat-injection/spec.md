# Chat Injection Capability Spec

## 1. Purpose

Provide the MVP read-side proof surface by injecting Cortex retrieval into an ordinary chat flow before prompt build.

## 2. Capability Boundary

This capability is responsible for:

- calling Cortex retrieval during chat orchestration
- receiving a bounded bundle
- injecting that bundle into the chat context
- proving the answer improves with Cortex enabled

This capability is not responsible for:

- full chat application UX
- long-term conversation continuity design

## 3. MVP Flow

1. user asks an ordinary chat question
2. orchestration calls Cortex `/retrieve`
3. Cortex returns a bounded bundle
4. orchestration injects the bundle into the prompt
5. the answer reflects seeded or captured knowledge

## 4. Functional Requirements

- the chat path can call Cortex synchronously
- the returned bundle is inspectable
- the bundle remains bounded
- the resulting answer is observably better than the same path without Cortex retrieval

## 5. Acceptance Bar

At least one ordinary chat scenario must clearly benefit from Cortex knowledge injection rather than generic model recall.

## 6. Deferred

- dedicated Cortex-native chat UI
- advanced continuity policies
- automatic clarification loops
