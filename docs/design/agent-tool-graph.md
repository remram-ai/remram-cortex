# Agent Tool Graph

## Purpose

This document defines the design doctrine for agent tool libraries as a layered graph rather than a flat inventory.

It is intended to be stable even if individual tools, providers, or runtime implementations change later.

The purpose is not to catalog tools.
The purpose is to teach agents how to traverse capabilities.

## Core Doctrine

The default traversal doctrine is:

1. determine the kind of work
2. choose the most likely domain
3. start at the lightest sufficient layer
4. escalate downward only when needed
5. switch domains when progress is weak or the problem was misclassified
6. verify before concluding
7. coordinate sequencing, escalation, delegation, and handoff when necessary

This doctrine is more important than any specific tool list.

## What This Design Is And Is Not

This design is:

- a capability-organization model
- a traversal model
- a trimming model
- an instruction-assembly model

This design is not:

- a generic tool catalog
- a fixed provider-specific taxonomy
- a replacement for runtime policy
- a replacement for verification discipline

## Tool Graph Vocabulary

### Domain

A top-level capability family such as software development, information discovery, or real-world operations.

### Subdomain

A narrower area inside a domain used when the parent family is still too broad.

Examples:

- web discovery inside information discovery
- repository editing inside software development
- service inspection inside systems / operations

### Layer

A capability band inside a domain or subdomain.

Layers usually move from:

- broader to narrower
- safer to riskier
- cheaper to more expensive
- exploratory to intervention-oriented

### Tool Node

A concrete callable tool or tightly related tool bundle attached to a domain layer.

### Escalation Edge

A downward edge that moves to a more direct, powerful, invasive, or expensive layer when weaker movement is insufficient.

### Domain-Switch Edge

A lateral edge that moves from one domain to another when the problem is reclassified or the current domain is not yielding progress.

### Verification Checkpoint

A required validation step attached to traversal, not an optional afterthought.

### Trimming Rule

A deterministic rule that removes domains, layers, or nodes for a given role or environment without changing the underlying doctrine.

### Assembly Profile

A named trimmed view of the full graph used for a specific agent, environment, or permission posture.

## Design Principles

### 1. Domain Before Tool

The agent should classify the work before selecting a tool.

That keeps tool choice from being driven by familiarity or raw power.

### 2. Lightest Sufficient Layer First

The agent should begin with the least invasive or least expensive layer likely to make progress.

Examples:

- discover before fetch when the source is unknown
- inspect before mutate
- read before patch
- query before intervene

### 3. Discovery And Retrieval Stay Distinct

Discovery finds candidate sources or locations.
Retrieval fetches actual source material.

The graph should preserve that distinction both externally and internally.

### 4. Software Development Is Usually A Separate Family

Software-development-heavy tools should not pollute the general-purpose capability map.

They form their own family because they bring a dense intervention stack:

- repo search
- file inspection
- patching
- tests
- diffs
- execution

### 5. Systems / Operations May Also Need Separation

If service control, logs, shell, deployment, or runtime inspection would dominate the general map, systems / operations should also be carved out as its own family.

### 6. Coordination Governs Traversal

Coordination is not just another peer bucket.
It governs:

- sequencing
- escalation
- retries
- delegation
- verification
- handoff

### 7. Verification Is First-Class

Every meaningful traversal should have a verification posture.

Verification is not just "double-check if convenient."
It is part of the path.

## Proposed Graph Structure

The current practical graph shape is:

1. coordination
2. reasoning and synthesis
3. information discovery
4. information retrieval
5. real-world operations
6. software development
7. systems / operations

This is not claimed as eternal truth.
It is the current useful shape because it preserves the most important distinctions while staying small enough to assemble and trim cleanly.

## Domain Structure

### Coordination

Role:

- governs traversal rather than replacing other domains

Typical responsibilities:

- decide whether to continue, escalate, switch, or hand off
- manage sequencing and retries
- enforce verification checkpoints
- decide whether sub-agents or deferred workflows are warranted

This domain may contain very few direct tools.
Its importance is doctrinal rather than volumetric.

### Reasoning And Synthesis

Role:

- think over gathered material
- compare options
- summarize
- reconcile
- structure outputs

This domain should stay distinct from access.
Reasoning is not retrieval.
Synthesis is not discovery.

### Information Discovery

Role:

- find likely sources, records, or targets

Typical layers:

1. broad search or candidate generation
2. targeted lookup or filtered search
3. domain-specific discovery when a general search is too weak

Example tool posture:

- web search
- memory search
- index search
- metadata search

### Information Retrieval

Role:

- fetch and inspect actual source material

Typical layers:

1. bounded fetch or read
2. structured record retrieval
3. deeper retrieval from specialized stores

Example tool posture:

- web fetch
- file read
- document read
- record get

