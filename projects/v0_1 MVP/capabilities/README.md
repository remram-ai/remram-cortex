# Capability Packs

This folder holds the capability-level delivery artifacts for the Cortex v0.1 MVP.

Each capability should live in its own numbered folder so the project reads in build order and so each capability has room for more than just a spec and a test plan later.

## Folder Contract

Each capability folder should contain at least:

- `spec.md`
- `test-plan.md`

Additional artifacts such as API notes, sample payloads, diagrams, or implementation checklists can be added later inside the same capability folder.

## Capability Order

1. `01-opensearch-service`
2. `02-git-provider`
3. `03-artifact-storage`
4. `04-artifact-intake`
5. `05-knowledge-extraction`
6. `06-quick-capture`
7. `07-retrieval`
8. `08-chat-injection`
9. `09-chat-interface`

## Source Documents

- [MVP Scope](../../../docs/design/v0_1-mvp-scope.md)
- [MVP Spec](../../../docs/design/v0_1-mvp-spec.md)
- [Architecture](../../../docs/remram-cortex/architecture.md)
