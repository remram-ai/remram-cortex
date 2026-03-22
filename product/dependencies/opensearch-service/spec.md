# OpenSearch Service Dependency Spec

## 1. Purpose

Provide the OpenSearch-backed indexing and query substrate Cortex uses for knowledge retrieval, bounded candidate search, and retrieval debugging.

This capability exists to make the locked Cortex retrieval model operational, not to turn Cortex into a raw document or vector store.

## 2. Context Pack

This is the minimum context pack an implementation thread should load before changing the OpenSearch service contract or its Cortex integration.

### 2.1 Cortex MVP And Architecture Sources

| File | Used For | Why It Matters To This Task |
| --- | --- | --- |
| `projects/v0_1 MVP/README.md` | MVP narrative and capability order | Confirms OpenSearch is the foundation capability and should stay scoped to retrieval substrate concerns. |
| `projects/v0_1 MVP/project-plan.md` | MVP deliverables and workstreams | States the concrete OpenSearch workstream: stand up the service, define mappings, and verify connectivity. |
| `projects/v0_1 MVP/test-plan.md` | Umbrella MVP acceptance | Shows how OpenSearch readiness is consumed by the broader import, retrieval, and chat proof loop. |
| `product/dependencies/README.md` | Product dependency contract | Confirms this spec and its paired regression plan are part of the Cortex dependency surface rather than a project-local capability pack. |
| `product/capabilities/retrieval/spec.md` | Retrieval-stage contract | OpenSearch must support the Cortex retrieval stack: governance first, typed signals, vector assist, and traces. |
| `docs/design/v0_1-mvp-scope.md` | MVP boundary and success criteria | Locks the OpenSearch role in the MVP and keeps it from growing into a parallel memory product. |
| `docs/design/v0_1-mvp-spec.md` | MVP data and flow contract | Defines the OpenSearch document shape and the artifact-intake, extraction, and retrieval loops the service must support. |
| `docs/remram-cortex/architecture.md` | Canonical Cortex architecture | The most important design source for governance filters, typed signals, semantic signature, vector assist, and OpenSearch ownership boundaries. |
| `docs/glossary.md` | Locked vocabulary | Prevents drift in terms like governance field, typed signal, semantic signature, retrieval trace, and knowledge object. |
| `docs/concepts/bounded-retrieval.md` | Retrieval-stage narrowing model | Explains why OpenSearch queries must be filter-first and why vector search stays subordinate. |
| `docs/concepts/governance-fields.md` | Hard-filter semantics | Clarifies which fields must behave like eligibility gates rather than fuzzy ranking inputs. |
| `docs/concepts/typed-signals.md` | Primary retrieval surface | Defines the fixed signal fields that drive the main OpenSearch scoring surface. |
| `docs/concepts/semantic-signature.md` | Soft routing bias | Clarifies that signature is a score bias, not a hard gate, which affects mapping and query design. |
| `docs/design/cortex-inspection-surfaces.md` | Inspection and debug expectations | Explains why retrieval traces, searchable objects, and provenance inspection are part of the service contract. |

### 2.2 Platform And Deployment Boundary Sources

These files live outside `remram-cortex` but are required context because this capability is deployed through the standard Moltbox service path.

