# UX/UI Standard

## Purpose

Define the minimum discovery, design, handoff, validation, and review required
for any user-facing change. This standard applies to web, mobile, desktop, CLI,
and other interactive products. The active project profile may add stricter
rules.

## Required inputs

Before design starts, identify:

- problem, business outcome, and affected user groups;
- available user evidence and explicitly labeled assumptions;
- current journey or workflow, if one exists;
- constraints, risks, dependencies, and applicable platform conventions;
- measurable success criteria.

Use `templates/ux-brief.md`. If research is intentionally skipped, record the
reason, approver, risks, and validation plan.

## Required design artifacts

Every user-facing change must provide, in proportion to its risk:

1. a user flow covering the main path, alternatives, errors, cancellation, and
   recovery;
2. wireframes or a prototype when behavior cannot be understood from the flow;
3. a design specification using `templates/design-specification.md`;
4. component and design-token mappings;
5. accessibility annotations;
6. human approval before implementation.

Small changes may combine these artifacts into the SPEC, but none of the
required information may be omitted without an approved exception.

## Interface states

The design specification must address all applicable states:

- initial, loading, progress, success, empty, partial, and stale data;
- validation, recoverable error, fatal error, offline, and timeout;
- disabled, read-only, selected, focused, hovered, pressed, and expanded;
- authentication, authorization, permission denied, and session expiration;
- first use, repeated use, destructive confirmation, undo, and cancellation.

## Responsive and platform behavior

Define supported viewports, orientations, input methods, zoom or text scaling,
and content reflow. Do not rely on an unspecified “responsive” requirement.
Record minimum supported devices and browsers in the QA plan.

Platform-native conventions take precedence unless an approved design decision
documents why they should be changed.

## Content and interaction

- Use clear task-oriented labels and consistent terminology.
- Define validation timing and actionable error messages.
- Do not use color, position, gesture, or icon alone to communicate meaning.
- Destructive actions require confirmation or a reliable undo path.
- Preserve user input after recoverable failures whenever feasible.
- Define keyboard, pointer, touch, and assistive-technology behavior as applicable.

## Usability validation

Usability testing is required for new or materially changed critical journeys,
high-risk assumptions, or behavior with significant support or conversion
impact. Use `templates/usability-test-plan.md` and record:

- participant profile and sample limitations;
- scenarios and success measures;
- observations rather than inferred intent;
- severity of findings and resulting decisions.

## Handoff readiness

Design is ready for implementation only when:

- the problem, scope, and user flow are approved;
- all applicable states and responsive rules are specified;
- components, tokens, assets, and content are identified;
- accessibility behavior is annotated;
- acceptance criteria are testable;
- unresolved questions, risks, and approved exceptions are recorded.

## Implementation review

Use `templates/design-review.md`. Review representative viewports and states,
realistic content, keyboard behavior, zoom or text scaling, and component/token
usage. A visual match alone is not sufficient: interaction, content, and
accessibility behavior must also match the approved specification.
