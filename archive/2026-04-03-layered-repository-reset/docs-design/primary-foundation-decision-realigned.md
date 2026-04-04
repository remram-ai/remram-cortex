# Primary Foundation Decision: Realigned

## Purpose

This document replaces the earlier "solo foundation" framing with a narrower and more useful question:

"What single primary foundation should anchor Cortex long term, if the goal is one-builder implementation, local and free infrastructure, fast initial usefulness, and low odds of replatforming stored memory later?"

Reviewed on `April 1, 2026`.

This memo uses the clarified decision lens from the user:

- optimize for one builder implementation burden
- optimize for local and free base infrastructure
- optimize for the fastest path to something usable
- optimize for the lowest likelihood of replatforming stored data later
- optimize for strongest fit to a **memory authority** layer, not just a retrieval subsystem

Two important corrections from the earlier passes:

- `OpenSearch` is relevant, but not a gate
- `Dream` is not a major selection criterion

## Scope

This is a decision about the **primary anchor platform**.

Minimal supporting pieces are allowed if they materially reduce startup cost without creating a second long-term authority.

This is **not** a composable stack bakeoff.

## Finalists

The serious finalists under this decision lens are:

1. `Mem0 OSS`
2. `Graphiti`
3. `Letta`

`Weaviate`, `Neo4j`, and `Qdrant` are all included as storage-first options because they are relevant to the storage posture question, but none naturally qualifies as a full memory authority platform on its own.

`memU` is intentionally excluded from this final field. We already gave it an optimistic pass, and it still did not clear the bar for this specific decision.

## Decision Lens

The right question for each contender is not "is it already Cortex?"

The right question is:

"If I anchor Cortex on this platform, how likely is it that I can keep building forward without regretting the stored model later?"

That breaks into five tests:

1. memory authority fit
2. custom work still required
3. long-term migration risk
4. stored data model evolvability
5. path toward the final Cortex direction of travel

## Executive Ranking

| Rank | Option | Why It Lands Here |
| --- | --- | --- |
| 1 | `Mem0 OSS` | Best overall compromise between usable-now, real memory behavior, local self-hosting, and survivable long-term evolution |
| 2 | `Graphiti` | Best structural fit to durable knowledge and provenance, but materially higher implementation and operations burden for one builder |
| 3 | `Letta` | Best personal-agent runtime, but too entangled with runtime memory and block editing to be the cleanest long-term Cortex authority |
| Wildcard | `Weaviate`-first custom build | Strongest storage-native alternative if you want to own the memory logic yourself while keeping a richer long-term object store |
| Wildcard | `Neo4j`-first custom build | Strongest graph-native storage wildcard if links, provenance, and traversal matter more than fastest retrieval ergonomics |
| Wildcard | `Qdrant`-first custom build | Very strong local retrieval substrate, but still not a real memory authority platform on its own |

## Summary Table

Scores are qualitative.

| Option | Memory Authority Fit | Custom Work Required | Long-Term Migration Risk | Stored Model Evolvability | Fast Path To Usable | Overall Read |
| --- | --- | --- | --- | --- | --- | --- |
| `Mem0 OSS` | Medium-High | Medium | Medium | Medium | High | Best overall balance |
| `Graphiti` | High | High | Low-Medium | High | Medium | Best structural fit, heavier lift |
| `Letta` | Medium | Medium-High | Medium-High | Medium | High | Great runtime shell, weaker authority anchor |
| `Weaviate`-first custom | Low-Medium | High | Medium | High | Medium | Strongest custom-storage route if you want richer object semantics |
| `Neo4j`-first custom | Medium | High | Low-Medium | High | Low-Medium | Strong graph substrate, but raw Neo4j is still heavier than the better-ranked paths |
| `Qdrant`-first custom | Low | High | High | Medium | Medium | Strong substrate, weak primary foundation |

## Contender 1: Mem0 OSS

### Memory Authority Fit

`Mem0` is the strongest contender overall because it is already a memory engine, not just a vector database or orchestration shell.

It gives you:

- persistent memory creation
- explicit memory update behavior
- delete or no-op logic
- metadata filtering
- history
- optional graph memory
- local and self-hosted deployment
- multiple backend options

That is enough to count as a real proto-authority layer.

It is not a perfect Cortex match.

Its natural durable unit is still closer to a memory entry or fact record than to a fully explicit Cortex knowledge object with first-class artifact identity, typed signals, and promotion state.

But it is close enough to evolve without immediate betrayal.

### Custom Work Still Required

The key custom work is not the core memory loop. `Mem0` already covers much of that.

The key custom work is the Cortex-specific discipline around it:

