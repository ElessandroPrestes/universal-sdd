# Security Standard

## Baseline

Security requirements are derived from the project's threat model, data
classification, legal obligations, and approved SPEC. Security is part of
design and review, not a release-only check.

- Never commit secrets, tokens, private keys, or production credentials.
- Validate untrusted input at trust boundaries and encode output for its context.
- Enforce authentication and authorization server-side or at the trusted boundary.
- Apply least privilege to people, agents, services, data, and automation.
- Protect sensitive data in transit, at rest, in logs, and in test evidence.
- Pin, review, and update dependencies according to project risk.
- Define safe failure, audit events, abuse controls, and incident ownership.
- Include migration, rollback, backup, and recovery risks for data changes.

A material security finding blocks release unless an authorized, time-bounded
exception documents user impact and mitigation.