### Real-World Operations

Role:

- perform bounded user-facing actions in external systems

Typical layers:

1. inspect state
2. prepare or draft action
3. execute action

Example tool posture:

- email read and send
- calendar inspect and update
- settings or task actions

### Software Development

Role:

- operate on code, repositories, tests, and developer workflows

Typical subdomains:

- repository discovery
- code retrieval
- patching and edits
- local verification
- version-control operations

Typical layer progression:

1. search and inspect
2. edit and patch
3. execute tests or local commands
4. repository-state mutation or broader intervention

This family should stay separate because it is unusually dense and intervention-heavy.

### Systems / Operations

Role:

- operate on runtime, service, host, or deployment surfaces

Typical subdomains:

- runtime inspection
- log and metrics inspection
- service control
- deployment and environment mutation

Typical layer progression:

1. inspect state
2. fetch logs or diagnostics
3. controlled service operations
4. deeper shell or deployment intervention

This family should often be more restricted than the others.

## Traversal Logic

### Step 1: Determine The Work Class

Ask:

- is this mostly discovery
- retrieval
- reasoning
- real-world action
- software development
- systems / operations
- coordination

If unclear, start from the least committing classification and verify quickly.

### Step 2: Choose The Most Likely Domain

The agent should pick the domain that best matches the current need, not the tool it likes most.

### Step 3: Start At The Lightest Sufficient Layer

Start with the cheapest layer likely to move the task forward.

That means:

- discover before retrieve when the object is unknown
- inspect before intervene
- read before write
- observe before operate

### Step 4: Escalate Downward Only When Needed

Escalation should happen when:

- the upper layer cannot resolve ambiguity
- the task explicitly requires stronger access
- verification requires a lower layer

Escalation should not happen just because the agent knows a stronger tool exists.

### Step 5: Switch Domains When Progress Is Weak

Switch domains when:

- the problem was misclassified
- evidence from the current domain is insufficient
- a separate domain is needed to verify or complete the task

Examples:

- discovery to retrieval
- retrieval to reasoning
- reasoning to software development
- reasoning to systems / operations

### Step 6: Verify Before Concluding

Verification must be explicit.

Examples:

- after discovery, retrieve an actual source
- after retrieval, inspect the source rather than relying on search snippets
- after patching, run tests
- after service intervention, inspect logs or health

### Step 7: Coordinate Handoff Or Delegation

When work spans multiple domains or needs more than one pass, coordination should govern:

- sequence
- handoff
- retry
- escalation approval
- delegation

## Discovery Versus Retrieval

This distinction is important enough to state directly.

### Discovery

Discovery answers:

- where should I look
- what candidates exist
- what is likely relevant

It is broad, candidate-oriented, and incomplete by design.

### Retrieval

Retrieval answers:

- fetch the source
- inspect the actual record
- read the concrete body

It is narrower and more authoritative.

### Design Rule

Do not let discovery masquerade as retrieval.

Examples:

- `WebSearch` is discovery
- `WebFetch` is retrieval
- memory search is discovery
- file or document read is retrieval

## Why Development And Systems Tools Are Separate

### Software Development

Software development is separated because its tool family is too rich and invasive to coexist cleanly with general-purpose capability teaching.

Without separation, a general agent starts to overfit to:

- repo search
- patching
- test execution
- diffs
- command execution

### Systems / Operations

Systems / operations should also be carved out when its authority surface is large enough to distort the general model.

That usually happens when the family includes:

- shell
- logs
- service control
- deployment
- runtime inspection

### Design Rule

General-purpose maps should not be forced to carry every coding and ops tool as if they were peers to ordinary discovery and retrieval.

## Deterministic Trimming Model

The full graph should be reducible without changing doctrine.

That is what trimming is for.

### Invariants

The following should remain stable across trimmed profiles:

- domain before tool
- start at the lightest sufficient layer
- explicit escalation
- explicit domain switching
- verification checkpoints
- coordination as the governing traversal layer

### What Can Be Removed

Profiles may remove:

- whole domains
- specific subdomains
- lower layers within a domain
- specific intervention nodes

### What Must Remain

Every usable profile should retain:

- coordination
- at least one reasoning or synthesis path
- at least one verification posture appropriate to the remaining domains

### Assembly Profiles

Useful profile examples include:

#### Coding-Focused Agent

Keep:

- coordination
- reasoning and synthesis
- software development
- limited retrieval and discovery

Trim:

- most real-world operations
- most systems / operations unless explicitly needed

#### Research-Focused Agent

Keep:

- coordination
- reasoning and synthesis
- information discovery
- information retrieval

Trim:

- software development intervention
- systems / operations
- most real-world actions

#### Systems Operator

Keep:

- coordination
- reasoning and synthesis
- systems / operations
- focused retrieval and discovery

