# OpenClaw Integration Assets

These assets are preparation-only integration material for the layered Cortex MVP.

They exist so we can do useful work before a live Moltbox appliance is ready.

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

- `moltbox-gateway` deploys or updates shared services and helps install OpenClaw-facing packages
- OpenClaw remains primarily native for runtime operation, config validation, and plugin lifecycle
- Cortex integrates through policy, prompt-context shaping, boundary hooks, and external service contracts

## Install Model Later

When Moltbox is ready, the plugin package here should be installable with a normal OpenClaw workflow such as:

```bash
openclaw plugins install -l <package-dir>
```

or from a packed tarball once we decide to publish or artifact it more formally.
