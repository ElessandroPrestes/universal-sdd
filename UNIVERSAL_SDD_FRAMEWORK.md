# Universal SDD Framework (USF)

> Version: 1.0.0

## Purpose

This framework provides a language-agnostic, AI-agnostic implementation of
Spec-Driven Development (SDD). It is intended to be copied into **any software
project** (web, mobile, backend, desktop, APIs, libraries, SaaS, ERP, CLI, etc.)
and then populated by an LLM by inspecting the real source code.

---

# Principles

1. Code is the Source of Truth.
2. Specifications drive implementation.
3. Humans approve business decisions.
4. AI executes within approved scope.
5. Every decision is documented.
6. Architecture evolves through ADRs.
7. Reviews are mandatory.
8. Documentation evolves with the code.

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
decisions/
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
- CI/CD
- Deployment
- Coding standards
- Known limitations
- Technologies intentionally NOT used

Whenever documentation diverges from source code, source code wins.

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

documentation

version

release notes

---

# Knowledge Base

```
knowledge/
 architecture/
 business/
 glossary/
 integrations/
 stack/
 patterns/
 decisions/
```

---

# Standards

```
standards/

coding.md
security.md
performance.md
testing.md
database.md
api.md
commits.md
accessibility.md
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

Mandatory templates

- SPEC
- TASK
- REVIEW
- ADR
- RFC
- BUG REPORT
- TEST PLAN
- RELEASE PLAN
- DEPLOY PLAN
- POST MORTEM

---

# Workflow

Idea

↓

Discovery

↓

Architecture

↓

Specification

↓

Human Approval

↓

Tasks

↓

Implementation

↓

Testing

↓

Review

↓

Refactor (if needed)

↓

Documentation

↓

Release

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
- Every architectural change must create an ADR.
- Every relevant implementation updates PROJECT.md.
- Documentation follows the code.

---

# Bootstrapping a New Project

When this framework is copied into a repository, the first AI must:

1. Read the entire repository.
2. Populate PROJECT.md from the existing code.
3. Detect technologies automatically.
4. Detect architecture.
5. Detect package manager/build system.
6. Detect testing strategy.
7. Populate Knowledge Base.
8. Create missing ADRs if required.
9. Suggest improvements but never apply without approval.
10. Wait for the first specification.

At this point the repository is considered SDD-ready.
