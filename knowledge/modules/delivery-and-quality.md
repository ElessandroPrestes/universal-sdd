# Delivery and quality context

## Metadata

| Field | Value |
|---|---|
| Domain | Delivery, quality, security, and operations |
| Owner | Documentation |
| Reviewed | 2026-09-15 |
| Applicability | UX, QA, release, and operational planning |
| Source of truth | `PROJECT.md` context index and linked standards |

## Experience and accessibility

User-facing changes follow `workflows/feature.md`, including discovery, design
approval, accessible specification, design review, and traceable evidence.
The framework has no graphical interface or design-token implementation.

Adopters use `standards/ux-ui.md`, `standards/design-system.md`, and
`standards/accessibility.md`. The framework recommends WCAG 2.2 Level AA as a
default for web projects; adopters declare their target, coverage, tools, and
assistive-technology matrix.

## Quality and security

`standards/testing.md` defines the strategy and
`standards/quality-gates.md` defines release controls. Framework artifacts are
validated through repository structure, internal references, Markdown
consistency, and human review. Adopting software projects define executable
commands, environments, thresholds when useful, compatibility coverage, and
evidence storage.

Documentation and evidence must not expose secrets, credentials, personal data,
or unsafe production data. Adopters define their detailed security standard and
threat model.

## Delivery and limitations

The framework has no CI/CD or deployment process. Consumers copy or adapt it
and connect quality gates to their automation.

- Technology profiles and automatic bootstrapping are planned, not implemented.
- There is no automated Markdown link or schema validation yet.
- The documentation API may change before version 1.0.
