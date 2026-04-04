# Graphiti And Neo4j Notes

`Graphiti + Neo4j` is the active Layer 3 durable-memory posture.

Why it stays active:

- episode-backed provenance
- temporal memory semantics
- invalidation and supersession
- graph-native retrieval over durable memory
- hybrid search at the Graphiti product layer

Current upstream docs support the following assumptions:

- `Graphiti` treats episodes as the core ingestion unit for messages, text, and structured data.
- `Graphiti` search includes semantic and hybrid retrieval modes at the framework layer.
- `Neo4j` remains an officially documented backend path for `Graphiti`.
- `Neo4j` itself now has both vector indexes and full-text indexes, which makes the chosen backend compatible with the hybrid retrieval posture even when Graphiti remains the main Layer 3 abstraction.
- `Graphiti` clearly documents provenance and point-in-time semantics, but I do not see a documented first-class confidence system that would replace Cortex trust states.
- Graph ontology customization is available, which makes artifact or document lineage nodes a natural fit inside Layer 3.

Important implementation rule:

- do not treat Graphiti as raw evidence storage
- ingest compact evidence packages with pointers back to canonical evidence or artifact revisions

`Neo4j` is the backend because the active posture favors durable integrity over an in-memory primary graph substrate.

Important caution:

- Historical or batched ingest should be handled carefully. Graphiti's bulk-add posture is useful, but it is not the right place to assume perfect invalidation semantics during replay-heavy ingestion. The safe architectural posture remains: keep raw evidence authoritative elsewhere, package bounded evidence into Graphiti, and reconcile durable memory deliberately.

Official references:

- https://help.getzep.com/graphiti/graphiti/overview
- https://help.getzep.com/graphiti/core-concepts/adding-episodes
- https://help.getzep.com/graphiti/working-with-data/searching
- https://help.getzep.com/graphiti/configuration/neo-4-j-configuration
- https://help.getzep.com/customizing-graph-structure
- https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/
- https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/full-text-indexes/
- https://neo4j.com/blog/developer/hybrid-retrieval-graphrag-python-package/
