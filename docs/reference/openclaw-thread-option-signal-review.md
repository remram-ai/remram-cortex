# OpenClaw Thread Option Signal Review

Review date: April 2, 2026

This note screens the projects mentioned in a recent `OpenClaw` memory thread.

The thread itself is anecdotal signal, not decision-grade evidence.
This review checks the underlying projects instead:

- what the project actually is
- whether it is a serious foundation candidate or just a supporting tool
- current GitHub star signal
- current contributor count signal

Star and contributor counts below were pulled from the GitHub API on April 2, 2026.

## Bottom Line

The thread surfaced a few genuinely meaningful projects:

- `QMD` is real and serious, not just a community hack.
- `lossless-claw` is a serious supporting component, but it is not a long-term memory authority.
- `Honcho` is a real contender in the runtime-memory category.
- the `Graphiti + OpenClaw` plugin ecosystem is real, but still small and early.
- `LanceDB` and `SurrealDB` are strong infrastructure projects, not complete memory foundations.

The thread also surfaced several interesting but still low-signal or narrow projects.

## Screened Options

| Option | Repo | Stars | Contributors | What It Is | Signal |
| --- | --- | ---: | ---: | --- | --- |
| `QMD` | [tobi/qmd](https://github.com/tobi/qmd) | 17,535 | 56 | local markdown or document search engine used by `OpenClaw` as a memory backend | strong |
| `lossless-claw` | [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | 3,940 | 33 | session-context and compaction alternative for `OpenClaw` | strong supporting tool |
| `Honcho` | [plastic-labs/honcho](https://github.com/plastic-labs/honcho) | 1,511 | 17 | memory service and user-modeling system | strong supporting or runtime-memory option |
| `OB1` | [NateBJones-Projects/OB1](https://github.com/NateBJones-Projects/OB1) | 1,086 | 13 | persistent memory infrastructure with cloud or local options | real wildcard |
| `LanceDB` | [lancedb/lancedb](https://github.com/lancedb/lancedb) | 9,751 | 186 | vector and search database substrate | strong substrate only |
| `SurrealDB` | [surrealdb/surrealdb](https://github.com/surrealdb/surrealdb) | 31,750 | 176 | multi-model database with document, graph, and vector support | strong substrate only |
| `cortex-engine` | [Fozikio/cortex-engine](https://github.com/Fozikio/cortex-engine) | 41 | 3 | opinionated local memory system inspired by long-lived agent identity | interesting but early |
| `Nex` | [nex-crm/nex-as-a-skill](https://github.com/nex-crm/nex-as-a-skill) | 16 | 8 | cross-tool knowledge graph and company-intelligence layer | interesting but early |
| `openclaw-graphiti-memory` | [clawdbrunner/openclaw-graphiti-memory](https://github.com/clawdbrunner/openclaw-graphiti-memory) | 64 | 1 | hybrid `OpenClaw` stack using files plus `Graphiti` | real but early |
| `openclaw-memory-graphiti` | [Contextable/openclaw-memory-graphiti](https://github.com/Contextable/openclaw-memory-graphiti) | 10 | 1 | `OpenClaw` memory plugin around `Graphiti` plus extra layers | real but early |
| `openclaw-graphiti-plugin` | [RobertoGongora/openclaw-graphiti-plugin](https://github.com/RobertoGongora/openclaw-graphiti-plugin) | 15 | 3 | `OpenClaw` plugin for `Graphiti + Neo4j` | real but early |
| `obsidian-qmd` | [achekulaev/obsidian-qmd](https://github.com/achekulaev/obsidian-qmd) | 22 | 1 | `Obsidian` plugin for working with `QMD` | accessory only |
| `discord-indexer-dotnet` | [patrick-slimelab/discord-indexer-dotnet](https://github.com/patrick-slimelab/discord-indexer-dotnet) | 1 | 1 | narrow Discord indexing utility | not decision-relevant |

## What Actually Matters

### `QMD`

This is the strongest thread-derived signal.

- The repo is substantial.
- The contributor count is real.
- `OpenClaw` officially documents it as a first-class memory backend.
- It reinforces the conclusion that the `OpenClaw` ecosystem currently trusts local search and routing more than ambitious memory-authority stacks.

Implication:

- `QMD` should stay in the decision set as the best practical `OpenClaw`-native option.
- It is still a search layer, not a full Cortex authority foundation.

### `lossless-claw`

This is a serious supporting project.

- The repo has enough stars and contributors to count as real ecosystem signal.
- It addresses session-context and compaction pain directly.
- It is complementary to `QMD`, not a replacement for a long-term memory authority.

Implication:

- worth tracking as a session-memory or context-management support layer
- not a primary Cortex foundation choice

### `Honcho`

This remains more important than the original thread ranking suggests.

- It has real community signal.
- It is already documented in the official `OpenClaw` memory docs.
- It fits runtime continuity and user modeling better than artifact-backed authority memory.

Implication:

- real contender for runtime memory
- still not the cleanest Cortex authority foundation

### `Graphiti` Plugin Ecosystem

The thread makes the `Graphiti` signal look broader than it currently is.

What the repo data shows:

- there are multiple real `OpenClaw + Graphiti` repos
- they are active
- but each is still small in stars and contributors

Implication:

- this is enough to prove viability
- it is not enough to prove maturity or mainstream success

This supports the current conclusion:

- `Graphiti` is a plausible long-term substrate
- `Graphiti + OpenClaw` is still an early-adopter path

### `cortex-engine`

This one is conceptually interesting because it looks closer to some Cortex ideas than the thread author probably realized.

But the public signal is still small:

- 41 stars
- 3 contributors

Implication:

- worth reading as a pattern donor
- not enough external proof to treat as a foundation candidate on ecosystem signal alone

### `Nex`

`Nex` is interesting because it explicitly positions itself as a knowledge graph or intelligence layer across agent sessions and external systems.

But right now the public OSS signal is still small:

- 16 stars
- 8 contributors

Implication:

- worth a future wildcard review
- not yet strong enough to jump ahead of `Mem0`, `Graphiti`, or `Cognee`

### `OB1`

`OB1` is the strongest wildcard from the thread outside the already-known field.

- over 1,000 stars
- double-digit contributors

Implication:

- worth a real future fit analysis if we want one more external contender
- still not enough by itself to displace the existing top candidates without deeper research

### `LanceDB` and `SurrealDB`

These are serious projects, but the thread mixes them into memory-rank talk in a misleading way.

They are:

- real
- active
- credible

But they are not complete memory foundations.
They are substrates.

Implication:

- they matter if we reopen the direct-database path
- they do not beat `Mem0` or `Graphiti` as first-order memory systems

## What The Thread Changes

The thread does not overturn the current recommendation.

It does strengthen three things:

1. `QMD` is unquestionably serious.
2. the `OpenClaw` ecosystem is converging on layered stacks, not one perfect memory system.
3. the `Graphiti` plugin scene is real, but still too small to count as strong mainstream proof.

It also introduces two worthwhile wildcards:

- `OB1`
- `Nex`

Neither has enough signal yet to outrank the current top candidates.

## Recommendation

Keep using the current top-level interpretation:

- best first-build foundation: `Mem0`
- best graph-native end-state candidate: `Graphiti`
- best practical `OpenClaw`-native option: `QMD`

Track these thread-derived additions:

- `lossless-claw` as a strong supporting tool
- `Honcho` as a strong runtime-memory option
- `OB1` as a future wildcard review candidate
- `Nex` as a future wildcard review candidate

Do not let the thread distort the real signal:

- serious stars and contributors matter
- official integration status matters
- substrate projects should not be confused with complete memory foundations

