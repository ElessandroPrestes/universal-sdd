# SPEC: <title>

## Metadata

| Field | Value |
|---|---|
| ID | SPEC-NNN |
| Status | Draft / In review / Approved / Implemented / Superseded |
| Owner | |
| Reviewers | Product / Design / Engineering / QA / Security |
| Created | YYYY-MM-DD |
| Updated | YYYY-MM-DD |
| Target release | |
| Refs: | Discovery: <path or N/A — reason>; Design: <path or N/A — reason>; ADRs: <ADR-NNN or N/A — reason> |

## Problem and outcome

Describe the problem, affected groups, current evidence, desired outcome, and
success measures. Distinguish facts from assumptions.

## Scope

### In scope

-

### Out of scope

-

## Functional behavior

Describe rules, permissions, validations, data changes, integrations, failure
handling, idempotency, concurrency, and applicable edge cases.

## Non-functional requirements

- Security and privacy:
- Performance and capacity:
- Reliability and recovery:
- Accessibility:
- Compatibility:
- Observability:

## Acceptance criteria

Use one YAML block per criterion. Do not add fulfillment-relevant free prose
outside these fields. `id` is immutable after approval so TASKs and QA evidence
can map to it.

### AC-001

```yaml
id: AC-001
title: <short observable behavior>
preconditions:
  - <required state or permission>
action: <actor action or triggering event>
expected_result: <observable result>
evidence_type: automated / manual / accessibility / design / other
```

## Technical approach

Summarize affected components, APIs, schemas, migrations, feature flags,
dependencies, compatibility, and rejected alternatives.

## Delivery and operations

- Rollout plan:
- Migration plan:
- Rollback plan:
- Monitoring and alerts:

## Risks and dependencies

| Risk or dependency | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|
| | | | | |

## Open questions

| Question | Owner | Due date | Resolution |
|---|---|---|---|
| | | | |

## Approval

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Product | | Approved / Rejected | | |
| Design | | Approved / Rejected / N/A | | |
| Engineering | | Approved / Rejected | | |
| QA | | Ready / Not ready | | |
