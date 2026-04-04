# Cortex Overview

Remram Cortex is the memory engine for Remram.

It is the layer that turns transient conversations, runtime evidence, and imported artifacts into durable knowledge. It makes retrieval a deliberate system capability instead of prompt sprawl and gives the platform a place where reflection, reconciliation, and long-horizon memory can live.

Runtime evidence captures raw experience. Cortex exists to distill that evidence into knowledge that can compound over time.

Cortex is not a memory plugin and not a chatbot convenience feature. It is a local-first intelligence infrastructure layer for knowledge maturation.

Cortex is not a transcript archive and not a vector-only memory store. It is a structured knowledge layer where governance filters, typed retrieval signals, provenance, and confidence govern memory quality, while lexical and vector signals only help rank already-eligible results.

When Cortex is fully realized, Remram stops behaving like a stateless assistant with a better transcript and starts behaving like a system that can remember, reorganize, and improve over time.

## What Cortex Means

Cortex is the center of long-lived intelligence in the Remram ecosystem:

- durable knowledge instead of transcript dependence
- bounded retrieval instead of uncontrolled context stuffing
- reflection and dream-cycle reconciliation instead of one-pass accumulation
- semantic signature as soft routing rather than hard taxonomy
- typed signal fields as the primary semantic retrieval surface
- bootstrap ingestion that can initialize continuity from historical conversations
- a dedicated system boundary for memory services, indexing, promotion, and recall
- vectors as subordinate ranking signals rather than the definition of memory truth

## Repository Boundary

This repository owns the implementation and authoritative design for Cortex.

The `remram` repository keeps the approved feature record and broader system-facing references. This repository keeps the service-local contracts, vocabulary, and architecture.

## Why It Matters

- users should not have to rebuild important context every time a session changes
- the platform needs a real memory layer instead of treating raw transcript history as durable truth
- retrieval should be structured, inspectable, and intentionally governed
- long-lived knowledge should improve through reflection, contradiction handling, and artifact promotion
- runtime compaction should reduce prompt weight without reducing durable knowledge
- high-value knowledge should be able to mature into lasting reviewable artifacts

## Related Documents

- [Charter](../charter.md)
- [Glossary](../../glossary.md)
- [Concepts](../../concepts/README.md)
- [Architecture](../../remram-cortex/architecture.md)
