# SPEC: Mechanized traceability

## Metadata

| Field | Value |
|---|---|
| ID | SPEC-001 |
| Status | Implemented |
| Owner | Spec Agent |
| Reviewers | Engineering / QA |
| Created | 2026-09-15 |
| Updated | 2026-09-15 |
| Target release | Unscheduled |
| Related UX brief | N/A — internal framework documentation and tooling change |
| Related design specification | N/A — no user-facing interface |
| Related ADRs | None identified; the change does not alter framework architecture |

## Problem and outcome

The framework requires traceability between approved requirements, executable
work, commits, and QA evidence, but it currently provides no stable identifier
scheme, machine-readable matrix, or commit-time validation. This makes audit
depend on manual document review.

The outcome is reusable, dependency-light framework artifacts that establish
and validate an auditable chain from SPEC to TASK, commit, and QA status.

## Scope

### In scope

- Document stable `SPEC-NNN`, `TASK-NNN-XX`, and `ADR-NNN` identifiers and
  their reference relationships.
- Add ID and `Refs:` fields to reusable SPEC and TASK templates without
  removing the existing lowercase templates.
- Document required `Spec-Ref:` and `Task-Ref:` commit trailers in `AGENTS.md`.
- Add a dependency-light reusable script that scans `specs/`, `tasks/`,
  `reviews/`, and Git history to generate a traceability matrix in `docs/`.
- Add an optional `commit-msg` hook template that validates the required
  trailers.

### Out of scope

- Automated acceptance-criteria verification or structured QA evidence.
- Context-budget restructuring, SPEC amendments, agent handoff contracts,
  external-content sanitization, and framework metrics.
- Installing hooks automatically, changing Git history, or requiring a specific
  programming language, CI provider, or issue tracker.

## Functional behavior

- The identifier guide specifies formats, uniqueness expectations, and how
  artifacts link to their predecessor in the delivery chain.
- The new templates make `ID` and `Refs:` explicit fields for future use while
  retaining backward-compatible existing template paths.
- The matrix generator reports, for each discovered SPEC, linked TASKs,
  matching Git commits, and available QA/review status without modifying source
  artifacts or Git history.
- The optional hook rejects commit messages missing the trailers required by
  the documented convention, while projects remain free to opt in by copying
  it to their Git hooks directory.

## Acceptance criteria

### AC-001: Identifier and linkage convention is reusable

```gherkin
Given a project adopting the framework
When it creates a SPEC, TASK, or ADR
Then the identifier guide defines the required identifier format and linkage
relationships without relying on project-specific examples
```

Evidence required: documentation review.

### AC-002: Templates capture required references

```gherkin
Given an author creates a SPEC or TASK using the new template
When it completes the metadata section
Then it has explicit ID and Refs fields for recording traceability
```

Evidence required: template inspection.

### AC-003: Commit references are documented and optionally validated

```gherkin
Given a project opts into the supplied commit-msg hook
When a commit message omits a required documented reference trailer
Then the hook rejects the commit message with an actionable error
```

Evidence required: local hook test.

### AC-004: The traceability matrix is reproducible

```gherkin
Given a repository containing SPECs, TASKs, reviews, and Git commits
When the matrix generator is run
Then it writes a consultable matrix that maps discovered SPECs to linked TASKs,
matching commits, and QA or review status
```

Evidence required: generator test using repository artifacts.

## Technical approach

Use Markdown documentation and templates plus a standard-library-only script
chosen during implementation. The script must tolerate missing optional
directories and unmatched references, reporting them as gaps rather than
inventing links. The generated matrix format will be Markdown or JSON, selected
in the implementation TASK based on reviewability and testability.

## Delivery and operations

- Rollout plan: publish new artifacts alongside existing templates.
- Migration plan: existing projects may retain current artifacts; new IDs and
  references are adopted incrementally.
- Rollback plan: remove opt-in use of the new script and hook; no data or Git
  history migration is performed.
- Monitoring and alerts: N/A — this framework currently has no runtime.

## Risks and dependencies

| Risk or dependency | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|
| Historical artifacts lack IDs or trailers | Incomplete matrix rows | High | Report gaps explicitly; do not require retroactive rewriting | Implementation Agent |
| Git is unavailable to the script | Commit data cannot be collected | Low | Exit with an actionable diagnostic while preserving source artifacts | Implementation Agent |
| Hook convention conflicts with adopter policy | Adoption friction | Medium | Keep hook optional and document installation/override expectations | Documentation Agent |

## Open questions

| Question | Owner | Due date | Resolution |
|---|---|---|---|
| Should the generated matrix be Markdown, JSON, or both? | Engineering reviewer | Before TASK approval | Open |

## Approval

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Engineering | | Pending | | |
| QA | | Pending | | |
| Human sponsor | User | Approved | 2026-09-15 | Approval recorded in the CLI conversation. |
