# Test Plan

## Core Scenarios

1. Policy overlays change runtime behavior.
   - different modes change tools, tone, or routing as expected
2. OpenClaw still owns Layer 2.
   - sessions, transcripts, and compaction remain OpenClaw-native
3. Startup context remains bounded.
   - the runtime bundle does not degrade into transcript replay
4. Policy stays inspectable.
   - the final resolved bundle can be reviewed for debugging

## Failure Checks

- policy injection should not duplicate or overwrite session continuity
- switching policy overlays should not require session migration
- context assembly should fail loudly if policy resolution is incomplete

## Evidence Of Completion

- at least one runtime demonstration with two different policy overlays
- one inspection surface showing resolved policy and bounded startup composition
