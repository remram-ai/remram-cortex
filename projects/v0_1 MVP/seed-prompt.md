# Cortex v0.1 MVP Seed Prompt

Use this to start a new focused thread on one capability or spec area in `remram-cortex`.

```text
You are joining active MVP design and implementation work in the `remram-cortex` repository.

Repository focus:
Cortex is the knowledge authority layer of Remram. It owns structured memory, reflection-driven consolidation, bounded retrieval, artifact intake, and artifact promotion. It is not a transcript store, not a vector-only memory system, and not a prompt assembler.

Current project:
We are working in `projects/v0_1 MVP/`.
The goal of this MVP is to land an operational memory system that can move from:

"ingest this document"

to:

"answer this question in the context of that document implicitly"

without requiring the user to restate the document every time.

Read these first:
1. `projects/v0_1 MVP/README.md`
2. `projects/v0_1 MVP/seed-prompt.md`
3. `projects/v0_1 MVP/project-plan.md`
4. `projects/v0_1 MVP/test-plan.md`
5. `projects/v0_1 MVP/capabilities/README.md`
6. the specific capability folder I ask you to work on
7. `docs/design/v0_1-mvp-scope.md`
8. `docs/design/v0_1-mvp-spec.md`
9. `docs/remram-cortex/architecture.md`
10. `docs/glossary.md`

Current capability sequence:
1. `01-opensearch-service`
2. `02-artifact-storage`
3. `03-git-service`
4. `04-git-provider`
5. `05-google-drive-provider`
6. `06-artifact-intake`
7. `07-knowledge-extraction`
8. `08-quick-capture`
9. `09-retrieval`
10. `10-chat-injection`
11. `11-chat-interface`

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
- stay tightly scoped to the capability or spec I ask about
- preserve the existing architecture unless there is a real contradiction
- keep designs implementable in Go and practical on OpenSearch
- update the capability `spec.md` and `test-plan.md` together if the capability changes
- update umbrella project docs only if the change affects sequencing, scope, or acceptance
- optimize for debuggability, explicit contracts, and incremental delivery
- treat the chat interface as a standalone MVP proof surface that can later be plugged into OpenClaw

For this thread, focus on:
[PASTE THE SPEC OR CAPABILITY YOU WANT TO DIG INTO HERE]
```
