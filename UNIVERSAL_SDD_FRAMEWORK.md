# Universal SDD Framework (USF)

> Version: pre-1.0 development draft

## Purpose

This framework provides a language-agnostic, AI-agnostic implementation of
Spec-Driven Development (SDD). It is intended to be copied into **any software
project** (web, mobile, backend, desktop, APIs, libraries, SaaS, ERP, CLI, etc.)
and then populated by an LLM by inspecting the real source code.

---

# Principles

1. An approved SPEC defines the intended behavior of a change.
2. PROJECT.md records the canonical current state of the project.
3. Code and QA evidence demonstrate the implemented behavior.
4. Any divergence among SPEC, PROJECT.md, code, and evidence is resolved explicitly.
5. Humans approve business and user-experience decisions.
6. AI executes within approved scope.
7. Every decision is documented.
8. Architecture evolves through ADRs.
9. Quality, design, accessibility, and code reviews are mandatory when applicable.
10. Documentation evolves with the code.

---

# Recommended Repository Layout

```text
/
PROJECT.md
AGENTS.md
CLAUDE.md
GEMINI.md
COPILOT.md

agents/
workflows/
profiles/
knowledge/
standards/
templates/
adr/
specs/
tasks/
reviews/
docs/
```

---

# PROJECT.md

The canonical project state.

Must contain:

- Project overview
- Business domain
- Architecture
- Stack
- Versions
- Dependencies
- Folder structure
- Runtime
- Environment variables
- APIs
- Security
- User experience and interface conventions
- Design system and accessibility baseline
- Testing strategy and quality gates
- CI/CD
- Deployment
- Coding standards
- Known limitations
- Technologies intentionally NOT used

For an active change, the approved SPEC is the acceptance baseline. After the
change is accepted, code, PROJECT.md, and QA evidence must be aligned. A
divergence is recorded and resolved as a defect, approved scope change, or
documentation debt; it must never be silently ignored.

---

# AI Entry Files

Each AI-specific file only redirects to PROJECT.md.

Example:

```md
Read PROJECT.md first.

Then identify:

- Active workflow
- Current agent
- Relevant specification
- Relevant task

Never start implementation before reading them.
```

---

# Agents

## Discovery Agent

Maps existing code.

Produces:

- project inventory
- missing documentation
- risks

Never modifies code.

---

## UX Research Agent

Discovers user needs before interface decisions are made.

Produces:

- UX brief
- user groups and needs
- journeys or task flows
- assumptions and research questions
- usability risks

Never invents user evidence. Assumptions must be labeled and approved.

---

## UX/UI Design Agent

Turns approved user needs and product requirements into implementable interface
behavior.

Produces:

- user flows
- wireframes or prototypes when needed
- design specification and component mapping
- responsive behavior and interface states
- accessibility annotations

Never starts implementation and never bypasses human design approval.

---

## Architecture Agent

Defines architecture.

Produces:

- architecture proposal
- ADRs
- impacts

Never writes production code.

---

## Spec Agent

Creates specifications.

Produces:

- SPEC
- acceptance criteria
- scope
- out-of-scope

Must ask questions whenever ambiguity exists.

---

## Task Agent

Breaks SPEC into executable tasks.

Produces:

- implementation order
- validation checklist
- risks

---

## Implementation Agent

Implements only approved tasks.

Never expands scope.

---

## Testing Agent

Creates or updates:

- unit tests
- integration tests
- e2e tests

Follows `standards/testing.md` and records evidence against acceptance criteria.

---

## QA Agent

Owns risk-based quality planning and independent validation.

Produces:

- QA plan and traceability matrix
- manual and exploratory test evidence
- regression result
- defect reports with severity and priority
- release quality recommendation

Does not silently accept failed gates or residual risk.

---

## Accessibility Review Agent

Validates applicable accessibility requirements using automated and manual
checks. Records violations, evidence, impact, and exceptions.

---

## Design Review Agent

Compares the implemented interface with the approved design specification.

Checks:

