# Graphiti And Neo4j Notes

`Graphiti + Neo4j` is the active Layer 3 durable-memory posture.

Why it stays active:

- episode-backed provenance
- temporal memory semantics
- invalidation and supersession
- graph-native retrieval over durable memory

Important implementation rule:

- do not treat Graphiti as raw evidence storage
- ingest compact evidence packages with pointers back to canonical evidence or artifact revisions

`Neo4j` is the backend because the active posture favors durable integrity over an in-memory primary graph substrate.