- canonical knowledge-object schema
- artifact registry and stable `artifact_id`
- stronger provenance tuples than free-form metadata alone
- retrieval bundle shaping and traces
- governance field contract
- richer merge outcomes like reinforce, contradict, supersede, retire

This is real work, but it is mostly overlay work rather than a full rewrite of the base system.

### Long-Term Migration Risk

This is the main weakness in `Mem0`.

By default, the stored object is still basically:

- text payload
- vector
- metadata
- separate history trail

That is workable.

But if you let the system drift into "unstructured memory facts with ever-growing metadata," you will eventually want a schema correction.

The migration risk is therefore **medium**, not low.

It stays acceptable only if you impose a Cortex-style metadata contract very early.

### Stored Data Model Evolvability

`Mem0`'s stored model is evolvable enough if you are disciplined:

- treat each memory as a proto-knowledge-object
- reserve metadata keys intentionally
- store stable source references from day one
- avoid backend-specific hacks in the canonical contract

If you do that, the system can evolve forward without immediately replatforming.

If you do not, you will end up with a payload swamp.

### Path Toward Final Cortex

`Mem0` keeps you on the right path if you use it as:

- the initial memory engine
- not the final semantic vocabulary

That means:

- let `Mem0` own extraction, search, update, and history
- let Cortex own canonical naming, artifact identity, provenance discipline, bundle shaping, and later maintenance policy

That is a healthy split.

### Best Storage Posture For Mem0

If `Mem0` is the base platform, I would not use `OpenSearch` first.

I would use:

- `Weaviate` if you want the strongest long-term storage semantics
- `Qdrant` if you want the simplest fastest local start and accept more future migration risk

Why `Weaviate` wins as the preferred phase-1 store:

- objects plus vectors are a better long-term fit than vector plus payload alone
- hybrid and filter-first retrieval are already strong
- it is local, free, and single-node friendly

Why `Qdrant` is still valid:

- extremely easy local start
- very good filter and hybrid support
- fast, simple, and practical

Why `Qdrant` is not preferred here:

- it is more clearly a vector engine with payloads than an object-first authority substrate
- that slightly increases the odds of later storage reshaping

## Contender 2: Graphiti

### Memory Authority Fit

`Graphiti` is the strongest structural fit in the field.

It already thinks in terms of:

- episodes as evidence
- entities and facts as durable structured knowledge
- validity windows
- provenance
- invalidation instead of destructive overwrite

That is extremely close to what a serious memory authority wants.

If the decision were based only on semantic fit, `Graphiti` would likely win.

### Custom Work Still Required

The custom work is not small:

- artifact registry and imported document discipline
- retrieval bundle shaping
- governance policy layer
- project-specific ontology and object naming
- operator inspection and review surfaces
- possibly a search projection later if document-heavy lexical retrieval matters more

`Graphiti` gives you the strongest knowledge substrate, but it does not remove the need for a real application layer around it.

### Long-Term Migration Risk

This is lower than `Mem0` **if** you are willing to accept graph-first durable memory.

It is higher than `Mem0` if you suspect you will later want a flatter non-graph authority model.

That is why the risk here is `low-medium`, not simply low.

You are buying into a real worldview.

It is a good worldview, but it is a worldview.

### Stored Data Model Evolvability

This is where `Graphiti` shines.

Episodes, facts, provenance, and temporal invalidation are all rich enough to grow forward.

You are unlikely to hit an early "this data shape was too cheap" wall.

The bigger risk is not data poverty.

The bigger risk is graph complexity.

### Path Toward Final Cortex

`Graphiti` keeps you on a strong path toward the final Cortex direction if you accept:

- graph-first truth
- projected views for simpler retrieval surfaces later

That is a defensible architecture.

It is not the easiest architecture.

### Why It Does Not Rank First

It loses on one-builder cost.

For one builder, the problem is not that `Graphiti` is wrong.

The problem is that:

- graph modeling is harder
- graph debugging is harder
- graph operations are heavier
- artifact and document handling still remain yours

That combination makes it a better long-term knowledge substrate than a practical first anchor for most solo builds.

## Contender 3: Letta

### Memory Authority Fit

`Letta` is compelling, but under this decision lens it is the weakest of the three finalists.

It is strongest when you want:

- a long-running personal agent
- editable memory blocks
- archival memory
- sleep-time reflection
- stateful behavior over time

Those are real strengths.

But they are not the same thing as a clean, evolvable, standalone memory authority.

### Custom Work Still Required

To make `Letta` the Cortex anchor, you would still need:

- a cleaner canonical object layer
- stronger artifact and provenance handling
- a clearer separation between working memory and durable knowledge
- more disciplined retrieval bundle shaping

At that point, you are bending `Letta` away from its natural center of gravity.