- layout and visual hierarchy
- component and token usage
- responsive behavior
- content and interaction states
- accessibility annotations

Outputs Approved, Approved with remarks, or Rejected. Never edits application
code while acting as reviewer.

---

## Review Agent

Reviews implementation.

Outputs:

- Approved
- Approved with remarks
- Rejected

Never edits application code.

---

## Refactor Agent

Only fixes issues identified by Review Agent.

Never creates new features.

---

## Documentation Agent

Updates:

PROJECT.md

ADRs

Knowledge Base

Specs

Tasks

---

## Release Agent

Validates release readiness.

Checks:

build

tests

quality gates

design and accessibility approvals when applicable

documentation

version

release notes

---

# Knowledge Base

Entries in `knowledge/` may be organized by architecture, business, glossary,
integrations, stack, patterns, or another taxonomy defined by the adopting
project. Use `templates/knowledge-entry.md` and avoid duplicating ADRs or SPECs.

---

# Standards

```
standards/

coding.md
security.md
performance.md
testing.md
quality-gates.md
database.md
api.md
commits.md
accessibility.md
ux-ui.md
design-system.md
```

---

# Profiles

Reusable project presets.

Examples

- backend-api
- laravel
- symfony
- spring
- dotnet
- express
- nextjs
- react
- angular
- vue
- flutter
- react-native
- cli
- library
- monolith
- microservice

The active profile defines validations, commands and conventions.

---

# Templates

Provided baseline templates:

- `templates/spec.md`
- `templates/project.md`
- `templates/task.md`
- `templates/adr.md`
- `templates/rfc.md`
- `templates/review.md`
- `templates/ux-brief.md`
- `templates/user-flow.md`
- `templates/design-specification.md`
- `templates/usability-test-plan.md`
- `templates/qa-plan.md`
- `templates/test-case.md`
- `templates/regression-checklist.md`
- `templates/accessibility-checklist.md`
- `templates/design-review.md`
- `templates/bug-report.md`
- `templates/release-plan.md`
- `templates/deploy-plan.md`
- `templates/post-mortem.md`

Adopting projects may extend or map these to canonical templates in their own
tooling while preserving the required metadata and traceability.

---

# Workflow

Idea

↓

Product and UX Discovery

↓

Architecture

↓

UX/UI Design (when user-facing)

↓

Human Design Approval

↓

Functional and Technical Specification

↓

Human Approval

↓

Tasks

↓

Implementation

↓

Automated and Manual QA

↓

Accessibility Review (when applicable)

↓

Design Review (when user-facing)

↓

Code Review

↓

Refactor (if needed)

↓

Documentation

↓

Release

Rejected reviews return to implementation and the applicable QA checks repeat.
Any requested scope change returns to specification and human approval.

---

# Universal Rules

- Never invent requirements.
- Never skip approval.
- Never modify unrelated files.
- Never introduce dependencies without justification.
- Every feature must have:
  - SPEC
  - TASK
  - REVIEW
- Every user-facing change must also have:
  - UX brief or an explicit reason why it is not needed
  - approved design specification
  - design review
  - accessibility evidence
- Every change must satisfy the applicable quality gates before release.
- Acceptance criteria must be traceable to test evidence.
- Failed gates and residual risks require an explicit human exception with owner and expiry.
- Every architectural change must create an ADR.
- Every relevant implementation updates PROJECT.md.
- Documentation and evidence align with the accepted implementation.

---

# Bootstrapping a New Project

When this framework is copied into a repository, the first AI must:

1. Read the entire repository.
2. Populate PROJECT.md from the existing code.
3. Detect technologies automatically.
4. Detect architecture.
5. Detect package manager/build system.
6. Detect testing strategy.
7. Detect the design system and interface conventions.
8. Detect the accessibility baseline.
9. Define applicable quality gates.
10. Populate Knowledge Base.
11. Create missing ADRs if required.
12. Suggest improvements but never apply without approval.
13. Wait for approved discovery, design, and specification artifacts as applicable.

At this point the repository is considered SDD-ready.
