# IDs and traceability

## Purpose

This convention makes the delivery chain auditable without imposing an issue
tracker, programming language, CI provider, or automatic Git-hook installation.
It supplements, rather than replaces, human approval and QA evidence.

## Stable identifiers

| Artifact | Format | Example | Allocation rule |
|---|---|---|---|
| Specification | `SPEC-NNN` | `SPEC-042` | Use the next unused three-digit sequence in `specs/`. |
| Specification amendment | `SPEC-NNN-vN` | `SPEC-042-v2` | Keep the base identifier and increment `N` only for an approved SPEC amendment. |
| Task | `TASK-NNN-XX` | `TASK-042-01` | Reuse the three-digit base SPEC number; increment the two-digit task sequence. |
| Architecture decision | `ADR-NNN` | `ADR-017` | Use the next unused three-digit sequence in `adr/`. |

Identifiers are immutable once an artifact is shared for review. Do not reuse an
identifier from a superseded, rejected, or deleted artifact. A SPEC amendment
references its predecessor and is a separate approval artifact; its tasks use
the amended SPEC identifier in their `Refs:` field.

## Required references

New artifacts use the uppercase templates in `templates/`. The legacy
lowercase templates remain available for compatible adoption.

| Artifact | Required `Refs:` content |
|---|---|
| SPEC | Discovery, design, and applicable ADR references; record `N/A — <reason>` when an upstream activity does not apply. |
| TASK | Its exact approved SPEC identifier, applicable acceptance-criterion IDs, and applicable ADRs. |
| QA or review artifact | The SPEC and TASK identifiers it verifies, using `Spec-Ref:` and `Task-Ref:` lines when no metadata table exists. |

References must be explicit. A missing, malformed, or unresolvable reference is
a traceability gap to be recorded and resolved; neither a person nor a script
may infer the intended link from matching prose or filenames.

## Commit trailers

Every implementation commit associated with an approved TASK includes exactly
one trailer for the SPEC and one for the TASK:

```text
Spec-Ref: SPEC-042
Task-Ref: TASK-042-01
```

Use the exact SPEC version when implementing an amendment, for example
`Spec-Ref: SPEC-042-v2`. A commit unrelated to an approved TASK omits both
trailers. Never add only one trailer.

To opt in to local validation, copy the supplied hook and make it executable:

```sh
cp templates/hooks/commit-msg .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```

The hook validates presence and format whenever either traceability trailer is
used. It is intentionally optional so existing adopters can migrate without
blocking historical or unrelated commits.

## Traceability matrix

Generate the repository matrix from its root with:

```sh
python3 scripts/generate_traceability.py
```

The default output is `docs/traceability-matrix.md`. It lists every discovered
SPEC, linked TASKs, commits whose trailers refer to the SPEC or linked TASK,
and linked QA/review records. It also lists gaps such as a TASK without an
existing SPEC or a SPEC without a TASK or commit reference. The generator reads
only `specs/`, `tasks/`, `reviews/`, and Git history; it does not edit source
artifacts or Git history. Use `--output <path>` to write a different matrix.

Markdown is the default format because it is reviewable in any repository. The
source script contains the deterministic extraction rules, so adopters can
convert the result to another reporting format without changing source records.
