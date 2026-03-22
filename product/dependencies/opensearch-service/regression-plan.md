# OpenSearch Service Dependency Regression Plan

## 1. Goal

Prove that Cortex has a working OpenSearch backend whose schema and behavior are compatible with the MVP retrieval model.

This capability is not finished just because OpenSearch starts.
It is finished when Cortex can index knowledge-object-shaped documents, query them safely, and inspect why retrieval behaved the way it did.

## 2. Context Pack

This is the minimum context pack an implementation or validation thread should load before changing or testing the OpenSearch service contract.

### 2.1 Cortex MVP And Architecture Sources

| File | Used For | Why It Matters To This Task |
| --- | --- | --- |
| `projects/v0_1 MVP/README.md` | MVP narrative and capability order | Confirms OpenSearch is the foundation capability and that later tests depend on it behaving predictably. |
| `projects/v0_1 MVP/project-plan.md` | MVP deliverables and workstreams | States the expected OpenSearch outcomes that this test plan must validate. |
| `projects/v0_1 MVP/test-plan.md` | Umbrella MVP acceptance | Shows how OpenSearch evidence feeds later import, retrieval, and chat acceptance. |
| `product/dependencies/README.md` | Product dependency contract | Confirms this regression plan is part of the Cortex dependency surface rather than a project-local capability pack. |
| `product/capabilities/retrieval/spec.md` | Retrieval-stage contract | OpenSearch tests must prove compatibility with the retrieval stack that consumes the index. |
| `docs/design/v0_1-mvp-scope.md` | MVP boundary and success criteria | Prevents validation from drifting into non-MVP behavior that does not matter to the first slice. |
| `docs/design/v0_1-mvp-spec.md` | MVP flow and data contract | Defines the document shapes, retrieval surfaces, and write/read loops the tests must exercise. |
| `docs/remram-cortex/architecture.md` | Canonical Cortex architecture | The main source for testing governance-first retrieval, typed signals, vector assist, and traceability. |
| `docs/glossary.md` | Locked vocabulary | Keeps the test language aligned on knowledge objects, governance fields, typed signals, and retrieval traces. |
| `docs/concepts/bounded-retrieval.md` | Retrieval narrowing model | Explains why the tests must verify governance filtering before semantic ranking. |
| `docs/concepts/governance-fields.md` | Hard-filter semantics | Tells the test plan which fields must behave as exclusion filters. |
| `docs/concepts/typed-signals.md` | Primary retrieval surface | Tells the test plan which fields must drive lexical scoring. |
| `docs/concepts/semantic-signature.md` | Soft routing bias | Tells the test plan what not to treat as a hard gate during validation. |
| `docs/design/cortex-inspection-surfaces.md` | Inspection and debug expectations | Explains why traces, mappings, documents, and provenance must remain operator-inspectable. |

### 2.2 Platform And Deployment Boundary Sources

These files live outside `remram-cortex` but are required context because the service is deployed and operated through Moltbox.

