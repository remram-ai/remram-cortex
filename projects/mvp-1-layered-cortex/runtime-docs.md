# Runtime Docs

The runtime proof surface for this MVP should demonstrate:

- OpenClaw session flow
- Layer 1 policy injection points
- `QMD`-backed hot working-memory retrieval
- turn-end and session-end semantic extraction
- explicit-checkpoint semantic extraction when needed
- notion creation, reuse, invalidation, and cleanup
- tentative cross-thread continuity under tighter retrieval rules
- reconciliation checkpoints into Layer 3
- Layer 4 workspace materialization across multiple threads
- artifact and reference handling without forcing early canon

Always-on `Mamba` listening is not required for this proof surface.

## Current Preparation Scaffold

The repository now includes a preparation-only implementation scaffold that stops short of live infrastructure.

It is intentionally limited to:

- policy bundle resolution
- bounded next-turn startup bundle assembly
- filesystem-backed Layer 5 runtime-evidence capture
- boundary-triggered semantic checkpoint generation
- local staging or outbox payloads for:
  - Layer 2 `QMD` mutations
  - Layer 4 support bodies
  - Layer 3 `Graphiti` episode packages
  - Reflection and Dream hook payloads

It does not attempt to:

- deploy or mutate live OpenClaw runtimes
- provision Postgres, Neo4j, or Graphiti
- assume a live Moltbox appliance
- turn the gateway into the owner of OpenClaw internals

## Prep Command

Run the local scaffold against the example transcript:

```bash
python -m remram_cortex run-boundary --input examples/phase1-session.json
```

The command writes inspectable artifacts under `.runtime/cortex/` by default.

## Appliance Target Posture

This scaffold is written for the current Moltbox direction:

- `moltbox-gateway` deploys shared services such as `Postgres` and helps deploy OpenClaw-facing skills
- OpenClaw runtime operation remains primarily native OpenClaw behavior
- Cortex should integrate through contracts and bounded payloads, not through gateway-owned replay or direct runtime-state ownership

## Layer 4 Contract

The initial appliance-facing Postgres contract for Phase 1 support bodies lives at:

- `sql/postgres/001_phase1_support_bodies.sql`

That schema is the intended database shape for later Moltbox deployment.
The current scaffold only stages matching JSON payloads locally so the contract can be reviewed before infrastructure exists.

## OpenClaw Prep Assets

While Moltbox is unavailable, the repo can still prepare:

- OpenClaw config overlays:
  - `integrations/openclaw/config/phase0-cortex-overlay.json5`
  - `integrations/openclaw/config/phase1-cortex-overlay.json5`
- an installable OpenClaw bridge package:
  - `integrations/openclaw/packages/cortex-phase1-bridge/`
- a bridge HTTP contract and local service skeleton:
  - `integrations/openclaw/cortex-bridge-service-contract.md`
  - `python -m remram_cortex serve`
- the appliance handoff sequence:
  - `moltbox-bring-up-plan.md`
