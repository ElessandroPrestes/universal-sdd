# SPEC: Structured QA evidence schema and contract

## Metadata

| Field | Value |
|---|---|
| ID | SPEC-005 |
| Status | Implemented |
| Owner | Spec Agent |
| Reviewers | QA / Engineering |
| Created | 2026-09-15 |
| Updated | 2026-09-15 |
| Target release | Unscheduled |
| Refs: | Discovery: N/A — framework internal change; Design: N/A — no user-facing interface; ADRs: N/A — quality workflow documentation only |

## Problem and outcome

Acceptance criteria in SPEC-004 became machine-consumable, and the QA-Verifier
workflow was defined to compare criteria against evidence. However, without a
structured QA evidence contract and template, verification could not be
performed deterministically, leaving QA-Verifier in a blocked, non-operational
state.

The outcome is a structured QA evidence schema and template
(`templates/QA_EVIDENCE_TEMPLATE.md`), a structured verification report template
(`templates/VERIFICATION_REPORT_TEMPLATE.md`), and updated workflow and testing
standards that make the QA-Verifier operational for active changes.

## Scope

### In scope

- Create `templates/QA_EVIDENCE_TEMPLATE.md` with structured YAML blocks per
  acceptance criterion result.
- Create `templates/VERIFICATION_REPORT_TEMPLATE.md` with reproducible Gate 3
  comparison outputs.
- Update `workflows/verification.md` to reference the structured evidence
  template and declare the verification step operational.
- Update `standards/testing.md` to require structured QA evidence for acceptance
  criteria validation.
- Add structural tests in `tests/test_structured_qa_evidence.py`.

### Out of scope

- Implementing automated parser scripts or CI runner executables.
- Retrofitting past completed SPECs with structured evidence files.
- Changing task IDs, commit trailers, or approval authorities.

## Functional behavior

- Each change requiring QA validation records evidence in a structured document
  based on `templates/QA_EVIDENCE_TEMPLATE.md`.
- Every applicable criterion `AC-NNN` from the SPEC must have an entry containing:
  `criterion_id`, `status` (`passed`, `failed`, or `exception`), `execution_type`,
  `execution_date`, `verified_by`, and `reproducible_evidence`.
- The QA-Verifier workflow step in `workflows/verification.md` compares the
  SPEC's structured criteria against the structured QA evidence.
- The QA-Verifier produces a report using `templates/VERIFICATION_REPORT_TEMPLATE.md`
  classifying any discrepancies as `missing`, `unmapped`, `failed`, or `ambiguous`.
- Code Review cannot proceed while applicable QA-Verifier findings remain open.

## Acceptance criteria

### AC-001: Canonical QA evidence template has machine-consumable criteria results

```yaml
id: AC-001
title: Canonical QA evidence template contains required YAML contract fields
preconditions:
  - An author creates a QA evidence artifact using templates/QA_EVIDENCE_TEMPLATE.md
action: Inspect the criteria evidence entries
expected_result: Each criterion entry contains criterion_id, status, execution_type, execution_date, verified_by, and reproducible_evidence fields
evidence_type: automated
```

### AC-002: Verification report template structures QA-Verifier divergence reporting

```yaml
id: AC-002
title: Verification report template structures comparison and Gate 3 findings
preconditions:
  - QA-Verifier produces a verification report using templates/VERIFICATION_REPORT_TEMPLATE.md
action: Inspect the report structure
expected_result: The template defines SPEC/TASK references, criterion-by-criterion status, divergence classification (missing, unmapped, failed, ambiguous), and Gate 3 pass/block decision
evidence_type: automated
```

### AC-003: Verification workflow and testing standard operationalize structured evidence

```yaml
id: AC-003
title: Verification workflow and testing standard reference structured QA evidence
preconditions:
  - Inspect workflows/verification.md and standards/testing.md
action: Verify references to QA evidence contract
expected_result: workflows/verification.md references templates/QA_EVIDENCE_TEMPLATE.md as operational, and standards/testing.md requires structured evidence for acceptance criteria
evidence_type: automated
```

## Technical approach

Provide canonical uppercase templates in `templates/` using clear YAML blocks
for machine extraction and human readability. Update references in
`workflows/verification.md` and `standards/testing.md` to link the contracts.
Automated unit tests in `tests/test_structured_qa_evidence.py` assert the presence
of required fields and cross-references.

## Risks and dependencies

| Risk or dependency | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|
| Incomplete evidence records | Falsely passing verifications | Medium | Require command, log/artifact, and verified_by in reproducible evidence | QA Agent |
| Unmapped or extra criteria in evidence | Obsolete or undocumented testing | Low | QA-Verifier flags unmapped criteria as blocking Gate 3 findings | QA-Verifier |
| Tooling expectations without parser code | Confusion about automated CI vs portable contract | Low | Clearly document the markdown/YAML format as portable and human/AI verifiable | Spec Agent |

## Open questions

| Question | Owner | Due date | Resolution |
|---|---|---|---|
| Will automated parser scripts be added in a future spec? | Engineering | Future release | Deferred; this spec defines the authoritative document contracts. |

## Approval

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Engineering | | Pending | | |
| QA | | Pending | | |
| Human sponsor | User | Approved | 2026-09-15 | Approval recorded in the CLI conversation. |
