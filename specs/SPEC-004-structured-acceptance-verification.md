# SPEC: Structured acceptance criteria and QA verification gate

## Metadata

| Field | Value |
|---|---|
| ID | SPEC-004 |
| Status | Approved |
| Owner | Spec Agent |
| Reviewers | Engineering / QA |
| Created | 2026-09-15 |
| Updated | 2026-09-15 |
| Target release | Unscheduled |
| Refs: | Discovery: N/A — framework internal change; Design: N/A — no user-facing interface; ADRs: N/A — quality workflow documentation only |

## Problem and outcome

Acceptance criteria currently allow prose and do not define a consumable
contract for comparing approved behavior to QA evidence. The rule against
silent divergence therefore depends on manual interpretation.

The outcome is a structured acceptance-criteria format in the canonical SPEC
template and a blocking QA-Verifier workflow step that reports every missing,
unmapped, failed, or ambiguous criterion before code review.

## Scope

### In scope

- Update `templates/SPEC_TEMPLATE.md` with a structured, stable acceptance
  criterion format.
- Add `workflows/verification.md` defining QA-Verifier inputs, comparison,
  output, divergence reporting, and its position before Code Review.
- Add the QA-Verifier as a blocking condition in `standards/quality-gates.md`.

### Out of scope

- Defining the structured QA-evidence file itself; that belongs to Melhoria 6.
- Implementing an automated parser, CI integration, or changing existing SPECs.
- Changing task IDs, commit trailers, approval authorities, or test strategy.

## Functional behavior

- Each new criterion in the canonical SPEC template has a stable `AC-NNN` ID,
  preconditions, action, expected observable result, and required evidence type
  in structured YAML.
- QA-Verifier compares every structured criterion to structured QA evidence;
  it emits a reproducible list of unmapped, missing, failed, or ambiguous items
  rather than inferring fulfillment.
- Until the QA-evidence contract of Melhoria 6 exists, the QA-Verifier gate is
  documented but cannot pass for changes that require QA evidence.
- Code Review cannot start while applicable QA-Verifier findings remain open.

## Acceptance criteria

### AC-001: Canonical SPEC template has machine-consumable criteria

```gherkin
Given an author uses the canonical SPEC template
When it defines an acceptance criterion
Then the criterion has structured ID, precondition, action, expected result,
and evidence-type fields without relying on free prose
```

Evidence required: template inspection.

### AC-002: QA-Verifier reports divergence before review

```gherkin
Given an approved SPEC and its QA evidence
When QA-Verifier compares criterion IDs and outcomes
Then it lists every missing, unmapped, failed, or ambiguous criterion before
Code Review may begin
```

Evidence required: workflow and gate review.

### AC-003: Verification is a blocking quality gate

```gherkin
Given QA-Verifier has unresolved applicable findings
When the change requests Code Review
Then the quality-gate standard blocks the transition until the findings are
resolved or have an authorized exception
```

Evidence required: standards review.

## Technical approach

Use a YAML code block per acceptance criterion in the uppercase canonical
template. The workflow specifies a technology-agnostic comparison contract and
names the forthcoming QA-evidence schema as a dependency. This preserves the
legacy lowercase template and avoids adding a parser before its input and
evidence schemas are both defined.

## Risks and dependencies

| Risk or dependency | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|
| QA-evidence schema is not yet available | Gate cannot produce a passing result | High | Mark Melhoria 6 as an explicit prerequisite for operational use | QA Agent |
| Existing SPECs use prose criteria | Migration burden | High | Preserve legacy templates and require the new format only for new canonical SPECs | Documentation Agent |
| Criteria are structurally complete but vague | False confidence | Medium | Require observable expected results and flag ambiguity as a finding | QA-Verifier |

## Open questions

| Question | Owner | Due date | Resolution |
|---|---|---|---|
| Should the QA-Verifier be automated after Melhoria 6? | Engineering reviewer | After Melhoria 6 | Deferred; this change defines only the portable contract and gate. |

## Approval

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Engineering | | Pending | | |
| QA | | Pending | | |
| Human sponsor | User | Approved | 2026-09-15 | Approval recorded in the CLI conversation. |
