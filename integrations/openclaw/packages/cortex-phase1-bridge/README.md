# Cortex Phase 1 Bridge

This is the initial OpenClaw plugin package for the Cortex Phase 1 prep pass.

It is designed to be:

- installable through the normal OpenClaw plugin workflow
- safe to enable in `dry-run` mode first
- explicit about what is staged locally versus what later belongs to live services

## Package Contents

- `openclaw.plugin.json`
- `index.js`
- `SKILL.md`

## Current Responsibility

The package currently does two narrow jobs:

1. capture lifecycle envelopes at bounded OpenClaw hook points
2. inject a prepared startup bundle when one exists for the current session

That makes it a useful pre-infrastructure bridge without claiming ownership of runtime internals.

## Future Expansion

Later, once Moltbox is ready and the Cortex service contract is pinned, this package can evolve to:

- call a local Cortex API instead of writing only spool envelopes
- fetch bounded startup bundles from a service rather than local files
- hand off session-end evidence processing to the deployed Cortex service

Those are later steps and are intentionally not required for this prep pass.

## Service Contract

The current prep contract for `service` mode is documented in:

- `../../cortex-bridge-service-contract.md`
