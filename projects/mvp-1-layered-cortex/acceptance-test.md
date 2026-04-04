# Acceptance Test

The MVP should prove the following end-to-end behaviors:

1. policy overlays affect runtime behavior without replacing OpenClaw session mechanics
2. `QMD` supports hot working-memory retrieval and notion storage
3. turn-end, session-end, and checkpoint-triggered semantic processing emit useful typed semantic outputs for downstream consumers
4. tentative cross-thread continuity is available under tighter rules without silently becoming durable truth
5. Graphiti plus Neo4j organizes durable concepts and relationships without becoming a body store
6. Layer 4 holds operational workspaces and external reference material cleanly
7. Layer 5 is only used when canonical publication is actually warranted

`Mamba` is a later optimization layer and is not required to pass the Phase 1 acceptance surface.
