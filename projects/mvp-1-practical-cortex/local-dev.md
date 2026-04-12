# Local Dev

Local development remains useful, but it is no longer the whole project story.

## What Local Development Covers Well

- the Python prep scaffold in `remram_cortex/`
- the HTTP bridge service contract
- inspectable local output under `.runtime/cortex/`
- test fixtures and scaffold behavior
- later Phase 4 and Phase 5 seam work before live infrastructure exists

Useful local commands:

```bash
python -m pytest -q
python -m remram_cortex run-boundary --input examples/phase1-session.json
python -m remram_cortex serve --host 127.0.0.1 --port 8091
```

## What Local Development Does Not Prove

- remote `OpenClaw` baseline behavior
- host-installed `QMD` sidecar behavior
- live web baseline on the appliance
- OpenAI escalation wiring on the host
- remote access posture
- deploy, rollback, and validation behavior through Moltbox

## Practical Rule

Use local development for:

- design seam validation
- payload shape validation
- scaffold testing
- later Cortex augmentation work

Use the remote proving lane for:

- actual Phase 1 baseline bring-up
- agent routing and escalation
- memory tuning
- operator validation
