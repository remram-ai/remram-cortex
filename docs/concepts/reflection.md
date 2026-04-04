# Reflection

Reflection is the branching post-runtime interpretation layer.

It is how runtime evidence becomes:

- staged notions for durable memory
- artifact impacts
- semantic checkpoints and continuity compression
- governed preference-policy updates

## Trigger

Reflection runs after execution boundaries such as:

- turn end
- session end
- explicit checkpoints
- compaction-related boundaries when needed

## Inputs

Reflection should read:

- raw evidence from the runtime evidence log
- the High-Signal Mamba stream
- existing durable memory when reconciliation requires it
- artifact support when the update touches Layer 4 or Layer 5

## Outputs

Reflection should branch one evidence feed into:

1. memory updates
2. artifact impacts
3. context compression products
4. governed preference-policy updates

Oversight should observe the same semantic products in parallel.

## Memory Path

The normal reflection memory path is:

1. derive a candidate notion from the semantic checkpoint stream
2. stage it
3. optionally expose it early as tentative cross-thread memory if the signal is high
4. reconcile it later against stronger evidence

## Compression Path

Reflection is also where the High-Signal Mamba stream is produced.

That stream exists so most consumers do not need raw evidence directly.

## What Reflection Does Not Do

Reflection does not make every semantic output automatically durable.

It also does not replace the slower reconciliation and maintenance work of the dream cycle.

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Semantic Signature](semantic-signature.md)
- [Typed Signals](typed-signals.md)
- [Artifact Intake](artifact-intake.md)
- [Dream Cycle](dream-cycle.md)
- [Artifact Promotion](artifact-promotion.md)
- [High-Signal Mamba Stream](high-signal-mamba-stream.md)
