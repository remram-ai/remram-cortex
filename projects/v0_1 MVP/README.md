# Cortex v0.1 MVP Project

This folder is the execution package for the first real Cortex slice.

The project goal is to land an operational memory system that can move from:

`ingest this document`

to:

`answer this question in the context of that document implicitly`

without forcing the user to manually restate the document every time.

## Narrative Overview

The project progresses capability by capability, with each layer making the next layer possible.

It starts with usable infrastructure. OpenSearch gives Cortex a real retrieval substrate. The Git provider gives Cortex a concrete local-first artifact provider. Artifact Storage then creates stable Cortex artifact identity so imported and captured artifacts are addressable by Cortex ID instead of file path.

Once storage exists, Cortex can form memory from evidence. Artifact Intake turns imported documents into bounded, source-linked slices. Knowledge Extraction turns those slices into structured knowledge objects with typed signals, signatures, provenance, and links. Quick Capture proves the same write path works for new thoughts, not just imported documents.

After the write path is real, the read path can become useful. Retrieval turns the stored structure into bounded, inspectable knowledge bundles. Chat Injection proves those bundles can influence a live answer before prompt build. Chat Interface provides the visible proof surface: a minimal chat harness that later can be swapped for an OpenClaw chat agent integration without changing Cortex semantics.

The project only counts as successful when these capabilities add up to one coherent behavior: import a document, consolidate it into durable memory, and later answer ordinary questions in its context as if the system remembers it.

## Capability Sequence

- [01 OpenSearch Service](capabilities/01-opensearch-service/spec.md)
- [02 Git Provider](capabilities/02-git-provider/spec.md)
- [03 Artifact Storage](capabilities/03-artifact-storage/spec.md)
- [04 Artifact Intake](capabilities/04-artifact-intake/spec.md)
- [05 Knowledge Extraction](capabilities/05-knowledge-extraction/spec.md)
- [06 Quick Capture](capabilities/06-quick-capture/spec.md)
- [07 Retrieval](capabilities/07-retrieval/spec.md)
- [08 Chat Injection](capabilities/08-chat-injection/spec.md)
- [09 Chat Interface](capabilities/09-chat-interface/spec.md)

## Documents

- [Project Plan](project-plan.md)
- [Test Plan](test-plan.md)
- [Capability Packs](capabilities/README.md)

## Design Inputs

- [MVP Scope](../../docs/design/v0_1-mvp-scope.md)
- [MVP Spec](../../docs/design/v0_1-mvp-spec.md)
- [Architecture](../../docs/remram-cortex/architecture.md)
