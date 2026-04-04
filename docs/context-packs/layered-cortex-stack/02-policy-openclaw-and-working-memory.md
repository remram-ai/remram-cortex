# Policy, OpenClaw, And Working Memory

## The Main Decision

Layer 1 is custom.

Layer 2 stays OpenClaw-native by default.

This is one of the most important choices in the current stack.

## Why Policy Is Custom

Policy is where Cortex-specific behavior lives.

It includes:

- role and mode composition
- approval and escalation rules
- tool policy
- prompt-budget discipline
- mutable preference-policy through a governed path

No off-the-shelf memory system was expected to solve this cleanly.

## Why Working Memory Stays In OpenClaw

OpenClaw already owns:

- sessions
- transcript continuity
- compaction
- runtime execution
- context-engine surfaces

That makes OpenClaw the natural Layer 2 base.

The stack deliberately avoids building a separate external working-memory store in phase 1.

## What Cortex Adds To Layer 2

Cortex does not replace OpenClaw working memory.

Cortex augments it through:

- policy-aware context assembly
- semantic checkpoint generation
- compressed continuity objects
- hooks that prepare continuity before compaction pressure becomes painful

## The Session Surface

OpenClaw sessions remain the evidence surface for live runtime behavior.

That means:

- the transcript is still the base runtime journal
- compaction is still an OpenClaw concern
- Cortex should plug into that surface rather than fork it immediately

## The Problem This Solves

The architecture is reacting to a practical issue:

- smaller context windows fill quickly
- raw transcript replay is expensive
- the system needs bounded continuity that still feels long-lived

The answer is not to replace OpenClaw.

The answer is to compress the session into a better semantic surface.

## The Working-Memory Product Model

The intended working-memory model is:

- OpenClaw keeps the session and compaction machinery
- Cortex emits compact continuity objects from the session stream
- runtime context is assembled from those continuity objects rather than from raw replay alone

The result is an "effectively larger context window" without pretending the model has infinite prompt budget.

## What Lives In Policy Versus Working Memory

Policy owns:

- persistent rules
- behavior constraints
- role posture
- approval requirements
- mode overlays

Working memory owns:

- recent continuity
- active goals
- recent decisions
- short-horizon assumptions
- in-flight runtime state

The system should not confuse the two.

## Mutable Preference Policy

Some policy-like state is allowed to change.

Examples:

- formatting preferences
- style preferences
- operating preferences
- stable mode biases

But access policy and other safety-critical rules should not share the same write path.

Preference-policy can update through a governed reflection path.

Access policy should require stronger approval.

## The Context Formula

The runtime context formula is:

**policy + working-memory continuity + durable-memory bundle + knowledge pointers**

This means working memory is not the whole startup context.

It is one bounded part of the full assembled stance.

## Why There Is No Redis In The Base Stack

The current design intentionally avoids a separate Redis working-memory store because:

- OpenClaw already has a session surface
- the real pain is context quality, not just storage
- the High-Signal Mamba stream solves the larger problem more directly
- another store would add complexity before it proves value

The architecture can revisit an external hot store later if OpenClaw becomes the blocker.

For now, the rule is:

**let OpenClaw do Layer 2, and let Cortex augment it intelligently**
