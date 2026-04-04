# Reflection

Reflection is the near-time interpretation and maintenance path.

It is how Cortex turns semantic outputs into staged memory, Layer 4 workspace updates, and hot-memory cleanup.

## Sequencing Clarification

Reflection exists before `Mamba`.

In Phase 1 and Phase 2, reflection runs on:

- turn-end semantic processing
- session-end semantic processing
- explicit-checkpoint semantic processing when needed

Later, `Mamba` becomes a better real-time signal source for the same downstream reflection path.

## What Reflection Does

Reflection is allowed to:

- update or stage notions
- prune notions
- merge notions
- demote stale notions
- expire low-value notions
- update Layer 4 operational workspaces
- use Layer 3 relationships to help organize Layer 4 work
- detect promotion candidates

## What Reflection Reads

Reflection may read:

- raw runtime evidence
- boundary-triggered semantic outputs
- the High-Signal Mamba Stream when available
- Layer 2 notions in `QMD`
- existing Layer 3 semantic structure
- Layer 4 workspace state

## What Reflection Does Not Do

Reflection is not:

- the always-on listener
- the only long-horizon maintenance path
- a reason to turn Layer 3 into a body store

Mamba emits signal later.

Reflection consumes signal whenever it is available.

Dream does the slower consolidation pass.

## Reflection And Layer 3

Reflection is allowed to use Layer 3 relationships to help Layer 4 organize itself.

That includes:

- identifying related threads
- identifying related workspaces
- detecting that several threads belong to the same emerging concept
- suggesting that a workspace is becoming a promotion candidate

The bodies remain in Layer 4.

## Reflection And Layer 2

Reflection is explicitly allowed to maintain the health of Layer 2.

This is where:

- notion cleanup
- notion pruning
- notion merging
- hot-memory hygiene

should happen.

## Related Concepts

- [Notion](notion.md)
- [High-Signal Mamba Stream](high-signal-mamba-stream.md)
- [Dream Cycle](dream-cycle.md)
- [Evidence Package](evidence-package.md)
