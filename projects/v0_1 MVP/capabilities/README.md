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
2. `02-artifact-storage`
3. `03-git-service`
4. `04-git-provider`
5. `05-google-drive-provider`
6. `06-artifact-intake`
7. `07-knowledge-extraction`
8. `08-quick-capture`
9. `09-retrieval`
10. `10-chat-injection`
11. `11-chat-interface`

## Source Documents

- [MVP Scope](../../../docs/design/v0_1-mvp-scope.md)
- [MVP Spec](../../../docs/design/v0_1-mvp-spec.md)
- [Architecture](../../../docs/remram-cortex/architecture.md)
