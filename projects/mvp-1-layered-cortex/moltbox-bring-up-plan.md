# Moltbox Bring-Up Plan

This document is the concrete handoff plan from repository prep work to appliance execution.

It assumes the current direction:

- `moltbox-gateway` deploys shared services and helps install OpenClaw-facing packages
- OpenClaw remains primarily native for runtime operation and plugin lifecycle
- Cortex integrates through explicit contracts, bounded hooks, and external service boundaries

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
4. Do not enable the Cortex bridge plugin yet.

### 2. Bring up the shared Cortex-adjacent services in test

1. Use `moltbox-gateway` to deploy the shared services needed for Phase 1:
   - `Postgres`
   - `Neo4j`
   - `Graphiti` service if we keep it as a separate service boundary
   - the Cortex Python service when we are ready to expose it beyond local staging
2. Validate service health and network reachability from the OpenClaw runtime.
3. Do not let the gateway take ownership of normal OpenClaw session internals.

### 3. Install the OpenClaw package in test

1. Install the plugin package from:
   - `integrations/openclaw/packages/cortex-phase1-bridge/`
2. Enable the package in `dry-run` mode first.
3. Merge the `Phase 1` overlay into the test runtime config.
4. Validate that:
   - the plugin is discoverable
   - the plugin is allowed and enabled
   - prompt injection permission is applied only for the bridge plugin
   - the bundled skill appears in the normal OpenClaw skill surface

### 4. Validate bridge-only hook behavior before live service calls

1. Run a controlled test conversation.
2. Confirm the plugin writes hook envelopes under its spool directory.
3. Confirm startup bundle injection is bounded and readable.
4. Confirm OpenClaw sessions, compaction, and transcript ownership remain native.
5. Fix hook-shape mismatches here before enabling service-backed behavior.

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
   - Layer 3 episode packaging
4. Keep Layer 2 OpenClaw-native.

### 6. Validate the full Phase 1 loop in test

1. Run transcript-driven smoke tests against test sessions.
2. Confirm:
   - Layer 5 evidence bodies are inspectable
   - Layer 4 records are source-linked
   - Layer 3 packages stay pointer-based and never become transcript dumps
   - Reflection and Dream hooks are emitted on the expected cadence
3. Compare continuity behavior against the pure Phase 0 baseline.

### 7. Promote cautiously to production

1. Take the approved Moltbox and OpenClaw backup or restore point first.
2. Repeat the install and config steps on `prod`.
3. Keep the first production activation in the narrowest safe mode.
4. Confirm rollback instructions are explicit before broadening the surface.

## Immediate Follow-On Work In This Repo

The next safe repo-only tasks are:

1. turn the bridge package into a fully documented OpenClaw install artifact with a packed tarball dry run
2. add sample config merge instructions for Moltbox runtime templates
3. define transcript-based acceptance fixtures for the first appliance smoke tests
4. decide whether the deployed Cortex bridge service stays stdlib-simple or moves to a fuller HTTP framework
