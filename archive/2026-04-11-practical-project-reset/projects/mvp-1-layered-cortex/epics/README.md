# Epics

These epics are capability tracks inside the phased activation model, not the phase model itself.

The phase plan is authoritative.

The current epic set should be read as implementation slices that cut across phases:

- `Phase 0`: baseline OpenClaw configuration and runtime bring-up
- `Phase 1`: foundational portions of Epics 01, 03, 04, and 05
- `Phase 2`: the reference-decomposition portions of Epic 04
- `Phase 3`: the owned-source maintenance portions of Epic 04 and Epic 05
- `Phase 4`: the authored-promotion portions of Epic 04 and Epic 05
- `Phase 5`: Epic 02 plus the later Intuition and optimization portions of Epic 05

The active epic set is:

1. [01-policy-and-openclaw-integration](01-policy-and-openclaw-integration/README.md)
2. [02-high-signal-mamba-stream](02-high-signal-mamba-stream/README.md)
3. [03-graphiti-neo4j-durable-memory](03-graphiti-neo4j-durable-memory/README.md)
4. [04-knowledge-plane-and-artifacts](04-knowledge-plane-and-artifacts/README.md)
5. [05-intuition-and-reconciliation](05-intuition-and-reconciliation/README.md)
