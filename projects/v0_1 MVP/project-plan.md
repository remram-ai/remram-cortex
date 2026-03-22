# Cortex v0.1 MVP Project Plan

## 1. Mission

Deliver the first end-to-end Cortex slice that can:

1. import source artifacts into a baseline knowledge base
2. persist or register those imports through artifact storage under stable Cortex identity
3. accept new low-friction captures
4. deduplicate or link those captures against existing knowledge
5. retrieve the resulting knowledge through the current Cortex retrieval model
6. improve at least one ordinary chat flow through knowledge injection

## 2. Canonical Product References

The stable Cortex design surface now lives under `product/`.

Use these as the canonical capability and dependency docs for this project:

### 2.1 Dependencies

- [01 OpenSearch Service](../../product/dependencies/opensearch-service/README.md)
- [02 Git Service](../../product/dependencies/git-service/README.md)

### 2.2 Capabilities

- [03 Artifact Storage](../../product/capabilities/artifact-storage/spec.md)
- [04 Git Provider](../../product/capabilities/git-provider/spec.md)
- [05 Google Drive Provider](../../product/capabilities/google-drive-provider/spec.md)
- [06 Artifact Intake](../../product/capabilities/artifact-intake/spec.md)
- [07 Knowledge Extraction](../../product/capabilities/knowledge-extraction/spec.md)
- [08 Quick Capture](../../product/capabilities/quick-capture/spec.md)
- [09 Retrieval](../../product/capabilities/retrieval/spec.md)
- [10 Chat Injection](../../product/capabilities/chat-injection/spec.md)
- [11 Chat Interface](../../product/capabilities/chat-interface/spec.md)

## 3. Project Execution Artifacts

This folder is the execution package for this MVP run.

Primary project artifacts:

- [README.md](README.md)
- [project-plan.md](project-plan.md)
- [seed-prompt.md](seed-prompt.md)
- [acceptance-test.md](acceptance-test.md)
- [acceptance-test.json](acceptance-test.json)
- [runtime-docs.md](runtime-docs.md)
- [epics/](epics/README.md)
- [acceptance-tests/](acceptance-tests/)

Use `acceptance-tests/` for executed project acceptance records and HAT notes.

## 4. Deliverables

### 4.1 Required

- OpenSearch service for local Cortex retrieval development
- artifact storage adapter contract implemented or stubbed against at least one provider
- local Git service for provider-backed artifact storage
- Git-backed local artifact provider implementation
- Google Drive provider design and integration path
- artifact intake pipeline for text-bearing artifacts
- quick capture submission path
- OpenSearch indexing for imported and captured knowledge
- one general chat integration path that consumes Cortex retrieval
- one minimal chat interface or harness that proves the end-to-end read path
- retrieval traces for debugging
- demo corpus and proof scenarios

### 4.2 Product Docs

Each native Cortex capability or local dependency should have the appropriate stable product docs under `product/`.

This project consumes those docs rather than owning a second canonical capability tree.

Current capability set:

1. [01 OpenSearch Service](../../product/dependencies/opensearch-service/README.md) `dependency`
2. [02 Git Service](../../product/dependencies/git-service/README.md) `dependency`
3. [03 Artifact Storage](../../product/capabilities/artifact-storage/spec.md) `capability`
4. [04 Git Provider](../../product/capabilities/git-provider/spec.md) `capability`
5. [05 Google Drive Provider](../../product/capabilities/google-drive-provider/spec.md) `capability`
6. [06 Artifact Intake](../../product/capabilities/artifact-intake/spec.md) `capability`
7. [07 Knowledge Extraction](../../product/capabilities/knowledge-extraction/spec.md) `capability`
8. [08 Quick Capture](../../product/capabilities/quick-capture/spec.md) `capability`
9. [09 Retrieval](../../product/capabilities/retrieval/spec.md) `capability`
10. [10 Chat Injection](../../product/capabilities/chat-injection/spec.md) `capability`
11. [11 Chat Interface](../../product/capabilities/chat-interface/spec.md) `capability`

### 4.3 Optional If Cheap

- simple status endpoints for import and capture jobs
- lightweight CLI harness for demoing imports and captures

## 5. Execution Phases

This project is implemented epic by epic.

Each epic owns:

- [README.md](epics/README.md) style epic charter
- epic `implementation-plan.md`
- epic `implementation-plan.json`
- epic `test-plan.md`
- epic `test-plan.json`
- epic `tests/`

The project plan ties those epics together.

### Epic Order

1. [01 OpenSearch Service](epics/01-opensearch-service/README.md)
2. [02 Git Service](epics/02-git-service/README.md)
3. [03 Artifact Storage](epics/03-artifact-storage/README.md)
4. [04 Git Provider](epics/04-git-provider/README.md)
5. [05 Google Drive Provider](epics/05-google-drive-provider/README.md)
6. [06 Artifact Intake](epics/06-artifact-intake/README.md)
7. [07 Knowledge Extraction](epics/07-knowledge-extraction/README.md)
8. [08 Quick Capture](epics/08-quick-capture/README.md)
9. [09 Retrieval](epics/09-retrieval/README.md)
10. [10 Chat Injection](epics/10-chat-injection/README.md)
11. [11 Chat Interface](epics/11-chat-interface/README.md)

### Sequencing Rationale

- the service dependencies are closed first so later work does not block on missing local substrate
- artifact identity and provider routing come next because all later evidence paths depend on them
- evidence-to-knowledge capabilities come before retrieval
- retrieval comes before chat proof surfaces
- the chat proof surfaces close the loop and provide the visible MVP demonstration

## 6. Primary Risks

- trying to support too many artifact formats too early
- treating Quick Capture like a separate notes product
- overbuilding Dream before the write or retrieval loop is proven
- weak merge logic producing duplicate objects that poison the demo
- storing duplicate artifact metadata in multiple places
- letting external source layout leak into Cortex artifact identity or hierarchy

## 7. Recommended Demo Dataset

Use a small but meaningful seed corpus:

- 5-15 project documents
- a few idea or strategy notes
- a few personal or operational notes only if needed for scope validation

Then run 3-5 quick captures that:

- reinforce one existing idea
- refine one imported concept
- create one genuinely new concept

## 8. Readiness Gate

Do not call the MVP done merely because import and capture both store data.

The release gate is retrieval usefulness:

- can Cortex find the right object
- from multiple valid framings
- without obvious duplication
- with traceable provenance
- and with visible chat-time benefit