| File | Used For | Why It Matters To This Task |
| --- | --- | --- |
| `d:/Development/RemRam/remram/docs/concepts/gateway.md` | Gateway control-plane model | Defines the canonical operator path for deploy, restart, status, and secret-managed service lifecycle. |
| `d:/Development/RemRam/remram/docs/concepts/service.md` | Service concept and lifecycle | Confirms OpenSearch is a first-class appliance service and that `moltbox opensearch <native command>` is the thin passthrough model. |
| `d:/Development/RemRam/remram/docs/concepts/snapshot.md` | Existing Moltbox snapshot vocabulary | Helps implementation threads avoid conflating runtime checkpoint snapshots with OpenSearch index snapshots and backups. |
| `d:/Development/RemRam/remram/docs/ai-context/recipes/service.md` | Standard service implementation recipe | Locks the repository split across `remram-cortex`, `moltbox-services`, `moltbox-gateway`, and `moltbox-runtime`. |
| `d:/Development/RemRam/remram/docs/overview/deployment-models.md` | Appliance deployment and snapshot model | Important for understanding where service-level backup behavior fits relative to gateway-managed runtime snapshot behavior. |
| `d:/Development/RemRam/remram/docs/operations/operator-workflow.md` | Canonical workstation operator flow | Confirms the intended SSH -> Moltbox CLI -> Gateway path and keeps this capability aligned with the real operator surface. |
| `d:/Development/RemRam/remram/reference/cli-reference.md` | CLI command contract | Locks the public Moltbox command tree, including `gateway service ...`, scoped secrets, and the `moltbox opensearch ...` passthrough namespace. |
| `d:/Development/RemRam/remram/docs/testing/cli-test-plan.md` | CLI validation discipline | Useful when defining how much evidence is required to treat the OpenSearch CLI surface as operationally ready rather than merely documented. |
| `d:/Development/RemRam/remram/docs/audits/cli-contract-audit.md` | Live CLI evidence baseline | Shows that `moltbox opensearch --version` and the broader CLI contract have already been exercised successfully on a real appliance. |
| `d:/Development/RemRam/remram/platform/services/opensearch/README.md` | Current platform-level service summary | Shows the present operator framing and service boundary that Cortex must fit into. |
| `d:/Development/RemRam/remram/platform/services/opensearch/spec.md` | Current platform OpenSearch spec | Captures the baseline appliance posture and highlights where Cortex now needs stronger requirements. |
| `d:/Development/RemRam/remram/platform/services/opensearch/operator-guide.md` | Existing operator workflow | Useful when defining the final control-plane and diagnostics surface for implementation. |
| `d:/Development/RemRam/remram/platform/services/opensearch/test-plan.md` | Existing platform validation | Useful for aligning Cortex acceptance with the appliance-level deploy and health expectations. |

### 2.3 Live Service Definition Surfaces

These are the files most likely to be edited during implementation work outside this repository.

| File | Used For | Why It Matters To This Task |
| --- | --- | --- |
| `d:/Development/RemRam/moltbox-services/services/opensearch/service.yaml` | Service registration metadata | Declares the compose project, container names, and deploy-time service identity consumed by the gateway. |
| `d:/Development/RemRam/moltbox-services/services/opensearch/compose.yml.template` | Actual container topology and runtime posture | This is where memory, CPUs, mounts, health checks, security-plugin posture, and internal networking are really expressed. |
| `d:/Development/RemRam/moltbox-services/services/opensearch/Dockerfile` | Service image build surface | This is the place to bake required plugins or CLI tooling into the image rather than mutating a live container manually. |

## 3. Capability Boundary

This capability is responsible for:

- bringing up one OpenSearch service usable by local Cortex development
- depending on the standard Moltbox service deployment pattern rather than ad hoc Docker handling
- defining the OpenSearch indexes and mappings Cortex depends on for MVP retrieval
- storing knowledge documents, retrieval metadata, and retrieval traces
- supporting filter-first lexical retrieval with optional vector assist
- exposing enough diagnostics to debug schema and query behavior

This capability is not responsible for:

- storing raw artifact bytes
- reflection or merge decisions
- prompt assembly or chat UX
- choosing the embedding model itself

## 4. MVP Deliverable

The MVP deliverable for this capability is:

- one Moltbox-managed single-node OpenSearch service that Cortex can reach reliably
- one idempotent bootstrap path that creates the required indexes and aliases
- one knowledge-document mapping aligned to governance-first, typed-signal-first retrieval
- one trace storage path for retrieval debugging
- one query path that works lexically even when vector assist is unavailable

The implementation should be practical to operate from Go and should not require OpenSearch-native complexity that the rest of the MVP does not yet need.

## 5. Deployment Boundary

This capability must use the standard Moltbox service pattern.

