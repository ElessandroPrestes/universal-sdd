# QA Verification Report: <title>

## Metadata

| Field | Value |
|---|---|
| ID | VR-NNN |
| Status | Passed / Blocked |
| SPEC | SPEC-NNN |
| TASK | TASK-NNN-XX |
| Evidence Ref | <path to QA evidence file> |
| Verifier | QA-Verifier |
| Execution Date | YYYY-MM-DD |

## Comparison results

QA-Verifier compares every structured criterion in the approved SPEC against the
structured QA evidence. Each item is classified as:

- **verified:** evidence matches the criterion, preconditions, action, and expected result, with passing status or approved exception.
- **missing:** no QA evidence entry exists for this criterion ID.
- **unmapped:** evidence cannot be linked exactly to one approved criterion ID.
- **failed:** linked evidence records a failed result.
- **ambiguous:** criterion or evidence lacks sufficient structured detail to confirm verification.

| Criterion ID | SPEC Expected Result | Evidence Status | Verifier Classification | Notes / Finding |
|---|---|---|---|---|
| AC-001 | | passed | verified | |
| AC-002 | | passed | verified | |

## Unresolved findings

List every missing, unmapped, failed, or ambiguous item. Any open finding blocks Code Review.

| Finding ID | Criterion | Classification | Description | Required action |
|---|---|---|---|---|
| | | | | |

## Gate 3 decision

- Gate status: **Pass** (Ready for Code Review) / **Blocked** (Findings open)
- Open findings count: 0
- Authorized exceptions: None / <reference>
- Verifier signature and timestamp:
