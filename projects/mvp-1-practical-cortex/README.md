# MVP 1: Practical Cortex

This is the active execution package for Cortex.

The earlier `mvp-1-layered-cortex` package has been archived under:

- `archive/2026-04-11-practical-project-reset/projects/mvp-1-layered-cortex/`

## Goal

Make the system genuinely useful before expanding into the deeper Cortex service graph.

That means:

- a stable remote `OpenClaw` baseline
- light but real memory through `QMD`
- web capability through `web_search` and `web_fetch`
- model escalation for work the local default model cannot carry
- a lightweight orchestrator that routes before it injects memory or escalates
- baseline specialist agents and a practical remote development loop

## Delivery Model

This package uses practical delivery phases with concrete epics inside each phase.

It does not try to make the project phases match the long-term architecture loops one-for-one.

The architecture docs still own the layer model and long-term authority rules.
This package owns the execution sequence.

## Immediate Target

The current execution target is:

- finish `Phase 1` foundation cleanly
- carry enough of `Phase 2` and `Phase 3` to make the system usable for day-to-day work

## Definition Of Done For The Current Baseline

The practical MVP baseline is ready when:

- `OpenClaw` is stable on the remote proving lane
- `QMD` runs as a sidecar on the host and is tuned light enough for the local default model
- the orchestrator decides whether memory, web, coding, or escalation is needed before taking the heavier path
- web baseline works without the browser path
- OpenAI escalation works for harder reasoning and coding cases
- baseline specialist agents exist for coding, research, and appliance management
- a repeatable local-to-remote test loop exists without normalizing break-glass behavior

## Documents

- [Project Charter](project-charter.md)
- [Project Plan](project-plan.md)
- [Acceptance Test](acceptance-test.md)
- [Runtime Docs](runtime-docs.md)
- [Local Dev](local-dev.md)
- [Moltbox Bring-Up Plan](moltbox-bring-up-plan.md)
- [Seed Prompt](seed-prompt.md)
- [Phases](phases/README.md)

## Recommended Handoff Path

For a new implementation thread, read in this order:

1. [../../docs/context-packs/cortex-core/README.md](../../docs/context-packs/cortex-core/README.md)
2. [../../docs/context-packs/cortex-core/00-repo-orientation.md](../../docs/context-packs/cortex-core/00-repo-orientation.md)
3. [../../docs/context-packs/cortex-core/01-terminology-and-legacy.md](../../docs/context-packs/cortex-core/01-terminology-and-legacy.md)
4. [../../docs/context-packs/cortex-core/02-layers-and-authority.md](../../docs/context-packs/cortex-core/02-layers-and-authority.md)
5. [../../docs/context-packs/cortex-core/05-phases-and-delivery.md](../../docs/context-packs/cortex-core/05-phases-and-delivery.md)
6. [../../docs/context-packs/cortex-core/08-live-appliance-quick-start.md](../../docs/context-packs/cortex-core/08-live-appliance-quick-start.md)
7. [Project Charter](project-charter.md)
8. [Project Plan](project-plan.md)
9. [Acceptance Test](acceptance-test.md)
10. [Phases](phases/README.md)
