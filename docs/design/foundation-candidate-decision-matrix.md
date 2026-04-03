# Foundation Candidate Decision Matrix

## Purpose

This memo consolidates the current contender field into one ranked decision matrix.

It is meant to answer two practical questions:

1. Which two candidates are worth a real deep dive next?
2. How do the researched candidates compare when scored against the clarified Cortex decision lens?

Reviewed on `April 2, 2026`.

## Scope

This is a matrix for the **primary foundation candidates** and the most relevant storage-first wildcards we have already researched.

It does **not** score `OpenClaw` separately because `OpenClaw` is best treated as the runtime shell, not the long-term memory authority.

It also intentionally leaves out:

- `memU`, because it already failed the optimistic fork test
- `LlamaIndex`, because it remained more useful around Cortex than under Cortex

## Short Answer

Under the original weighting in this memo, the two I would deep dive next are:

1. `Mem0`
2. `Graphiti`

Why these two:

- `Mem0` is the best practical build path
- `Graphiti` is the best long-term authority fit

If you want one speed-oriented spike and one architecture-oriented spike, that pair gives the cleanest contrast.

If you want a third wildcard after that, it should be `Cognee`.

Important correction:

- if we assume a strong AI-assisted build loop, then implementation burden matters less than in a normal one-builder analysis
- under that adjusted lens, `Graphiti` becomes more attractive and can reasonably move into the number-one slot

## Recommended Deep-Dive Shapes

Do not deep dive the products in their weakest posture.

Use these shapes:

| Candidate | Deep-dive shape |
| --- | --- |
| `Mem0` | `Mem0 + OpenClaw`, with `Weaviate` or `Qdrant` behind it depending whether you optimize for long-term storage semantics or fastest start |
| `Graphiti` | `Graphiti + Neo4j + OpenClaw` |
| `Cognee` | `Cognee + Postgres/pgvector + Neo4j + Redis` |

## Decision Lens

Scores are `1-10`, where higher is better.

The weights are aligned to your current priorities:

| Criterion | Weight | Meaning |
| --- | --- | --- |
| Memory authority fit | `30%` | How naturally the platform can act as the durable authority layer |
| Replatform safety | `20%` | Lowest likelihood that stored data has to be rebuilt later |
| One-builder burden | `15%` | How survivable the implementation is for one builder using AI heavily |
| Time to first usable system | `15%` | How quickly it can become meaningfully useful |
| Stored model evolvability | `10%` | How well the stored model can grow toward Cortex |
| Integration leverage | `10%` | Existing runtime, API, MCP, plugin, and tooling seams |

Important note:

- these are comparative architecture scores, not benchmark measurements
- the matrix is meant to clarify tradeoffs, not simulate false precision

## AI-Building Adjustment

The base matrix still assumes that implementation burden and time-to-first-usable matter a lot.

Your correction is valid:

- in an AI-heavy build loop, custom implementation is cheaper than in a traditional solo build

That does **not** remove the importance of operational complexity, but it does reduce the penalty on contenders that are architecturally stronger and merely harder to wire together.

Under that adjusted lens, the weights shift roughly like this:

| Criterion | Base Weight | AI-Building Weight |
| --- | --- | --- |
| Memory authority fit | `30%` | `35%` |
| Replatform safety | `20%` | `25%` |
| One-builder burden | `15%` | `10%` |
| Time to first usable system | `15%` | `10%` |
| Stored model evolvability | `10%` | `15%` |
| Integration leverage | `10%` | `5%` |

That shifts the top of the field.

## AI-Building Ranking

If we score the same field with the AI-building weights above, the ranking becomes:

| Rank | Candidate | AI-Building Read |
| --- | --- | --- |
| 1 | `Graphiti` | Best long-term authority fit once custom build cost is discounted |
| 2 | `Mem0` | Still the best practical accelerator, but no longer clearly ahead of Graphiti |
| 3 | `Cognee` | Benefits from the reduced penalty on complexity, but still remains less clean than Graphiti |
| 4 | `Letta` | Still runtime-strong, still authority-weaker |
| 5 | `Neo4j`-first custom | Gains value when custom graph work is less scary |
| 6 | `Weaviate`-first custom | Still a strong storage route, but not enough authority semantics on its own |
| 7 | `Qdrant`-first custom | Still primarily a retrieval substrate |

So the practical interpretation is:

- normal solo-builder lens: `Mem0` slightly ahead of `Graphiti`
- AI-builder lens: `Graphiti` slightly ahead of `Mem0`

The top two do **not** change.

What changes is:

- which one should be considered the default favorite

## Weighted Matrix

