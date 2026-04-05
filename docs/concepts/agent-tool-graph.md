# Agent Tool Graph

An agent tool library should be modeled as a layered graph, not as a flat list of callable functions.

That distinction matters because real tool use is not just selection.
It is classification, traversal, escalation, verification, and constraint.

## Why A Graph Instead Of A Flat List

A flat tool inventory teaches the wrong behavior.

It encourages:

- premature tool selection before the kind of work is understood
- overreliance on familiar high-power tools
- accidental mixing of unrelated capability families
- brittle prompt guidance tied to today's exact tool names

A graph teaches a better doctrine:

- determine the work first
- choose the most likely domain
- start at the lightest sufficient layer
- escalate only when weaker movement fails
- switch domains explicitly when the problem was misclassified
- verify before concluding

The graph is therefore both a capability model and a traversal model.

## Domains, Layers, And Movement

In this model:

- tools belong to domains
- domains may contain subdomains
- domains and subdomains may contain layers
- layers express increasing power, cost, invasiveness, or directness

Movement through the graph has meaning.

- moving downward is escalation
- moving sideways is domain switching
- moving upward is retreat to a safer or cheaper layer

This makes tool use teachable.
The agent is not memorizing a catalog.
It is following a traversal doctrine.

## Why Discovery And Retrieval Must Stay Distinct

Discovery and retrieval are different kinds of work and should not collapse into one bucket.

Discovery answers:

- where should I look
- what candidates exist
- what is likely relevant

Retrieval answers:

- fetch the thing
- inspect the thing
- read the actual source

When these are conflated, agents skip too quickly from broad search to false certainty.
Keeping them distinct forces a useful pattern:

1. discover
2. retrieve
3. verify
4. only then synthesize or act

That distinction applies both externally and internally.

- web search is discovery
- page fetch or file read is retrieval
- memory search is discovery
- document or record read is retrieval

## Why Software Development Should Be Carved Out

Software development tools are unusually dense, invasive, and self-reinforcing.

They tend to dominate any mixed tool list because they include:

- search
- read
- patch
- test
- execute
- diff
- inspect

If they stay inside a general-purpose capability map, they pollute the doctrine.
The agent starts thinking like a coding agent even when the task is not software work.

So software development should usually be its own tool family.

That carve-out improves:

- instruction assembly
- role-specific trimming
- safer defaults
- cleaner general-assistant behavior

## When Systems / Operations Should Also Be Carved Out

Systems and operations tools deserve the same treatment when they are powerful enough to overwhelm the general model.

That usually happens when the tool family includes:

- shells
- service control
- deployment commands
- runtime inspection
- log access
- infrastructure mutation

At that point, systems / operations is no longer just another domain.
It is a restricted intervention family with its own escalation logic and safety posture.

## Why Escalation And Domain Switching Must Be Explicit

Escalation is not just "use a stronger tool."
It is a change in risk, cost, or authority.

Domain switching is not just "try something else."
It means the current classification is weak or failing.

Treating both as explicit movement through a graph makes reasoning clearer:

- the agent can explain why it escalated
- the system can trim the graph deterministically
- verification points can be attached to graph movement rather than sprinkled ad hoc

## Why This Model Fits Instruction Assembly And Cortex

This model is stable even when tool names and providers change.

That makes it useful as:

- markdown-first design authority today
- instruction-assembly input for role-specific tool bundles
- a future Cortex-backed memory artifact for capability teaching, trimming, and retrieval

The important point is that the graph is not a transient tool manifest.
It is a durable cognition model for how agents should understand available action.

## Bottom Line

The agent tool graph exists to teach agents:

- domain before tool
- lightest sufficient layer before escalation
- discovery before retrieval when appropriate
- explicit switching when classification is weak
- verification before conclusion

That is why the graph is foundational infrastructure rather than a nicer catalog.
