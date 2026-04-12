# Runtime Docs

The current active project phases do not require the full Cortex service graph yet.

That means the runtime story is split into two layers:

- the practical baseline phases that operate primarily through remote `OpenClaw`, `QMD`, web capability, escalation, routing, and operator surfaces
- the later Cortex augmentation phases that use the prep scaffold already checked into this repo

## Current Phase Alignment

### Phase 1 Through Phase 3

These phases are mostly about:

- remote `OpenClaw` baseline behavior
- `QMD` sidecar behavior
- model routing and escalation
- agent profiles
- remote access
- deploy, validate, and rollback posture

They do not require the Python scaffold in this repo to be the live runtime yet.

### Phase 4 And Later

The current local scaffold under `remram_cortex/` becomes relevant in the later augmentation phases.

It already provides:

- policy bundle resolution
- bounded startup bundle assembly
- filesystem-backed Layer 5 runtime-evidence capture
- boundary-triggered semantic checkpoint generation
- local staging or outbox payloads for:
  - Layer 2 `QMD` mutations
  - Layer 4 support bodies
  - Layer 3 `Graphiti` episode packages
  - Reflection and Dream hook payloads

That scaffold is best understood as a prep and seam-definition layer for later phases, not as proof that the practical baseline phases are already done.

## Local Scaffold Commands

Run the Python tests:

```bash
python -m pytest -q
```

Run the sample boundary locally:

```bash
python -m remram_cortex run-boundary --input examples/phase1-session.json
```

Start the local bridge service:

```bash
python -m remram_cortex serve --host 127.0.0.1 --port 8091
```

## Active Runtime Rule

Do not make the later Cortex augmentation scaffold a prerequisite for the first useful baseline.

The practical execution order is:

1. baseline remote `OpenClaw`
2. `QMD`
3. web
4. escalation
5. routing
6. agents
7. dev loop
8. only then the deeper Cortex augmentation seam
