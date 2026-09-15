# SPEC: SPEC amendment protocol

## Metadata

| Field | Value |
|---|---|
| ID | SPEC-003 |
| Status | Approved |
| Owner | Spec Agent |
| Reviewers | Product / Engineering / QA |
| Created | 2026-09-15 |
| Updated | 2026-09-15 |
| Target release | Unscheduled |
| Refs: | Discovery: N/A — framework internal change; Design: N/A — no user-facing interface; ADRs: N/A — workflow documentation only |

## Problem and outcome

Implementation discoveries currently have no lightweight, auditable route for
clarifying an approved SPEC. Teams may either bypass the approval record or
repeat a full approval cycle for wording that does not change observable
behavior.

The outcome is a reusable change-request record and objective gate criteria
that distinguish a clarification from a scope change, preserve SPEC versions,
and ensure any material behavior change returns to human approval.

## Scope

### In scope

- Extend the ID and traceability guide with the SPEC amendment lifecycle and
  `SPEC-NNN-vN` reference rules.
- Add `templates/CHANGE_REQUEST_TEMPLATE.md` with distinct lightweight
  clarification and scope-change flows.
- Add objective classification and approval requirements to
  `standards/quality-gates.md`.

### Out of scope

- Changing the existing approval authority, quality-gate sequence, task-ID
  scheme, or traceability generator.
- Automatically approving, merging, or applying a change request.
- Defining issue-tracker, notification, or asynchronous-approval tooling.

## Functional behavior

- A lightweight clarification records the question, resolution, rationale, and
  asynchronous approval; it cannot modify observable behavior or acceptance
  criteria.
- A scope change records impact and creates an amended SPEC version, requiring
  the full applicable human approval cycle before implementation continues.
- Quality gates classify a request using explicit observable-behavior and
  acceptance-criteria tests; uncertainty is treated as a scope change.

## Acceptance criteria

### AC-001: SPEC amendments preserve versioned traceability

```gherkin
Given an approved SPEC requires a scope change
When an amendment is recorded
Then the guide defines its SPEC-NNN-vN identifier, predecessor reference, and
approval relationship without overwriting the prior approved SPEC
```

Evidence required: documentation review.

### AC-002: Change requests expose both decision paths

```gherkin
Given an implementation discovery
When an author uses the change-request template
Then it can record either a lightweight clarification or a scope change with
the required impact, decision, and approval fields for that path
```

Evidence required: template inspection.

### AC-003: Classification is a blocking quality gate

```gherkin
Given a proposed change request
When its observable behavior or acceptance-criteria impact is uncertain or changed
Then the quality-gate standard classifies it as a scope change and blocks
implementation until human approval is recorded
```

Evidence required: standards review.

## Technical approach

Use Markdown documentation and a reusable template only. Preserve `SPEC-NNN`
as the base identifier and add `-vN` only for approved scope amendments. The
implementation will explicitly record that a clarification is not a new SPEC
version, while a scope change never replaces the approved predecessor.

## Risks and dependencies

| Risk or dependency | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|
| Clarifications are mislabeled to bypass approval | Undocumented scope expansion | Medium | Use objective gate questions and classify uncertainty as scope change | QA Agent |
| Versioning conflicts with task or commit references | Broken traceability | Low | Document exact references and preserve prior artifacts | Implementation Agent |
| Async approval lacks durable evidence | Unverifiable decision | Medium | Require approver, timestamp, and stable approval reference | Spec Agent |

## Open questions

| Question | Owner | Due date | Resolution |
|---|---|---|---|
| Which human roles may give asynchronous clarification approval? | Product owner | 2026-09-15 | Resolved: the same human authority that approved the base SPEC. |

## Approval

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Product | | Pending | | |
| Engineering | | Pending | | |
| QA | | Pending | | |
| Human sponsor | User | Approved | 2026-09-15 | Approval recorded in the CLI conversation. |
