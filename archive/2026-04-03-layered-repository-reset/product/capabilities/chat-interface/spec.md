# Chat Interface Capability Spec

## 1. Purpose

Provide a minimal chat interface or harness that proves Cortex retrieval can improve live conversation and can later be plugged into OpenClaw as a chat agent surface.

## 2. Capability Boundary

This capability is responsible for:

- one user-facing or test-facing chat surface
- calling Cortex retrieval before prompt build
- showing or exposing the bounded bundle used for the answer
- proving the end-to-end read path from memory to answer

This capability is not responsible for:

- final OpenClaw integration
- long-term multi-session continuity design
- production chat UX polish

## 3. MVP Requirements

- simple chat request input
- retrieval call before answer generation
- bounded bundle injection
- answer output
- enough visibility to compare with a no-Cortex baseline

## 4. Functional Requirements

- interface can send a question through the Cortex-backed path
- interface can expose the retrieved bundle or trace for debugging
- interface can be replaced later by an OpenClaw adapter without changing Cortex retrieval semantics

## 5. Deferred

- production UI polish
- mobile client
- full OpenClaw chat-agent packaging
