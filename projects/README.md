# Project Packages

This folder holds project-scoped execution packages for Cortex.

Use `projects/` for temporal execution work.
Use [../product/](../product/README.md) for stable product design.

## Start Here

- If you want the current project map, open the specific project `README.md`.
- If you want the repeatable project artifact rules, keep reading this file.
- If you are executing a project thread, read the project `README.md`, then `project-plan.md`, then `acceptance-test.md`, then the specific epic folder.
- If a thread changes stable behavior rather than only the current run, switch back to [../product/](../product/README.md) and update the owning stable docs there.

## 1. Core Boundary

The rule is:

- `product/` owns the stable Cortex surface
- `projects/` owns execution posture, sequencing, proof, and leave-behind delivery artifacts

That means:

- product capabilities and dependencies should not be redefined inside a project folder
- project folders should point to product docs rather than duplicating them
- project artifacts may restate scope, order, acceptance, and evidence requirements for that specific run

## 2. What Lives In Product

Use `product/` for artifacts that should survive multiple projects.

Current pattern:

- `product/capabilities/<name>/spec.md`
- `product/capabilities/<name>/regression-plan.md`
- `product/dependencies/<name>/README.md`
- `product/dependencies/<name>/spec.md`
- `product/dependencies/<name>/regression-plan.md`

Notes:

- the stable contract lives in `spec.md`
- the long-lived validation surface lives in `regression-plan.md`
- if a dependency later becomes a shared platform item, move the canonical docs into `remram/platform/` and leave a pointer or thin overlay in Cortex

## 3. What Lives In Projects

Use `projects/` for artifacts that belong to one execution package only.

Examples:

- project charter and scope
- epic ordering
- project definition of done
- project user stories
- project-level acceptance testing
- epic-level implementation and testing
- runtime walkthrough notes
- test result artifacts
- human acceptance testing records

Do not create a `capabilities/` tree under new projects.
If an older project still has one, treat it as transitional and migrate the references back to `product/`.

## 4. Canonical Project Shape

Going forward, new projects should follow this shape:

```text
projects/
  <project>/
    README.md
    project-plan.md
    acceptance-test.md
    runtime-docs.md
    seed-prompt.md       # optional, active thread bootstrap prompt
    epics/
      01-<epic-name>/
        README.md
        implementation-plan.md
        test-plan.md
        tests/
          001-test-result-ddmmyyyy.md
    acceptance-tests/
      001-test-result-ddmmyyyy.md
```

Read that shape as:

- `README.md` = project charter
- `project-plan.md` = epic sequencing
- `acceptance-test.md` = project acceptance criteria and scenarios
- `acceptance-tests/` = executed acceptance and HAT records
- `epics/<epic>/` = implementation work package for one epic

Default rule:

- keep the project tree small
- only add new top-level project files when they are clearly project-scoped rather than epic-scoped

## 5. Project README Contract

`projects/<project>/README.md` is the project charter.

It should define:

- project goal
- narrative summary
- definition of done
- primary user stories
- epic list in intended execution order
- links to the relevant product capabilities and dependencies
- links to the project plan, acceptance test, runtime docs, epics, and test artifacts
- optional link to the active `seed-prompt.md` if the project uses one

If someone needs to understand what the project is trying to accomplish, they should start with the project `README.md`.

## 6. Project Plan Contract

`projects/<project>/project-plan.md` is the sequencing and delivery plan for the project.

It should define:

- epic order
- why that order exists
- cross-epic dependencies
- execution phases when useful
- readiness gates or major handoff points

It should not become a second copy of every capability spec.

The project plan ties the epics together.
The epics define the implementation work.

## 7. Project Acceptance Test Contract

`projects/<project>/acceptance-test.md` is the project-level acceptance plan.

It should test:

- project user stories
- project definition of done
- cross-capability behavior
- end-to-end workflows
- system-level proof that the project actually delivered the intended outcome

This is not the same thing as a product regression plan.

Short version:

- project `acceptance-test.md` = "did this project deliver what it was supposed to deliver?"
- product `regression-plan.md` = "what must stay true for this capability or dependency over time?"

If those documents overlap, that is acceptable.
They serve different scopes.

The executed records for that plan belong in `acceptance-tests/`, not back in `product/`.

## 8. Epic Contract

Each epic should live under:

```text
projects/<project>/epics/<epic-id>/
```

Each epic should contain at least:

- `README.md`
- `implementation-plan.md`
- `test-plan.md`
- `tests/`

### 8.1 Epic README

The epic `README.md` is the epic charter.

It should define:

- epic goal
- why the epic exists in this project
- the product capabilities or dependencies it touches
- definition of done for the epic
- dependencies on earlier epics

### 8.2 Epic Implementation Plan

The epic `implementation-plan.md` is the developer-facing execution plan for that epic.

Use it for:

- deliverable breakdown
- implementation order inside the epic
- local assumptions
- risks
- dependencies
- validation references

This is the right place for detailed implementation sequencing.

Going forward, prefer epic-level implementation plans over a project-level `implementation-plan.md`.
If an older project still has a project-level implementation plan, treat it as transitional and migrate that detail into the relevant epic folders.

### 8.3 Epic Test Plan

The epic `test-plan.md` proves that the epic itself is complete.

It should define:

- epic-specific scenarios
- boundary and failure cases
- concrete acceptance proof for the deliverables in that epic

Epic test plans are narrower than the project test plan and more execution-facing than product regression plans.

### 8.4 Epic Tests Folder

Each epic should keep executed test artifacts directly under:

- `projects/<project>/epics/<epic-id>/tests/`

Use simple run artifacts such as:

- `tests/001-test-result-ddmmyyyy.md`
- `tests/002-test-result-ddmmyyyy.md`

## 9. Runtime Docs

`projects/<project>/runtime-docs.md` is the leave-behind walkthrough for the delivered project slice.

Default rule:

- include it unless there is a strong reason not to

It should explain:

- how to exercise the delivered behavior
- how to operate or inspect the result
- where to find key commands, traces, or proof surfaces

## 10. Tests Folder

Keep executed project test artifacts directly under:

- `projects/<project>/acceptance-tests/`

Use simple run artifacts such as:

- `acceptance-tests/001-test-result-ddmmyyyy.md`
- `acceptance-tests/002-test-result-ddmmyyyy.md`

This folder is also the home for HAT (human acceptance testing) records.

If a specific run needs supporting files, put them beside the run record or in a same-numbered sibling folder.

## 11. Temporary Material

If a project uses a seed prompt actively, keep it at the project root as `seed-prompt.md`.

Do not multiply prompt variants or treat seed prompts as canonical design artifacts.

## 12. Pattern Summary

Use these rules when creating future Cortex work:

- write stable behavior into `product/`
- write project intent into project `README.md`
- sequence the work in `project-plan.md`
- test the full project in project `acceptance-test.md`
- keep any active seed prompt at project root as `seed-prompt.md`
- implement epic by epic under `epics/`
- give every epic its own `implementation-plan.md`
- give every epic its own `test-plan.md`
- keep executed project artifacts under `acceptance-tests/` and epic artifacts under epic `tests/`
- keep long-lived capability validation in `product/.../regression-plan.md`
- keep prompt churn low and avoid polluting the project tree with throwaway prompt variants
