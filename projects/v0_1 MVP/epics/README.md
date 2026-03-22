# Epic Records

This folder holds the epic-scoped execution package for `v0_1 MVP`.

Read the project [README.md](../README.md) first for the charter and [project-plan.md](../project-plan.md) for the sequence. Then use a specific epic folder as the local execution package.

Each epic should contain:

- `README.md`
- `implementation-plan.md`
- `implementation-plan.json` once the epic enters active execution
- `test-plan.md`
- `test-plan.json` once the epic enters active execution
- `tests/`

Each epic stores its executed test artifacts directly under `tests/`, for example:

- `tests/001-test-result-ddmmyyyy.md`
- `tests/002-test-result-ddmmyyyy.md`

Use the markdown files for context and the JSON companions for stable IDs, procedures, and execution inventory when an epic becomes active.

Current epic set:

1. [01 OpenSearch Service](01-opensearch-service/README.md)
2. [02 Git Service](02-git-service/README.md)
3. [03 Artifact Storage](03-artifact-storage/README.md)
4. [04 Git Provider](04-git-provider/README.md)
5. [05 Google Drive Provider](05-google-drive-provider/README.md)
6. [06 Artifact Intake](06-artifact-intake/README.md)
7. [07 Knowledge Extraction](07-knowledge-extraction/README.md)
8. [08 Quick Capture](08-quick-capture/README.md)
9. [09 Retrieval](09-retrieval/README.md)
10. [10 Chat Injection](10-chat-injection/README.md)
11. [11 Chat Interface](11-chat-interface/README.md)
