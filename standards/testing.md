# Testing Standard

## Purpose

Define a risk-based testing strategy that demonstrates conformance to the
approved SPEC and prevents regressions. Test type and depth depend on impact,
not only on implementation size.

## Test levels

- **Unit:** isolated business rules, transformations, and component logic.
- **Integration:** boundaries such as database, service, queue, filesystem, or
  component integration.
- **Contract:** compatibility between independently deployed consumers and providers.
- **End-to-end:** critical journeys across the deployed system.
- **Manual/exploratory:** emergent behavior, usability, content, recovery, and
  risks that automation does not adequately cover.
- **User/business acceptance (UAT):** confirmation by authorized stakeholders
  that critical business workflows and acceptance outcomes are fit for use.
- **Non-functional:** accessibility, security, performance, resilience,
  compatibility, and observability when applicable.
- **Visual regression:** stable visual contracts for important components and
  screens, with reviewed baselines and controlled environments.

Prefer the lowest reliable test level that proves the behavior. Do not duplicate
every assertion at every level.

## QA plan and traceability

Every material change requires `templates/qa-plan.md`. Each acceptance criterion
must map to one or more of:

- an automated test identifier;
- a manual test case and execution record;
- an approved reason why validation is not applicable.

The mapping must include positive, negative, permission, error, boundary, and
recovery behavior when relevant.

## Test environments and data

Record environment, build or commit, configuration, dependencies, feature flags,
accounts, and data prerequisites. Test data must be deterministic, privacy-safe,
isolated, and recoverable. Never copy sensitive production data without an
approved and compliant process.

## Regression and compatibility

Use `templates/regression-checklist.md` to select affected journeys, integrations,
platforms, browsers, devices, locales, and assistive technologies. Regression
scope must follow the impact analysis; “only changed files” is not sufficient.

## Reliability

A test is useful only when its result is repeatable and diagnosable. A flaky test
must be recorded with an owner and remediation target. Quarantine requires an
approved exception and replacement coverage; silent retries must not conceal a
failure.

## Coverage

Projects may define numeric coverage thresholds, but line coverage alone is not
a quality gate. Required coverage includes critical risks, acceptance criteria,
business rules, failures, and integration boundaries.

## Defects

Use `templates/bug-report.md`.

Severity describes user or system impact:

- **S1 Critical:** security or safety incident, widespread outage, unrecoverable
  data loss, or a critical journey blocked without workaround.
- **S2 High:** major function or user group blocked; workaround is impractical.
- **S3 Medium:** degraded behavior with a reasonable workaround.
- **S4 Low:** minor problem with limited functional impact.

Priority describes repair order and is decided separately from severity.

## Evidence and results

Evidence must include build, environment, command or steps, result, timestamp,
and relevant logs, reports, screenshots, recordings, or links. A reviewer must be
able to reproduce the conclusion without relying on undocumented context.
