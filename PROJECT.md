# Universal SDD Project State

## Overview

Universal SDD Framework (USF) is a language- and AI-agnostic documentation
framework for Spec-Driven Development. This repository contains the framework's
canonical guidance, roles, standards, workflows, and templates.

## Domain and users

- Domain: software-development governance and delivery.
- Primary users: product, design, engineering, QA, accessibility, architecture,
  documentation, and release practitioners working with people or AI agents.
- Main outcome: approved requirements become traceable implementation and
  reproducible quality evidence.

## Current version and status

- Documented version: pre-1.0 development draft.
- Status: active development.
- Runtime: none; the project currently consists of Markdown documentation.
- Dependencies: none.

## Canonical source hierarchy

- An approved SPEC is the acceptance baseline for an active change.
- This `PROJECT.md` records the canonical current state of the framework project.
- Repository content and QA evidence demonstrate what has been delivered.
- Divergence is handled explicitly as a defect, scope change, or documentation debt.

## Repository structure

| Path | Responsibility |
|---|---|
| `README.md` | Portuguese overview and adoption entry point |
| `UNIVERSAL_SDD_FRAMEWORK.md` | Core language-agnostic framework definition |
| `AGENTS.md` and AI entry files | Shared session startup and scope protocol |
| `agents/` | Specialized role contracts and boundaries |
| `workflows/` | End-to-end delivery workflows |
| `standards/` | Operational UX/UI, design-system, accessibility, testing, and gate rules |
| `templates/` | Versioned artifacts for specifications, design, QA, evidence, and defects |
| `specs/`, `tasks/`, `reviews/`, `adr/` | Versioned change and decision records |
| `knowledge/` and `profiles/` | Reusable context and project-specific adaptations |
| `docs/` | Adoption, architecture, governance, and reference documentation |

## Architecture

The framework is modular Markdown. The core document defines universal
governance; role files define ownership; standards define normative rules;
workflows define sequence and gates; templates capture decisions and evidence.
Adopting projects may extend these documents through profiles but must record
exceptions to baseline quality gates.

## UX/UI and design system

- UX/UI process: `standards/ux-ui.md`.
- Design-system governance: `standards/design-system.md`.
- User-facing work follows `workflows/feature.md` and requires discovery, design
  approval, accessible specifications, design review, and traceable evidence.
- The framework itself has no graphical interface or design-token implementation.

## Accessibility

- Baseline policy: `standards/accessibility.md`.
- Adopting projects must declare their standard, version, conformance target,
  platform coverage, tools, and assistive-technology matrix.
- The framework recommends WCAG 2.2 Level AA as the default for web projects.

## Testing and QA

- Strategy: `standards/testing.md`.
- Release controls: `standards/quality-gates.md`.
- UX/UI and QA artifacts are validated through repository structure, internal
  references, Markdown consistency, and human review.
- Adopting software projects must define executable commands, environments,
  numeric thresholds where useful, compatibility coverage, and evidence storage.

## Security and privacy

Documentation and evidence must not expose secrets, credentials, personal data,
or unsafe production test data. Adopting projects define their detailed security
standard and threat model.

## CI/CD and deployment

No CI/CD or deployment process is currently implemented. Consumers copy or
adapt the framework into their repositories and connect its quality gates to
their own automation.

## Known limitations

- Technology profiles and automatic bootstrapping are planned but not implemented.
- The project has no automated Markdown link or schema validation yet.
- The documentation API may change before version 1.0.

## Technologies intentionally not used

- No programming language or application framework is required.
- No AI vendor-specific behavior is normative.
- No design, issue-tracking, test-management, or CI vendor is mandatory.