Repository ownership should stay split as follows:

- `remram-cortex` defines the Cortex-side contract, index shape, and retrieval expectations
- `moltbox-services` owns the `opensearch` service definition, compose topology, and container build inputs
- `moltbox-gateway` owns deploy, restart, status, and deployment metadata behavior
- `moltbox-runtime` owns runtime-facing configuration that points clients at the service

Cortex should not embed a parallel service definition inside this repository.
It should describe the contract it needs from the shared `opensearch` service and consume that service over the appliance network.

## 6. Service Requirements

### 6.1 Local Runtime Shape

The first implementation should assume:

- one single-node OpenSearch container managed as the `opensearch` appliance service
- deployment through `moltbox gateway service deploy opensearch`
- status and health inspection through `moltbox gateway service status opensearch`
- optional native CLI passthrough through `moltbox opensearch <native command>`
- persistence on a service data volume rather than container-local ephemeral state
- internal-only networking on the appliance service network
- no high-availability behavior
- replica settings appropriate for a single-node deployment

Direct Docker commands are an implementation detail, not the normal operator path.

The service must expose enough readiness information for Cortex startup checks to distinguish:

- service unreachable
- service reachable but unbootstrapped
- service bootstrapped and ready for reads and writes

Service health and Cortex index bootstrap are separate states.
A healthy `opensearch` container does not by itself mean the Cortex indexes and aliases exist yet.

### 6.2 Bootstrap Behavior

OpenSearch bootstrap must be idempotent.

Running bootstrap repeatedly must not corrupt existing mappings or require operators to delete indexes manually.

The practical MVP pattern should be:

- create a versioned knowledge index such as `cortex-knowledge-v1`
- create a stable alias such as `cortex-knowledge-current`
- create a versioned retrieval-trace index such as `cortex-retrieval-trace-v1`
- create a stable alias such as `cortex-retrieval-trace-current`

Versioned indexes plus stable aliases keep schema evolution possible without changing every Cortex caller.

The expected operational sequence is:

1. deploy or confirm the shared `opensearch` service through the gateway
2. verify the service is healthy
3. run Cortex index bootstrap
4. verify aliases and mappings

### 6.3 Required Tool And Plugin Posture

The MVP should use the standard OpenSearch distribution rather than the minimal distribution.

The Cortex retrieval stack should rely on the following OpenSearch capabilities:

- core query DSL, filters, bulk APIs, aliases, mappings, and BM25-style lexical scoring
- the bundled `k-NN` plugin for `knn_vector` fields and assistive vector search
- the bundled Security plugin for authenticated service access and least-privilege roles
- the bundled SQL plugin for operator-side inspection and debugging when needed
- the bundled Index Management plugin for snapshot-management policies
- the bundled Performance Analyzer plugin for node-level diagnostics

The MVP should not depend on:

- ML Commons or Neural Search for embedding generation or retrieval orchestration
- Dashboards-only administration as the primary control path
- ingest-time artifact parsing inside OpenSearch
- extra analysis plugins unless the corpus proves a concrete need

For the initial Cortex vector posture, prefer `knn_vector` with a Lucene/HNSW method definition.

That is the practical MVP default because:

- Cortex uses vectors as assistive scoring, not as the primary retrieval authority
- governance filters already bound the candidate set before vector search matters
- Lucene is a good fit for smaller deployments and filter-friendly search behavior

Faiss remains a future path if corpus scale or measured retrieval latency justifies the added operational complexity.

If additional plugins are later required, they must be baked into the Docker image in `moltbox-services`.
They should not be installed manually on a running appliance host.

### 6.4 Resource And Storage Posture

The initial appliance allocation for the shared `opensearch` service should be:

- 64 GiB of service memory
- 4 CPU cores
- no GPU devices
- one dedicated OpenSearch data path on the hottest CPU-local NVMe-backed SSD available on the appliance

The JVM heap should not consume the full 64 GiB allocation because Lucene, `k-NN`, and the filesystem cache all need native memory outside the heap.

A practical starting posture is:

