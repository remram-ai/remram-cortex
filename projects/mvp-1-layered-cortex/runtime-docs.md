# Runtime Docs

The runtime proof surface for this MVP should demonstrate:

- OpenClaw session flow
- Layer 1 policy injection points
- `QMD`-backed hot working-memory retrieval
- turn-end and session-end semantic extraction
- explicit-checkpoint semantic extraction when needed
- notion creation, reuse, invalidation, and cleanup
- tentative cross-thread continuity under tighter retrieval rules
- reconciliation checkpoints into Layer 3
- Layer 4 workspace materialization across multiple threads
- artifact and reference handling without forcing early canon

Always-on `Mamba` listening is not required for this proof surface.
