# Product Capabilities

This folder holds the stable Cortex-owned capability definitions.

These are product capabilities, not project artifacts.

If you are working current execution order, acceptance, or proof, use [../../projects/](../../projects/README.md) instead of inferring sequence from this folder.

## Current Capability Set

- [artifact-storage](artifact-storage/spec.md)
- [git-provider](git-provider/spec.md)
- [google-drive-provider](google-drive-provider/spec.md)
- [artifact-intake](artifact-intake/spec.md)
- [knowledge-extraction](knowledge-extraction/spec.md)
- [quick-capture](quick-capture/spec.md)
- [retrieval](retrieval/spec.md)
- [chat-injection](chat-injection/spec.md)
- [chat-interface](chat-interface/spec.md)

## Folder Contract

Each capability folder should contain at least:

- `spec.md`
- `regression-plan.md`

Additional artifacts such as `operator-guide.md`, provider notes, sample payloads, or diagrams may be added when the capability needs them.

When changing a stable capability, update `spec.md` and `regression-plan.md` together unless there is a strong reason not to.

Execution order is project-specific and should be expressed under [../../projects/](../../projects/README.md), not by encoding sequence into these folder names.
