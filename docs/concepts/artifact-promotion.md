# Artifact Promotion

Artifact promotion is the process of turning stabilized Layer 4 work into a Layer 5 `authored_artifact`.

Promotion is the point where authored canon becomes warranted for a specific body of work.

It is not the same as:

- runtime evidence capture
- reference intake
- owned-source intake

Those are intake flows.

Promotion is the authored publication flow.

## When Promotion Makes Sense

Promotion is appropriate when the result is:

- stable across multiple runs
- reusable by humans or other systems
- reviewable and worth versioning
- better expressed as a document, spec, or other durable artifact

## Promotion Rule

Not every knowledge object or workspace should be promoted.

Layer 4 remains the operational authority during active work.

Promotion is for work that benefits from:

- canonical authorship
- revision history
- stable outward reuse
- explicit maintenance as canon

## After Promotion

Promotion requires review and approval before publish.

In the current architecture, `Git` is introduced in the promotion phase as the first backend for authored canon.

Once promotion happens:

- the authored artifact becomes the canonical source for that body
- Layer 4 remains the operational working body around it
- Layer 3 keeps support, supersession, and semantic relationships around it

That means promotion is not a one-way archive move.

Meaningful canonical revision must be able to:

- re-enter Layer 4 operational knowledge through reprocessing
- trigger Layer 3 semantic reconciliation where support, summaries, or supersession are affected

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Artifact Intake](artifact-intake.md)
- [Artifact Provider](artifact-provider.md)
- [Reflection](reflection.md)
- [Dream](dream-cycle.md)
- [Knowledge And Artifact Architecture](../design/knowledge-and-artifact-architecture.md)
