# Risk and Approval Policy

## Green — continue

Criteria:

- reversible
- within approved scope
- low cost and low blast radius
- deterministic checks pass
- evidence is sufficient

Examples:

- formatting and file organization
- generating a draft from an approved template
- low-risk refactoring with passing tests
- filtering clearly irrelevant research candidates

Human action: no item-by-item review; optional sampling.

## Yellow — decide

Criteria:

- meaningful product or architecture trade-off
- moderate uncertainty or cost
- changes scope, dependency, UX, or data model
- evidence is incomplete but a bounded decision is possible

Examples:

- choosing between two open-source foundations
- adding a major dependency
- changing information architecture
- accepting a known maintenance burden

Human action: review compact evidence and choose approve, revise, defer, or reject. The workflow may continue automatically only if the user explicitly delegated this class of decisions.

## Red — explicit approval

Criteria:

- irreversible or destructive
- production deployment or external publication
- security, privacy, legal, financial, credential, or compliance impact
- destructive data migration or deletion
- critical evidence contradiction
- high blast radius

Human action: explicit approval required. Silence is not approval.

## Gray — verify

Criteria:

- not tested
- source unavailable
- tool access missing
- stale or conflicting evidence
- result depends on an unverified assumption

Human action: define the smallest verification experiment. Gray cannot be reported as passed.

## Escalation rules

- Any critical license, security, or privacy issue overrides aggregate scores.
- A failed red-risk check blocks execution.
- Repeated green-item errors escalate the batch to yellow and increase sampling.
- If a yellow decision changes the task card, rerun affected research and validation gates.
