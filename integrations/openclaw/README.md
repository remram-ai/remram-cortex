# OpenClaw Integration Assets

These assets are preparation-only integration material for the layered Cortex MVP.

They exist so we can do useful work before a live Moltbox appliance is ready.

For live appliance work, `moltbox-gateway` is the source of truth for:

- the managed service inventory
- the public `moltbox` CLI contract
- the verification surfaces available to restricted operators
- the snapshot-first recovery model

For live repo ownership:

- `moltbox-services` owns baseline service definitions and service-local docs
- `moltbox-runtime` owns the final promoted runtime layer and overlays
- `remram-skills` owns reusable skills/plugins when they become shared assets

## Scope

This folder is for:

- Cortex-specific OpenClaw config overlays
- plugin or skill packages that are meant to be installed into OpenClaw later
- hook and context-assembly prep work that can be reviewed locally
- Moltbox handoff material for the eventual appliance rollout

This folder is not for:

- live runtime deployment
- appliance mutation scripts
- replay-heavy runtime ownership
- pretending the gateway owns normal OpenClaw internals

## Current Assets

- `config/phase0-cortex-overlay.json5`
- `config/phase1-cortex-overlay.json5`
- `packages/cortex-phase1-bridge/`

## Target Posture

The intended operational split is:

- `moltbox-services` defines shared baseline services
- `moltbox-runtime` carries the promoted runtime artifact layer
- `moltbox-gateway` provides the operator-facing deploy, validation, and recovery surface
- OpenClaw remains primarily native for runtime operation, config validation, and plugin lifecycle
- Cortex integrates through policy, prompt-context shaping, boundary hooks, and external service contracts

Important live-baseline constraints:

- normal service-plane mutation uses `moltbox service ...`
- normal runtime mutation uses `moltbox test|prod openclaw ...`
- routine validation should prefer `moltbox test verify runtime|web` and `moltbox prod verify runtime`
- raw Docker and break-glass SSH are not the normal path when the operator surface can do the job
- the current web baseline is `web_search` + built-in `web_fetch`
- native `memory-core` is disabled in the default local lane
- do not reintroduce the old Playwright wrapper architecture as the intended baseline

## Install Model Later

When Moltbox is ready, the plugin package here should be installable with a normal OpenClaw workflow such as:

```bash
openclaw plugins install -l <package-dir>
```

or from a packed tarball once we decide to publish or artifact it more formally.

If the restricted operator path is missing a needed install or validation capability, treat that as a Gateway/operator-surface gap to close in `moltbox-gateway` rather than normalizing raw host mutation.

If a new service is needed, put the baseline service artifact and service-local docs in `moltbox-services`, not here.
