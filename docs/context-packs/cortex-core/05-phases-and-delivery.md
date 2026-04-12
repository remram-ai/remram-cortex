# Phases And Delivery

## Delivery Sequence

The architecture still uses the long-term layered loops described in the design docs.

The active execution package now uses practical delivery phases:

- `Phase 1`: OpenClaw foundation
- `Phase 2`: baseline agents and access
- `Phase 3`: dev/test loop
- `Phase 4`: Cortex augmentation
- `Phase 5`: memory services
- `Phase 6`: sources and artifacts
- `Phase 7`: optimization

## Immediate Build Target

The current target is:

- finish the baseline assistant first
- make memory, web, and escalation usable
- add specialist agents and a repeatable dev loop before bringing in the heavier Cortex service graph

That means:

- prove remote `OpenClaw`
- enable light `QMD`
- keep memory bounded
- use web when freshness is needed
- escalate harder work instead of overloading the default local model
- route before invoking heavier capabilities

## What Is Explicitly Deferred

- browser as a baseline dependency
- `Mamba`
- `Intuition`
- `OpenSearch`
- the heavier Layer 3 and Layer 4 service graph until the practical baseline is solid

## Sequencing Rule

The architecture is already valid before `Mamba`.

The practical baseline is already valuable before the deeper Cortex service graph exists.

Optimization should improve a system that is already useful.
