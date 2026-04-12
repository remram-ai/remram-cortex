# Moltbox Bring-Up Plan

This document is the handoff path from repo work into the live Moltbox proving lane.

It follows the current Gateway operator contract and the new practical execution phases.

## Baseline Rules

- `moltbox-gateway` owns the live operator contract
- `test` is the current proving lane
- `prod` is protected
- `web_search` plus built-in `web_fetch` is the intended web baseline
- browser is not part of the baseline
- break-glass access is not the routine path

## Phase 1 Bring-Up

### 1. Prove The Current OpenClaw Baseline On `test`

1. Validate the existing runtime and verification surfaces.
2. Confirm the lane is healthy before adding memory or routing changes.
3. Keep the baseline on the official CLI and verification surfaces.

### 2. Install And Prewarm `QMD` On The Host

1. Treat `QMD` as a host-side dependency beside OpenClaw.
2. Do not make the user's local workstation the required place where `QMD` runs.
3. Enable `QMD` as the selected memory backend on the proving lane.
4. Prewarm it explicitly so first-use latency does not surprise the normal chat path.

### 3. Tune Memory To Stay Light

1. Keep retrieval counts, snippet sizes, and injected characters small.
2. Treat memory as a bounded retrieval helper, not as background transcript stuffing.
3. Keep session transcript indexing off or tightly constrained until the baseline proves it is worth enabling.

### 4. Configure The Web Baseline

1. Keep the web path on `web_search` plus built-in `web_fetch`.
2. Do not reintroduce browser as a baseline dependency.
3. Validate the working web lane through the official test verification surface.

### 5. Wire OpenAI Escalation

1. Add the secrets and runtime configuration needed for OpenAI-backed escalation.
2. Keep the local model as the default fast path.
3. Use OpenAI only when the orchestrator decides the task is above the local model's ceiling.

### 6. Add The Lightweight Orchestrator

1. Keep the first routing pass small and fast.
2. Classify whether the task needs:
   - direct local answer
   - web
   - memory
   - coding path
   - escalation
3. Only invoke memory when continuity is actually needed.

## Phase 2 Bring-Up

### 7. Add Baseline Specialist Agents

1. Start with:
   - default assistant
   - coding agent
   - research or thinking agent
   - management or operator agent
2. Keep responsibilities explicit.
3. Favor handoff over one giant all-purpose agent.

### 8. Add Remote Access

1. Make remote usage straightforward from the proving lane.
2. Avoid normalizing "everything has to happen on the user's laptop."

## Phase 3 Bring-Up

### 9. Establish The Dev/Test Loop

1. Use the proving lane as the first repeatable remote validation target.
2. Define deploy, validate, inspect, and rollback steps clearly.
3. Keep the workflow on official Moltbox surfaces whenever possible.

### 10. Integrate The Sandbox Or Coding Environment

1. Wire in the separate coding environment when it is ready.
2. Keep it supportive of the dev loop rather than inventing a second control plane.

## Later Phases

The later Cortex augmentation and memory-service phases should not be blocked on unresolved baseline runtime problems.

Bring in:

- policy bundles
- evidence capture
- semantic hooks
- `Postgres`
- `Neo4j`
- `Graphiti`
- a separate `cortex` service boundary

only after the baseline assistant, routing, and operator workflow are already usable.
