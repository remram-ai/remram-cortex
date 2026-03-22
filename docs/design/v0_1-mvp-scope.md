# Cortex v0.1 MVP Scope

## 1. Objective

The first Cortex MVP should prove one closed loop:

1. establish a baseline knowledge base from imported artifacts
2. let the user add new knowledge through low-friction capture
3. retrieve imported and captured knowledge together through the same Cortex model
4. inject that knowledge into ordinary chat so the system visibly behaves better

This MVP is centered on three inputs:

- [Artifact Intake](../concepts/artifact-intake.md)
- external dependency: `artifact-storage` from Forge
- Quick Capture as the primary proof surface

The design goal is not to deliver "all of Cortex."
It is to prove that Cortex can seed knowledge, accept new knowledge cheaply, and retrieve both through one durable model.

## 2. Product Thesis

Artifact Intake and Artifact Storage establish the first trustworthy evidence path.

Quick Capture proves that Cortex is not just an offline importer. It shows that new thoughts can enter the system, deduplicate or link against seeded knowledge, and become useful retrieval targets immediately.

General chat with Cortex knowledge injection proves that Cortex is not just a storage backend. It shows that retrieved knowledge can actually improve a live user interaction.

That combination gives Cortex:

- a baseline knowledge base
- a live write surface
- a retrieval proof surface
- a visible runtime read surface

Without all three, the MVP is structurally incomplete.

## 3. MVP Slice

### 3.1 Core Deliverable

The v0.1 MVP delivers:

- a minimal artifact storage dependency contract
- artifact intake for baseline knowledge seeding
- text-first Quick Capture as the primary user-facing or test-facing entry point
- retrieval over the combined imported and captured knowledge
- ordinary chat with Cortex knowledge injection as the primary read-side proof surface
- retrieval traces sufficient to debug what Cortex did

Imported artifacts must become Cortex-managed assets after intake. The MVP should not depend on the external folder tree, original file path, or mutable source-system layout as the canonical organization inside Cortex.

### 3.2 Intended User Story

A user should be able to:

1. import a small set of existing documents into Cortex
2. wait for Cortex to extract source-linked knowledge objects
3. quick-capture a new thought related to those imported materials
4. ask for that knowledge later and get a bounded retrieval bundle that includes both seeded and newly captured knowledge
5. ask an ordinary chat question and receive a better answer because Cortex knowledge was injected before prompt build

### 3.3 Reference Demo Case

A representative proof case is:

1. import OpenTrails or related project artifacts
2. quick-capture a new idea like "reseller network for trail lodging"
3. have Cortex link or refine that idea against imported project knowledge
4. retrieve it later through queries framed as:
   - "find more camping spots"
   - "how could OpenTrails make money"
   - "places to stay while hiking"
5. ask the same question in ordinary chat and have the runtime answer improve because Cortex injected the linked project knowledge

If that works, the retrieval model is doing real work rather than just replaying text.

## 4. MVP Principles

- One evidence path, not separate memory silos.
- Quick Capture should ride the same durable model as imported artifacts.
- Reflection should do the hard write-time work so retrieval stays cheap.
- Imported artifacts are evidence; knowledge objects are the durable memory.
- Artifact Storage should be a dependency contract, not a parallel metadata authority.
- Text-first is acceptable for the MVP if it buys clarity and speed.

## 5. In Scope

### 5.1 Artifact Storage Dependency

The MVP includes the subset of artifact storage behavior Cortex actually needs:

- persist or register Cortex-managed artifacts through a configurable provider contract
- persist lightweight capture artifacts for Quick Capture submissions
- return stable artifact identifiers and deterministic internal paths
- route artifacts by policy rather than by source path
- preserve original source references as provenance without making them canonical storage paths

This is a dependency contract, not a full Forge lifecycle implementation.

### 5.2 Artifact Intake

The MVP includes:

- import submission into Cortex
- original artifact persistence through artifact storage
- text extraction and bounded source slicing
- source-linked provenance
- knowledge-object creation or reinforcement
- OpenSearch indexing of resulting knowledge

Artifact intake should treat the imported source as an input to be registered into Cortex ownership, not as a document that continues to define Cortex hierarchy by where it happened to live before import.

