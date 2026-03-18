# Reflection

Reflection is the post-run extraction pass that converts runtime evidence into candidate knowledge deltas.

It is the first step that turns activity into memory.

## Trigger

Reflection is expected to run from the runtime `agent_end` boundary after a unit of execution is complete and after the user-visible response has already been delivered.

## What Reflection Does

Reflection:

- reads bounded run evidence such as tool outputs and artifacts
- compares that evidence with existing related knowledge
- proposes small memory updates instead of rewriting the whole graph
- may surface candidate dimensions for later dream-cycle promotion

Typical deltas include add, revise, correct, relate, strengthen, weaken, retire, and propose-dimension.

Reflection should be incremental and independent of prompt visibility. Its inputs come from persisted evidence, not from whatever still happens to remain in the live context window.

Reflection output should be structured delta data, not a free-form narrative summary.

It may also emit dense functional summaries of a thread so future retrieval can lean on compressed process memory instead of full chat replay.

## What Reflection Does Not Do

Reflection does not globally reconcile the full memory graph. That is the job of the dream cycle.

## Related Concepts

- [Knowledge Object](knowledge-object.md)
- [Dream Cycle](dream-cycle.md)
- [Artifact Promotion](artifact-promotion.md)
