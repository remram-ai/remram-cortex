# Cortex v0.1 MVP Test Plan

## 1. Test Goal

Prove that Cortex can establish a baseline knowledge base from imported artifacts and then evolve that base through Quick Capture without splitting into parallel memory paths.

This is the umbrella test plan for the MVP. Detailed test plans for each capability live under [capabilities/](capabilities/README.md).

## 2. Test Categories

### 2.1 Infrastructure Tests

- OpenSearch service starts and is reachable
- Cortex index mapping can be created
- local Git-backed provider persists and resolves artifacts correctly

### 2.2 Artifact Storage Tests

- imported artifact is persisted and addressable by `artifact_id`
- capture artifact is persisted and addressable by `artifact_id`
- stored paths are predictable and stable
- the Cortex-managed imported copy can be reopened after knowledge extraction completes
- Cortex artifact resolution does not depend on the original source-system path remaining unchanged
- provider metadata is preserved on the artifact record

### 2.3 Artifact Intake Tests

- Markdown import creates source-linked slices
- text import creates source-linked slices
- PDF import creates source-linked slices when text is extractable
- extracted slices produce knowledge objects with provenance

### 2.4 Knowledge Extraction Tests

- imported evidence becomes structured knowledge-object deltas
- capture evidence becomes structured knowledge-object deltas
- typed signals and signature are attached to resulting objects
- obvious duplicate noise is reduced through merge discipline

### 2.5 Quick Capture Tests

- a short capture becomes a persisted capture artifact
- the capture produces one or more knowledge-object deltas
- the capture can reinforce an existing object instead of duplicating blindly
- the capture can create a new object when no existing object is relevant

### 2.6 Retrieval Tests

- imported knowledge is retrievable
- capture-derived knowledge is retrievable
- linked imported plus captured knowledge can be retrieved together
- retrieval trace explains filters and ranking contributors

### 2.7 General Chat Injection Tests

- ordinary chat can call Cortex retrieval before prompt build
- the returned bundle is bounded and inspectable
- the final chat answer uses seeded or captured knowledge in a way the no-Cortex path would miss

### 2.8 Chat Interface Tests

- a minimal chat harness can submit a user question
- the harness shows or exposes the retrieved bundle used for the answer
- the harness can be used as the proof surface before any OpenClaw integration exists

### 2.9 Capability Detail Documents

- [01 OpenSearch Service](capabilities/01-opensearch-service/test-plan.md)
- [02 Git Provider](capabilities/02-git-provider/test-plan.md)
- [03 Artifact Storage](capabilities/03-artifact-storage/test-plan.md)
- [04 Artifact Intake](capabilities/04-artifact-intake/test-plan.md)
- [05 Knowledge Extraction](capabilities/05-knowledge-extraction/test-plan.md)
- [06 Quick Capture](capabilities/06-quick-capture/test-plan.md)
- [07 Retrieval](capabilities/07-retrieval/test-plan.md)
- [08 Chat Injection](capabilities/08-chat-injection/test-plan.md)
- [09 Chat Interface](capabilities/09-chat-interface/test-plan.md)

## 3. Acceptance Scenarios

### Scenario 1: Baseline Knowledge Seeding

1. import a small project document set
2. confirm Cortex-managed imported copies exist in artifact storage
3. confirm knowledge objects were created
4. run retrieval queries against the imported corpus

Expected result:

- knowledge is retrievable with source-linked provenance
- the imported artifact is still reachable by Cortex artifact ID regardless of source path drift

### Scenario 2: Quick Capture Refines Existing Knowledge

Seed state:

- imported OpenTrails or similar project docs already exist

Action:

- submit capture: "Reseller network for trail lodging along hiking routes"

Expected result:

- capture is stored as an artifact
- Cortex links to the existing project knowledge area
- Cortex does not create a clearly duplicate object if a matching idea already exists

### Scenario 3: Multi-Angle Retrieval

After Scenario 2, retrieve with multiple phrasings:

- "find more camping spots"
- "how could OpenTrails make money"
- "places to stay while hiking"

Expected result:

- the same underlying concept is reachable from all three queries
- ranking may differ, but the canonical object remains discoverable

### Scenario 4: Provenance Audit

1. choose one retrieved object
2. inspect its provenance
3. open the linked imported or capture artifact

Expected result:

- the object can be traced back to the evidence that created or reinforced it

### Scenario 5: General Chat Knowledge Injection

Seed state:

- imported artifacts and at least one related quick capture already exist

Action:

- ask an ordinary chat question that should benefit from Cortex knowledge

Expected result:

- orchestration retrieves a Cortex bundle before prompt build
- the final answer reflects that knowledge
- the answer is materially better than the same chat without Cortex retrieval

## 4. Failure Conditions

The MVP should be considered failed or incomplete if:

- import works but retrieval cannot find imported knowledge reliably
- quick capture stores notes but bypasses the normal knowledge-object model
- duplicate objects proliferate for obvious near-duplicates
- retrieval cannot explain why an object was returned
- general chat never shows a meaningful difference when Cortex retrieval is enabled
- provenance from object back to artifact is broken
- artifact resolution breaks because the source system renamed or moved the original file

## 5. Required Test Outputs

- import job result samples
- capture job result samples
- retrieval trace samples
- before and after object examples for one dedup or refine case
- list of known misses or ambiguous cases

## 6. Stretch Validation

If time allows, validate one ambiguous query where multiple results should compose rather than collapse to one answer. That helps confirm the retrieval model is behaving like Cortex rather than a naive single-hit search.
