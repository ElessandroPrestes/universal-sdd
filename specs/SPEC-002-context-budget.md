# SPEC: Context budget by delivery phase

## Metadata

| Field | Value |
|---|---|
| ID | SPEC-002 |
| Status | Approved |
| Owner | Spec Agent |
| Reviewers | Engineering / QA / Documentation |
| Created | 2026-09-15 |
| Updated | 2026-09-15 |
| Target release | Unscheduled |
| Refs: | Discovery: N/A — framework internal change; Design: N/A — no user-facing interface; ADRs: N/A — documentation and retrieval structure only |

## Problem and outcome

`PROJECT.md` currently combines all framework state in one document and agents
receive no precise, phase-specific context bundle. As the knowledge base grows,
agents either load too much context or make inconsistent omissions.

The outcome is a short canonical project index, modular knowledge records with
metadata-only discovery, and an explicit context budget for Discovery,
Architecture, Implementation, QA, and Review. An agent can therefore retrieve
only the active SPEC, assigned TASK where applicable, and the knowledge modules
explicitly relevant to its phase.

## Scope

### In scope

- Add `docs/context-budget.md` with exact required files and permitted sections
  for Discovery, Architecture, Implementation, QA, and Review.
- Reduce `PROJECT.md` to a short canonical index that links to modular context.
- Create `knowledge/INDEX.md` containing metadata and retrieval guidance, not
  the copied content of its modules.
- Move the current project-state content into reusable domain modules under
  `knowledge/modules/` without losing canonical information.
- Add an explicit `AGENTS.md` rule forbidding agents from loading the full
  knowledge base when the active SPEC references selected modules.
- Preserve existing paths where possible and document a migration path for
  adopters that rely on monolithic `PROJECT.md`.

### Out of scope

- Changing workflow order, quality gates, IDs, task references, or agent roles.
- Building semantic search, embeddings, a vector database, token counting, or
  a runtime context loader.
- Altering adopter-project knowledge content beyond reusable templates and
  migration guidance.

## Functional behavior

- Each phase’s budget names the mandatory documents, optional documents, and
  prohibited broad reads; a phase may load only knowledge modules named by its
  active SPEC or explicitly justified by a recorded risk.
- `PROJECT.md` remains the canonical entry point, but its detail is represented
  by links to modules rather than duplicated prose.
- `knowledge/INDEX.md` supports selective retrieval using module title, domain,
  owner, update date, summary metadata, and source-of-truth status.
- A migration note makes the new modules additive and allows adopters to retain
  their existing monolithic file while transitioning.

## Acceptance criteria

### AC-001: Every delivery phase has an enforceable context bundle

```gherkin
Given an agent starts Discovery, Architecture, Implementation, QA, or Review
When it consults the context-budget guide
Then it can identify the exact required files, allowed module selection, and
prohibited repository-wide reads for that phase
```

Evidence required: documentation review.

### AC-002: Project context supports selective retrieval

```gherkin
Given an agent opens PROJECT.md and knowledge/INDEX.md
When it needs context for an active change
Then it can locate relevant modules from metadata without loading every module
or losing any prior canonical project-state category
```

Evidence required: migration and link audit.

### AC-003: Active work loads only relevant knowledge

```gherkin
Given an active SPEC references selected knowledge modules
When an agent follows AGENTS.md
Then it loads the active SPEC, its assigned TASK when applicable, and only the
referenced modules unless a documented risk requires another module
```

Evidence required: policy inspection.

### AC-004: Adoption remains backward compatible

```gherkin
Given a project using the prior monolithic PROJECT.md convention
When it adopts the new guidance
Then it has a documented incremental migration path and no required file is
renamed or removed
```

Evidence required: documentation review.

## Technical approach

The implementation will use Markdown only. It will inventory each current
`PROJECT.md` category before moving it to one or more named knowledge modules,
then link the short index and metadata index to those modules. The exact module
boundaries will follow that inventory and be recorded in the implementation TASK
to avoid duplicating or silently discarding current canonical state.

## Risks and dependencies

| Risk or dependency | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|
| Context budget omits a material source | Incorrect delivery decision | Medium | Require a documented risk-based exception and validate each phase bundle | QA Agent |
| Detail is lost while modularizing PROJECT.md | Documentation divergence | Medium | Audit every current section against the new index and modules | Documentation Agent |
| Modules reproduce normative policies | Conflicting sources of truth | Medium | Link to authoritative standards and workflows instead of copying them | Implementation Agent |

## Open questions

| Question | Owner | Due date | Resolution |
|---|---|---|---|
| What maximum length qualifies PROJECT.md as a short index? | Engineering reviewer | 2026-09-15 | Resolved: target 75 lines or fewer, excluding a final newline. |

## Approval

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Engineering | | Pending | | |
| QA | | Pending | | |
| Documentation | | Pending | | |
| Human sponsor | User | Approved | 2026-09-15 | Approval recorded by the instruction to execute. |