- `OPENSEARCH_JAVA_OPTS=-Xms31g -Xmx31g`
- `bootstrap.memory_lock=true`

That keeps the heap close to half of the service memory while preserving room for native memory and page cache.

The service definition should also ensure:

- `vm.max_map_count >= 262144` on the host
- `nofile >= 65536`
- effective unlimited memlock when memory locking is enabled
- `/dev/shm` is sized appropriately if Performance Analyzer remains enabled
- the data path does not land on a network filesystem

### 6.5 Backup And Snapshot Posture

The shared `opensearch` service should have a built-in backup path using OpenSearch snapshots rather than raw filesystem copies of the live data directory.

The initial backup posture should be:

- one filesystem snapshot repository mounted into the container from the dedicated backup HDD
- one nightly snapshot-management policy configured inside OpenSearch
- bounded retention so OpenSearch backups do not consume the full backup drive
- API-managed snapshot creation and deletion rather than manual file deletion inside the repository path

The practical first-pass design is:

- host backup mount rooted on the separate 14 TB spinning disk
- one dedicated OpenSearch subdirectory on that disk rather than handing the entire disk directly to the container
- container mount such as `/mnt/opensearch-backups`
- `path.repo` configured in `opensearch.yml` for that mount
- one registered snapshot repository of type `fs`
- one nightly Snapshot Management policy for the Cortex indexes

The backup job should be implemented through OpenSearch Snapshot Management or equivalent OpenSearch-native scheduling, not through an ad hoc host cron that copies Lucene files directly.

Retention must be explicit.
The implementation does not need to consume the full 14 TB disk and should preserve headroom for future service growth, recovery artifacts, and operational flexibility.

At minimum, the implementation should define:

- snapshot schedule
- repository path
- repository name
- snapshot naming convention
- retention count or age rules
- restore drill expectations

Manual implementation task:

- bootstrap and verify the host mount for the backup HDD and expose the intended subdirectory to the `opensearch` container through the service definition

That host mount/bootstrap work is expected during implementation because the exact appliance mount inventory is not owned in this repository.

### 6.6 Access And Security Posture

The target MVP deployment should not run with the Security plugin disabled.

Instead, the service should use:

- an initial admin credential injected through Moltbox-managed secrets
- one dedicated Cortex service account and role
- authenticated Cortex access over the appliance network

The Cortex service role should grant only the permissions needed to:

- inspect cluster and alias health needed for startup and bootstrap
- create or update Cortex indexes, mappings, and aliases
- bulk write, refresh, search, and read Cortex knowledge documents and retrieval traces

Steady-state Cortex traffic should use the dedicated service account rather than the admin credential.

The role split should stay explicit:

- the operator or admin path owns snapshot repository registration, snapshot-policy management, plugin inspection, and throwaway smoke-index lifecycle
- the Cortex service account owns Cortex bootstrap plus normal Cortex read and write traffic against Cortex-owned indexes and aliases

If the implementation allows the Cortex service account to manage temporary smoke indexes, that permission should be limited to a narrow Cortex-owned pattern such as `cortex-smoke-*` rather than broad cluster-wide index administration.

Security bootstrap may happen during service deploy or during the first Cortex bootstrap pass, but the secrets and role definitions must not be hard-coded in this repository.

### 6.7 Operator And CLI Surfaces

Operator control should remain on the Moltbox CLI plane:

- `moltbox gateway service deploy opensearch`
- `moltbox gateway service restart opensearch`
- `moltbox gateway service status opensearch`

The thin native passthrough should remain available for OpenSearch-native commands already present in the image.

The operator surface should support at least:

- version inspection
- plugin inventory inspection
- health and CAT-style diagnostics
- snapshot repository and snapshot-policy inspection
- future exposure of `opensearch-cli` through the same control plane if that utility is added to the service image

This capability also requires one documented operator-ready command path for index administration.

By the end of the capability, an implementation thread must not have to guess how to:

