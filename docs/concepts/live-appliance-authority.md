# Live Appliance Authority

This concept defines how Cortex should relate to the live Moltbox appliance.

## Core Rule

For live appliance behavior, `moltbox-gateway` is the source of truth.

That includes:

- the managed service inventory
- the public `moltbox` CLI contract
- restricted-operator verification surfaces
- the snapshot-first recovery model
- the current web-tooling baseline

Older `remram` or Cortex design notes may still be useful background, but they do not override the Gateway repo for live appliance work.

This does not mean the live service inventory is frozen forever.

New services may be added as part of Cortex delivery, but they must be added the Moltbox way:

- define and track the baseline service in `moltbox-services`
- use `moltbox-runtime` for approved promoted runtime artifacts and runtime-baseline changes
- make the service discoverable in the official Gateway docs and operator surfaces when the operator contract or workflow changes
- deploy and validate through the official CLI and service-plane path

## Repo Authority Map

Use the repos this way:

- `remram`
  - ecosystem framing
  - approved feature records
  - overview docs and cross-repo pointers
  - not the live authority for appliance behavior or service definitions
- `moltbox-gateway`
  - live CLI contract
  - operator workflows
  - verification surfaces
  - recovery workflow
  - Gateway/OpenClaw operating model
- `moltbox-services`
  - baseline service definitions
  - baseline service config/examples
  - service-local docs
- `moltbox-runtime`
  - final deployable runtime artifacts
  - promoted runtime layer and overlays
  - not the primary authority for baseline service definitions
- `remram-skills`
  - reusable skills/plugins and their docs

## Why This Exists

Cortex has a larger architectural horizon than the current appliance baseline.

Without an explicit rule, it is too easy to let:

- future-service assumptions
- older repo history
- host-only drift
- convenience workarounds

silently replace the actual operator contract.

This concept exists to prevent that drift.

## Practical Consequences

When working against the live appliance:

1. load the current Gateway guides and design docs first
2. treat `test` as the proving lane
3. treat `prod` as a protected managed pet
4. mutate services through `moltbox service ...`
5. mutate runtimes through native `moltbox test|prod openclaw ...`
6. prefer `moltbox test|prod verify ...` for routine validation

When the project needs a new service:

1. put the service definition, baseline config, and service-local docs in `moltbox-services`
2. if it changes the promoted runtime layer, land that portion in `moltbox-runtime`
3. update `moltbox-gateway` only when the operator contract, workflow, verification surface, or recovery story changes
4. deploy it through the official service plane

Do not normalize:

- raw Docker as the normal path
- break-glass SSH for routine work
- replay-era Gateway ownership of OpenClaw internals
- the old Playwright detour as the web baseline

## Cortex Boundary

This rule does not shrink the Cortex architecture.

It means:

- Cortex architecture docs can describe the intended long-term stack
- Cortex implementation plans can describe future service additions
- but live appliance behavior must still honor the current Gateway contract until that contract is intentionally changed

If Cortex needs a new live operator capability, the gap should be closed explicitly in `moltbox-gateway` rather than bypassed in ad hoc host workflows.
