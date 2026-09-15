# Context budget by phase

## Shared rules

Start with `AGENTS.md`, this guide, and the short `PROJECT.md` index. Load a
knowledge module only when the active SPEC names it in `Refs:` or a material
risk is documented with the module and reason. An index is retrieval metadata,
not a reason to load every listed module. Never replace a required artifact
with a repository-wide search or an inferred summary.

## Discovery

**Must load:** the incoming request; `AGENTS.md`; `PROJECT.md` sections
“Current state”, “Canonical hierarchy”, and “Context index”; and the metadata
table in `knowledge/INDEX.md`.

**May load:** only modules selected by the request's domain or a recorded risk;
existing research directly linked by the request.

**Do not load:** future SPECs, TASKs, all modules, or unrelated implementation
history.

## Architecture

**Must load:** approved discovery output; `AGENTS.md`; the same three
`PROJECT.md` sections; `knowledge/INDEX.md` metadata; modules selected by the
discovery output; and ADRs directly relevant to the decision.

**May load:** applicable standards named by the discovery output and existing
architecture evidence for the affected boundary.

**Do not load:** the full knowledge base, unrelated ADRs, or all repository code.

## Implementation

**Must load:** active approved SPEC in full; assigned TASK in full; `AGENTS.md`;
`PROJECT.md` sections “Canonical hierarchy” and “Context index”; modules named
in the SPEC's `Refs:`; linked ADRs; and standards named by the TASK.

**May load:** files directly identified by the TASK and additional modules only
with a recorded material-risk exception.

**Do not load:** unreferenced knowledge modules, unrelated SPECs or TASKs, or
the repository as undifferentiated context.

## QA

**Must load:** active SPEC sections “Metadata”, “Scope”, “Acceptance criteria”,
“Non-functional requirements”, and “Risks and dependencies”; assigned TASK;
QA plan and available evidence; `AGENTS.md`; `PROJECT.md` section “Context
index”; referenced modules; and `standards/testing.md` plus
`standards/quality-gates.md`.

**May load:** linked ADRs, affected implementation files, and risk-relevant
standards such as accessibility or security.

**Do not load:** unreferenced modules, unrelated test suites, or all prior QA
evidence.

## Review

**Must load:** active SPEC sections “Metadata”, “Scope”, “Acceptance criteria”,
“Technical approach”, “Risks and dependencies”, and “Approval”; assigned TASK;
the changed-file diff; QA evidence; `AGENTS.md`; `PROJECT.md` section “Context
index”; referenced modules; linked ADRs; and applicable standards.

**May load:** narrowly scoped regression evidence and modules required to assess
a documented risk.

**Do not load:** every module, unrelated change history, or broad repository
content not needed to evaluate the diff.

## Migration for adopters

Keep an existing monolithic `PROJECT.md` as the entry point during migration.
First create `knowledge/INDEX.md`, then move one current-state domain at a time
to `knowledge/modules/`, replacing the moved prose with a link in the index.
Preserve all existing paths and mark the migration complete only after each old
category is represented by the index or a linked module.
