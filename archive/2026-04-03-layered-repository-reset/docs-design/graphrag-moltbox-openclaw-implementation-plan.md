# GraphRAG on Moltbox to OpenClaw to Cortex Implementation Plan

## Purpose

This document is the full implementation plan for adopting `Microsoft GraphRAG` as a serious Cortex contender focused on durable artifact memory, corpus synthesis, and graph-shaped retrieval.

It covers the full path from:

- standing up the baseline GraphRAG architecture as dockerized `Moltbox` services
- connecting that stack to `OpenClaw`
- expanding the stack until it covers as much of the practical Cortex vision as GraphRAG can cover without turning into a custom rewrite

Reviewed on `April 2, 2026`.

## Blunt Read

`GraphRAG` is not the cleanest primary foundation for all of Cortex.

It is one of the strongest foundations for the document-memory slice of Cortex.

The right implementation posture is:

- stay close to stock GraphRAG in phase 1
- use built-in `LanceDB` instead of forcing an external vector database immediately
- package GraphRAG behind a thin facade service
- integrate OpenClaw primarily through a `contextEngine`
- treat all durable long-term memory as artifacts that GraphRAG can ingest
- accept coarse corpus partitioning early

Do not start by:

- forcing `OpenSearch` into phase 1
- building a parallel canonical memory database
- treating raw parquet outputs as an app-owned schema
- running a full GraphRAG indexing pass after every message

If the work is done in the right order, the first usable system is realistic in about `1 to 2 weeks` of focused AI-assisted implementation, and a credible "Cortex on GraphRAG" v1 is realistic in about `5 to 8 weeks`.

## Planning Assumptions

- One human builder, heavily AI-assisted.
- Local and free infrastructure is required.
- Dockerized services are preferred when they do not create unnecessary burden.
- Model APIs are allowed if they speed up progress.
- `OpenSearch` is a preference, not a hard requirement.
- `Dream` is not a gating selection criterion.

## Core Architectural Decision

Treat `GraphRAG` as the durable authority for long-term artifact memory.

Treat `OpenClaw` as the runtime shell and agent host.

Treat recent session history as hot runtime state, and treat post-turn or imported artifacts as the durable memory feed into GraphRAG.

That produces the cleanest shape:

```text
Channels / Agents / Tools
          |
          v
OpenClaw Gateway
  - runtime orchestration
  - session lifecycle
  - custom GraphRAG context engine
  - optional GraphRAG memory tools
          |
          v
GraphRAG Facade API
  - ingest normalized artifacts
  - run local / global / drift / basic query
  - generate follow-up questions
  - schedule update jobs
          |
          v
GraphRAG Workspace Volume
  - input/
  - prompts/
  - cache/
  - output parquet
  - LanceDB
          ^
          |
GraphRAG Index Worker
  - prompt-tune
  - index / update
  - standard vs fast
  - scheduled maintenance
```

## Guardrails

- `GraphRAG` is the only durable authority for long-term artifact memory.
- OpenClaw `MEMORY.md` and daily notes are not allowed to become the true long-term authority.
- Phase 1 durable memory is artifact-first: preferences, decisions, lessons, and summaries become tiny artifacts.
- One GraphRAG workspace serves one coarse trust or corpus boundary.
- Full fine-grained governance is deferred; coarse partitioning is the phase-1 answer.
- `fast` indexing is for iteration; `standard` indexing is for durable important corpora.
- `LanceDB` stays in phase 1 unless a concrete limitation appears.

## Phase 0: Validation Spike

Duration:

- `2 to 4 days`

Goal:

- prove that GraphRAG is valuable enough in your real corpora to justify the integration work

Tasks:

1. Create a small standalone GraphRAG workspace.
2. Run `graphrag init`.
3. Run `prompt-tune` on a representative sample.
4. Index one small corpus with `--method fast`.
5. Re-index the same corpus with `--method standard`.
6. Compare `Local`, `Global`, `DRIFT`, and `Basic`.
7. Inspect `documents`, `text_units`, `entities`, `relationships`, `communities`, and `community_reports`.

