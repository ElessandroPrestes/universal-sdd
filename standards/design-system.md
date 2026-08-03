# Design System Standard

## Purpose

Keep interface decisions consistent, accessible, reusable, and traceable. A
project may use an internal system, a third-party system, or a documented set of
platform-native conventions.

## Source and ownership

`PROJECT.md` must identify:

- the design system and its version or revision;
- the canonical location for tokens, components, icons, and content guidance;
- maintainers and approval responsibilities;
- supported platforms and known gaps.

Design files must not be the only source of component behavior. Implementable
states, properties, and accessibility semantics must be documented in the
repository or a versioned system referenced from it.

## Tokens

Use semantic tokens for at least:

- color and contrast roles;
- typography;
- spacing and sizing;
- borders, radius, elevation, and opacity;
- motion duration and easing;
- breakpoints or layout rules where applicable.

Avoid introducing raw values when an appropriate token exists. A new token must
have a semantic purpose, owner, usage guidance, and migration impact.

## Components

Each reusable component must define:

- purpose, supported variants, and prohibited usage;
- content rules and localization behavior;
- interactive states and transitions;
- keyboard and assistive-technology semantics;
- responsive behavior;
- examples and automated tests appropriate to its risk.

Prefer extending an existing component over creating a visually similar local
variant. Product-specific composition may remain local when it is not reusable.

## Change governance

Changes that affect existing consumers require:

1. impact analysis;
2. design and engineering review;
3. accessibility review;
4. versioning or migration notes;
5. visual and behavioral regression evidence.

Breaking changes must not be silently released. Deprecations need an owner,
replacement guidance, and removal target.

## Review checklist

- Only approved components and tokens are used.
- New patterns are justified and documented.
- All component states are implemented.
- Content works with realistic length and localization.
- Accessibility semantics are preserved by composition.
- The implemented component has relevant test and review evidence.
