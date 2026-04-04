# memU Spike Evaluation

## Purpose

Run a short bounded spike against `memU` to harvest implementation lessons for Cortex without changing the canonical Cortex architecture.

This is a learning spike, not an adoption plan.

## Why Run It

The gap analysis in [memu-gap-analysis.md](../reference/memu-gap-analysis.md) concludes that memU is useful to study but not a fit as the Cortex foundation.

The spike should answer practical questions that documentation review alone cannot settle:

- which parts of memU feel materially faster to work with than the current Cortex implementation plan
- whether its reinforcement and salience logic are worth borrowing
- whether its workflow and interceptor model should influence Cortex service design
- how much friction appears when trying to map memU output back to Cortex knowledge-object expectations

## Non-Goals

Do not use this spike to:

- replace the OpenSearch dependency roadmap
- redefine Cortex memory around categories or resource summaries
- merge memU directly into the `remram-cortex` implementation plan
- treat memU output as canonical Cortex truth

## Timebox

- target: 1 to 2 focused working days
- stop once the evaluation questions are answered

## Inputs

Use the same shape of seed corpus already expected by the Cortex MVP:

- 5 to 15 project documents
- a few idea or strategy notes
- 3 to 5 quick-capture-style follow-up notes

Use one or two query sets that match the Cortex retrieval acceptance language, for example:

- `places to stay while hiking`
- `how could OpenTrails make money`
- `find more camping spots`

## Evaluation Questions

### 1. Write Path

- How clean is the ingest and extraction loop for imported artifacts?
- Does memU produce useful atomic items or mostly summary noise?
- How often do repeated captures reinforce versus duplicate?

### 2. Read Path

- Are results explainable enough for debugging?
- Do category-first results help or hurt compared with Cortex's planned bounded retrieval model?
- Does query rewriting improve recall or mostly hide weak write-path structure?

### 3. Data Model Fit

- Can memU `Resource` and `MemoryItem` outputs map cleanly to Cortex artifact and knowledge-object expectations?
- What Cortex-required fields are still missing after ingestion?
- How much custom glue would be needed before the result is useful to Cortex?

### 4. Implementation Patterns

- Is the workflow-step pattern worth borrowing directly?
- Are interceptor hooks useful enough to become a Cortex requirement?
- Is the salience scoring model worth translating into early Cortex ranking heuristics?

## Exit Criteria

The spike is complete when we have written answers for:

- what memU does better than the current Cortex implementation plan
- what memU cannot satisfy without architectural conflict
- which ideas should be borrowed into Cortex design or implementation
- whether any roadmap change is justified

The expected default result is:

- no roadmap pivot
- selective borrowing of implementation patterns only

## Expected Deliverable

Leave behind one short written result in this repo that captures:

- findings
- borrowable patterns
- rejected adoption paths
- any concrete follow-up changes worth making in Cortex docs or implementation specs

## Decision Rule

Only revisit the Cortex roadmap if the spike shows a clear win that survives this test:

Would the borrowed value still hold after restoring the Cortex requirements for:

- knowledge objects
- artifact-provider identity
- source-linked provenance
- governance-first retrieval
- typed signals
- semantic signature
- Dream and promotion

If the answer is no, the value belongs in the "learn from it" bucket, not the "adopt it" bucket.