| Rank | Candidate | Authority Fit | Replatform Safety | Builder Burden | Time To Usable | Model Evolvability | Integration Leverage | Weighted Score | Why It Lands Here |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `Mem0` | `8` | `7` | `8` | `9` | `7` | `10` | `8.1` | Best practical balance; strongest shipped path to something useful without obviously poisoning the long-term direction |
| 2 | `Graphiti` | `10` | `9` | `5` | `6` | `9` | `6` | `8.0` | Best semantic authority fit and lowest data-model regret risk; loses only on solo-builder friction |
| 3 | `Cognee` | `7` | `7` | `6` | `6` | `7` | `8` | `6.8` | Serious wildcard with real lifecycle and extension seams, but a less clean canonical authority than Graphiti and a heavier multi-store posture than Mem0 |
| 4 | `Letta` | `6` | `6` | `7` | `8` | `6` | `6` | `6.5` | Great personal-agent runtime and reflective behavior, but memory remains too entangled with runtime context management |
| 5 | `Weaviate`-first custom | `4` | `7` | `5` | `6` | `8` | `5` | `5.9` | Strongest storage-first custom route if you want to own the memory logic yourself |
| 6 | `Neo4j`-first custom | `5` | `8` | `3` | `4` | `8` | `4` | `5.4` | Strong graph-native substrate, but too much memory-engine work still sits above it |
| 7 | `Qdrant`-first custom | `3` | `5` | `6` | `7` | `5` | `6` | `5.0` | Fast and practical retrieval substrate, but not a convincing long-term authority anchor on its own |

## Why `Mem0` And `Graphiti` Are The Top Two

### `Mem0`: Best Practical Start

`Mem0` wins the real-world starting decision because it combines:

- the fastest credible path to a useful system
- an actual memory engine rather than a raw storage layer
- official OpenClaw integration
- survivable long-term evolution if we impose discipline early

What it does **not** win:

- the cleanest canonical authority model
- the strongest provenance and temporal semantics

That is why it wins as the best practical start, not as the purest end-state substrate.

### `Graphiti`: Best Long-Term Authority Fit

`Graphiti` wins the end-state argument because it already has:

- episodes as evidence
- facts as durable graph objects
- temporal validity and invalidation
- provenance lineage
- graph-aware retrieval and maintenance primitives

What it does **not** win:

- easiest integration
- fastest path to first usefulness
- lowest operations burden

That is why it lands second in the weighted matrix but still remains one of the two required deep dives.

Under the AI-building lens, this is the contender that benefits the most.

## Why `Cognee` Is Third, Not Top Two

`Cognee` became much more credible once we evaluated it on its strongest external-service posture.

Its advantages are real:

- `add -> cognify -> memify -> search` is a real lifecycle
- graph plus vector plus relational split is serious
- datasets, sessions, permissions, and NodeSets are useful scoping primitives
- official API, MCP, and OpenClaw surface area exist

But it still falls behind the top two because:

- its authority model is more pipeline-shaped than canonical-object-shaped
- its strongest posture is multi-store and therefore heavier
- self-hosted `Neo4j` dataset-routing looks rougher than the docs initially suggest
- its temporal and correction semantics still look weaker than `Graphiti`

So `Cognee` is a very good third deep dive, not the first or second.

## Best Candidate By Question

| Question | Winner | Why |
| --- | --- | --- |
| Best path to a useful system fast | `Mem0` | Memory behavior is already shipped and OpenClaw integration already exists |
| Best long-term memory authority fit | `Graphiti` | Strongest evidence, fact, provenance, and temporal structure |
| Best wildcard | `Cognee` | Real lifecycle engine plus serious dockerized external-store posture |
| Best storage-first custom route | `Weaviate` | Strongest object-plus-search substrate if we build the memory layer ourselves |
| Best graph substrate if you insist on graph-first from scratch | `Neo4j` | Richest raw graph representation, but too much still needs to be built |
| Best fast retrieval substrate | `Qdrant` | Very practical, but not enough authority semantics on its own |

## Blunt Recommendation

If you are choosing the **two** to go deep on, choose:

1. `Mem0`
2. `Graphiti`

If you want the recommendation restated under the **AI-building** lens, then I would phrase it this way:

1. `Graphiti`
2. `Mem0`

If you only have time for **one** deep dive:

- choose `Mem0` if you want the highest chance of reaching a usable system quickly
- choose `Graphiti` if you care more about the long-term memory model than the shortest path to a usable prototype

If you do a **third** after those:

- choose `Cognee`

That gives you the cleanest coverage of the actual decision space:

- fastest practical path
- strongest end-state authority fit
- strongest wildcard platform

## Supporting Docs

- [Primary Foundation Decision: Realigned](primary-foundation-decision-realigned.md)
- [Mem0 + OpenClaw Lifecycle Architecture](mem0-openclaw-lifecycle-architecture.md)
- [Mem0 + Weaviate + OpenClaw Lifecycle Architecture](mem0-weaviate-openclaw-lifecycle-architecture.md)
- [Graphiti + Neo4j + OpenClaw Lifecycle Architecture](graphiti-neo4j-openclaw-lifecycle-architecture.md)
- [Cognee Cortex Fit Analysis](../reference/cognee-cortex-fit-analysis.md)
- [Neo4j Cortex Fit Analysis](../reference/neo4j-cortex-fit-analysis.md)
- [Weaviate Cortex Fit Analysis](../reference/weaviate-cortex-fit-analysis.md)

## External Sources

- https://docs.mem0.ai/open-source/overview
- https://docs.mem0.ai/integrations/openclaw
- https://help.getzep.com/graphiti/graphiti/overview
- https://docs.letta.com/guides/core-concepts/memory/memory-blocks
- https://docs.letta.com/guides/core-concepts/memory/archival-memory
- https://docs.cognee.ai/setup-configuration/overview
- https://docs.cognee.ai/core-concepts/main-operations/memify
- https://qdrant.tech/documentation/overview/
- https://docs.weaviate.io/weaviate/concepts/search/hybrid-search
