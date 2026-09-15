# Quality Gates Standard

## Purpose

Define auditable entry and exit criteria for each stage. The active profile may
add stricter checks but must not remove these baseline gates without an approved
exception.

## Gate 1: Ready for design

- Problem, affected users, outcome, constraints, and risks are recorded.
- Evidence and assumptions are distinguishable.
- Research needs and success measures are defined.

## Gate 2: Ready for implementation

- UX brief and user flow are approved for user-facing changes.
- Design specification covers applicable states, content, responsiveness,
  components, tokens, and accessibility.
- SPEC has approved scope, out-of-scope, and testable acceptance criteria.
- Dependencies, migrations, risks, observability, and rollback are addressed.
- Tasks and QA plan provide acceptance-criteria traceability.
- Unresolved questions are closed or explicitly accepted.

## SPEC amendment classification

Before implementation continues after a discovery, create a change request and
classify it using `templates/CHANGE_REQUEST_TEMPLATE.md`.

A request is a **lightweight clarification** only if every statement is true:

- it does not change any observable result, including user experience, API,
  permissions, data, error behavior, compatibility, performance, reliability,
  security, or operation;
- it does not add, remove, weaken, reinterpret, or otherwise alter an
  acceptance criterion;
- its question, resolution, rationale, and durable asynchronous approval from
  the same human authority that approved the base SPEC are recorded.

A request is a **scope change** if any statement above is false or unknown. It
is a blocking gate: stop implementation, create the next `SPEC-NNN-vN` with a
predecessor reference, assess applicable design and technical impacts, and
obtain a new applicable human approval cycle before creating or continuing
implementation TASKs. No agent may classify uncertainty as a clarification.

## Gate 3: Ready for review

- Approved tasks are implemented without undocumented scope expansion.
- Required automated tests pass in the defined environment.
- Manual, exploratory, compatibility, and non-functional checks are completed as applicable.
- Regression scope is executed.
- QA-Verifier in `workflows/verification.md` compares every applicable
  structured acceptance-criterion ID with structured QA evidence before Code
  Review starts.
- Missing, unmapped, failed, or ambiguous QA-Verifier findings block Code Review
  until resolved or covered by an authorized exception.
- Documentation and release-impact notes are updated.
- Defects and residual risks are recorded.

## Gate 4: Ready for release

- Acceptance criteria have passing evidence.
- Build and required CI checks pass.
- No open S1 or S2 defects exist.
- S3 and S4 defects have an explicit disposition.
- Code review is approved.
- Design review and accessibility review are approved for applicable changes.
- Product or business acceptance is recorded when UAT is required.
- Security, performance, data, deployment, and rollback checks pass when applicable.
- QA provides a release recommendation.
- Version and release notes are ready.

## Gate 5: Done

- The accepted implementation is deployed or distributed as planned.
- Smoke checks and required monitoring confirm expected behavior.
- PROJECT.md, SPEC, decisions, tests, and evidence reflect the delivered state.
- Follow-up work has an owner and target.
- Learning that changes future behavior is captured in standards or the Knowledge Base.

## Exceptions

A human with documented authority may approve an exception. It must contain:

- failed or skipped gate;
- reason and evidence;
- user, business, security, and operational impact;
- mitigation and monitoring;
- accountable owner;
- expiration or remediation date;
- approval identity and timestamp.

An exception does not turn a failed check into a passing check. Expired
exceptions block subsequent releases until renewed or resolved.

## Release decision

The QA recommendation is one of:

- **Go:** all applicable gates pass;
- **Go with accepted risk:** only authorized, unexpired exceptions remain;
- **No-go:** a blocking gate failed or evidence is incomplete.
