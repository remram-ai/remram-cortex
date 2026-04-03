# Microsoft GraphRAG Memory System Context

## Purpose

This document captures the actual architecture behind the Microsoft `GraphRAG` memory-style workflow highlighted in Adam Lucek's walkthrough and notebook repo.

The point is not to treat the video as the source of truth.

The point is to preserve the useful model:

- what `GraphRAG` is really doing
- why it feels "memory-like"
- which parts are genuinely strong
- which parts are closer to corpus indexing than live memory authority

Reviewed on `April 2, 2026`.

## Executive Take

Adam Lucek's walkthrough is pointing at a real and important pattern.

`Microsoft GraphRAG` is not just "vector search plus a graph."

It is a staged indexing and query system that:

- extracts entities and relationships from text
- organizes those entities into communities
- generates summaries at multiple levels of graph granularity
- supports different query modes for local facts, global themes, and deeper multi-hop exploration

That is why it feels closer to a memory system than a plain vector database.

The deepest insight is this:

`GraphRAG` is best understood as a graph-structured sensemaking engine over a document corpus.

It gives you:

- semantic objects
- explicit relationships
- hierarchical summaries
- multiple retrieval modes
- follow-up question generation

It does not, by itself, give you:

- a transactional memory authority
- stable, intentional canonical knowledge objects
- first-class write policy
- session or agent lifecycle memory
- governance and provenance policy in the Cortex sense

## What Adam Lucek's Example Actually Is

The video and notebook repo are best read as a guided breakdown of the official Microsoft `GraphRAG` pattern, not as a separate framework.

The repo is a notebook-based explanation of:

- why vector-only `RAG` breaks on broad "sensemaking" questions
- how entity and relationship extraction changes the retrieval surface
- why community detection matters
- how `Local`, `Global`, and `DRIFT` search behave differently

That makes it useful for Cortex in two ways:

- as a concept reference for graph-shaped memory and multi-scale retrieval
- as a concrete implementation example of the "offline summarization plus online query" pattern

## The Core Problem GraphRAG Solves

The official `GraphRAG` paper frames the target problem clearly:

- traditional `RAG` works better for explicit retrieval problems
- it performs worse on broad questions about an entire corpus
- broad corpus questions are really query-focused summarization problems

The classic example is:

"What are the main themes in this dataset?"

That is not just nearest-neighbor retrieval.

It requires:

- seeing structure across many chunks
- understanding which concepts are connected
- collapsing many local details into higher-level summaries

This is the central value proposition of `GraphRAG`.

## The GraphRAG Knowledge Model

The official dataflow and query docs show a fairly consistent internal model.

The important objects are:

### 1. Documents

The raw source files being indexed.

### 2. Text Units

Documents are chunked into `Text Units`.

These are the raw passages that remain linked to extracted graph artifacts.

### 3. Entities

Named or distinct concepts extracted from text.

These become graph nodes and also receive descriptions.

### 4. Relationships

Edges between entities, including descriptions and weights.

These are not just implicit similarity links. They are extracted, described, and used for traversal and community detection.

### 5. Claims and Covariates

These are optional structured augmentations.

They matter because they show `GraphRAG` is not limited to just node-edge extraction. The indexing model already anticipates additional typed structured data.

### 6. Communities

`GraphRAG` runs community detection over the entity graph.

This creates clusters of related concepts at different levels of granularity.

The docs and paper make this hierarchy central, not optional decoration.

### 7. Community Reports

Each community gets an LLM-generated summary report, and those reports can themselves be summarized.

These reports are the key innovation behind the "global" and "sensemaking" behavior.

### 8. Embeddings

Embeddings are generated for downstream vector search over:

- entity descriptions
- text units
- community reports

This is important.

`GraphRAG` does not reject vector search.

It subordinates vector search to a richer graph-and-summary index.

## Why Communities Matter So Much

The community layer is where the system stops behaving like plain retrieval.

The default indexing flow:

- extracts a graph
- partitions it into communities
- generates reports for those communities
- summarizes the reports for shorthand use

The official docs explicitly position these reports as giving a high-level understanding of the graph at several levels of granularity, from an entire graph-level view down to lower-level local clusters.

This is the closest thing in stock `GraphRAG` to:

- abstraction layers
- Dream-like condensation
- big-picture recall

This is also why the `Leiden` algorithm appears in the architecture.

The reason is not cosmetic.

`GraphRAG` needs communities that are meaningfully connected, because the quality of the later summaries depends on the quality of the graph partitions. The `Leiden` method is attractive here because it improves on Louvain by addressing poorly connected communities and using a refinement phase to keep communities well connected.

## Default Indexing Workflow

