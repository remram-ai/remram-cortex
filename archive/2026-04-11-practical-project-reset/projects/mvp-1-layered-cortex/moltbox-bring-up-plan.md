# Moltbox Bring-Up Plan

This document is the concrete handoff plan from repository prep work to appliance execution.

It assumes the current direction:

- `moltbox-services` owns baseline service definitions and service-local docs
- `moltbox-runtime` owns final promoted runtime artifacts and overlays
- `moltbox-gateway` owns the operator-facing deploy, verification, and recovery contract
- OpenClaw remains primarily native for runtime operation and plugin lifecycle
- Cortex integrates through explicit contracts, bounded hooks, and external service boundaries

It also assumes the current live appliance baseline:

- managed services are `gateway`, `caddy`, `ollama`, `searxng`, `test`, and `prod`
- `test` is the proving lane
- `prod` is a protected managed pet
- routine validation should stay on `moltbox test verify runtime|web` and `moltbox prod verify runtime` where possible
- raw Docker and break-glass SSH are not the normal path
- the web baseline is `web_search` + built-in `web_fetch`
- native `memory-core` is disabled in the default local lane
- the Playwright detour is not part of the intended baseline

## What We Can Do Before Infrastructure Exists

These are valid and useful now:

1. compose the OpenClaw config overlays for `Phase 0` and `Phase 1`
2. prepare the initial OpenClaw plugin package and bundled skill assets
3. lock the Postgres Layer 4 schema for Phase 1 support bodies
4. keep the filesystem-backed Layer 5 and hook staging surfaces inspectable
5. define the exact handoff sequence for Moltbox `test` first, then `prod`

Those assets now exist in this repository.

## Ready-Now Assets

- OpenClaw overlays:
  - `integrations/openclaw/config/phase0-cortex-overlay.json5`
  - `integrations/openclaw/config/phase1-cortex-overlay.json5`
- OpenClaw plugin package:
  - `integrations/openclaw/packages/cortex-phase1-bridge/`
- Bridge service contract:
  - `integrations/openclaw/cortex-bridge-service-contract.md`
- Layer 4 Postgres contract:
  - `sql/postgres/001_phase1_support_bodies.sql`
- Prep runtime scaffold:
  - `remram_cortex/`

## Once Moltbox Is Ready

### 1. Establish the Phase 0 OpenClaw baseline

1. Deploy or validate the baseline OpenClaw runtime on Moltbox `test`.
2. Merge the `Phase 0` Cortex overlay into the approved Moltbox OpenClaw baseline.
3. Validate that:
   - OpenClaw starts cleanly
   - config validation passes
   - `QMD` is selected as the working-memory backend
   - compaction and pruning remain native OpenClaw behavior
   - `moltbox test verify runtime` passes
   - `moltbox test verify web` passes
4. Do not enable the Cortex bridge plugin yet.

### 2. Bring up the shared Cortex-adjacent services in test

1. Treat this as an explicit service-plane expansion step, not an assumption about the current baseline.
2. Add the shared services needed for Phase 1 to the tracked Moltbox service inventory only when we are ready to support them cleanly:
   - `Postgres`
   - `Neo4j`
   - `Graphiti`
   - `Cortex`
3. Land those additions the Moltbox way so they are globally discoverable:
   - service definitions, baseline config, and service-local docs in `moltbox-services`
   - promoted runtime-layer changes in `moltbox-runtime` when required
   - official Gateway docs only when the operator contract or workflow changes
4. Deploy those services through the official service plane:
   - `moltbox service deploy <service>`
5. Validate service health and network reachability from the OpenClaw runtime.
6. Do not let the gateway take ownership of normal OpenClaw session internals.
7. If routine validation of those services requires raw host orchestration, close the missing operator surface in `moltbox-gateway` instead of treating the workaround as normal.

### 3. Install the OpenClaw package in test

1. Install the plugin package from:
   - `integrations/openclaw/packages/cortex-phase1-bridge/`
2. Use native OpenClaw install/config flows through the official `moltbox test openclaw ...` path.
3. If the restricted operator contract is missing a needed install action, add the narrowest safe Gateway surface rather than normalizing raw shell mutation.
4. Enable the package in `dry-run` mode first.
5. Merge the `Phase 1` overlay into the test runtime config.
6. Validate that:
   - the plugin is discoverable
   - the plugin is allowed and enabled
   - prompt injection permission is applied only for the bridge plugin
   - the bundled skill appears in the normal OpenClaw skill surface

### 4. Validate bridge-only hook behavior before live service calls

1. Run a controlled test conversation.
2. Confirm the plugin writes hook envelopes under its spool directory.
3. Confirm startup bundle injection is bounded and readable.
4. Confirm OpenClaw sessions, compaction, and transcript ownership remain native.
5. Re-run the official verification surfaces that should remain true after the plugin is added:
   - `moltbox test verify runtime`
   - `moltbox test verify web`
6. Fix hook-shape mismatches here before enabling service-backed behavior.

### 5. Switch the bridge from `dry-run` to service-backed mode

1. Point the bridge config at the deployed Cortex service.
2. Keep the same bounded hook entry points:
   - `before_prompt_build`
   - compaction boundary hooks
   - `agent_end`
3. Confirm the bridge now hands off:
   - Layer 5 evidence capture
   - semantic checkpoint creation
   - Layer 4 support-body staging
   - Layer 3 episode packaging through the separate `Graphiti` service boundary
4. Keep Layer 2 OpenClaw-native.

### 6. Validate the full Phase 1 loop in test

1. Run transcript-driven smoke tests against test sessions.
2. Confirm:
   - Layer 5 evidence bodies are inspectable
   - Layer 4 records are source-linked
   - Layer 3 packages stay pointer-based and never become transcript dumps
   - Reflection and Dream hooks are emitted on the expected cadence
3. Compare continuity behavior against the pure Phase 0 baseline.
4. Keep using the official verification surfaces so runtime and web regressions are caught on the same lane:
   - `moltbox test verify runtime`
   - `moltbox test verify web`

### 7. Promote cautiously to production

1. Take the approved Moltbox and OpenClaw backup or restore point first.
2. Repeat the install and config steps on `prod`.
3. Keep the first production activation in the narrowest safe mode.
4. Validate through the official protected-runtime surface:
   - `moltbox prod verify runtime`
5. Confirm rollback instructions are explicit before broadening the surface.

## Immediate Follow-On Work In This Repo

The next safe repo-only tasks are:

1. turn the bridge package into a fully documented OpenClaw install artifact with a packed tarball dry run
2. add sample config merge instructions for Moltbox runtime templates
3. define transcript-based acceptance fixtures for the first appliance smoke tests
4. decide whether the deployed Cortex bridge service stays stdlib-simple or moves to a fuller HTTP framework
