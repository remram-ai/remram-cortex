# Live Appliance Quick Start

Use this note when a Cortex thread will touch the real Moltbox appliance or any of the sibling Moltbox repos.

## Current Active Project

- The only active project package in this repo is `projects/mvp-1-layered-cortex/`.
- The older `v0_1 MVP` package is archived and should not be treated as the current implementation plan.

## Repo Authority Split

- `remram-cortex`: Cortex architecture, project package, prep scaffold, bridge package, and SQL contracts
- `moltbox-gateway`: live appliance operator contract, CLI, deploy, verification, recovery, and SSH-role docs
- `moltbox-services`: baseline service definitions, baseline config examples, and service-local docs
- `moltbox-runtime`: promoted runtime artifacts and runtime overlays used on the release path
- `remram`: historical background only for this topic unless an active doc points back to it explicitly

## Workstation Access

- SSH aliases live in `C:\Users\Jason\.ssh\config`.
- Current aliases are `moltbox`, `moltbox-admin`, `moltbox-ai-test`, `moltbox-ai-prod`, and `moltbox-breakglass`.
- The current installed key path is `C:\Users\Jason\.ssh\id_ed25519`.
- Legacy local keys `C:\Users\Jason\.ssh\jason-codex` and `C:\Users\Jason\.ssh\codex-bootstrap` still exist, but they are not the current live host keys.
- The workstation config is the source of truth for the current host mapping. The current local config points all five aliases at the same host.

## Operator Lanes

- `moltbox` or `moltbox-admin`: human admin lane as `jpekovitch`
- `moltbox-ai-test`: restricted test lane for normal AI mutation on `test` plus limited service work
- `moltbox-ai-prod`: restricted prod diagnostics lane with no normal prod mutation rights
- `moltbox-breakglass`: emergency admin lane only
- `test` is the proving lane
- `prod` is a protected managed pet

## Current Appliance Baseline

- Managed services are `gateway`, `caddy`, `ollama`, `searxng`, `test`, and `prod`.
- Public service names `test` and `prod` map to `openclaw-test` and `openclaw-prod`.
- Planned Phase 1 additions such as `postgres`, `neo4j`, `graphiti`, and `cortex` are allowed project targets, but they are not live-baseline facts yet.

## First Commands

Run these first when orienting on the real environment:

```text
ssh moltbox "moltbox gateway status"
ssh moltbox "moltbox service list"
ssh moltbox "moltbox service status test"
ssh moltbox "moltbox service status prod"
ssh moltbox-ai-test "moltbox test verify runtime"
ssh moltbox-ai-test "moltbox test verify web"
ssh moltbox-ai-prod "moltbox prod verify runtime"
```

## Deploy And Change Rules

- Service-plane mutation goes through `moltbox service ...`.
- Gateway self-update goes through `moltbox gateway update`.
- Runtime mutation goes through native `moltbox test openclaw ...` or `moltbox prod openclaw ...`.
- Build changes in the repo that owns the change, commit and push them, pull the exact revision on the host under `/opt/moltbox/repos/...`, then deploy through the official CLI.
- If the task needs a new service definition, land it in `moltbox-services`.
- If the task changes promoted runtime artifacts or overlays, land it in `moltbox-runtime`.
- If the task needs a new operator workflow, deploy surface, verification command, or recovery rule, land it in `moltbox-gateway`.

## Debug And Verification

Prefer these supported surfaces before raw shell inspection:

```text
moltbox gateway status
moltbox gateway logs
moltbox service list
moltbox service status <service>
moltbox service logs <service>
moltbox test openclaw health --json
moltbox test openclaw models status --json
moltbox test verify runtime
moltbox test verify web
moltbox prod openclaw health --json
moltbox prod verify runtime
```

## Guardrails

- Do not use raw Docker as the normal path.
- Do not use break-glass SSH as the routine path.
- Do not treat replay-era Gateway internals as the normal runtime ownership model.
- If routine validation requires raw shell or break-glass access, treat that as a missing operator surface to close in `moltbox-gateway`.
- Recovery is snapshot-first: snapshot before risky change, roll back with ZFS first, and keep OpenClaw native backups as the runtime backup layer.

## Host Paths

- `/usr/local/bin/moltbox`
- `/etc/moltbox/config.yaml`
- `/opt/moltbox/repos/moltbox-gateway`
- `/opt/moltbox/repos/moltbox-services`
- `/opt/moltbox/repos/moltbox-runtime`
- `/srv/moltbox-state`
- `/srv/moltbox-logs`
- `/var/lib/moltbox`
- `/mnt/moltbox-backup`

## Read Next

- `moltbox-gateway/docs/guides/operator-guide.md`
- `moltbox-gateway/docs/ai-context/cortex-implementation-thread-prompt.md`
- `docs/design/deployment-plan.md`
- `projects/mvp-1-layered-cortex/project-plan.md`