Exit criteria:

- at least one corpus produces useful `Global` and `Local` answers
- community reports feel materially better than plain vector search for synthesis questions

## Phase 1: Moltbox Baseline Deployment

Duration:

- `3 to 5 days`

Goal:

- stand up a dockerized GraphRAG baseline with separate containers aligned to Moltbox

Recommended containers:

### 1. `graphrag-api`

Responsibilities:

- expose a thin HTTP facade
- accept artifact ingestion requests
- expose query endpoints
- expose job trigger endpoints

Implementation note:

- this is a small custom Python `FastAPI` wrapper around GraphRAG library and CLI calls

### 2. `graphrag-indexer`

Responsibilities:

- run `prompt-tune`
- run `index`
- run `update`
- execute scheduled maintenance

### 3. `openclaw-gateway`

Responsibilities:

- host agents and channels
- load the future `openclaw-graphrag` plugin
- manage sessions, tools, hooks, and compaction

### 4. Shared `graphrag-workspace` volume

Contents:

- `input/`
- `output/`
- `prompts/`
- `cache/`
- `settings.yaml`
- `LanceDB`

What not to add in phase 1:

- no Redis
- no Postgres
- no OpenSearch
- no second durable memory system

## Phase 2: GraphRAG Facade Contract

Duration:

- `2 to 4 days`

Goal:

- stabilize the service boundary so OpenClaw integration is simple

Recommended API surface:

- `POST /ingest/artifact`
- `POST /ingest/batch`
- `POST /jobs/index`
- `POST /jobs/update`
- `POST /query/local`
- `POST /query/global`
- `POST /query/drift`
- `POST /query/basic`
- `POST /query/questions`

Request contract for ingest:

- `artifact_id`
- `artifact_kind`
- `workspace_id`
- `title`
- `content`
- `metadata`
- `source_uri`
- `provider`
- `created_at`
- `updated_at`

Important design decision:

- normalize everything into GraphRAG input artifacts now, even if the payloads are tiny

## Phase 3: OpenClaw Integration

Duration:

- `3 to 5 days`

Goal:

- make GraphRAG usable in live agent workflows without pretending it is just a search tool

Build:

### 1. `openclaw-graphrag` plugin

Capabilities:

- register a `contextEngine`
- optionally register memory search tools
- optionally register CLI helpers
- call the GraphRAG facade

### 2. GraphRAG context engine behavior

Use the OpenClaw context-engine lifecycle:

- `ingest`: stash or queue new messages for summarization
- `assemble`: choose the right GraphRAG query mode and inject retrieved memory
- `compact`: summarize long sessions into durable artifacts
- `afterTurn`: persist approved summaries or lessons into GraphRAG

Recommended phase-1 assembly policy:

- use `Local` for specific grounded questions
- use `Global` for themes, overviews, or comparisons across a corpus
- use `DRIFT` for investigative or exploratory questions
- keep recent raw session messages from OpenClaw in the context window

## Phase 4: Durable Artifact Modeling

Duration:

- `4 to 7 days`

Goal:

- make GraphRAG cover more of the Cortex vision without adding a second durable store

Artifact kinds to introduce:

- `imported_document`
- `session_summary`
- `user_preference`
- `project_rule`
- `decision_record`
- `tool_lesson`
- `operator_annotation`

Required metadata for each artifact:

- stable `artifact_id`
- `workspace_id`
- `artifact_kind`
- `source_uri`
- `provider`
- timestamps

Important compromise:

- these are still artifacts, not transactional records

## Phase 5: Retrieval Policy And Routing

Duration:

- `4 to 6 days`

Goal:

- stop using one generic recall path for every question

Implement:

- a query router that chooses query mode, workspace, response style, and retrieval budget
- question-generation support for follow-up suggestions
- response templates that distinguish `Local`, `Global`, and `DRIFT`

