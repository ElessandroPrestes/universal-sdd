# Accessibility Standard

## Baseline

Each project must record its accessibility target in `PROJECT.md`, including the
standard, version, conformance level, supported platforms, and any legal or
contractual requirements. For web projects, WCAG 2.2 Level AA is the recommended
default unless the project explicitly adopts another approved baseline.

Automated tools support review but never replace manual and assistive-technology
validation.

## Design requirements

Every user-facing design must address, when applicable:

- logical reading, focus, and interaction order;
- keyboard access and visible focus;
- names, roles, values, instructions, and status announcements;
- text and non-text contrast;
- zoom, text resizing, reflow, orientation, and target size;
- alternatives for images, audio, video, gesture, motion, and time limits;
- errors, validation, recovery, and destructive actions;
- reduced motion and user display preferences;
- language, localization, and understandable content.

Accessibility annotations must be present in the design specification rather
than deferred entirely to implementation.

## Implementation requirements

- Prefer native semantic elements and platform controls.
- Preserve expected keyboard and assistive-technology behavior.
- Do not add unnecessary roles or override native semantics without evidence.
- Associate labels, instructions, errors, and descriptions programmatically.
- Announce dynamic status changes when users need them to continue.
- Ensure custom components have documented semantics and interaction tests.
- Do not disable zoom or prevent user display preferences without an approved exception.

## Required validation

Use `templates/accessibility-checklist.md`. The QA plan must select applicable
checks, environments, and assistive technologies. At minimum, validate:

1. automated scan of changed user-facing surfaces;
2. keyboard-only or equivalent non-pointer operation;
3. visible focus and logical focus order;
4. zoom, text scaling, and reflow as applicable;
5. names, roles, values, instructions, errors, and announcements;
6. contrast and non-color communication;
7. at least one representative assistive-technology path for critical journeys.

## Defect handling

Accessibility defects use the same severity model as other defects, considering
whether a user is blocked, loses data, cannot understand content, or must use an
unreasonable workaround. A failed applicable requirement blocks release unless
an authorized exception records scope, user impact, mitigation, owner, and expiry.

## Evidence

Evidence must identify the build, environment, viewport or device, input method,
assistive technology and version when used, steps, expected result, actual
result, and artifact links. Avoid screenshots as the sole evidence for semantic
or announced behavior.
