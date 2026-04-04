# Implementation Plan

## Objective

Build the High-Signal Mamba Stream as Cortex's narrow always-on high-signal channel between live session activity and downstream consumers.

This epic is Phase 3 by default.

It can be pulled forward as a Phase `1.5` spike only if the post-Phase-1 gate says local continuity pressure justifies it.

## Workstreams

1. Define the semantic checkpoint schema.
   - typed payloads
   - source references
   - confidence and timing fields
   - notion and oversight hints
2. Build checkpoint production from session activity.
   - always-on near-time listening
   - bounded event emission during active sessions
   - rebuildability from evidence packages when needed
3. Support downstream consumption modes.
   - working-memory assembly
   - notion staging in `QMD`
   - oversight and reflection
   - later checkpoint and nightly consumers
4. Integrate the stream with downstream consumers.
   - context continuity assembly
   - `QMD` notion staging
   - oversight
   - reflection and Layer 4 workspace hints

## Deliverables

- semantic checkpoint payload contract
- consumer watermark or idempotence model
- source-linking contract back to evidence packages
- working demonstration of the always-on listener against the existing Phase 1 hooks

## Dependencies

- Epic 01 Layer 1/2 integration boundary
- Phase 1 boundary-triggered semantic processing hooks
- evidence package model

## Exit Criteria

- semantic checkpoints are produced from session evidence with stable source links
- at least two downstream consumers can use the same stream without bespoke formats
- the stream can be explained as a rebuildable semantic projection, not a second authority

## Notes

- The stream is the primary near-time consumer surface once this epic lands.
- Raw evidence remains a backing journal, not the normal subscribe surface.
- Mamba is narrow by design.
- It is not the general reflection engine or the document decomposition engine.
- The Phase 1 hooks must survive after Mamba arrives.
- Mamba augments boundary-triggered semantic processing rather than invalidating it.
