# Execution Packaging and Delivery Protocol

## 1. Build the smallest coherent increment

The first implementation should complete one usable end-to-end loop. Exclude attractive but nonessential features.

## 2. Package the task

Use [../assets/development-task-package-template.md](../assets/development-task-package-template.md).

A strong package answers:

- Why is this being built?
- What exact behavior is required?
- What is reused and what is custom?
- What must not change?
- What is explicitly out of scope?
- How will completion be verified?
- Where must execution pause for approval?

## 3. Implementation discipline

- inspect before editing
- follow repository conventions
- avoid unnecessary dependencies
- preserve backward compatibility unless approved
- handle errors and empty states
- add or update tests and golden cases
- keep changes reviewable
- document setup, decisions, evidence, and rollback

## 4. Verification

Run relevant checks:

- schema and deterministic assertions
- lint and type checks
- unit and integration tests
- build
- critical user-flow test
- persistence/restart test
- permission/security checks
- regression cases

If a check cannot run, state why and mark it gray.

## 5. Delivery report and review package

Return detailed delivery evidence plus a compact review package containing:

- summary of changes
- tests and outcomes
- known limitations and untested items
- deviations from task package
- risk lights
- approval required for the next action
- migration or rollback notes

## 6. Feedback compilation

Translate informal feedback into a change request containing current behavior, observed problem, desired behavior, constraints, affected scope, acceptance criteria, regression cases, and risk grade.
