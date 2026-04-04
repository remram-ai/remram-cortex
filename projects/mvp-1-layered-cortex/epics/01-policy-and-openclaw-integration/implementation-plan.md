# Implementation Plan

## Objective

Stand up Layer 1 policy and the OpenClaw integration seam without replacing OpenClaw's native Layer 2 session mechanics.

## Workstreams

1. Define the Cortex policy bundle.
   - role and mode overlays
   - tool and approval rules
   - prompt-budget discipline
   - mutable preference-policy boundary
2. Implement OpenClaw-facing policy assembly.
   - resolve policy for a run
   - inject policy into runtime context cleanly
   - keep the policy bundle inspectable
3. Establish the custom context-engine posture.
   - use OpenClaw's context-engine seam rather than replacing sessions
   - keep Layer 2 OpenClaw-native
   - reserve Cortex-owned logic for policy-aware assembly and semantic augmentation
4. Prove bounded runtime startup behavior.
   - policy first
   - compact working-memory continuity second
   - bounded durable-memory bundle third
   - knowledge pointers only when needed

## Deliverables

- policy bundle schema and example overlays
- OpenClaw integration boundary document or code scaffold
- bounded startup assembly contract
- explicit statement of what remains OpenClaw-owned versus Cortex-owned

## Dependencies

- active layered architecture docs
- OpenClaw context-engine and session model

## Exit Criteria

- a run can resolve and inject a policy bundle without replacing OpenClaw sessions
- the startup assembly order is explicit and bounded
- the integration surface for later Mamba and Layer 3 work is stable

## Notes

- This epic should not invent a separate working-memory store.
- The output here should make Epic 02 possible without revisiting Layer 1/2 ownership.
