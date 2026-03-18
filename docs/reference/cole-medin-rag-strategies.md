# Cole Medin RAG Strategies Guide

## Source

- Title: Every RAG Strategy Explained in 13 Minutes (No Fluff)
- Creator: Cole Medin
- Video: https://youtu.be/tLMViADvSNE?si=qr43o169HVhB9EZi
- Companion repo: https://github.com/coleam00/ottomator-agents/tree/main/all-rag-strategies

## Companion Repo Notes

The companion repository is useful because it is not just a link dump. It includes:

- `docs/` for theory and research notes
- `examples/` for short pseudocode examples
- `implementation/` for educational code examples

The repository README explicitly describes the implementation folder as educational and not production-ready. That matters for Cortex: this is a pattern library and learning reference, not a codebase to copy directly into the service.

## Why This Matters For Cortex

This guide is a useful external reference because Cortex is not a generic RAG product, but it will still need several mature retrieval patterns inside its bounded knowledge-retrieval layer.

The video is a compact survey of common RAG strategies. For Cortex, the value is not in copying the whole stack. The value is in identifying which retrieval and chunking techniques can be adapted to a knowledge-authority system with stronger governance, provenance, confidence, and lifecycle controls.

## Strategies Covered By The Guide

The source video description lists these strategies:

1. reranking
2. agentic RAG, including hybrid search
3. knowledge graphs
4. contextual retrieval
5. query expansion
6. multi-query RAG
7. context-aware chunking
8. late chunking
9. hierarchical RAG using metadata
10. self-reflective RAG
11. fine-tuned embeddings

The repo also marks which strategies currently have fuller example coverage:

- code examples: reranking, agentic RAG, contextual retrieval, query expansion, multi-query RAG, context-aware chunking, self-reflective RAG
- pseudocode only: knowledge graphs, late chunking, hierarchical RAG, fine-tuned embeddings

That makes the repo more useful for implementation pattern review in some areas than others.

## Implementation Context From The Repo

The example implementation stack in the companion repo is:

- Pydantic AI
- PostgreSQL plus pgvector
- Docling
- OpenAI models and embeddings

That stack does not match Cortex directly. Cortex is currently oriented around a standalone Go service and OpenSearch. The transferable value is the retrieval and chunking patterns, not the exact framework or storage choices.

## Likely Cortex Relevance

### High Relevance

- reranking
  Cortex already assumes filter-first retrieval plus reranking. This reference is directly relevant to how lexical, vector, confidence, and freshness signals should combine inside the eligible set.
- hybrid search
  Cortex retrieval already combines structured eligibility with lexical and vector signals. This is one of the clearest direct overlaps.
- context-aware chunking
  Useful for bootstrap ingestion and artifact import, where raw inputs need to be segmented without destroying surrounding structure.
- late chunking
  Potentially useful for preserving richer semantics during ingestion before knowledge extraction or retrieval indexing.
- hierarchical retrieval using metadata
  Strong fit with the Cortex dimension system, where metadata and scope should gate eligibility before semantic ranking begins.

- self-reflective retrieval patterns
  The repo treats this as a retrieval strategy. In Cortex, the closest analogue is not generic self-correction during retrieval but the stronger Reflection and Dream lifecycle. Even so, the implementation examples may still be useful when evaluating retrieval-time quality-control patterns.

### Medium Relevance

- contextual retrieval
  Relevant if Cortex needs richer retrieval context for imported artifacts or continuity objects, but it must remain bounded and inspectable.
- query expansion
  Potential enhancement for recall quality, especially when users ask underspecified questions.
- multi-query RAG
  Potential orchestration or retrieval-layer enhancement for broader recall when one query formulation is too narrow.
- fine-tuned embeddings
  Relevant to the open embedding-strategy question, especially if Cortex needs better domain sensitivity without abandoning local-first constraints.

### Lower Or Deferred Relevance

- knowledge graphs
  Cortex already stores relationships between knowledge objects, but a dedicated graph-first retrieval layer is not yet part of the current MVP path.
- agentic RAG
  Relevant only in a constrained way. Cortex should expose retrieval as a structured system capability, while orchestration remains responsible for deciding when and how to invoke it.

## Cortex-Specific Interpretation

This guide should be used as a retrieval-technique catalog, not as a substitute architecture.

Cortex still differs from generic RAG systems in several important ways:

- Cortex stores knowledge objects, not raw transcript chunks, as canonical durable memory.
- Eligibility filtering and dimensions remain primary; vector similarity stays subordinate.
- Retrieval is part of a broader maturation system that includes Reflection, Dream, artifact promotion, and bootstrap ingestion.
- Prompt injection remains controlled by orchestration, not by retrieval heuristics alone.

## Recommended Follow-Up

Use this reference when evaluating:

- reranking and hybrid scoring policy
- chunking strategies for bootstrap ingestion and artifact import
- hierarchical retrieval patterns that align with dimensions
- whether query expansion or multi-query retrieval belongs in Cortex, orchestration, or both
- future embedding strategy decisions
- which repo examples are mature enough to study first versus which are only conceptual pointers

Do not treat the guide as a canonical Cortex design source. The authoritative model remains in [architecture.md](../remram-cortex/architecture.md).