| File | Used For | Why It Matters To This Task |
| --- | --- | --- |
| `d:/Development/RemRam/remram/docs/concepts/gateway.md` | Gateway control-plane model | Defines the canonical deploy, restart, status, and secret-management path the tests must exercise. |
| `d:/Development/RemRam/remram/docs/concepts/service.md` | Service concept and lifecycle | Confirms the native passthrough and the first-class service lifecycle model the tests should validate. |
| `d:/Development/RemRam/remram/docs/concepts/snapshot.md` | Existing Moltbox snapshot vocabulary | Helps validation avoid confusing runtime checkpoint snapshots with OpenSearch backup snapshots. |
| `d:/Development/RemRam/remram/docs/ai-context/recipes/service.md` | Standard service implementation recipe | Explains the repository split so validation can distinguish Cortex contract issues from service-definition issues. |
| `d:/Development/RemRam/remram/docs/overview/deployment-models.md` | Appliance deployment and snapshot model | Useful for understanding where service-level OpenSearch backups fit relative to gateway-managed runtime snapshots. |
| `d:/Development/RemRam/remram/docs/operations/operator-workflow.md` | Canonical operator flow | Confirms the real operator path the tests should use instead of drifting into ad hoc Docker-only validation. |
| `d:/Development/RemRam/remram/reference/cli-reference.md` | CLI contract baseline | Locks the command tree that validation should treat as public contract, including `moltbox gateway service ...` and `moltbox opensearch ...`. |
| `d:/Development/RemRam/remram/docs/testing/cli-test-plan.md` | CLI wrapper validation model | Helps this plan distinguish full service-lifecycle validation from thin-wrapper CLI validation. |
| `d:/Development/RemRam/remram/docs/audits/cli-contract-audit.md` | Live CLI evidence baseline | Shows that the documented `moltbox opensearch --version` passthrough has already succeeded in live validation. |
| `d:/Development/RemRam/remram/platform/services/opensearch/README.md` | Current platform-level service summary | Useful baseline for operator expectations and current service framing. |
| `d:/Development/RemRam/remram/platform/services/opensearch/spec.md` | Current platform OpenSearch spec | Useful baseline for validating where the Cortex requirements are stricter than the present service posture. |
| `d:/Development/RemRam/remram/platform/services/opensearch/operator-guide.md` | Existing operator workflow | Useful for validating that the test steps match the intended operator control path. |
| `d:/Development/RemRam/remram/platform/services/opensearch/test-plan.md` | Existing platform validation | Useful for aligning Cortex validation with appliance-level service-health checks. |

### 2.3 Live Service Definition Surfaces

These are the files most likely to be inspected or changed during implementation work outside this repository.

| File | Used For | Why It Matters To This Task |
| --- | --- | --- |
| `d:/Development/RemRam/moltbox-services/services/opensearch/service.yaml` | Service registration metadata | Tells the validator which service identity and container names the gateway is actually deploying. |
| `d:/Development/RemRam/moltbox-services/services/opensearch/compose.yml.template` | Actual container topology and runtime posture | This is where resource limits, mounts, health checks, networking, and security posture really live. |
| `d:/Development/RemRam/moltbox-services/services/opensearch/Dockerfile` | Service image build surface | This is the place to verify or add plugin/tooling changes rather than hand-editing a running container. |

## 3. Required Test Areas

### 3.1 Service And Bootstrap

- `moltbox gateway service deploy opensearch` deploys the shared service successfully
- `moltbox gateway service status opensearch` reports a healthy service after deploy
- OpenSearch service is reachable from Cortex after gateway deployment
- cluster health can be queried successfully after deploy
- cluster health is acceptable for a single-node deployment and not left in an unexplained `red` state
- readiness checks can distinguish unreachable, reachable-but-unbootstrapped, and bootstrapped states
- bootstrap creates the required versioned indexes and stable aliases
- bootstrap is idempotent across repeated runs
- service health and Cortex bootstrap state can be distinguished cleanly

### 3.2 Tooling, CLI, And Plugin Posture

- `moltbox opensearch --version` proves native CLI passthrough reachability
- the implementation thread can point to one documented command path for health, index inventory, temporary index lifecycle, and snapshot inspection
- the exact command(s) used for temporary index create and delete are captured as test evidence for reuse
- plugin inventory exposes `opensearch-knn`
- plugin inventory exposes `opensearch-security`
- plugin inventory exposes `opensearch-sql`
- plugin inventory exposes `opensearch-index-management`
- plugin inventory exposes `opensearch-performance-analyzer`
- version and plugin inventory can be inspected through the Moltbox control plane
- Cortex vector mappings can be created with the intended `knn_vector` posture
- the MVP path does not require ML Commons or Neural Search features to be enabled

### 3.3 Resource, Storage, Backup, And Security Posture

