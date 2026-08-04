# Workflow State

## Identity

- Project:
- Task card version:
- Task card presentation evidence:
- Review package version:
- Review package presentation evidence:
- Skill version:
- Last updated:

## Current gate

- Phase:
- Status: Not started / In progress / Review pending / Approval pending / Passed / Invalidated / Failed
- Risk grade:
- Next allowed action:

## Mandatory confirmation gates

| Gate | Required user input | Blocks until passed | Status | Evidence |
|---|---|---|---|---|
| Gate A — task-card confirmation | `确认任务卡 TC-N` for the currently displayed card | Research, validation, packaging, implementation | Pending(TC-N) / Passed(TC-N) / Invalidated | Display ref + confirmation ref |
| Gate B — review-package decision | Selection/delegation for currently displayed `RP-N` after its display | Validation, packaging, implementation | Pending(RP-N) / Passed(RP-N) / Invalidated | Display ref + selection ref |

Rules: Green does not bypass either gate. `修改`/`补充` never pass Gate A. An early authorization or old selection never passes Gate B. A material task-card change invalidates Gate A and all downstream artifacts; a material review-package change invalidates Gate B and downstream artifacts. Red requires a separate explicit approval before the named irreversible action.

## Gate evidence and invalidation

- Task card presentation evidence: message/reference where current `TC-N` was shown
- Task card confirmation evidence: response/reference that explicitly confirms `TC-N`
- Review package presentation evidence: message/reference where current `RP-N` was shown
- Review package selection evidence: response/reference selecting or delegating `RP-N`
- Invalidated: list the superseded artifact version, reason, and timestamp whenever a material change occurs

## Artifacts

| Artifact | Version | Status | Location |
|---|---|---|---|
| Task card | | | |
| Research report | | | |
| Review package | | | |
| Validation report | | | |
| Execution package | | | |
| Acceptance report | | | |

## Evidence and assumptions

- Verified facts:
- Runtime-tested facts:
- Inferences:
- Assumptions:
- Evidence gaps:

## Decisions and approvals

- Latest decision:
- Decision owner:
- Approval status:
- Bound task-card version:
- Bound review-package version:
- Selection/delegation message:
- Conditions:

## Open risks

- Red:
- Yellow:
- Gray:

## Handoff note

[What the next agent needs to know without reading the full chat]
