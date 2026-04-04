# Mamba And SSM Stream Notes

This note captures the current Mamba and state-space-model assumptions behind the High-Signal Mamba Stream.

Sequencing clarification:

- the long-term architecture still wants this stream
- the current delivery plan defers it by default until Phase 3
- Phase 1 proves the spine with boundary-triggered semantic processing instead

It is a supporting reference for the active Cortex architecture, not a commitment to one exact model family or checkpoint.

## Main Architectural Takeaway

The strongest pattern is a two-tier setup:

1. a small, continuously running streaming sensor
2. a larger writer or coding model that is only invoked when the sensor detects something worth promoting

This fits Cortex because the architecture already separates:

- always-on semantic checkpointing
- slower durable-memory promotion
- optional code or artifact guidance

## Why SSMs Matter Here

State-space models are attractive for the stream role because they maintain a fixed-size recurrent state instead of a Transformer-style key-value cache that grows with sequence length.

For Cortex, that means:

- long or unbounded logs become more tractable
- near-time semantic compression can stay predictable
- the stream can be treated as continuous infrastructure rather than a batch-only summarization job

## Why Mamba Is A Good Fit

The useful Mamba-specific idea is the selection mechanism.

That gives the model a learned "keep vs. forget" behavior that maps well to:

- salience detection
- memory-worthiness detection
- checkpoint boundary detection
- routing into slower downstream processing

This is why the active Cortex framing treats "Mamba" less as a brand-name checkpoint choice and more as the architectural role of a continuously running semantic gate.

## What Cortex Should Borrow From This

The current note supports these assumptions:

- the semantic checkpoint stream should be continuously available
- the stream should usually be produced by a smaller and cheaper model than the writer or coder
- only high-signal windows should wake the more expensive model
- the stream should emit structured checkpoint payloads, not only prose summaries

That aligns with the active design where the stream can feed:

- working-memory assembly
- notion capture
- oversight
- artifact-impact hints
- later durable-memory reconciliation

## Recommended Model Role Split

### Stream Sensor

The stream sensor should be:

- small or medium
- cheap enough to run continuously
- optimized for salience, tagging, and boundary detection

It should decide whether a bounded window is worth turning into:

- a notion
- an oversight event
- a coding-assistance trigger
- an artifact-impact event

### Writer Or Coder

The writer should be:

- stronger
- more expensive
- only invoked when bounded evidence is already selected

It is the right place for:

- durable-memory object writing
- structured artifact-impact extraction
- code review or coding supervision
- richer explanation

## Implication For Cortex

The "Mamba stream" should not be interpreted too literally as:

- one permanent commitment to one exact Mamba checkpoint
- one model doing both sensing and writing

The better interpretation is:

- a continuously running SSM-like or Mamba-like sensor layer
- plus downstream writers triggered on bounded, high-signal windows

## Practical Model Candidates

The research note suggests three broad categories:

- tiny or small Mamba-family checkpoints for always-on sensing
- code-tuned Mamba-family models such as Codestral Mamba for code-heavy writing
- hybrid long-context models such as Bamba when a stronger general writer is needed

For Cortex, the architectural lesson matters more than the exact checkpoint list:

- keep the sensor cheap
- keep the writer bounded
- do not pay large-model cost on the whole log stream

## Mamba-2 And Mamba-3 Relevance

The note also supports a useful maturity split:

- `Mamba-2` looks practical enough to inform current architecture
- `Mamba-3` is promising, especially for decode efficiency, but should be treated as exploratory until ecosystem support stabilizes

That means the active stack should not lock itself to `Mamba-3`.

## Bottom Line

The Cortex stream should be designed as:

- continuously running
- sensor-first
- source-linked
- bounded on the expensive path

That is the most important architectural lesson from the current Mamba research note.