Trim:

- real-world operations
- most software-development tooling unless needed for deployment or diagnostics

#### Lightweight General Assistant

Keep:

- coordination
- reasoning and synthesis
- basic discovery
- basic retrieval
- narrow real-world operations

Trim:

- software development
- systems / operations
- invasive intervention layers

#### Restricted Safe Agent

Keep:

- coordination
- reasoning
- discovery
- non-invasive retrieval

Trim:

- all intervention-heavy domains
- all lower mutation layers

## Worked Examples

### Example 1: Mature / Full Tool Graph

A mature graph may look like:

- coordination
  - planning
  - sequencing
  - delegation
  - verification policy
- reasoning and synthesis
  - summarization
  - comparison
  - structured output shaping
- information discovery
  - web discovery
  - internal memory discovery
  - index discovery
- information retrieval
  - web fetch
  - file or document read
  - record retrieval
- real-world operations
  - email
  - calendar
  - tasks
  - settings
- software development
  - repo discovery
  - code read
  - patching
  - tests
  - diffs
  - git operations
- systems / operations
  - runtime inspection
  - log retrieval
  - service control
  - deployment
  - shell

This is large, but still coherent because traversal stays domain-first and layer-aware.

### Example 2: Minimal Starting Stack

A minimal starting stack can still follow the same doctrine:

- coordination
- reasoning and synthesis
- web discovery
- web retrieval
- local file read
- one narrow action family if needed

The doctrine stays the same even though the graph is much smaller.

### Example 3: Discovery Versus Retrieval Versus Escalation

Suppose the agent needs a current vendor policy.

Path:

1. choose information discovery
2. use a broad discovery layer to find candidate pages
3. switch to information retrieval
4. fetch the actual page
5. verify by reading the source
6. only then move to reasoning and synthesis

If the page is blocked or incomplete, escalation may occur within retrieval rather than jumping straight to a stronger reasoning tool.

### Example 4: Keeping Software Development Separate

Suppose a general assistant also has coding capability.

Without separation:

- repo search
- file read
- patch
- test
- shell

all sit beside ordinary web and document tools.

That teaches the wrong lesson.
The agent begins with implementation posture even when the problem is not software work.

With separation:

- the agent first decides whether the task is software development at all
- only then does it traverse the software-development family

### Example 5: Keeping Systems / Operations Separate

Suppose the environment exposes:

- service status
- logs
- shell
- deployment controls

These should not appear as ordinary peers beside lightweight search and retrieval tools in a general assistant profile.

Instead:

- they live in systems / operations
- lower layers can be trimmed away
- the domain may be absent entirely in safer profiles

## Canonical Definition Shape

The graph definition should be stable and compact.

A lightweight pseudo-shape is:

```text
tool_graph:
  domains:
    - id: coordination
      doctrine:
        start_rule: governs traversal
        verification_rule: always explicit
      layers:
        - id: planning
          tools: [...]
      domain_switch_guidance: [...]

    - id: information_discovery
      subdomains:
        - id: web
          layers:
            - id: broad
              tools: [...]
            - id: targeted
              tools: [...]
      escalation_edges:
        - from: broad
          to: targeted
          when: candidate quality is weak
      verification_checkpoints:
        - retrieve an actual source before concluding

  trimming_rules:
    - profile: lightweight_general
      remove_domains: [software_development, systems_operations]
      remove_layers: []
      retain_invariants:
        - domain_before_tool
        - explicit_verification

  assembly_profiles:
    - id: coding_focused
      preferred_domains:
        - software_development
        - reasoning_and_synthesis
      restrictions:
        - real_world_operations limited
```

The important point is not the exact syntax.
The important point is that future tool graphs define:

- parent domains
- optional subdomains
- layers
- escalation edges
- domain-switch guidance
- tool attachments
- trimming rules
- verification rules
- assembly-profile overrides

## Relationship To The Existing Cortex Architecture

This tool graph design primarily impacts Layer 1 and instruction assembly.

It does not introduce a new memory layer.

Its main architectural effects are:

- stronger policy composition for agent capability teaching
- cleaner deterministic trimming for different agent roles and environments
- a better bridge from markdown design authority into future Cortex-backed capability memory

In the current layered stack, this belongs closest to:

- Layer 1 policy composition
- bounded startup assembly
- future operational knowledge about agent capability profiles

It should not be mistaken for:

- Layer 2 working memory
- Layer 3 durable semantic memory itself
- a runtime tool registry replacement

## Bottom Line

The agent tool graph is the canonical model for how agents should understand available tools:

- domain before tool
- lightest sufficient layer before escalation
- discovery distinct from retrieval
- software development and systems / operations carved out when needed
- deterministic trimming for role and environment
- verification as part of traversal

That is why it should become design authority rather than staying an informal prompt habit.
