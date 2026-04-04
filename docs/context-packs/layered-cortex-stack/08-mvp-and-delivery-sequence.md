# MVP And Delivery Sequence

## MVP Goal

MVP 1 proves the simplified locked stack:

- `OpenClaw`
- Cortex policy layer
- `QMD` hot working memory
- narrow Mamba high-signal stream
- `Graphiti + Neo4j` durable memory
- `Postgres` operational middle layer
- `Git` canonical artifacts when applicable

## Epic Order

1. policy and OpenClaw integration
2. QMD-backed Layer 2 and Mamba stream
3. Graphiti plus Neo4j durable memory
4. Layer 4 operational knowledge
5. reflection, Dream, oversight, and promotion readiness

## What MVP Explicitly Excludes

MVP excludes:

- OpenSearch
- a second graph system
- a second Graphiti mode
- premature canonicalization of budding ideas

## The 10 Design-Lock Answers

1. Choose `QMD` explicitly for Layer 2 hot working memory and notions.
2. The notion ledger lives in `QMD`.
3. Tentative cross-thread memory is allowed under tighter retrieval rules, but it is not silently authoritative before reconciliation.
4. No `OpenSearch` for now. `Postgres` remains the operational middle-layer authority for MVP.
5. Keep full transcripts hot for roughly `90` to `120` days since last access, then move them to cold storage. Keep compact metadata and semantic checkpoints hot much longer.
6. Keep the trust model minimal. Use lightweight states and avoid inventing a giant second semantics system.
7. Use stable anchor identity and pointer-based relationships in Graphiti. Do not turn Graphiti into a document body store.
8. Keep the split hard. OpenClaw owns runtime and workflow mechanics. Cortex owns memory, policy composition, reconciliation, and governed preference-policy behavior.
9. Mamba is a narrow always-on Layer 2 listener that emits a high-signal stream from session activity.
10. MVP 1 includes OpenClaw, Cortex policy, QMD, Mamba, Graphiti plus Neo4j, Postgres, and Git when canon is warranted. OpenSearch and additional service expansion are deferred.