### Long-Term Migration Risk

This is the biggest reason it ranks third.

The memory model is entangled with runtime agent behavior:

- memory blocks
- archival memory
- sleep-time background editing
- conversation search

That is excellent for a personal agent shell.

It is not ideal as the long-term anchor for a system that wants a memory authority layer to stand apart from runtime.

### Stored Data Model Evolvability

`Letta`'s model is evolvable enough for personal continuity.

It is less evolvable for a future Cortex authority because the abstraction boundary is less clean.

You are more likely to later split storage and runtime apart.

That makes migration risk meaningfully higher than with `Mem0` or `Graphiti`.

### Path Toward Final Cortex

`Letta` can get you to a very satisfying personal assistant.

It is less convincing as the single anchor for final Cortex.

That is why it remains a finalist but not the recommendation.

## Wildcard: Weaviate-First Custom Build

### Why It Is Included

`Weaviate` deserves to stay in the field because it is the strongest storage-native alternative if you do **not** want your long-term store to feel like "vectors plus payloads."

It brings:

- local and free deployment
- object-plus-vector storage
- hybrid search
- filter-first retrieval
- richer schema than most vector engines
- a more believable long-term substrate if you later tighten Cortex semantics around it

### Why It Is Not A Primary Foundation Winner

Like `Qdrant`, `Weaviate` is still infrastructure rather than a memory platform.

It does not give you:

- memory extraction policy
- update or contradiction rules
- evidence-to-memory merge logic
- artifact lifecycle
- maintenance loops
- memory authority semantics

So a `Weaviate`-first route is also effectively:

"build custom Cortex now, using Weaviate as the first durable store"

That is a better long-term storage posture than `Qdrant`.

It is still not the best answer to the primary foundation question because it fails the same authority-layer test.

### When Weaviate Is The Right Call

`Weaviate` is the right move if you decide:

- you want to own the memory logic yourself
- you care about lower future storage reshaping risk than `Qdrant`
- you still want a local single-node system with strong hybrid and filtering support

If you reject all external memory platforms and want the cleanest storage substrate for a custom layer, `Weaviate` is the best such option reviewed so far.

## Wildcard: Neo4j-First Custom Build

### Why It Is Included

`Neo4j` deserves to stay in the field because it is a materially better long-term wildcard than `Qdrant` if your memory model cares about:

- explicit links
- provenance
- contradiction and supersession
- graph traversal

It gives you:

- local and free Community Edition
- strong graph modeling
- Cypher queries
- full-text indexes
- vector indexes
- a believable long-term home for knowledge objects, artifacts, and evidence relationships

### Why It Is Not A Primary Foundation Winner

`Neo4j` is still infrastructure, not a memory platform.

It does not give you:

- extraction logic
- merge policy
- Dream-like maintenance
- artifact lifecycle
- authority semantics

It also asks more from one builder than `Weaviate`:

- more graph modeling
- more manual retrieval fusion
- more query design

### When Neo4j Is The Right Call

`Neo4j` is the right move if you decide:

- the final durable model should be graph-first
- you are comfortable building more memory behavior yourself
- you care more about relationship richness than fastest first retrieval

The most important practical note is this:

if what attracts you to `Neo4j` is graph-native memory authority, the better move is usually `Graphiti on Neo4j`, not raw Neo4j alone.

## Wildcard: Qdrant-First Custom Build

### Why It Is Included

`Qdrant` was explicitly requested as an option, and it does deserve a fair look.

It brings:

- local and free deployment
- local mode and on-disk mode
- payload filtering
- hybrid search support
- good developer ergonomics
- strong performance for vector retrieval

Those are all real advantages.

### Why It Is Not A Primary Foundation Winner

`Qdrant` is still a storage and retrieval engine, not a memory platform.

It does not give you:

- memory formation policy
- update or merge logic
- contradiction handling
- provenance discipline
- artifact model
- authority semantics

So a `Qdrant`-first route is effectively:

"build custom Cortex now, using Qdrant as the first store"

That is a legitimate route.

It is not the best answer to this specific decision because it fails the "memory authority layer, not just retrieval subsystem" test.

### When Qdrant Is The Right Call

`Qdrant` is the right move only if you decide:

- you trust your own service layer more than any existing memory framework
- you want the simplest possible local search engine
- you are comfortable building the memory logic yourself immediately

That is a real option.

It is just not the best external primary foundation.

## Why memU Is Out

`memU` is out because the combined criteria should keep it out.

Even after the optimistic pass, the remaining issues still matter too much for this decision:

- category-first worldview
- placeholder merge stage
- lower maturity than the stronger contenders
- too much fork pressure before the system becomes truly useful

