# OpenClaw And Live Appliance Boundary

## OpenClaw Boundary

OpenClaw owns:

- runtime execution
- sessions
- transcript continuity
- hooks
- compaction
- tool execution

Cortex adds:

- Layer 1 policy composition
- `QMD`-backed hot working memory
- boundary-triggered semantic processing
- Layer 3 and Layer 4 orchestration
- evidence, promotion, and reconciliation rules

## Live Appliance Rule

For live Moltbox appliance behavior, `moltbox-gateway` is the source of truth for:

- operator workflows
- public CLI contract
- verification surfaces
- recovery model
- current web-tooling baseline

This repo may describe the intended Cortex seam, but it does not override the live operator contract.

## External Repo Split

- `moltbox-gateway`: operator and appliance behavior
- `moltbox-services`: baseline service definitions
- `moltbox-runtime`: promoted runtime artifacts
- `remram-cortex`: Cortex architecture and integration shape

## Practical Reminder

Do not treat host-only shortcuts or older notes as the live authority when working against the appliance.
