# Cortex v0.1 MVP Project Charter

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

## Authority Chain

- this project charter owns the top-level user need, scope, and definition of done
- `project-plan.md` owns epic breakdown and sequencing
- `epics/<epic>/<component>-requirements.md` owns the epic-local business slice and local definition of done
- `epics/<epic>/<component>-spec.md` owns the epic-local technical design
- `epics/<epic>/implementation-plan.json` owns the epic-local deliverable breakdown once the epic enters active execution
- `epics/<epic>/test-plan.json` owns the epic-local validation model once the epic enters active execution

## Stable Product References

- [MVP Scope](../../docs/design/v0_1-mvp-scope.md)
- [MVP Spec](../../docs/design/v0_1-mvp-spec.md)
- [Architecture](../../docs/remram-cortex/architecture.md)
