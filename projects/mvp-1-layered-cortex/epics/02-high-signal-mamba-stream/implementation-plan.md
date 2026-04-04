# Implementation Plan

## Objective

Build the High-Signal Mamba Stream as Cortex's semantic checkpoint bus between raw evidence and downstream consumers.

## Workstreams

1. Define the semantic checkpoint schema.
   - typed payloads
   - source references
   - confidence and timing fields
   - notion and oversight hints
2. Build checkpoint production from OpenClaw evidence.
   - near-time production when cheap
   - checkpoint production at session boundaries
   - rebuildability from evidence packages
3. Support three consumption modes.
   - optimistic
   - on-demand
   - nightly
4. Integrate the stream with downstream consumers.
   - context-engine continuity assembly
   - Layer 3 notion staging
   - oversight
   - knowledge-impact hints

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
