# Phase 1: OpenClaw Foundation

## Goal

Make the baseline assistant useful.

## Epics

1. Remote OpenClaw baseline
2. `QMD` sidecar bring-up
3. Light memory tuning
4. Web baseline
5. OpenAI escalation
6. Lightweight orchestrator

## Key Rules

- `QMD` runs on the host beside OpenClaw
- memory stays light
- the orchestrator decides whether memory is needed before it is injected
- browser stays out of the baseline

## Exit Criteria

- the proving lane is stable
- QMD is working and prewarmed
- web works
- escalation works
- routing works without making the fast path feel heavy
