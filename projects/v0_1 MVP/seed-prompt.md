# Cortex v0.1 MVP Seed Prompt

Use this to start a new focused thread on one capability or spec area in `remram-cortex`.

```text
You are joining active MVP design and implementation work in the `remram-cortex` repository.

Repository focus:
Cortex is the knowledge authority layer of Remram. It owns structured memory, reflection-driven consolidation, bounded retrieval, artifact intake, and artifact promotion. It is not a transcript store, not a vector-only memory system, and not a prompt assembler.

Current project:
We are working in `projects/v0_1 MVP/`.
The stable product docs live under `product/`.
The goal of this MVP is to land an operational memory system that can move from:

"ingest this document"

to:

"answer this question in the context of that document implicitly"

without requiring the user to restate the document every time.

Read these first:
1. `projects/v0_1 MVP/README.md`
2. `projects/README.md`
3. `projects/v0_1 MVP/seed-prompt.md`
4. `projects/v0_1 MVP/project-plan.md`
5. `projects/v0_1 MVP/acceptance-test.md`
6. `projects/v0_1 MVP/epics/README.md`
7. the specific epic folder I ask you to work on, if the thread is epic-scoped
8. `product/README.md`
9. `product/capabilities/README.md`
10. `product/dependencies/README.md`
11. the specific capability or dependency folder I ask you to work on, if the thread is product-scoped
12. `docs/design/v0_1-mvp-scope.md`
13. `docs/design/v0_1-mvp-spec.md`
14. `docs/remram-cortex/architecture.md`
15. `docs/glossary.md`

Current capability sequence:
1. `opensearch-service` dependency
2. `git-service` dependency
3. `artifact-storage` capability
4. `git-provider` capability
5. `google-drive-provider` capability
6. `artifact-intake` capability
7. `knowledge-extraction` capability
8. `quick-capture` capability
9. `retrieval` capability
10. `chat-injection` capability
11. `chat-interface` capability

Important architectural constraints:
- hard governance filters before semantic scoring
- semantic signature is a soft routing bias, not a hard gate
- typed signals are the primary retrieval surface
- vector similarity is assistive only
- links are primary; trees, clusters, and views are derived
- artifacts are provider-backed and configurable
- Cortex owns stable artifact identity even when a provider is external
- local Git is the safe default and fallback provider
- Google Workspace and other providers are configurable, not required everywhere
- Cortex should not depend on Forge; Forge is at most background context for how work can be packaged, not the Cortex process model

Artifact and provider model:
- `artifact_storage` defines the Cortex-owned provider contract
- `git_service` is the local Git substrate used by the Git provider
- `git_provider` is the safe default local provider
- `google_drive_provider` is the collaborative document provider
- provider choice is routed by artifact policy, not by source path

When working in a thread:
- stay tightly scoped to the capability, dependency, or spec I ask about
- preserve the existing architecture unless there is a real contradiction
- keep designs implementable in Go and practical on OpenSearch
- update the paired `spec.md` and `regression-plan.md` together when a stable product doc changes
- update umbrella project docs only if the change affects sequencing, scope, or acceptance
- optimize for debuggability, explicit contracts, and incremental delivery
- treat the chat interface as a standalone MVP proof surface that can later be plugged into OpenClaw

For this thread, focus on:
[PASTE THE SPEC OR CAPABILITY YOU WANT TO DIG INTO HERE]
```
