# memU Gap Analysis

## Source

- Repo: https://github.com/NevaMind-AI/memU
- Reviewed on: 2026-04-01
- Primary upstream references reviewed:
  - README: https://github.com/NevaMind-AI/memU/blob/main/README.md
  - Local architecture note: https://github.com/NevaMind-AI/memU/blob/main/docs/architecture.md
  - ADR 0001 workflow pipelines: https://github.com/NevaMind-AI/memU/blob/main/docs/adr/0001-workflow-pipeline-architecture.md
  - ADR 0002 storage and vector strategy: https://github.com/NevaMind-AI/memU/blob/main/docs/adr/0002-pluggable-storage-and-vector-strategy.md
  - ADR 0003 scoped data model: https://github.com/NevaMind-AI/memU/blob/main/docs/adr/0003-user-scope-in-data-model.md
  - Core runtime files:
    - https://github.com/NevaMind-AI/memU/blob/main/src/memu/app/service.py
    - https://github.com/NevaMind-AI/memU/blob/main/src/memu/app/memorize.py
    - https://github.com/NevaMind-AI/memU/blob/main/src/memu/app/retrieve.py
    - https://github.com/NevaMind-AI/memU/blob/main/src/memu/database/models.py

## Why This Reference Matters

memU is one of the few open memory projects that is:

- actively maintained
- self-hostable
- multimodal
- scoped for long-running agents
- explicit about agent memory rather than generic chat history

That makes it worth studying for Cortex even though the architectural center of gravity is different.

As viewed on 2026-04-01, the repo showed:

- 13.3k stars
- 984 forks
- 287 commits
- 24 releases
- latest release `v1.5.1` dated 2026-03-23
- 61 open issues
- 32 open pull requests

That is enough activity to treat it as a real implementation reference rather than a dead experiment.

## memU In One Page

memU's local runtime is a Python package centered on `MemoryService`.

Its durable model is three main layers plus one relation edge:

- `Resource`: source artifact record
- `MemoryItem`: extracted memory summary with embedding
- `MemoryCategory`: grouped topic summary
- `CategoryItem`: item-to-category link

Its main write path is `memorize(...)`:

1. fetch resource
2. preprocess multimodal input
3. extract memory entries with LLM prompts
4. run a placeholder `dedupe_merge` step
5. persist resources, items, and category links
6. update category summaries

Its main read path is `retrieve(...)`:

1. decide whether retrieval is needed
2. optionally rewrite the query
3. search categories
4. search items
5. search resources
6. optionally stop early through sufficiency checks

The storage backends are:

- in-memory
- SQLite with brute-force vector search
- Postgres with optional `pgvector`

The scope model is flexible and first-class. `user_id` or other configured scope fields are merged into every stored entity and reused by `where` filters across write and read paths.

## Where memU Aligns With Cortex

### 1. It treats memory as a real system concern

memU is not just "append chat history and hope." It has explicit ingestion, extraction, retrieval, persistence, and integration surfaces. That matches the broad Cortex instinct in [overview.md](../overview/overview.md) and [architecture.md](../remram-cortex/architecture.md).

### 2. It has a practical self-hosted developer loop

The project already ships:

- local storage options
- tests
- examples
- release cadence
- contributor workflow

That is useful because Cortex is still documentation-first.

### 3. It has a clean workflow-pipeline pattern

The workflow-step architecture, pipeline manager, and interceptor model are solid implementation references for:

- staged ingestion
- staged retrieval
- observability hooks
- low-risk extension points

This is one of the clearest "borrow the pattern, not the product" opportunities.

### 4. It has a usable reinforcement idea

memU already models reinforcement count and recency-aware salience. Cortex also expects reinforcement metadata. memU's salience scoring is simpler than the Cortex design, but it is a credible implementation reference for early ranking heuristics.

### 5. It validates scoped memory as a first-class concern

The scoped data model is genuinely relevant to Cortex because Cortex governance also needs hard ownership and visibility boundaries before semantic ranking begins.

## Where memU Diverges Hard From Cortex

### 1. Canonical memory model

Cortex centers memory on canonical knowledge objects with:

- governance fields
- typed signals
- semantic signature
- explicit provenance
- typed links
- retention and promotion state

memU centers memory on:

- resource records
- item summaries
- category summaries

That is a real architectural mismatch, not a naming difference.

`MemoryItem` in memU is too thin to be a Cortex knowledge object. It has:

