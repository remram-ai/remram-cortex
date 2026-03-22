# Cortex v0.1 MVP Project Plan

## 1. Mission

Deliver the first end-to-end Cortex slice that can:

1. import source artifacts into a baseline knowledge base
2. persist or register those imports through artifact storage under stable Cortex identity
3. accept new low-friction captures
4. deduplicate or link those captures against existing knowledge
5. retrieve the resulting knowledge through the current Cortex retrieval model
6. improve at least one ordinary chat flow through knowledge injection

## 2. Deliverables

### 2.1 Required

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

### 2.2 Capability Packs

Each MVP capability must have:

- one capability spec
- one capability test plan

Current capability set:

- [01 OpenSearch Service](capabilities/01-opensearch-service/spec.md)
- [02 Artifact Storage](capabilities/02-artifact-storage/spec.md)
- [03 Git Service](capabilities/03-git-service/spec.md)
- [04 Git Provider](capabilities/04-git-provider/spec.md)
- [05 Google Drive Provider](capabilities/05-google-drive-provider/spec.md)
- [06 Artifact Intake](capabilities/06-artifact-intake/spec.md)
- [07 Knowledge Extraction](capabilities/07-knowledge-extraction/spec.md)
- [08 Quick Capture](capabilities/08-quick-capture/spec.md)
- [09 Retrieval](capabilities/09-retrieval/spec.md)
- [10 Chat Injection](capabilities/10-chat-injection/spec.md)
- [11 Chat Interface](capabilities/11-chat-interface/spec.md)

### 2.3 Optional If Cheap

- simple status endpoints for import and capture jobs
- lightweight CLI harness for demoing imports and captures

## 3. Execution Phases

### Phase 1: Contract And Storage Foundation

Deliver:

- [01 OpenSearch Service](capabilities/01-opensearch-service/spec.md)
- [02 Artifact Storage](capabilities/02-artifact-storage/spec.md)
- [03 Git Service](capabilities/03-git-service/spec.md)
- [04 Git Provider](capabilities/04-git-provider/spec.md)
- stable artifact ID generation
- predictable storage layout

Exit criteria:

- imported and captured artifacts can both be written and resolved by ID
- imported artifacts remain resolvable by Cortex ID without relying on the original source path

The first provider may still be local Git even if the long-term model supports multiple providers.

### Phase 2: Evidence To Knowledge Baseline

Deliver:

- [05 Google Drive Provider](capabilities/05-google-drive-provider/spec.md)
- [06 Artifact Intake](capabilities/06-artifact-intake/spec.md)
- [07 Knowledge Extraction](capabilities/07-knowledge-extraction/spec.md)

Exit criteria:

- a starter corpus can be imported and results in retrievable knowledge objects

### Phase 3: Retrieval Baseline

Deliver:

- [08 Quick Capture](capabilities/08-quick-capture/spec.md)
- [09 Retrieval](capabilities/09-retrieval/spec.md)

Exit criteria:

- imported knowledge can be rediscovered through multiple query framings

### Phase 4: Operator Proof Surface

Deliver:

- [10 Chat Injection](capabilities/10-chat-injection/spec.md)
- [11 Chat Interface](capabilities/11-chat-interface/spec.md)

Exit criteria:

- a new capture can update an existing knowledge area instead of creating obvious duplicate noise

### Phase 5: End-To-End Proof And Hardening

Deliver:

- repeatable demo scenarios
- acceptance test execution
- identified gaps for v0.2

Exit criteria:

- the MVP success criteria from the design docs are demonstrably satisfied
- at least one ordinary chat example clearly improves because Cortex injected the right bundle

## 4. Suggested Work Breakdown

### Workstream A: [01 OpenSearch Service](capabilities/01-opensearch-service/spec.md)

- stand up local OpenSearch service
- define Cortex index mapping
- verify indexing and query connectivity

### Workstream B: [02 Artifact Storage](capabilities/02-artifact-storage/spec.md)

- define provider capability model
- define artifact routing policy
- define import and capture container layout
- verify source lookup by artifact ID
- preserve external source refs as provenance only

### Workstream C: [03 Git Service](capabilities/03-git-service/spec.md) And [04 Git Provider](capabilities/04-git-provider/spec.md)

- implement local adapter
- stand up the local Git-backed service or repository foundation
- wire the Git provider into artifact storage defaults

### Workstream D: [05 Google Drive Provider](capabilities/05-google-drive-provider/spec.md)

- define provider contract fit for Google-native docs
- define provider metadata, authority, and sync boundary
- define later ingestion or watch path without blocking the MVP core

### Workstream E: [06 Artifact Intake](capabilities/06-artifact-intake/spec.md)

- define import job shape
- implement parser pipeline for supported formats
- emit source-linked slices
- hand slices to knowledge extraction

### Workstream F: [07 Knowledge Extraction](capabilities/07-knowledge-extraction/spec.md)

- define MVP object-kind subset
- implement reflection merge discipline
- generate typed signals and signature

### Workstream G: [09 Retrieval](capabilities/09-retrieval/spec.md)

- define OpenSearch mapping
- implement scoring query
- implement rerank pass and trace output

### Workstream H: [08 Quick Capture](capabilities/08-quick-capture/spec.md)

- define submission contract
- store raw capture artifact
- invoke reflection path
- test dedup or linking against seeded corpus

### Workstream I: [10 Chat Injection](capabilities/10-chat-injection/spec.md)

- define orchestration hook contract
- define bundle injection shape
- run before/after answer comparisons

### Workstream J: [11 Chat Interface](capabilities/11-chat-interface/spec.md)

- define the minimal chat harness surface
- wire retrieval into the harness
- expose bundle and trace visibility for debugging

## 5. Primary Risks

- trying to support too many artifact formats too early
- treating Quick Capture like a separate notes product
- overbuilding Dream before the write or retrieval loop is proven
- weak merge logic producing duplicate objects that poison the demo
- storing duplicate artifact metadata in multiple places
- letting external source layout leak into Cortex artifact identity or hierarchy

## 6. Recommended Demo Dataset

Use a small but meaningful seed corpus:

- 5-15 project documents
- a few idea or strategy notes
- a few personal or operational notes only if needed for scope validation

Then run 3-5 quick captures that:

- reinforce one existing idea
- refine one imported concept
- create one genuinely new concept

## 7. Readiness Gate

Do not call the MVP done merely because import and capture both store data.

The release gate is retrieval usefulness:

- can Cortex find the right object
- from multiple valid framings
- without obvious duplication
- with traceable provenance
- and with visible chat-time benefit
