# Governance and structure

## Metadata

| Field | Value |
|---|---|
| Domain | Framework governance and repository organization |
| Owner | Documentation |
| Reviewed | 2026-09-15 |
| Applicability | Architecture, governance, and adoption work |
| Source of truth | `PROJECT.md` context index and linked normative documents |

## Repository responsibilities

| Path | Responsibility |
|---|---|
| `README.md` | Portuguese overview and adoption entry point |
| `UNIVERSAL_SDD_FRAMEWORK.md` | Core language-agnostic framework definition |
| `AGENTS.md` and AI entry files | Shared session startup and scope protocol |
| `agents/` and `workflows/` | Role contracts and end-to-end delivery flow |
| `standards/` | Normative operational practices and gates |
| `templates/` | Versioned reusable artifacts |
| `specs/`, `tasks/`, `reviews/`, `adr/` | Change, decision, and evidence records |
| `knowledge/`, `profiles/`, `docs/` | Reusable context, adaptations, and reference guidance |

## Modular architecture

The core document defines universal governance; role files define ownership;
standards define normative rules; workflows define sequence and gates; and
templates capture decisions and evidence. Adopting projects may extend these
documents through profiles, but exceptions to baseline quality gates require
approval.