The official default dataflow breaks the process into staged transformations.

### Phase 1. Compose Text Units

Raw documents are chunked into `Text Units`.

This establishes the bounded source passages that later graph objects can point back to.

### Phase 2. Document Processing

The source documents are linked to the text units and written into document tables.

### Phase 3. Graph Extraction

This phase extracts:

- entities
- relationships
- optional claims

It also summarizes entity and relationship descriptions across mentions.

This matters because the graph is not just a bag of raw extractions. It is consolidated into more useful descriptions.

### Phase 4. Graph Augmentation

This is where community detection happens and graph tables are produced.

At this point the system has a usable entity graph plus a hierarchy of communities.

### Phase 5. Community Summarization

This is the signature step.

For each community, the LLM generates a report containing an overview plus references to important entities, relationships, and claims in that subgraph.

Those reports are then summarized again for shorthand use.

### Phase 6. Text Embeddings

The system generates embeddings for artifacts that need vector search downstream. The docs call out:

- entity descriptions
- text unit text
- community report text

The result is not one index.

It is a layered knowledge package:

- raw text
- graph structure
- cluster structure
- generated summaries
- embeddings over multiple artifact types

## Baseline Setup Flow

The official quickstart is simple:

1. `pip install graphrag`
2. `graphrag init`
3. put source text in `input/`
4. configure `.env` and `settings.yaml`
5. optionally run prompt tuning
6. run `graphrag index`
7. query the output

The docs note that `init` creates:

- `.env`
- `settings.yaml`
- `input/`

The indexing run produces an `output/` directory with parquet tables and embeddings written to the configured vector store.

This matters for Cortex because it shows the true storage posture:

- `GraphRAG` is pipeline-first
- outputs are materialized artifacts
- the default mental model is "build index, then query"

## Query Modes

The official query docs describe four main retrieval modes plus question generation.

### Local Search

Best for:

- specific facts
- entity-centric questions
- questions needing both structure and supporting raw text

The official docs describe it this way:

- identify entities semantically related to the query
- use those entities as access points into the graph
- gather connected entities, relationships, covariates, community reports, and linked text units
- rank and filter them into one context window
- answer from that mixed context

This is not basic vector `RAG`.

It is a structured mixed-context retrieval method.

### Global Search

Best for:

- broad themes
- corpus-wide questions
- sensemaking over large collections

The official docs say global search uses community reports from a chosen hierarchy level and answers in a map-reduce pattern:

- split community reports into chunks
- generate intermediate responses with rated points
- aggregate the highest-importance points
- produce the final answer

This is the core "big picture" capability that the original paper emphasizes.

### DRIFT Search

Best for:

- multi-hop exploration
- questions that need both high-level context and local detail
- deeper investigation without paying full global-search cost every time

The official docs describe `DRIFT` as combining local and global behavior:

- start from the most relevant community reports
- generate an initial answer plus follow-up questions
- use local search to refine those follow-ups
- build a hierarchical result of questions and answers

This is especially important for Cortex, because it looks much closer to an exploratory memory workflow than ordinary retrieval.

### Basic Search

`GraphRAG` also ships a rudimentary basic vector `RAG` mode so users can compare standard retrieval against the graph-aware methods.

That is useful conceptually because the framework is telling you:

- vector retrieval still matters
- but the graph index exists to answer different classes of questions better

### Question Generation

This is easy to miss, but it is one of the more Cortex-relevant pieces.

The question generation flow uses the same local-search-style context construction to generate likely next questions from prior queries.

That makes it useful for:

- investigative follow-ups
- conversation steering
- active exploration of a corpus

## Built-In Extension Points Worth Noting

`GraphRAG` has more extension room than a casual first read suggests.

### Prompt Tuning

The official docs provide:

- default prompts
- auto tuning
- manual tuning

Auto tuning is explicitly encouraged so the graph-generation prompts adapt to the domain.

That matters because the quality of extracted entities, relationships, claims, and reports is highly prompt-sensitive.

### Bring Your Own Graph

The `BYOG` path is important.

The docs explicitly support providing your own `entities.parquet`, `relationships.parquet`, and optionally `text_units.parquet`, then running only the community and reporting workflows you need.

This means `GraphRAG` can be used as:

- a full end-to-end graph extraction system
- a downstream summarization/query layer on top of another graph producer

That makes it much more interesting for Cortex than a locked black-box pipeline.

### Workflow Subsetting

The docs show that you can run just selected workflows such as:

- `create_communities`
- `create_community_reports`
- `generate_text_embeddings`

This is important if we ever want to use only the summarization/query layers and provide our own upstream knowledge objects.

## Why It Feels Like A Memory System

