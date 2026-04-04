# Cole Medin RAG Strategies Guide

## Source

- Title: Every RAG Strategy Explained in 13 Minutes (No Fluff)
- Creator: Cole Medin
- Video: https://youtu.be/tLMViADvSNE?si=qr43o169HVhB9EZi
- Companion repo: https://github.com/coleam00/ottomator-agents/tree/main/all-rag-strategies

## Why This Reference Matters

The guide is useful as a retrieval-pattern catalog.

It is not a Cortex architecture source on its own, but it is a strong external sanity check for what Cortex should adopt, translate, constrain, or defer.

The companion repo explicitly positions its implementations as educational rather than production-ready. That matters for Cortex: the value is in the strategy patterns, not in copying the exact stack.

## Repo Shape

The `all-rag-strategies` folder provides:

- `docs/` for theory and research notes
- `examples/` for short pseudocode
- `implementation/` for educational code examples

The strategy overview in the repo currently covers:

1. reranking
2. agentic RAG
3. knowledge graphs
4. contextual retrieval
5. query expansion
6. multi-query RAG
7. context-aware chunking
8. late chunking
9. hierarchical RAG using metadata
10. self-reflective RAG
11. fine-tuned embeddings

GitHub repo: https://github.com/coleam00/ottomator-agents/tree/main/all-rag-strategies

## Cortex Alignment

### Direct Fits

#### Hybrid Retrieval

Cortex aligns strongly with hybrid retrieval, but with stricter governance.

Practical Cortex mapping:

- OpenSearch `filter` over governance fields
- OpenSearch `should` over typed signal fields
- optional vector scoring inside the bounded candidate set

This is the main retrieval surface for Cortex.

#### Reranking

Reranking is a direct fit.

Cortex should rerank with:

- signal-field match quality
- semantic signature similarity
- confidence
- freshness
- reinforcement
- relationship expansion

This is one of the clearest overlaps with the guide.

#### Hierarchical Retrieval Using Metadata

This maps directly to Cortex's governance-first retrieval model.

The repo describes metadata-driven narrowing for complex document retrieval. Cortex applies the same principle at the knowledge-object level by enforcing ownership, audience, scope, lifecycle, and temporal validity before semantic ranking begins.

#### Context-Aware Chunking

This is highly relevant for artifact intake and bootstrap ingestion.

Cortex should use chunking as an ingestion tactic to preserve source structure before knowledge extraction, not as a second durable memory tier.

### Partial Fits

#### Contextual Retrieval

Contextual retrieval is most useful for imported artifacts or continuity summaries where a source slice needs more document-level framing before it embeds well.

It is less central to canonical knowledge-object retrieval, because Cortex expects reflection to have already distilled the durable object.

#### Query Expansion

Query expansion is useful when the user asks an underspecified question and initial retrieval confidence is weak.

For Cortex, this should be:

- a fallback
- bounded
- inspectable

It should not become the default answer to mediocre reflection quality.

#### Multi-Query RAG

Multi-query retrieval can improve recall, but it increases latency and complexity.

For Cortex, it makes more sense as:

- a low-confidence fallback
- or a Dream-time analysis tool

than as the default live retrieval path.

#### Late Chunking

Late chunking is promising for imported artifacts and historical backfill where larger document context may improve extraction quality. It is relevant to ingestion, not to the durable memory unit itself.

### Translated Rather Than Adopted

#### Self-Reflective RAG

The guide treats self-reflection as a retrieval-time strategy.

Cortex should translate that idea into its lifecycle:

- Reflection handles immediate post-run extraction and merge decisions
- Dream handles slower global reconciliation

That keeps self-correction out of the hottest retrieval path.

#### Knowledge Graphs

Knowledge graphs are conceptually relevant because Cortex stores typed links and uses relationship expansion.

However:

- Cortex does not need graph-first infrastructure for the first architecture pass
- OpenSearch plus typed links is sufficient for the current model

So this is relationship-aware retrieval, not a full graph-RAG commitment.

#### Agentic RAG

The companion repo treats agentic RAG as autonomous selection between retrieval tools.

For Cortex, the parallel is weaker:

- orchestration may choose when to call Cortex or when to fetch full artifacts
- Cortex retrieval itself should remain predictable and bounded

The architecture should not depend on an agent improvising memory policy at retrieval time.

### Deferred Or Open

#### Fine-Tuned Embeddings

Potentially relevant later if local or domain-specific embeddings materially improve ranking quality. This remains an embedding-strategy question, not a foundational architecture requirement.

## OpenSearch Practicality

The reference stack in the repo uses PostgreSQL plus pgvector, Docling, and hosted model services. Cortex instead targets OpenSearch plus a standalone Go service.

That still maps well:

- BM25 and multi-field lexical scoring map cleanly to OpenSearch
- governance filters map cleanly to `bool.filter`
- vector backstop maps to OpenSearch k-NN or vector scoring
- reranking can happen in Cortex after OpenSearch returns a bounded candidate set
- chunking strategies remain applicable at ingest time

The main architectural difference is that Cortex stores canonical knowledge objects rather than raw document chunks as the durable memory surface.

## Practical Takeaways For Cortex

Use this reference to justify and refine:

- governance-first hierarchical retrieval
- hybrid lexical plus vector retrieval
- multi-stage reranking
- context-aware chunking for import and bootstrap
- selective fallback expansion when recall is weak

Do not use it to justify:

- vector-first memory
- chunk-first canonical storage
- fully agentic retrieval policy
- query-time self-reasoning as the default compensation for weak reflection

## Bottom Line

Cole Medin's guide is a strong external fit for Cortex if it is read as a retrieval-technique catalog.

The closest direct matches are:

- hybrid retrieval
- reranking
- hierarchical metadata retrieval
- chunking strategies for ingestion

The most important Cortex-specific translation is this:

generic RAG often spends intelligence at retrieval time;
Cortex should spend most of that intelligence during Reflection and Dream so retrieval remains fast and predictable.

The authoritative Cortex model remains [architecture.md](../remram-cortex/architecture.md).
