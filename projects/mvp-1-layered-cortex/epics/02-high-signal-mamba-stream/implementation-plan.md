# Implementation Plan

## Objective

Build the High-Signal Mamba Stream as Cortex's narrow always-on high-signal channel between live session activity and downstream consumers.

## Workstreams

1. Define the semantic checkpoint schema.
   - typed payloads
   - source references
   - confidence and timing fields
   - notion and oversight hints
2. Build checkpoint production from OpenClaw evidence.
   - always-on near-time listening
   - bounded event emission during active sessions
   - rebuildability from evidence packages when needed
3. Support downstream consumption modes.
   - working-memory assembly
   - notion staging in `QMD`
   - reflection and oversight
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
- working demonstration of at least one optimistic and one boundary-based producer

## Dependencies

- Epic 01 Layer 1/2 integration boundary
- evidence package model

## Exit Criteria

- semantic checkpoints are produced from session evidence with stable source links
- at least two consumers can use the same stream without bespoke formats
- the stream can be explained as a rebuildable semantic projection, not a second authority

## Notes

- The stream is the primary consumer surface.
- Raw evidence remains a backing journal, not the normal subscribe surface.
- Mamba is narrow by design.
- It is not the general reflection engine or the document decomposition engine.
