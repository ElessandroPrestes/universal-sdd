# Feature Workflow

## Purpose

Provide the default end-to-end workflow for a feature. Non-user-facing changes
may mark design activities not applicable with a recorded reason. Riskier
profiles may introduce additional approvals.

## 1. Product and UX discovery

Owner: Product and UX Research.

Artifacts:

- `templates/ux-brief.md`;
- existing evidence, assumptions, user groups, current journey, and risks;
- success measures.

Exit: Gate 1 in `standards/quality-gates.md` passes.

## 2. Architecture and feasibility

Owner: Architecture.

Confirm constraints, integrations, data, security, performance, observability,
and architectural decisions. Create an ADR for architectural change.

## 3. UX/UI design

Owner: UX/UI Design.

Artifacts:

- `templates/user-flow.md`;
- wireframe or prototype when needed;
- `templates/design-specification.md`;
- accessibility annotations.

Exit: authorized human design approval is recorded.

## 4. Functional and technical specification

Owner: Spec Agent.

The SPEC links discovery and design artifacts and defines scope, out-of-scope,
acceptance criteria, data, integrations, security, performance, observability,
migration, rollback, and risks.

Exit: business and technical approval is recorded.

## 5. Tasks and QA planning

Owners: Task Agent and QA Agent.

Create implementation tasks, `templates/qa-plan.md`, test cases, compatibility
matrix, regression scope, and acceptance-criteria traceability.

Exit: Gate 2 passes.

## 6. Implementation

Owner: Implementation Agent.

Implement only approved tasks. Add the lowest reliable automated tests that
prove behavior. Record scope questions rather than making undocumented product
or design decisions.

## 7. QA and regression

Owners: Testing and QA Agents.

Run automated, manual, exploratory, compatibility, visual, accessibility,
security, performance, and user/business acceptance checks according to risk.
Record reproducible evidence and defects.

Exit: Gate 3 passes.

## 8. Independent reviews

Owners: Accessibility Review, Design Review, and Review Agents.

Perform applicable reviews independently. Rejected work returns only the
identified issues to implementation or refactoring. Scope changes return to SPEC
and human approval.

Exit: all applicable reviews are approved.

## 9. Release decision

Owners: QA and Release Agents.

QA issues Go, Go with accepted risk, or No-go. Release confirms build, gates,
documentation, version, release notes, deployment, rollback, and monitoring.

Exit: Gate 4 passes.

## 10. Delivery and learning

Run smoke checks and monitor defined signals. Align code, PROJECT.md, SPEC,
decisions, tests, and evidence. Record follow-up work and update standards when a
reusable lesson is identified.

Exit: Gate 5 passes.
