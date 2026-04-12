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
- the current Moltbox Gateway operator contract when the work targets the live appliance baseline

## Exit Criteria

- a run can resolve and inject a policy bundle without replacing OpenClaw sessions
- the startup assembly order is explicit and bounded
- the integration surface for later Mamba and Layer 3 work is stable
- the implementation posture stays compatible with the live Moltbox contract:
  - Gateway remains thin
  - runtime mutation stays on native OpenClaw surfaces
  - routine validation can stay on `moltbox test verify ...` where appropriate

## Notes

- This epic should not invent a separate working-memory store.
- The output here should make Epic 02 possible without revisiting Layer 1/2 ownership.
- If a live-appliance implementation needs a new operator capability, close the gap in `moltbox-gateway` explicitly rather than normalizing raw Docker, break-glass SSH, or replay-era runtime ownership.
- The live web baseline is `web_search` + built-in `web_fetch`, with native `memory-core` disabled in the default local lane; do not reintroduce the old Playwright detour as the intended baseline.
- New services are allowed when the project needs them, but they must be added through the official Moltbox path so they are globally discoverable:
  - service definitions, baseline config, and service-local docs in `moltbox-services`
  - promoted runtime-layer changes in `moltbox-runtime`
  - current Gateway docs only when the operator contract or workflow changes
