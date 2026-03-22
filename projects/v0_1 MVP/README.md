# Cortex v0.1 MVP Project

This folder is the execution package for the first real Cortex slice.

The project goal is to land an operational memory system that can move from:

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

## Capability Sequence

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

## Documents

- [Seed Prompt](seed-prompt.md)
- [Project Plan](project-plan.md)
- [Test Plan](test-plan.md)
- [Capability Packs](capabilities/README.md)

## Design Inputs

- [MVP Scope](../../docs/design/v0_1-mvp-scope.md)
- [MVP Spec](../../docs/design/v0_1-mvp-spec.md)
- [Architecture](../../docs/remram-cortex/architecture.md)
