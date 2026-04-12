# Project Plan

## Framing

This package replaces the archived architecture-first execution plan with a practical delivery plan.

The layered architecture is still the design authority.
What changes here is the execution sequence.

The main correction is:

- do not force the project phases to mirror the long-term Cortex loops
- do not jump to the heavier memory-service graph before the baseline assistant is useful

## Delivery Doctrine

The active execution doctrine is:

1. make the fast default path work
2. keep the local default model responsive
3. route before invoking heavier capabilities
4. treat memory as a retrieval capability, not as automatic prompt stuffing
5. keep browser out of the default baseline
6. prove changes on the current Moltbox operator path

In practice, that means the orchestrator should decide:

- can the local model answer directly
- does this need fresh web information
- does this need memory or continuity
- is this a coding task
- is this above the local model's reasoning or coding ceiling

Memory should only be invoked when needed.
If memory is used, the injected result should stay small and bounded.

## Live Appliance Authority

When this project targets the live Moltbox appliance:

- `moltbox-gateway` is the source of truth for current appliance behavior
- `test` is the proving lane
- `prod` is a protected managed pet
- normal service-plane mutation uses `moltbox service ...`
- normal runtime mutation uses native `moltbox test|prod openclaw ...`
- routine validation should prefer `moltbox test verify runtime|web` and `moltbox prod verify runtime`
- raw Docker, break-glass SSH, replay-era runtime ownership, and the old Playwright detour are not the intended baseline

Current live-baseline facts still come from Gateway:

- managed services are `gateway`, `caddy`, `ollama`, `searxng`, `test`, and `prod`
- a separate remote `dev` runtime is not a baseline fact yet

If a dedicated `dev` lane is introduced later, it must land through tracked Moltbox changes rather than through host-only drift.

## Immediate Execution Posture

The current target is:

- complete `Phase 1`
- carry enough of `Phase 2` to make the system useful
- carry enough of `Phase 3` to make iteration repeatable

Do not make `Graphiti`, `Neo4j`, `Postgres`, or a separate `cortex` service a prerequisite for the first useful baseline.

## Phase 1: OpenClaw Foundation

### Goal

Stand up a useful baseline assistant on top of remote `OpenClaw`.

### Core Epics

1. Baseline remote OpenClaw runtime
2. `QMD` sidecar memory bring-up
3. Light memory tuning
4. Web baseline through `web_search` and `web_fetch`
5. OpenAI escalation
6. Lightweight orchestrator and intent mapping

### Required Posture

- `QMD` runs beside OpenClaw on the host, not as a hidden local-workstation dependency
- memory limits stay small enough for the local default model
- browser stays out of the baseline
- the orchestrator decides whether memory is needed before memory is injected

### Exit Criteria

- remote `OpenClaw` runs cleanly on the proving lane
- `QMD` is enabled and prewarmed on the host
- memory retrieval is bounded and light
- web baseline works without browser
- OpenAI escalation works for harder tasks
- the orchestrator can route between direct answer, web, memory, coding, and escalation paths

### Non-Goals

- specialist agent library
- dedicated development lane
- Cortex evidence loop
- durable memory services

## Phase 2: Baseline Agents And Access

### Goal

Add a small set of specialist agents and make the system convenient to use remotely.

### Core Epics

1. Default assistant profile
2. Coding agent
3. Thinking and research agent
4. Management and operator agent
5. Remote chat and access posture

### Exit Criteria

- baseline specialist agents exist with clear responsibilities
- the default assistant can hand work off rather than trying to do everything itself
- remote usage does not require the user's main workstation to be the only place work can happen

### Non-Goals

- rich multi-agent autonomy
- deep policy stack redesign
- durable memory graph work

## Phase 3: Dev/Test Loop

### Goal

Create a repeatable workflow for changing, deploying, validating, and backing out the baseline system.

### Core Epics

1. Local-to-remote development workflow
2. Test-lane deploy and validation flow
3. Logs and diagnostics surface
4. Rollback and recovery posture
5. Sandbox or coding-environment integration

### Exit Criteria

- code and config changes can be tested without improvising host mutation
- deploy and validation use official Moltbox surfaces
- logs and rollback steps are explicit
- the workflow does not depend on routine break-glass access

### Non-Goals

- full Cortex semantic loop
- multi-service durable-memory deployment

## Phase 4: Cortex Augmentation

### Goal

Add the first real Cortex-owned behavior around the now-usable baseline.

### Core Epics

1. Policy bundle and startup assembly
2. Layer 5 runtime evidence capture
3. Boundary-triggered semantic hooks
4. QMD notion lifecycle integration
5. Reflection and reconciliation scaffolding

### Notes

Most of the current Python scaffold in this repo belongs here rather than in the first baseline phases.

### Exit Criteria

- policy bundle resolution is explicit
- evidence capture is inspectable
- boundary hooks produce bounded outputs for downstream work
- QMD remains the hot memory layer rather than becoming durable authority

## Phase 5: Memory Services

### Goal

Introduce the heavier service graph only after the baseline and augmentation seams are stable.

### Core Epics

1. `Postgres` for operational knowledge
2. `Neo4j`
3. `Graphiti`
4. separate `cortex` service boundary
5. trust and promotion model across QMD and durable memory

### Exit Criteria

- service ownership is clean across `remram-cortex`, `moltbox-services`, `moltbox-runtime`, and `moltbox-gateway`
- Layer 3 and Layer 4 services are reachable and bounded
- durable memory does not become a transcript dump

## Phase 6: Sources And Artifacts

### Goal

Expand beyond chat and baseline continuity into retained sources and authored outputs.

### Core Epics

1. one-way reference intake
2. maintained owned sources
3. dirty-state tracking
4. authored artifact promotion
5. bottom-up reprocessing

### Exit Criteria

- outside material can be retained intentionally without collapsing everything into canon
- owned sources and authored outputs have a clear lifecycle

## Phase 7: Optimization

### Goal

Improve signal quality and efficiency only after the main spine is already working.

### Core Epics

1. `Mamba`
2. `Intuition`
3. latency and cost tuning
4. operational hardening

### Exit Criteria

- optimization improves an already-working system rather than rescuing an incomplete one

## Why This Order

- the first useful system needs memory, web, and escalation more urgently than it needs `Graphiti`
- the baseline assistant should learn when to invoke memory rather than always dragging memory into the prompt
- specialist agents and a dev loop matter before deeper architecture services because they determine whether the project is operable
- heavier Cortex services should land only after the runtime, routing, and operator posture are solid
