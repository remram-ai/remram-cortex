# Cortex v0.1 MVP Project

This folder is the execution package for the first real Cortex slice.

## Project Goal

Land an operational memory system that can move from:

`ingest this document`

to:

`answer this question in the context of that document implicitly`

without forcing the user to manually restate the document every time.

## Narrative Overview

The project progresses capability by capability, with each layer making the next layer possible.

It starts with usable infrastructure. OpenSearch gives Cortex a real retrieval substrate. Artifact Storage defines the Cortex-owned provider contract and stable artifact identity so imported and captured artifacts are addressable by Cortex ID instead of file path. Git Service gives the project the concrete local Git repository mechanics it can build on. Git Provider uses that service as the safe default local provider. Google Drive Provider expands the same provider model into collaborative document territory without changing Cortex artifact identity.

Once storage exists, Cortex can form memory from evidence. Artifact Intake turns imported documents into bounded, source-linked slices. Knowledge Extraction turns those slices into structured knowledge objects with typed signals, signatures, provenance, and links. Quick Capture proves the same write path works for new thoughts, not just imported documents.

After the write path is real, the read path can become useful. Retrieval turns the stored structure into bounded, inspectable knowledge bundles. Chat Injection proves those bundles can influence a live answer before prompt build. Chat Interface provides the visible proof surface: a minimal chat harness that later can be swapped for an OpenClaw chat agent integration without changing Cortex semantics.

The project only counts as successful when these capabilities add up to one coherent behavior: import a document, consolidate it into durable memory, and later answer ordinary questions in its context as if the system remembers it.

## Definition Of Done

The project is done when:

- required services are operational enough for Cortex MVP work
- imported and captured artifacts resolve through Cortex-owned identity
- knowledge extraction produces durable structured knowledge with provenance
- retrieval returns bounded, inspectable results that honor the Cortex retrieval model
- at least one chat proof surface shows a materially better answer because Cortex retrieval ran first
- provenance and retrieval traces remain inspectable enough to debug the result

## Primary User Stories

- As a user, I can ingest a document once and later ask ordinary questions without restating its contents.
- As a user, I can add a quick capture and have Cortex reinforce or extend the existing knowledge base.
- As an operator, I can bring up the required service dependencies and confirm they are healthy and usable.
- As a developer or tester, I can inspect provenance, retrieval traces, and service posture when behavior is wrong.
- As a reviewer, I can see a visible before-and-after proof that Cortex improved a chat answer.

## Start Here

- If you are evaluating the MVP, read this file, then [Acceptance Test](acceptance-test.md), then [Runtime Docs](runtime-docs.md).
- If you are implementing an epic, read this file, then [Project Plan](project-plan.md), then the specific epic folder, then the relevant product spec and regression plan.
- If you are starting an AI thread, read [Seed Prompt](seed-prompt.md) after this file and follow its scoped reading order.

## Canonical Product References

The stable Cortex design surface now lives under [../../product/](../../product/README.md).

The MVP still executes in this order:

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

## Epic Sequence

This project executes epic by epic.

Current epic order:

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

## Execution Documents

- [Seed Prompt](seed-prompt.md)
- [Project Plan](project-plan.md)
- [Acceptance Test](acceptance-test.md)
- [Acceptance Test Data](acceptance-test.json)
- [Runtime Docs](runtime-docs.md)
- [Epic Records](epics/README.md)
- [Acceptance Tests](acceptance-tests/)

Project artifact roles:

- `README.md` is the charter and reader entry point
- `project-plan.md` sequences the epics
- `acceptance-test.md` explains project-level acceptance
- `acceptance-test.json` is the executable acceptance inventory with stable test IDs
- `acceptance-tests/` stores executed acceptance and HAT records
- `epics/` holds epic implementation plans, epic test plans, their structured companions, and epic test artifacts

## Design Inputs

- [MVP Scope](../../docs/design/v0_1-mvp-scope.md)
- [MVP Spec](../../docs/design/v0_1-mvp-spec.md)
- [Architecture](../../docs/remram-cortex/architecture.md)
