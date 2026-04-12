# Local Dev

This project can now be developed and tested locally without a live Moltbox appliance or OpenClaw runtime.

## Python Service And Contracts

Run the Python tests:

```bash
python -m unittest discover -s tests
```

Run a sample boundary locally:

```bash
python -m remram_cortex run-boundary --input examples/phase1-session.json
```

Start the local bridge service:

```bash
python -m remram_cortex serve --host 127.0.0.1 --port 8091
```

Useful endpoints once the service is running:

- `GET /healthz`
- `GET /v1/sessions/<session-id>/startup-bundle/latest`
- `POST /v1/openclaw/hooks`
- `POST /v1/openclaw/boundaries`

## OpenClaw Bridge Package

Run the local Node tests for the bridge package:

```bash
cd integrations/openclaw/packages/cortex-phase1-bridge
npm test
```

Those tests cover:

- service-mode startup bundle fetch
- service-mode hook posting
- local spool fallback when the service is unavailable

## Current Local Scope

Local development currently covers:

- the Cortex runtime scaffold
- the HTTP bridge service contract
- the OpenClaw bridge package
- the initial Layer 4 SQL contract

Local development does not yet cover:

- a live OpenClaw runtime
- shared-service deployment through `moltbox-gateway`
- appliance network, secrets, or backup behavior
