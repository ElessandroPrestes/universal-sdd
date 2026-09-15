# Universal SDD Project State

## Current state

| Field | Value |
|---|---|
| Product | Universal SDD Framework (USF) |
| Version and status | Pre-1.0 development draft; active development |
| Runtime and dependencies | Markdown documentation only; no runtime or dependencies |
| Primary outcome | Approved requirements become traceable implementation and reproducible quality evidence |

## Canonical hierarchy

1. An approved SPEC is the acceptance baseline for an active change.
2. This index and its linked project-state modules record canonical current state.
3. Repository content and QA evidence demonstrate delivered behavior.
4. Resolve divergence as a defect, scope change, or documentation debt.

## Context index

Use `knowledge/INDEX.md` to select a module. Do not load every module; follow
the phase bundle in `docs/context-budget.md` and the active SPEC's `Refs:`.

| Module | Current-state coverage |
|---|---|
| `knowledge/modules/framework-overview.md` | Domain, users, outcome, version, runtime, dependencies, excluded technologies |
| `knowledge/modules/governance-and-structure.md` | Repository responsibilities and modular-document architecture |
| `knowledge/modules/delivery-and-quality.md` | UX, accessibility, QA, security, delivery, and known limitations |

## Authoritative framework documents

| Need | Source |
|---|---|
| Framework definition | `UNIVERSAL_SDD_FRAMEWORK.md` |
| Session protocol | `AGENTS.md` and AI entry files |
| Roles and workflow | `agents/` and `workflows/` |
| Normative practices | `standards/` |
| Change records | `specs/`, `tasks/`, `reviews/`, `adr/` |
| Reusable artifacts | `templates/`, `knowledge/`, `profiles/`, `docs/` |

## Migration

Existing adopters may retain a monolithic `PROJECT.md` while incrementally
creating modules and an index. No existing file path is removed or renamed.
