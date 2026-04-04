# OpenClaw Integration Notes

OpenClaw is the runtime shell for Cortex.

The active integration posture is:

- let OpenClaw own sessions and working-memory mechanics
- keep Cortex above it for policy, semantic checkpointing, and durable-memory orchestration

Important surfaces:

- sessions
- hooks
- compaction
- context-engine inputs
- tool calls
- checkpoint boundaries like `/stop` and `/reset`

Operational rule:

- do not replace OpenClaw Layer 2 until OpenClaw itself is the blocker
- prefer augmentation through policy and the High-Signal Mamba stream