- query cluster health
- inspect index inventory
- create a temporary `cortex-smoke-*` index
- delete that temporary `cortex-smoke-*` index
- inspect snapshot repositories, policies, and completed snapshots

The exact command path may be:

- native OpenSearch command passthrough if that is sufficient
- a service-bundled helper exposed through the existing Moltbox service namespace
- an authenticated OpenSearch HTTP client path that is already part of the documented operator workflow

What is not acceptable is relying on undocumented break-glass Docker exec work as the only known way to do normal index administration.

The exact commands do not need to be standardized in this repository, but they do need to be written down in the implementation-facing operator docs and proven by the paired test plan.

By the end of this capability, the service should be operationally ready for follow-on Cortex implementation work.

That means an operator or implementation thread can, without further architecture clarification:

- deploy the service
- confirm cluster health
- access the native passthrough surface through Moltbox
- create a temporary test index using the documented operator path
- delete that temporary test index using the same path

For OpenSearch, index lifecycle is the concrete readiness proof.
If someone says "create a table" in implementation discussion, the actual OpenSearch operation should be understood as "create an index".

## 7. OpenSearch Data Surfaces

### 7.1 Required Indexes

The MVP requires two OpenSearch data surfaces:

- a primary knowledge index for durable knowledge objects and retrieval fields
- a retrieval-trace index for persisted debug records

The knowledge index is mandatory.
The trace index is also part of the MVP because retrieval must remain inspectable.

### 7.2 Knowledge Document Contract

At minimum, each indexed knowledge document must contain:

- stable knowledge-object identity
- canonical statement and optional summary
- object kind
- governance fields
- typed signal fields
- semantic signature
- ranking metadata
- provenance
- typed links
- timestamps

A practical first-pass document shape is:

```json
{
  "knowledge_id": "ko_...",
  "statement": "Reseller network for trail lodging along hiking routes",
  "summary": "Partnership model for trail lodging inventory",
  "object_kind": "idea",
  "owner_ref": "person:jason",
  "audience": ["person:jason"],
  "knowledge_space": ["project:opentrails"],
  "lifecycle_state": "active",
  "valid_from": "2026-03-21T00:00:00Z",
  "valid_until": null,
  "domain": ["outdoors", "travel"],
  "activity": ["trip planning"],
  "need": ["find places to stay"],
  "object": ["trail lodging"],
  "mechanism": ["reseller network"],
  "semantic_signature": "8a31",
  "confidence": 0.81,
  "freshness_ts": "2026-03-21T00:00:00Z",
  "reinforcement_count": 2,
  "artifact_ids": ["art_..."],
  "provenance": [
    {
      "artifact_id": "art_...",
      "slice_id": "slice_...",
      "source_location": {
        "page": 3,
        "section": "Lodging"
      }
    }
  ],
  "links": [
    {
      "link_type": "relates_to",
      "target_ref": "project:opentrails"
    }
  ],
  "embedding": [0.12, 0.08, 0.44],
  "created_at": "2026-03-21T00:00:00Z",
  "updated_at": "2026-03-21T00:00:00Z"
}
```

This contract is intentionally knowledge-object-shaped.
It must not degrade into transcript chunks or source-document blobs pretending to be durable memory.

### 7.3 Mapping Rules

The mapping must support the retrieval architecture already locked in the repo.

Required mapping rules:

- governance fields such as `owner_ref`, `audience`, `knowledge_space`, and `lifecycle_state` use exact-match or bounded field types such as `keyword`, `boolean`, and `date`
- typed signal fields `domain`, `activity`, `need`, `object`, and `mechanism` are multi-valued analyzed text fields
- typed signal fields should also expose exact subfields for debugging or exact-match use
- `statement` and `summary` remain searchable text fields
- `semantic_signature` is stored in a compact form such as `keyword` or integer-like representation
- ranking fields such as `confidence`, `freshness_ts`, and `reinforcement_count` use numeric or date-friendly types
- provenance and typed links are stored as structured objects that preserve their tuples
- the vector field uses an OpenSearch-supported vector type parameterized by the configured embedding dimensions