That does **not** mean it is useless.

It does mean it should not be the final recommendation for the primary Cortex anchor.

## Blunt Recommendation

### Best Primary Foundation

**Choose `Mem0 OSS` as the primary foundation.**

### Why

It is the best overall compromise between:

- fast path to something usable
- low one-builder burden
- real memory-engine behavior
- local and free deployment
- enough evolvability to avoid an early total rewrite

`Graphiti` is structurally richer, but too heavy as the first anchor for one builder.

`Letta` is more of a runtime shell than a clean authority anchor.

`Qdrant` is a strong store, not a memory platform.

### Minimal Supporting Pieces To Accept In Phase 1

If you choose `Mem0`, the minimum acceptable supporting pieces are:

1. `Weaviate` as the durable local store
2. local filesystem storage for raw imported artifacts
3. one model endpoint for extraction and embeddings

For the model endpoint:

- use `Ollama` if fully local matters more than quality
- use a stronger remote API temporarily if fast initial quality matters more than strict locality

If you want the absolute simplest local start, `Qdrant` can replace `Weaviate` in phase 1.

I would only do that if you consciously accept a slightly higher chance of future storage reshaping.

### What Still Needs To Be Custom Built

Even with `Mem0` as the base, Cortex still needs custom work for:

- artifact identity and import bookkeeping
- provenance schema and source references
- canonical knowledge-object contract
- governance fields and retrieval traces
- bounded bundle assembly
- stronger merge and retirement policies
- typed retrieval signals if you still want them later
- Dream or maintenance loops

### Practical Translation

Use `Mem0` as the engine.

Do **not** let `Mem0` define the final Cortex vocabulary.

Define the Cortex contract early, keep the stored metadata disciplined, and treat the base platform as the memory machine you are gradually civilizing into the final system.

## Related Docs

- [Solo Foundation Decision: Optimistic Contender Deep Dive](solo-foundation-optimistic-contenders-deep-dive.md)
- [Solo Foundation Decision: Top 3 Options](solo-foundation-top-3-decision.md)
- [LlamaIndex Cortex Fit Analysis](../reference/llamaindex-cortex-fit-analysis.md)
- [Neo4j Cortex Fit Analysis](../reference/neo4j-cortex-fit-analysis.md)
- [Weaviate Cortex Fit Analysis](../reference/weaviate-cortex-fit-analysis.md)
- [Architecture](../remram-cortex/architecture.md)

## Sources

- `Mem0` features overview: https://docs.mem0.ai/open-source/features/overview
- `Mem0` repo: https://github.com/mem0ai/mem0
- `Mem0` memory engine: https://github.com/mem0ai/mem0/blob/main/mem0/memory/main.py
- `Mem0` history storage: https://github.com/mem0ai/mem0/blob/main/mem0/memory/storage.py
- `Mem0` OpenSearch vector store: https://github.com/mem0ai/mem0/blob/main/mem0/vector_stores/opensearch.py
- `Mem0` Weaviate vector store: https://github.com/mem0ai/mem0/blob/main/mem0/vector_stores/weaviate.py
- `Graphiti` repo: https://github.com/getzep/graphiti
- `Graphiti` README: https://github.com/getzep/graphiti/blob/main/README.md
- `Graphiti` MCP server README: https://github.com/getzep/graphiti/blob/main/mcp_server/README.md
- `Graphiti` paper: https://arxiv.org/abs/2501.13956
- `Letta` context engineering guide: https://docs.letta.com/guides/agents/context-engineering
- `Letta` Docker docs: https://docs.letta.com/letta-code/docker
- `Letta` RAG overview: https://docs.letta.com/tutorials/rag-overview/
- `Letta` repo: https://github.com/letta-ai/letta
- `Neo4j` Community Edition: https://neo4j.com/product/community-edition/
- `Neo4j` Docker intro: https://neo4j.com/docs/operations-manual/current/docker/introduction/
- `Neo4j` vector indexes: https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/
- `Neo4j` full-text indexes: https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/full-text-indexes/
- `Weaviate` docs: https://docs.weaviate.io/weaviate
- `Weaviate` Docker installation: https://docs.weaviate.io/deploy/installation-guides/docker-installation
- `Weaviate` search concepts: https://docs.weaviate.io/weaviate/concepts/search
- `Qdrant` docs: https://qdrant.tech/documentation/
- `Qdrant` payload docs: https://qdrant.tech/documentation/concepts/payload/
- `Qdrant` local mode docs: https://qdrant.tech/documentation/frameworks/langchain/
- `Qdrant` hybrid search tutorial: https://qdrant.tech/documentation/tutorials-search-engineering/hybrid-search-fastembed/