- `resource_id`
- `memory_type`
- `summary`
- `embedding`
- `happened_at`
- free-form `extra`

That is useful, but it is not the same as the Cortex object described in [knowledge-object.md](../concepts/knowledge-object.md).

### 2. Bucket-first pressure

Cortex explicitly rejects bucket-first canonical storage. One object should have many retrieval paths.

memU uses categories as a first-class memory layer and as a primary retrieval stage. That pushes the system toward topic buckets and summary folders. Cortex can derive views later, but it does not want categories to become the authority surface.

### 3. Retrieval semantics

Cortex retrieval is:

1. governance filter
2. semantic signature bias
3. typed signal scoring
4. lexical grounding
5. vector assist
6. relationship expansion
7. bounded bundle plus trace

memU retrieval is closer to:

1. query rewrite and intention routing
2. category similarity
3. item similarity
4. resource similarity
5. optional LLM sufficiency checks

That is a much more vector-centric and query-time-intelligence-centric model than the Cortex retrieval rules in [bounded-retrieval.md](../concepts/bounded-retrieval.md) and [product/capabilities/retrieval/spec.md](../../product/capabilities/retrieval/spec.md).

### 4. Write-time intelligence versus read-time intelligence

Cortex wants Reflection and Dream to do the hard work so retrieval stays cheap and predictable.

memU already does some write-time extraction, but it still leans heavily on retrieval-time query rewriting, category staging, and sufficiency decisions. It does not implement the Cortex Reflection and Dream split.

The clearest signal of this gap is that `dedupe_merge` in `memorize.py` is still a placeholder, while Cortex treats merge discipline as a core memory-quality requirement.

### 5. Artifact identity and provider boundary

Cortex has a strong artifact model:

- stable internal `artifact_id`
- provider contract
- source-location provenance
- separation between evidence artifacts and promoted artifacts
- provider authority is never allowed to redefine memory authority

memU's `Resource` record is much lighter:

- URL
- modality
- local path
- caption
- embedding

That is fine for memU, but it does not satisfy the artifact-provider and provenance model in:

- [artifact-intake.md](../concepts/artifact-intake.md)
- [artifact-storage spec](../../product/capabilities/artifact-storage/spec.md)
- [v0.1 MVP spec](../design/v0_1-mvp-spec.md)

### 6. Provenance depth

Cortex wants source-linked slices with page, section, offset, frame, or similar location data where possible.

memU links items back to a `resource_id`, but it does not expose Cortex-level slice provenance as a first-class durable contract.

That means Cortex would still need to add a more exact provenance model even if memU were reused.

### 7. OpenSearch versus SQL plus pgvector

The current Cortex roadmap is built around OpenSearch as the retrieval substrate, including:

- index and alias bootstrap
- typed-signal lexical fields
- governance filters
- retrieval traces
- operator-facing service posture

memU is built around in-memory, SQLite, or Postgres storage with optional `pgvector`.

Adopting memU as the core engine would not be a small implementation substitution. It would invalidate or bypass the current OpenSearch dependency work under:

- [product/dependencies/opensearch-service/spec.md](../../product/dependencies/opensearch-service/spec.md)
- [projects/v0_1 MVP/epics/01-opensearch-service/opensearch-service-spec.md](../../projects/v0_1%20MVP/epics/01-opensearch-service/opensearch-service-spec.md)

### 8. Conversation continuity

Cortex keeps conversation continuity as a separate possible object type beside knowledge objects.

memU treats conversations as one more resource modality that yields items and categories. That is a simpler model, but it does not give Cortex the explicit continuity layer described in [conversation-layer.md](../concepts/conversation-layer.md).

### 9. Dream and promotion are missing

Dream is not a side feature in Cortex. It is the asynchronous reconciliation layer that:

- deduplicates
- resolves contradictions
- normalizes retrieval cues
- raises principles
- identifies promotion candidates

memU currently has reinforcement tracking and category summarization, but not the Dream-cycle model in [dream-cycle.md](../concepts/dream-cycle.md).

Artifact promotion is also outside memU's core model.

### 10. Product posture

memU's defaults clearly bias toward personal-assistant memory:

- personal info
- preferences
- relationships
- activities
- goals
- habits
- work life

That is not wrong, but it is a different product center than Cortex's project-scoped knowledge-authority model.

## Gap Matrix Against The Current Cortex MVP

