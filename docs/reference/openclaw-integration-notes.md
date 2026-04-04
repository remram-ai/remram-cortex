# OpenClaw Integration Notes

OpenClaw is the runtime shell for Cortex.

The active integration posture is:

- let OpenClaw own sessions and working-memory mechanics
- keep Cortex above it for policy, semantic checkpointing, and durable-memory orchestration

Important surfaces:

- sessions
- hooks
- compaction
- context-engine inputs and lifecycle methods
- tool calls
- checkpoint boundaries like `/stop` and `/reset`

Current upstream docs support the following assumptions:

- OpenClaw exposes a real `context-engine` extension surface rather than forcing all context behavior through static prompt assembly.
- Sessions and transcript continuity remain OpenClaw-owned even when a custom context engine is used.
- Compaction writes continuity back into the session surface, which is why Cortex should prepare semantic checkpoints ahead of prompt pressure instead of waiting until context is already overflowing.
- Memory and context-engine are separate plugin slots, which supports the current posture of leaving Layer 2 with OpenClaw while Cortex owns policy and Layer 3 separately.
- `QMD` is a stronger OpenClaw-native memory engine than the builtin engine when you want reranking, query expansion, extra-path indexing, and session transcript indexing.
- `Dreaming` exists in OpenClaw as an experimental background promotion pass, but it promotes short-term recalls into Markdown long-term memory and should not be confused with Cortex Layer 3 consolidation.

Operational rule:

- do not replace OpenClaw Layer 2 until OpenClaw itself is the blocker
- prefer augmentation through policy and the High-Signal Mamba stream

Implementation takeaways:

- Treat the OpenClaw session as the native evidence surface for Layer 2.
- Use the context engine for policy-aware bounded assembly, not for replacing session mechanics.
- Use hooks and checkpoint boundaries to close evidence windows, emit semantic checkpoints, and trigger slower reconciliation.

Official references:

- https://docs.openclaw.ai/context-engine
- https://docs.openclaw.ai/concepts/context
- https://docs.openclaw.ai/compaction
- https://docs.openclaw.ai/reference/session-management-compaction
- https://docs.openclaw.ai/concepts/memory
- https://docs.openclaw.ai/concepts/memory-qmd
- https://docs.openclaw.ai/concepts/memory-dreaming
- https://docs.openclaw.ai/tools/plugin
