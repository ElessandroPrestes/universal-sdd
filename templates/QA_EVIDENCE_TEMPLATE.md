# QA Evidence: <title>

## Metadata

| Field | Value |
|---|---|
| ID | QA-EVIDENCE-NNN |
| Status | In progress / Complete |
| SPEC | SPEC-NNN |
| TASK | TASK-NNN-XX |
| QA Owner | |
| Execution Date | YYYY-MM-DD |
| Build / Commit | |
| Environment | |

## Environment configuration

- OS / Architecture:
- Runtime / Engine:
- Dependencies / Service versions:
- Feature flags / Configurations:
- Test accounts / Permissions:
- Test data baseline / Seed:

## Acceptance criteria evidence

Record one structured YAML entry for each acceptance criterion defined in the SPEC.
Do not infer results or use free prose outside these fields. Every applicable criterion
must be evaluated.

### AC-001 evidence

```yaml
criterion_id: AC-001
status: passed # passed | failed | exception
execution_type: automated # automated | manual | exploratory | accessibility | visual | performance | security
execution_date: YYYY-MM-DD
verified_by: <QA Agent / tester name>
preconditions_met: true
action_taken: <exact action or trigger executed>
observable_result: <observed result matching SPEC expected_result>
reproducible_evidence:
  command: <exact command line executed, or N/A>
  log_or_artifact: <file path, URI, or artifact reference>
  details: <summary of stdout/stderr, screenshots, or reproduction steps>
exception_ref: N/A # N/A or approved exception reference
```

### AC-002 evidence

```yaml
criterion_id: AC-002
status: passed # passed | failed | exception
execution_type: manual # automated | manual | exploratory | accessibility | visual | performance | security
execution_date: YYYY-MM-DD
verified_by: <QA Agent / tester name>
preconditions_met: true
action_taken: <exact action or trigger executed>
observable_result: <observed result matching SPEC expected_result>
reproducible_evidence:
  command: N/A
  log_or_artifact: <path to test notes, screenshot, or video>
  details: <step-by-step verification log>
exception_ref: N/A # N/A or approved exception reference
```

## Summary and findings

| Total criteria | Passed | Failed | Exception |
|---|---|---|---|
| | | | |

### Defects and regressions

| Defect ID | Severity | Criterion | Summary | Status |
|---|---|---|---|---|
| | | | | |

### Residual risks and exceptions

| Exception ID | Criterion | Reason | Approved by | Expiry |
|---|---|---|---|---|
| | | | | |

## Recommendation

- Recommendation: Go / Go with accepted risk / No-go
- Rationale:
- QA Owner and Date:
