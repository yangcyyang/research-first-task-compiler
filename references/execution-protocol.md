# Execution Guardrails Protocol

> Applies after the plan-mode handoff, inside plan mode and execution. This skill defines guardrails, not the implementation plan itself.

## 1. Step rhythm

Borrowed from ai-dev-tasks: work one small, reviewable step at a time; report what changed and continue. The user may pause or redirect between steps without breaking the workflow.

## 2. Validation spike first

The first plan task is the validation spike (see [validation-protocol.md](validation-protocol.md)): cheapest falsifiable checks first, 30-minute timebox. A failed critical assumption is a material change — return to research and re-open Gate B with a new RP version.

## 3. Implementation discipline

- inspect the current repository before editing
- preserve existing conventions
- avoid unnecessary dependencies
- preserve backward compatibility unless approved
- handle errors and empty states
- test after each meaningful change
- do not silently broaden scope
- document deviations, decisions, evidence, and rollback
- update relevant documentation with the implementation

## 4. Red-line approvals

External publication, paid operations, production deployment, credential changes, deletion, migrations, or other irreversible actions require explicit authorization naming the action and its impact. Silence is not approval. Green/yellow/gray handling follows [risk-and-approval-policy.md](risk-and-approval-policy.md).

## 5. Verification

Run relevant checks in this order where available:

- schema and deterministic assertions
- lint and type checks
- unit and integration tests
- build
- critical user-flow test
- persistence/restart test
- permission/security checks
- regression cases

If a check cannot run, state why and mark it gray.

## 6. Delivery report

Return a compact report containing:

- summary of changes
- tests and outcomes
- known limitations and untested items
- deviations from the confirmed plan
- risk lights
- approval required for the next action
- migration or rollback notes

## 7. Feedback compilation

Translate informal feedback into a change request containing current behavior, observed problem, desired behavior, constraints, affected scope, acceptance criteria, regression cases, and risk grade.
