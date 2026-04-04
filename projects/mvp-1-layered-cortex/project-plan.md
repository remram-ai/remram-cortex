# Project Plan

## Epic Order

1. Policy and OpenClaw integration
2. High-Signal Mamba stream
3. Graphiti + Neo4j durable memory
4. Knowledge plane and artifacts
5. Oversight and reconciliation

## Why This Order

- Layer 1 and Layer 2 must be stable before the system can feed durable memory cleanly
- the semantic checkpoint stream must exist before notion staging and oversight make sense
- durable memory should be brought up before artifact-heavy reconciliation
- knowledge and artifacts need the layer contracts in place first
- oversight and reconciliation should harden the system after the main data flows exist
