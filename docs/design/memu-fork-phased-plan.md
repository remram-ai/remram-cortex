# memU Fork Phased Plan

## Purpose

This document describes a practical phased path if `remram-cortex` deliberately chose to fork `memU`.

It assumes the goal is not to keep stock memU semantics forever.

The goal is to use memU as the starting skeleton and evolve it toward Cortex while staying honest about:

- temporary compromises
- extension cost
- where we are diverging from upstream
- what can still be contributed back

## Planning Rule

Each phase must answer one question:

"Are we still extending memU, or have we crossed into replacing its core assumptions?"

That line matters because once too many core assumptions change, the fork loses most of the benefit of having started from memU.

## Architectural Guardrails

To stay architecturally consistent with Cortex, the fork should protect these guardrails from the beginning even when the implementation is incomplete:

1. durable truth must converge toward enriched item or object records, not categories
2. source artifacts must converge toward stable Cortex-owned identity
3. retrieval must converge toward governance-first bounded bundles
4. categories may assist, but must not become the authority layer
5. vectors may assist, but must not become the truth layer

## Phase 0: Stock memU Baseline

### Goal

Get a real working system with minimal divergence.

### Keep As-Is

- `Resource`, `MemoryItem`, `MemoryCategory`, `CategoryItem`
- `memorize(...)`
- `retrieve(...)`
- patch and CRUD workflows
- local OpenAI wrapper integration
- SQLite or Postgres backends
- multimodal preprocess path

### Cortex Interpretation

- `Resource` = proto-artifact
- `MemoryItem` = proto-knowledge-object
- `MemoryCategory` = proto-derived view

### Compromises

- accept category-first retrieval temporarily
- accept weak provenance temporarily
- accept no Dream
- accept Postgres or SQLite instead of OpenSearch

### Exit Criteria

- stock memU runs on a small Cortex seed corpus
- we document what works well and what feels structurally wrong

## Phase 1: Cortex Metadata Overlay

### Goal

Extend existing memU records with Cortex-critical metadata without yet rewriting retrieval.

### Extend `Resource`

Add fields or `extra` content for:

- `artifact_id`
- `provider`
- `authority_mode`
- `source_uri`
- `source_ref`
- `artifact_kind`
- `artifact_class`
- `original_name`
- `media_type`

### Extend `MemoryItem`

Add fields or `extra` content for:

- `canonical_statement`
- `object_kind`
- `confidence`
- `freshness_ts`
- `reinforcement_count`
- provenance tuples
- typed links
- promotion state

### Extend Scope Model

Use memU's scope mechanism to add Cortex-like governance fields such as:

- `owner_ref`
- `knowledge_space`
- `lifecycle_state`

Potentially defer more complex multi-valued visibility fields until later.

### Keep

- stock retrieval order
- category summaries
- current ingestion flow

### Compromises

- many Cortex semantics still live in `extra`
- retrieval is still not truly typed-signal-first

### Exit Criteria

- one imported artifact can be traced through stable artifact metadata into enriched items
- quick-capture-like patch or item creation carries the same governance metadata

## Phase 2: Reflection Upgrade

### Goal

Turn memU's placeholder merge stage into real Cortex-style reflection.

### Key Change

Replace pass-through `dedupe_merge` with a merge-decision stage that can:

- reinforce
- refine
- relate
- create
- supersede
- contradict

### Additions

- provenance-key idempotency
- canonical statement update rules
- structured delta logs
- richer item mutation discipline

### What Stays MemU-Like

- workflow-step orchestration
- database repositories
- resource ingestion pipeline

### What Starts Diverging

- extraction prompts become Cortex-oriented
- memory mutation becomes much more structured

### Exit Criteria

- duplicate captures reinforce existing items instead of producing obvious noise
- imported evidence and direct captures follow the same durable item path

## Phase 3: Retrieval Rebalance

### Goal

Move from memU's category-first retrieval toward Cortex-style bounded retrieval without fully discarding categories.

### Retrieval Shift

From:

- query rewrite
- category recall
- item recall
- resource recall

Toward:

- governance filter
- item or object recall
- typed-signal and text scoring
- vector assist
- relationship expansion
- bounded bundle assembly

### Categories In This Phase

Categories remain allowed as:

- priors
- fallback summaries
- continuity summaries
- operator inspection surfaces

But categories stop being the main semantic center.

### Required New Surfaces

- retrieval trace object
- bounded bundle shape
- signal-aware scoring
- signature-aware biasing

### Compromises

- categories may still be queried for continuity or compression
- lexical retrieval may still be imperfect if typed fields are not fully normalized yet

### Exit Criteria

- imported and captured knowledge come from one unified item or object pool
- retrieval returns bundles, not just loose category/item/resource lists
- traces explain filters and scoring contributors

## Phase 4: Typed Signals And Semantic Signature

### Goal

Introduce the most Cortex-specific retrieval surfaces.

### Add To `MemoryItem`

- `domain[]`
- `activity[]`
- `need[]`
- `object[]`
- `mechanism[]`
- `semantic_signature`