Suggested routing rules:

- `Global`: overviews, trends, themes, summaries, compare-and-contrast
- `Local`: people, files, decisions, concrete factual follow-up
- `DRIFT`: "how does this connect", "trace this idea", "what else should I look at"
- `Basic`: cheap fallback

## Phase 6: Dream-Lite And Maintenance

Duration:

- `4 to 7 days`

Goal:

- use GraphRAG's community-report machinery as a practical stand-in for the Dream slice of Cortex

Implement:

- scheduled `update` jobs
- periodic full `standard-update` for important corpora
- community-report refresh after material corpus changes
- operator command to regenerate summaries for a workspace
- planning surfaces that summarize top community reports

## Phase 7: Provenance And Inspection

Duration:

- `3 to 5 days`

Goal:

- make the system inspectable enough to trust

Implement:

- artifact metadata conventions in ingested content
- API responses that return source document IDs or text-unit citations where possible
- operator endpoint to inspect the originating artifact for a returned memory
- optional local visualization or search UI

## Phase 8: Whole-Cortex Expansion Without A Rebuild

Duration:

- `2 to 4 weeks`

Goal:

- push the stack as far toward the Cortex vision as GraphRAG can reasonably go

Workstreams:

- richer artifact taxonomy
- better session-summary prompts
- more accurate routing between `Local`, `Global`, and `DRIFT`
- domain-specific prompt tuning per workspace
- custom vector store only if a real limitation appears
- `BYOG` if stock extraction becomes the main limitation

## What Still Has To Be Custom Even At Maturity

Even after a successful GraphRAG implementation, several Cortex concerns still remain ours:

- fine-grained governance-first retrieval
- artifact-provider identity policy
- write approval policy for runtime-derived memories
- clean operator UX for correction and curation
- stronger canonical semantics for non-document memory

## When To Stop Investing

Stop investing in this path if one or more of these become clearly true:

- you need strong low-latency per-turn mutable memory objects
- coarse workspace partitioning is not enough
- GraphRAG indexing cost is too high for the value you get
- most important memories are tiny structured facts, not artifacts
- the OpenClaw context-engine bridge becomes more complicated than the value of GraphRAG's query modes

## Recommendation

If you want to give GraphRAG a real chance as a contender, this is the right posture:

- keep phase 1 native to GraphRAG
- containerize it as `graphrag-api` plus `graphrag-indexer`
- keep built-in `LanceDB`
- use a shared workspace volume
- integrate with OpenClaw through a custom context engine
- treat all durable memory as artifacts first
- use community reports as Dream-lite instead of rebuilding that layer

The biggest compromise is also the key to making it viable:

- do not fight the artifact-first, corpus-first worldview too early

## Sources

- Microsoft GraphRAG docs: <https://microsoft.github.io/graphrag/>
- GraphRAG Getting Started: <https://microsoft.github.io/graphrag/get_started/>
- GraphRAG Indexing Methods: <https://microsoft.github.io/graphrag/index/methods/>
- GraphRAG Outputs: <https://microsoft.github.io/graphrag/index/outputs/>
- GraphRAG Bring Your Own Graph: <https://microsoft.github.io/graphrag/index/byog/>
- GraphRAG Prompt Tuning Overview: <https://microsoft.github.io/graphrag/prompt_tuning/overview/>
- GraphRAG CLI: <https://microsoft.github.io/graphrag/cli/>
- GraphRAG Detailed Configuration: <https://microsoft.github.io/graphrag/config/yaml/>
- GraphRAG paper: <https://arxiv.org/abs/2404.16130>
- OpenClaw Context Engine: <https://docs.openclaw.ai/concepts/context-engine>
- OpenClaw Memory Overview: <https://docs.openclaw.ai/concepts/memory>
- OpenClaw Plugins: <https://docs.openclaw.ai/plugins>
- OpenClaw Hooks: <https://docs.openclaw.ai/automation/hooks>