The signature field exists for soft routing bias, not as a hard eligibility gate.
The vector field exists for assistive similarity, not as the primary retrieval authority.

### 7.4 Retrieval Trace Contract

The retrieval-trace surface must preserve enough information to inspect what happened during retrieval.

At minimum, a trace record should be able to store:

- request identity and timestamp
- applied governance filters
- the raw query shape or a normalized query summary
- top candidate IDs returned from OpenSearch
- score contributors that Cortex or OpenSearch used
- suppression or truncation notes when the bundle was bounded

The exact trace schema may evolve, but the service must make persisted traces queryable and inspectable during the MVP.

## 8. Query Compatibility Requirements

This capability must support the query patterns required by the retrieval design.

At minimum, OpenSearch must be compatible with:

- `bool.filter` over governance fields before semantic ranking
- lexical scoring over typed signal fields
- lexical matching on `statement` and `summary`
- document fetch by `knowledge_id`
- provenance lookup by `artifact_id`
- optional vector assist inside an already governance-bounded candidate set

The first practical implementation does not need to compute semantic-signature distance inside OpenSearch.
That bias may be applied in Cortex after OpenSearch returns a bounded candidate set.

Relationship expansion also does not need graph-native infrastructure in this capability.
It only needs OpenSearch documents to preserve typed links clearly enough for Cortex to follow them after the primary match.

## 9. Write Requirements

The OpenSearch service must allow Cortex to:

- create indexes and aliases safely
- insert or upsert one knowledge document by stable ID
- bulk write knowledge documents during import or reflection jobs
- read a document back by ID
- refresh the index in a controlled way so new knowledge becomes queryable quickly enough for the MVP loop
- persist retrieval-trace documents

For the MVP, import and capture outputs should become searchable quickly after write completion.
Using explicit refresh behavior at the end of a write path is acceptable if it keeps the system predictable and debuggable.

## 10. Diagnostics And Debuggability

This capability must support operator inspection of:

- service health
- gateway-managed deploy and status results
- index existence
- alias resolution
- current mappings
- sample stored documents
- raw query responses
- persisted retrieval traces

If vector functionality is disabled, misconfigured, or temporarily unavailable, Cortex should still be able to perform lexical retrieval over the same knowledge index.
That degraded mode should be explicit in diagnostics rather than silently changing retrieval behavior.

## 11. Acceptance Requirements

The capability is acceptable for the MVP when all of the following are true:

- the shared `opensearch` service can be deployed and inspected through the Moltbox CLI
- the service image exposes the required tool and plugin posture for Cortex retrieval and diagnostics
- the service runs with the intended 64 GiB, 4-core, dedicated-NVMe posture
- the backup HDD mount and snapshot repository path are configured as intended
- nightly backups are configured through an OpenSearch-native snapshot mechanism with bounded retention
- one backup smoke flow has been proven by successful repository verification, snapshot creation, and restore validation for a throwaway index
- the Security plugin is enabled and Cortex can authenticate with a dedicated service account
- Cortex can connect to a local OpenSearch service reliably
- the documented operator path can confirm cluster health, native CLI reachability, and snapshot state
- the documented operator path can create, inspect, and delete a temporary `cortex-smoke-*` index successfully
- the exact command path for temporary index lifecycle and snapshot inspection is already documented well enough for the next implementation thread to reuse directly
- bootstrap creates the required indexes and aliases idempotently
- the knowledge mapping accepts all required governance, typed-signal, provenance, link, and ranking fields
- sample knowledge documents can be inserted, updated, and queried without schema mismatches
- lexical retrieval works over typed signals and canonical text
- vector-capable mappings are accepted when configured, but vector similarity is not required for basic retrieval success
- retrieval traces can be stored and inspected

## 12. Deferred

The following are deferred beyond this MVP capability:

- multi-node or high-availability deployment
- production-scale shard and index-lifecycle tuning
- graph-native relationship storage
- vector-first retrieval
- complex in-engine signature-distance scoring