The broader architecture may use different providers for different artifact classes. That configurability should not leak into the Cortex memory model.

### 5.3 Quick Capture

The MVP includes:

- text-first quick capture
- immediate normalization into a capture artifact
- reflection-driven extraction into knowledge objects
- dedup, refine, or link behavior against existing seeded knowledge
- retrieval visibility through the same Cortex retrieval stack

Quick Capture is the main proof surface because it exercises the write path, retrieval path, and dedup behavior with the lowest user friction.

### 5.4 General Chat With Knowledge Injection

The MVP also includes a general chat path that consumes Cortex retrieval during prompt construction.

This is the user-facing proof surface for:

- knowledge injection
- retrieval usefulness
- visible continuity improvement

The user should be able to ask an ordinary chat question and receive a better answer because Cortex supplied relevant imported or captured knowledge.

### 5.5 Retrieval

The MVP includes retrieval over:

- imported artifact-derived knowledge
- quick-capture-derived knowledge
- links between them

Retrieval should use the architecture already locked:

- governance filters
- semantic signature bias
- typed signal scoring
- assistive vector matching
- relationship expansion

### 5.6 Observability

The MVP includes enough visibility to debug failures:

- import status
- extraction status
- object counts created or updated
- retrieval trace for matching and ranking
- artifact-to-object provenance lookup

## 6. Out Of Scope

The MVP explicitly does not need to deliver:

- voice-first Quick Capture
- autonomous feasibility analysis
- dormant idea resurfacing
- MyFeed-triggered updates
- full Dream automation quality loops
- artifact promotion workflows
- image-only OCR or rich multimodal intake guarantees
- multi-user family sharing UX
- complete Forge lifecycle container support beyond Cortex's immediate artifact-storage dependency
- provider-specific collaboration sync such as Google change watching

## 7. Hard Scoping Decisions

### 7.1 Text-First Quick Capture

Quick Capture should be text-first in v0.1.

Voice capture is attractive, but it is not required to prove Cortex memory quality. Text capture is enough to validate:

- low-friction input
- dedup behavior
- retrieval usefulness

### 7.2 Document-First Artifact Intake

Artifact intake should prioritize text-bearing artifacts first:

- Markdown
- text
- PDF

Images may still be stored through artifact storage, but image-native extraction should not block the MVP.

### 7.3 One Durable Model

Quick Capture should not bypass Cortex structure.

Each capture should become:

1. a lightweight evidence artifact in artifact storage
2. a reflection input
3. one or more resulting knowledge objects

That keeps imported artifacts and captured thoughts on one provenance model.

### 7.4 Canonical Artifact Ownership

For this MVP, the authoritative artifact identity after intake is the Cortex artifact record, not the original Drive path, chat attachment location, or local filesystem path.

That gives Cortex:

- stable provenance anchors
- deterministic inspection targets
- freedom to reorganize source systems later without breaking memory links

The provider behind that artifact may still vary. The Cortex artifact record remains the stable abstraction.

## 8. Success Criteria

The MVP succeeds if it can demonstrate all of the following:

- a user can import a starter corpus and establish a non-empty knowledge base
- imported knowledge is traceable back to artifact source locations
- imported artifacts remain addressable by Cortex artifact ID even if the source system later changes names or layout
- a quick capture can reinforce, refine, or link to imported knowledge instead of duplicating it blindly
- retrieval can find the same idea from multiple valid angles
- ordinary chat visibly improves because Cortex injected the right bundle
- the system can explain why a given object was retrieved

## 9. Key Risks

- over-scoping artifact intake into a full multimodal parser platform
- letting Quick Capture become a separate note-taking system instead of a Cortex write surface
- bypassing artifact storage and creating duplicate evidence paths
- relying on retrieval-time reasoning to compensate for weak reflection output
- treating every capture as a new object rather than enforcing merge discipline

## 10. MVP Outcome

If this slice works, Cortex will have proven:

- baseline knowledge can be seeded from real artifacts
- new ideas can be incorporated cheaply
- retrieval is useful because reflection and provenance were done correctly

That is enough to move from architecture debate into narrower implementation specs.