- rendered service config or live container state shows the intended 64 GiB memory allocation
- rendered service config or live container state shows the intended 4 CPU cores
- no GPU device requirement is present
- the OpenSearch data path resolves to the dedicated NVMe-backed storage target
- the backup repository path resolves to the intended subdirectory on the separate 14 TB backup HDD
- `path.repo` is configured for the mounted backup path
- the snapshot repository can be registered and verified successfully
- one nightly snapshot-management policy exists with explicit retention
- one snapshot can be triggered or awaited successfully and reaches a completed success state
- one throwaway restore drill succeeds from the registered snapshot repository
- host `vm.max_map_count` satisfies OpenSearch requirements
- heap and memory-lock settings render as expected
- the Security plugin is enabled
- initial admin credentials are injected through Moltbox-managed secrets or an equivalent secret path
- a dedicated Cortex service account and role can authenticate successfully
- the Cortex service account has the least-privilege permissions needed for Cortex bootstrap and normal read/write paths

### 3.4 Schema Compatibility

- the knowledge index mapping is created successfully
- the retrieval-trace index mapping is created successfully
- governance fields are exact-match or bounded field types
- typed signal fields are indexed as analyzed text
- typed signal fields expose exact subfields for debugging
- provenance and typed-link fields are accepted as structured objects
- vector-capable fields are accepted when vector support is enabled

### 3.5 Write, Read, And Permission Behavior

- a temporary `cortex-smoke-*` index can be created through the documented operator path
- the same temporary `cortex-smoke-*` index can be listed, inspected, and deleted through that same path
- the exact credential path for that lifecycle is clear in the evidence
- the operator or admin credential has the permissions needed for snapshot and smoke-index administration
- the Cortex service account has the permissions needed for Cortex bootstrap against Cortex-owned indexes and aliases
- a knowledge document can be inserted by stable ID
- a knowledge document can be updated by stable ID without duplicate-write ambiguity
- a small bulk document set can be indexed successfully
- newly written documents become searchable after the expected refresh behavior
- a knowledge document can be fetched directly by ID
- provenance can be queried by `artifact_id`
- a retrieval trace document can be written and read back

### 3.6 Query Compatibility

- lexical queries over typed signal fields return the expected match
- lexical queries over `statement` and `summary` return the expected match
- governance filters exclude wrong-scope documents before ranking matters
- retrieval-path queries execute without schema errors
- lexical retrieval still works when vector input is omitted

### 3.7 Diagnostics

- gateway deploy and status output can be captured for debugging
- the exact CLI or HTTP command path used for health, snapshot inspection, and temporary index lifecycle can be captured for debugging
- current aliases can be inspected
- current mappings can be inspected
- snapshot repository and snapshot-policy state can be inspected
- raw query responses can be captured for debugging
- persisted retrieval traces can be inspected after a test query

## 4. Acceptance Scenario

1. run `moltbox gateway service deploy opensearch`
2. run `moltbox gateway service status opensearch` and confirm the service is healthy
3. query cluster health and confirm the cluster is reachable and healthy enough for single-node operation
4. run `moltbox opensearch --version`
5. identify and record the documented operator command path for health, index inventory, snapshot inspection, and temporary index lifecycle
6. inspect version and plugin inventory through the Moltbox control plane
7. confirm the rendered service posture matches:
   - 64 GiB memory
   - 4 CPU cores
   - dedicated NVMe-backed data path
   - dedicated backup-HDD snapshot path
   - no GPU requirement
8. verify `path.repo`, register the filesystem snapshot repository, and confirm the repository verifies successfully
9. verify or create the nightly snapshot-management policy with explicit retention
10. authenticate with the initial admin credential and provision or verify the Cortex service account and role
11. create a temporary `cortex-smoke-<id>` index using the documented operator path
12. insert one sentinel document into that temporary smoke index
13. confirm the smoke index can be listed and the sentinel document can be read back
14. trigger or wait for one snapshot execution that includes the smoke index and confirm the snapshot reaches a success state
15. delete the original smoke index
16. restore the snapshot into a throwaway restore target and confirm the sentinel document is readable again
17. clean up the restored smoke index
18. run the Cortex bootstrap path using the Cortex service account
19. confirm the knowledge and retrieval-trace aliases resolve to versioned indexes
20. index a small sample knowledge set containing:
   - one OpenTrails lodging idea in the correct governance scope
   - one unrelated document in the same owner scope
   - one similar document outside the allowed governance scope