| Area | Cortex MVP direction | memU current shape | Gap size |
| --- | --- | --- | --- |
| Core store | OpenSearch plus artifact-provider boundary | in-memory, SQLite, Postgres, `pgvector` | High |
| Durable unit | knowledge object | summary-based memory item plus category summary | High |
| Retrieval | governance-first, typed-signal-first, inspectable | category/item/resource recall with vector or LLM ranking | High |
| Artifact identity | stable internal artifact ID and provider contract | lightweight resource record | High |
| Provenance | source-linked slices and artifact linkage | resource linkage only | High |
| Merge discipline | Reflection decisions plus Dream cleanup | reinforcement and dedupe placeholder | High |
| Continuity | optional conversation object | conversation as resource modality | Medium |
| Promotion | explicit future artifact-promotion path | not core | High |
| Dev ergonomics | not implemented yet | strong | Low |
| Pipeline architecture | not implemented yet | strong | Low |
| Scope filtering | governance model | configurable scope fields | Medium |
| Reinforcement scoring | required metadata | salience and recency logic exists | Low |

## What memU Could Teach Cortex

The most valuable things to learn from memU are implementation patterns, not memory truth semantics.

Strong candidates:

- workflow pipelines and step interception
- profile-routed LLM and embedding clients
- scoped record model generation
- reinforcement and salience heuristics
- pragmatic self-hosted examples and tests
- fast local developer onboarding

These are all learnable without adopting memU's canonical data model.

## What Cortex Would Still Need Even If memU Were Reused

If Cortex tried to build on memU anyway, it would still need to add or rewrite:

- the knowledge-object contract
- typed signal fields
- semantic signature generation and scoring
- stable artifact-provider identity
- source-slice provenance
- OpenSearch integration and mappings
- retrieval-trace contract
- relationship expansion over typed links
- conversation-object handling
- Dream reconciliation
- artifact promotion

At that point, the fork would be rewriting the heart of the system rather than accelerating it.

## Roadmap Impact

Using memU as the Cortex foundation would materially disrupt the current roadmap.

### What It Would Break Or Reopen

- Epic 01 OpenSearch Service would stop being the central retrieval dependency.
- Retrieval design would shift from OpenSearch lexical plus governance plus typed signals to SQL or `pgvector`-centric recall.
- Artifact Storage and provider work would still remain because memU does not replace the Cortex provider contract.
- Knowledge Extraction would need a model translation layer or a rewrite of memU item generation.
- Retrieval would still need a redesign to match Cortex semantics.
- Dream and promotion would remain net-new epics.

### What It Would Not Save

memU does not eliminate the hard Cortex work around:

- knowledge authority
- provenance depth
- artifact semantics
- inspectable bounded retrieval
- promotion and reconciliation

The main thing it would save is implementation scaffolding.

## Option Review

### Try It And Learn

Yes.

This is the best fit.

Use memU as:

- a spike target
- a workflow-pattern reference
- a source of retrieval and reinforcement heuristics
- a benchmark for onboarding and developer UX

Do not treat it as the canonical Cortex architecture.

### Use It And Contribute

Not as the Cortex core.

There may be selective contribution opportunities if we want to upstream generic improvements such as:

- stronger provenance fields
- better trace or interceptor surfaces
- richer merge and dedupe stages
- more explicit scope patterns

But "use it and contribute" is not the right primary strategy for `remram-cortex`.

### Fork It And Evolve

Not now.

The license allows it and the repo is active enough that a fork is technically viable, but the architecture mismatch is too large. A fork would quickly become a deep rewrite across storage, retrieval, artifact semantics, and memory truth models.

Forking only makes sense if the goal is a short-lived prototype that is allowed to diverge permanently from upstream.

### Smile And Move On

Also no.

There is enough value here to justify study, especially around:

- pipeline architecture
- reinforcement heuristics
- self-hosted developer ergonomics
- integration wrappers

Ignoring it completely would leave useful implementation ideas on the table.

## Recommendation

Primary recommendation: try it and learn.

Operational translation for Cortex:

- keep the current Cortex architecture and MVP roadmap intact
- do not adopt memU as the base memory engine
- do not fork it for mainline Cortex work
- run a short bounded spike to harvest implementation patterns and UX lessons

That keeps the value and avoids importing a conflicting memory model.

## Suggested Next Step

If we spend time on memU at all, it should be a bounded spike against the current Cortex MVP corpus and not a roadmap pivot.

See [memu-spike-evaluation.md](../design/memu-spike-evaluation.md) for a concrete way to do that without destabilizing the current plan.