Even though `GraphRAG` is not a general memory authority, it feels memory-like for good reasons.

It already contains several patterns Cortex cares about:

### Multi-Scale Recall

The system can answer at:

- passage level
- entity-neighborhood level
- community level
- whole-corpus thematic level

### Explicit Connections

Entities and relationships are first-class instead of being latent only in vectors.

### Condensed Memory

Community reports are compressed memory artifacts.

They preserve more structure than flat chunk summaries.

### Follow-Up Exploration

`DRIFT` and question generation create a path for guided exploration rather than one-shot retrieval.

### Mixed Context Retrieval

Responses are built from both:

- structured graph artifacts
- original source text

That combination is why the answers can feel more coherent than plain chunk retrieval.

## What GraphRAG Is Not

This is where the limits matter.

Stock `GraphRAG` is not:

- a live memory service for ongoing agent turns
- a transactional write model for durable memories
- a canonical object model for manually curated knowledge
- a policy engine for promotion, suppression, or conflict resolution
- a first-class provenance and governance system in the Cortex sense

It is primarily:

- a corpus transformation pipeline
- a graph-and-summary query engine

That distinction matters a lot.

It means the natural unit of truth is closer to:

- corpus artifacts
- extracted graph tables
- community summaries

than to:

- deliberate long-lived memory objects being actively maintained over time

## The Most Cortex-Relevant Ideas To Steal

If we never use `GraphRAG` directly, it is still worth mining for patterns.

The strongest patterns are:

### 1. Community Reports As Dream-Lite

Offline graph-cluster summarization is a credible way to build higher-order memory views without inventing everything from scratch.

### 2. Multiple Query Modes For Different Memory Questions

`Local`, `Global`, and `DRIFT` are a strong template for:

- fact recall
- big-picture recall
- exploratory reasoning

### 3. Graph Plus Text, Not Graph Instead Of Text

The best answers still use original passages.

That is architecturally important.

### 4. Prompt-Tuned Extraction

If memory quality depends on extraction quality, the extraction prompts need to become first-class assets.

### 5. Bring Your Own Graph

This is the biggest extension seam.

It means the summarization and query layers can be reused even if the upstream knowledge model is ours.

## Bottom Line

Adam Lucek's walkthrough is worth keeping as a serious reference.

The Microsoft `GraphRAG` stack demonstrates a real architecture that is close to parts of the Cortex vision:

- graph-shaped meaning extraction
- multi-level summaries
- multiple retrieval modes
- guided exploration over large corpora

Its natural home in the Cortex knowledge base is:

- definitely as an example architecture
- definitely as a document-memory and sensemaking reference
- possibly as a subsystem option later
- only cautiously as a primary foundation

The next question is not "is this real?"

It is:

"Which parts of this should be treated as reusable Cortex patterns, and which parts only make sense for corpus-centric document intelligence?"

## Sources

- Adam Lucek GraphRAG Breakdown repo: <https://github.com/ALucek/GraphRAG-Breakdown>
- Microsoft GraphRAG docs: <https://microsoft.github.io/graphrag/>
- GraphRAG Getting Started: <https://microsoft.github.io/graphrag/get_started/>
- GraphRAG Default Dataflow: <https://microsoft.github.io/graphrag/index/default_dataflow/>
- GraphRAG Query Overview: <https://microsoft.github.io/graphrag/query/overview/>
- GraphRAG Local Search: <https://microsoft.github.io/graphrag/query/local_search/>
- GraphRAG Global Search: <https://microsoft.github.io/graphrag/query/global_search/>
- GraphRAG DRIFT Search: <https://microsoft.github.io/graphrag/query/drift_search/>
- GraphRAG Question Generation: <https://microsoft.github.io/graphrag/query/question_generation/>
- GraphRAG Bring Your Own Graph: <https://microsoft.github.io/graphrag/index/byog/>
- GraphRAG Prompt Tuning Overview: <https://microsoft.github.io/graphrag/prompt_tuning/overview/>
- GraphRAG CLI / init docs: <https://microsoft.github.io/graphrag/cli/>
- GraphRAG paper: <https://arxiv.org/abs/2404.16130>
- LinkedIn customer-service KG + RAG case study: <https://arxiv.org/abs/2404.17723>
- Unifying Large Language Models and Knowledge Graphs: A Roadmap: <https://arxiv.org/abs/2306.08302>
- Fine-Tuning LLMs review: <https://arxiv.org/abs/2408.13296>
- Google Knowledge Graph introduction: <https://blog.google/products-and-platforms/products/search/introducing-knowledge-graph-things-not/>
- Leiden algorithm overview: <https://en.wikipedia.org/wiki/Leiden_algorithm>
