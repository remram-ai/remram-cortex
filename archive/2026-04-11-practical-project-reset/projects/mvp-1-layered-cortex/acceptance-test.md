# Acceptance Test

This acceptance test is the current `Phase 1` surface on top of the `Phase 0` baseline.

It should prove the following end-to-end behaviors:

1. the Phase 0 OpenClaw baseline runs locally with safe config, compaction, pruning, and `QMD`
2. policy overlays affect runtime behavior without replacing OpenClaw session mechanics
3. chat transcripts enter the Layer 5 runtime-evidence path
4. turn-end, session-end, and checkpoint-triggered semantic processing emit useful typed semantic outputs for downstream consumers
5. tentative cross-thread continuity is available under tighter rules without silently becoming durable truth
6. Graphiti plus Neo4j organizes durable concepts and relationships without becoming a body store
7. Layer 4 holds chat-derived support bodies, summaries, and candidate facts or beliefs cleanly

`Mamba` is a later optimization layer and is not required to pass the Phase 1 acceptance surface.
