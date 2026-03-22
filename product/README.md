# Product Surface

This folder holds the stable Cortex product surface.

Use it for design material that should outlive one MVP run or one execution thread.

## Start Here

- If you want the stable Cortex capability map, start with [capabilities/README.md](capabilities/README.md).
- If you want the stable dependency map, start with [dependencies/README.md](dependencies/README.md).
- If you are changing a stable product area, read the specific `spec.md` and `regression-plan.md` together.
- If you are looking for current delivery order, acceptance, or proof, switch to [../projects/](../projects/README.md).

## Structure

- [capabilities/README.md](capabilities/README.md): Cortex-owned capabilities
- [dependencies/README.md](dependencies/README.md): service-shaped or external dependencies Cortex relies on

## Stable Artifact Contract

The default stable artifact set is:

- capabilities: `spec.md` plus `regression-plan.md`
- dependencies: `README.md`, `spec.md`, and `regression-plan.md`

Optional artifacts such as operator guides, provider notes, sample payloads, or diagrams may be added when the surface needs them.

When a stable regression plan becomes an active execution surface, add a `regression-plan.json` companion so tests can be tracked by stable IDs instead of prose alone.

## Boundary

`product/` is the Cortex equivalent of the platform registry layer in `remram`, but scoped to this repository as one product-sized implementation boundary.

That means:

- native Cortex behavior belongs under `capabilities/`
- platform-shaped dependencies may live under `dependencies/`
- when a dependency is already owned canonically in `remram/platform/`, the local dependency folder should prefer a pointer or a thin overlay rather than a second competing source of truth

Project-specific sequencing, execution records, and evidence belong under [../projects/](../projects/README.md), not here.