21. index one retrieval-trace sample for the test query
22. run a governance-filtered lexical query such as `places to stay while hiking`
23. fetch the winning knowledge document by ID
24. query provenance by `artifact_id`

Expected result:

- the service deploy and status path succeeds through the Moltbox CLI
- cluster health is queryable after deploy
- native CLI passthrough is reachable through Moltbox
- the operator-ready command path for routine index administration is identified and recorded
- the required plugin/tooling set is present
- the service runs with the intended memory, CPU, and storage posture
- the snapshot repository and nightly backup policy are active against the mounted backup path
- a smoke snapshot succeeds and a throwaway restore drill proves the backup is usable
- security is enabled and the Cortex service account authenticates successfully
- the temporary smoke index can be created, inspected, and deleted without additional setup work
- the OpenTrails lodging idea is indexed and returned
- the wrong-scope document is excluded by governance filters
- the query executes without schema mismatch
- the winning document can be reopened by ID
- the trace record and provenance are inspectable

## 5. Optional Vector Scenario

If vector support is enabled in the local OpenSearch configuration:

- index sample embeddings for the same document set
- run the same query with vector assist enabled
- confirm the mapping accepts vector fields and the query still succeeds

Expected result:

- vector assist can contribute to retrieval
- lexical retrieval remains valid and queryable even without relying on vector-first behavior

## 6. Failure Conditions

- service deploy fails through the gateway pipeline
- service status never becomes healthy after deploy
- cluster health cannot be queried after deploy
- cluster health remains `red` or otherwise unhealthy for single-node operation without a clear documented explanation
- native CLI passthrough is unreachable or undocumented
- no documented command path exists for routine index administration and snapshot inspection
- required plugins or operator tooling are missing
- the live resource posture drifts from the intended 64 GiB, 4-core, dedicated-NVMe target
- the data path is mounted to the wrong storage target
- the backup repository path is missing, mis-mounted, or points at the wrong device
- snapshot repository verification fails
- the nightly snapshot policy is missing or retention is undefined
- a backup can be configured but cannot complete a successful smoke snapshot
- a smoke snapshot succeeds but a throwaway restore drill fails
- the Security plugin remains disabled
- the Cortex service account cannot authenticate or lacks required permissions
- the documented operator credentials cannot create, inspect, or delete a temporary smoke index
- service is unreachable from Cortex
- bootstrap is not idempotent
- required indexes or aliases are missing
- mapping rejects governance, typed-signal, provenance, link, or ranking fields
- upsert behavior creates ambiguous duplicates for the same stable ID
- governance filters fail to exclude wrong-scope documents
- retrieval queries fail because the index shape is incompatible
- lexical retrieval depends on vector support to function at all
- retrieval traces cannot be persisted or inspected

## 7. Test Outputs

- gateway deploy and status evidence
- cluster-health evidence
- native CLI passthrough evidence
- exact operator command-path evidence for health, snapshot inspection, and smoke-index lifecycle
- version and plugin-inventory evidence
- rendered resource and storage posture evidence
- snapshot repository, snapshot policy, snapshot success, restore-drill, and retention evidence
- temporary smoke-index create/inspect/delete evidence
- security bootstrap and Cortex service-account evidence
- service startup and readiness evidence
- alias-resolution evidence
- knowledge-index mapping sample
- retrieval-trace mapping sample
- sample indexed knowledge documents
- sample query request and result
- sample provenance lookup
- sample retrieval-trace record