### Retrieval Behavior

- governance filters first
- typed fields become primary scoring surface
- signature becomes routing bias
- embeddings remain assistive

### Implementation Options

Option A:

- keep Postgres and implement lexical plus vector behavior there first

Option B:

- dual-write into OpenSearch for retrieval while Postgres remains the system of record

Option C:

- implement an OpenSearch backend for the memU repository layer

### Recommendation Inside The Fork

Option A first, then B if needed.

Reason:

- Option C is the cleanest long-term abstraction answer
- but it gives up too much of the practical acceleration of starting from memU

### Exit Criteria

- at least one concept is rediscoverable from multiple phrasings through typed fields
- signature bias exists and is inspectable

## Phase 5: Artifact Provider Model

### Goal

Turn proto-artifacts into a real artifact-provider boundary.

### Add

- provider adapters
- stable artifact resolution
- Cortex-owned identity independent of original source path
- version and retention metadata

### Transitional Shortcut

Use local filesystem or Git-backed provider first.

### What This Unlocks

- stronger provenance
- better imports
- promotion path later
- external-source drift tolerance

### Exit Criteria

- artifact can be moved or renamed externally without losing Cortex identity
- provenance lookup remains stable by artifact ID

## Phase 6: Dream And Promotion

### Goal

Add the Cortex layers that memU does not currently have.

### Dream Responsibilities

- cross-item deduplication
- contradiction surfacing
- signal normalization
- principle formation
- stale-memory decay
- promotion candidate detection

### Promotion Responsibilities

- render high-value stabilized knowledge into durable artifacts
- preserve linkage back to source items and artifacts

### What This Means For The Fork

At this point the fork is no longer "mostly stock memU."

It is a distinctly Cortex-shaped system still carrying memU infrastructure DNA.

### Exit Criteria

- retrieval quality improves because Dream exists, not because prompts became heavier
- high-value knowledge can be promoted into durable reviewable artifacts

## OpenSearch Decision Point

This needs to be explicit because it is the biggest roadmap fork.

### Option 1: Relax OpenSearch For Early Phases

Use Postgres plus `pgvector` first.

Pros:

- stays closest to memU
- fastest path to running system
- least rewrite upfront

Cons:

- diverges from current `remram-cortex` MVP dependency posture
- later migration cost

### Option 2: Add OpenSearch As Side Index

Keep memU storage but dual-write retrieval surfaces into OpenSearch.

Pros:

- preserves more of the current Cortex roadmap
- avoids fully replacing memU storage layer

Cons:

- more operational complexity
- two truth-like stores unless carefully governed

### Option 3: Rebuild memU Around OpenSearch

Implement a new backend or rewrite repository assumptions.

Pros:

- closer to current Cortex architecture

Cons:

- rapidly destroys the point of starting from memU

### Recommended Decision

If we truly fork memU, choose Option 1 first.

If OpenSearch is non-negotiable from the outset, the project should seriously question whether "fork memU" is still the most effective strategy.

## Acceptable Requirement Relaxations

These are the relaxations that still preserve the spirit of Cortex:

- OpenSearch is deferred, not abandoned
- categories remain as transitional derived surfaces
- provenance starts shallow and becomes structured later
- typed signals start in `extra` and become first-class later
- Dream arrives after reflection and retrieval are real

## Requirement Relaxations That Are Not Acceptable

These would break architectural consistency:

- categories remain the long-term truth surface
- vectors remain the long-term primary truth surface
- source path remains the durable artifact identity
- governance is treated as a soft hint rather than a hard gate
- provenance never goes beyond `resource_id`
- no Dream or promotion layer is ever planned

## Upstream Contribution Lanes

The more we want to contribute back, the more we should separate:

- general memU improvements
- Cortex-specific philosophy

Likely upstreamable:

- better dedupe and merge hooks
- trace and observability improvements
- richer artifact metadata
- item-reference and provenance utilities
- item-first optional retrieval modes

Likely fork-only:

- typed signal schema
- semantic signature
- Dream cycle
- promotion layer
- Cortex authority model

## Final Recommendation

The optimistic path is real, but only under a disciplined reading:

Fork memU if the objective is to accelerate from a working memory skeleton and you are willing to phase Cortex purity in over time.

Do not fork memU if the objective is to preserve every current Cortex architectural choice from day one, especially:

- OpenSearch-first substrate
- category-free authority model
- rich provenance from the first operational cut

The honest recommendation is:

- a memU fork is viable
- it can probably achieve most Cortex goals eventually
- it requires temporary compromises that must be written down explicitly
- the biggest real decision is whether we are willing to defer or relax OpenSearch early

## Related Docs

- [memU Fork Feasibility](../reference/memu-fork-feasibility.md)
- [memU Gap Analysis](../reference/memu-gap-analysis.md)
- [memU Spike Evaluation](memu-spike-evaluation.md)
- [memU Fork Storage Decision: Postgres vs OpenSearch](memu-postgres-vs-opensearch-decision.md)
- [Cortex Architecture](../remram-cortex/architecture.md)
