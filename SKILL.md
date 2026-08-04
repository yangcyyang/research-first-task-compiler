---
name: 先查再造
aliases: [rftc, research-first-task-compiler, research-first, task-compiler]
description: |
  先查再造 — 把模糊需求编译成结构化任务卡 + 证据驱动的执行方案。先搜索已有产品和开源项目，再比较复用策略，运行最小验证，生成压缩审阅包，插入人工审批关卡，产出开发任务包并验证交付。适用于想复用而非从零造轮子的场景。
  触发方式：「先查再造」「先查再造师」「research-first」「task-compiler」
  Turns brief natural-language product, workflow, prototype, automation, research, or software requests into structured task cards and evidence-driven execution. It researches existing products and open-source projects before invention, compares reuse strategies, runs minimum validation, generates compact risk-ranked review packages, inserts human approval gates, produces implementation packages, and verifies delivery. Use when the user wants practical reuse, reduced prompt-writing effort, controlled agent output, or repeatable human-agent collaboration."
license: MIT
compatibility: "Works with Agent Skills-compatible tools. Research needs web or GitHub access; runtime validation needs repository, shell, and relevant runtimes. Independent review benefits from a separate agent/model. When tools are unavailable, mark claims and tests as unverified and return an executable plan instead."
triggers:
  - 先查再造
  - 先查再造师
  - research-first
  - task-compiler
metadata:
  author: generated-for-user
  version: "1.3.0"
  language: zh-CN
---

# Research-First Task Compiler

## Purpose

Convert short, imperfect natural-language requests into reliable, evidence-driven work without forcing the user to write a large prompt or manually review every generated detail.

Use this operating model:

```text
Natural-language request
→ task card shown to user
→ Gate A: user confirms task card
→ research existing solutions
→ producer self-check
→ independent review when available
→ compact review package + risk grade shown to user
→ Gate B: user selects a direction
→ minimum validation
→ execution package
→ implementation and automated checks
→ acceptance review
```

The user owns intent, priorities, trade-offs, and high-risk approvals. This skill owns structure, research discipline, evidence tracking, output compression, review routing, validation, execution packaging, and acceptance checks.

## Core rules

1. Accept concise, fragmented, or conversational input. Do not require a long form.
2. Infer reasonable details and label assumptions. Ask only questions that materially change architecture, cost, legal/compliance risk, data access, or irreversible actions.
3. For product, tool, workflow, system, prototype, automation, research, or development tasks, do not default to inventing or coding from scratch.
4. Before substantial design or implementation, investigate existing products, open-source projects, reusable components, frameworks, and adjacent solutions unless the user explicitly skips research.
5. Separate sourced facts, agent inference, assumptions, and runtime-verified evidence.
6. Never claim a repository, feature, or workflow was tested unless it was actually inspected or run with sufficient evidence.
7. Do not dump all generated material into the main response. The task card and compact review package are exceptions: they must be shown directly in the conversation at their respective gates; keep other detail in files or expandable sections.
8. Human review focuses on decisions, high-risk items, evidence gaps, and irreversible actions—not every line of low-risk output.
9. Use deterministic checks, schemas, tests, and source verification before LLM-based judgment whenever possible.
10. A producer's self-review is not sufficient for important conclusions. Use an independent reviewer agent/model when available.
11. Preserve workflow state, evidence, decisions, and unresolved risks in files so another agent can continue without rereading the full chat.
12. User feedback may be plain language. Compile it into a structured change request automatically.
13. **Gate A — task-card confirmation is mandatory and version-bound.** Every displayed task card has a `Task-card version` (for example `TC-2`). Only an explicit confirmation of the current displayed task-card version passes Gate A. A modification or addition never passes Gate A: compile a new version, display it, invalidate all downstream artifacts, and remain pending.
14. **Gate B — review-package decision is mandatory and version-bound.** Every displayed review package has a `Review-package version` (for example `RP-3`). A selection or delegated choice passes Gate B only after that exact review-package version has been displayed and is recorded against it. A prior authorization, an old selection, or a selection for an undisplayed version is invalid. A material review-package change must invalidate Gate B, clear its selected direction, and require a new displayed package plus a new selection.
15. Green is a risk grade, not permission to bypass Gate A or Gate B. Red actions always require explicit approval; gray evidence is never treated as a pass.

## Detect the current phase

| User intent | Phase |
|---|---|
| “我想做一个……” | Intake and task compilation |
| “先整理需求” | Task card only |
| “先找开源项目/调研现有方案” | Research gate |
| “给我审阅包/别输出太多” | Review gate |
| “比较这些项目” | Candidate comparison and review |
| “我选择方案 B” | Decision recording |
| “验证能不能跑” | Minimum validation |
| “生成开发任务包” | Execution packaging |
| “开始开发/实施” | Execution |
| “结果有这些问题” | Change compilation |
| “检查是否完成” | Acceptance verification |

When ambiguous, choose the safest earlier gate. Do not code when the user is still exploring options. Record the artifact version, display message reference, user response reference, and explicit confirmation/selection in workflow state before moving on. Follow [assets/gate-transition-contract.md](assets/gate-transition-contract.md) for the mandatory state transitions.

## Phase 1 — Compile the task

Create a concise project task card using [assets/task-card-template.md](assets/task-card-template.md). See the completed style reference at [examples/rss-daily-task-card.md](examples/rss-daily-task-card.md).

Extract or infer:

- problem and desired outcome
- users and scenarios
- existing materials or system
- must-have capabilities
- constraints and exclusions
- deliverable and acceptance signals
- assumptions and unresolved decisions
- expected reversibility and risk level

Do not block on missing details unless they materially affect the solution. **Always display the completed task card in the main response with a new task-card version, then set workflow state to `Gate A — approval pending` and stop.** End with exactly one bounded request: `请回复：确认任务卡 TC-N / 修改：… / 补充：…`.

**Forbidden before Gate A passes:** web or repository research, candidate comparison, runtime validation, execution-package generation, implementation, or any external side effect. A request to “先调研” still produces the task card first; it does not skip Gate A. `修改` or `补充` creates a new task-card version and keeps Gate A pending; it cannot be interpreted as approval.

## Phase 2 — Apply the research gate

Follow [references/research-protocol.md](references/research-protocol.md). Enter this phase only after Gate A is recorded as approved.

Research in layers:

1. comparable products and public implementations
2. complete open-source projects suitable for reuse
3. reusable components, libraries, templates, or infrastructure
4. adjacent-domain patterns that can transfer
5. architecture and implementation references

Deeply compare 3–5 serious candidates instead of dumping a long list. Classify each candidate as:

- use directly
- fork and modify
- extract a component
- combine with other projects
- architecture reference only
- reject

End with a recommended reuse strategy, evidence gaps, and a falsifiable minimum-validation plan.

## Phase 3 — Run the review gate

Follow [references/review-protocol.md](references/review-protocol.md) and [references/risk-and-approval-policy.md](references/risk-and-approval-policy.md). See the completed style reference at [examples/rss-daily-review-package.md](examples/rss-daily-review-package.md).

Before asking the user to read detailed work:

1. the producer performs a checklist-based self-check;
2. an independent reviewer checks the result when available;
3. deterministic checks verify links, schemas, calculations, tests, and required fields where possible;
4. all material is compressed into [assets/review-package-template.md](assets/review-package-template.md).

The main review package contains only:

1. one-sentence conclusion
2. decision summary
3. strongest supporting evidence
4. red/yellow/green/gray risk items
5. explicit questions requiring human choice
6. location of detailed evidence

The reviewer evaluates the producer's result; it should not silently replace it with a new long answer.

**Always display the completed review package in the main response with a new review-package version, then set workflow state to `Gate B — decision pending` and stop.** End with a bounded selection such as `请选择：方案 A（RP-N）/ 方案 B（RP-N）/ 方案 C（RP-N）/ 退回调研`. The user may also explicitly delegate the selection for `RP-N`.

**Forbidden before Gate B passes:** candidate validation, execution-package generation, code or configuration implementation, deployment, or external side effects. Do not infer a choice from silence, praise, a prior authorization, or a request for more detail. If research or the review package materially changes, issue a new review-package version and invalidate Gate B together with the prior selection.

## Phase 4 — Apply risk-based approval

Use exactly these grades:

- **Green** — low-risk, reversible, within approved scope, evidence sufficient. May continue automatically unless the user requested manual approval.
- **Yellow** — meaningful trade-off, moderate uncertainty, cost, or scope impact. Pause for a compact user decision unless the user delegated the choice.
- **Red** — irreversible, production-changing, security/privacy/legal/financial impact, destructive action, or critical evidence failure. Require explicit approval.
- **Gray** — not verified or tool access unavailable. Do not treat as passed; create a verification plan.

Record decisions using [assets/decision-log-template.md](assets/decision-log-template.md). A selection at Gate B is required even when the selected direction is Green and must name or be recorded against the current review-package version. Red actions require an additional explicit approval that names the action and its impact.

## Phase 5 — Run minimum validation

Follow [references/validation-protocol.md](references/validation-protocol.md) and [assets/validation-report-template.md](assets/validation-report-template.md). Enter this phase only after Gate B records a selected direction or an explicit delegated choice.

Validate the smallest set of capabilities that can disprove the candidate quickly:

- clone/install/start
- execute the critical workflow
- make one representative modification
- persist and reload data where relevant
- inspect extension points and architecture
- review license and maintenance risk
- record environment, commands, failures, and evidence

Mark every item Passed, Partially passed, Failed, or Not tested. If runtime tools are unavailable, label the result “desk review only”.

After validation, run the review gate again. Do not send raw logs as the primary output.

## Phase 6 — Generate the execution package

Follow [references/execution-protocol.md](references/execution-protocol.md) and [assets/development-task-package-template.md](assets/development-task-package-template.md). Enter this phase only after Gate B records a selected direction or an explicit delegated choice.

Include:

- objective and business context
- selected foundation and reuse strategy
- validated vs unvalidated capabilities
- in-scope and out-of-scope items
- functional behavior and data model
- implementation sequence
- error handling and edge cases
- deterministic tests and evaluation cases
- acceptance criteria and delivery artifacts
- assumptions, risks, rollback, and approval gates

Keep the first iteration small enough to validate the core loop.

## Phase 7 — Execute safely

When tools permit implementation, and only after Gate B passes:

1. inspect the current repository before editing;
2. preserve existing conventions;
3. implement in small, reviewable increments;
4. test after each meaningful change;
5. do not silently broaden scope;
6. document deviations and evidence;
7. update relevant documentation with the implementation;
8. stop at yellow or red approval gates.

For external publication, paid operations, production deployment, credential changes, deletion, migrations, or other irreversible actions, require explicit authorization.

## Phase 8 — Evaluate and verify acceptance

Follow [references/evaluation-protocol.md](references/evaluation-protocol.md) and [assets/acceptance-checklist.md](assets/acceptance-checklist.md).

Prefer this order:

1. deterministic assertions and schema checks
2. unit/integration/build tests
3. golden test cases and regression comparison
4. source/evidence verification
5. LLM reviewer for qualities that cannot be checked deterministically
6. human review for yellow/red decisions

Use [assets/golden-eval-cases.md](assets/golden-eval-cases.md) to maintain representative examples. Report evidence, failures, untested items, residual risks, and the recommended next action.

Never equate “content/code generated” with “task completed”.

## Phase 9 — Compile feedback into a change package

The user may say only:

> “功能能跑，但提示词入口太深。我希望点击图片后直接展开，同时不要影响拖动。”

Convert it into:

- current behavior
- problem
- desired behavior
- constraints
- affected components
- acceptance criteria
- regression checks
- risk grade and required approval

Do not make the user rewrite feedback as a formal prompt.

## State and evidence discipline

For multi-step work, maintain [assets/workflow-state-template.md](assets/workflow-state-template.md).

At each gate record:

- current phase and status
- artifact versions
- evidence sources
- assumptions and confidence
- decision owner
- approval status
- next allowed action

This file is the handoff source of truth, not the chat transcript.

## Stop conditions

Stop research and move to review/validation when:

- 3–5 credible candidates have been compared; and
- at least one candidate plausibly satisfies the core requirement; or
- further search is unlikely to change the decision.

Stop validation and reject a candidate when a critical requirement, license condition, security constraint, or integration assumption fails.

Stop execution when:

- a yellow/red approval is pending;
- Gate A or Gate B is pending;
- evidence contradicts the chosen approach;
- scope materially changes;
- tests reveal a critical regression;
- the required tools or data are unavailable.

Skip the research gate only when:

- the task is a small change in an existing system;
- the user mandates a specific implementation;
- the user explicitly asks not to browse; or
- research cost clearly exceeds task value.

When skipping, state the reason.

## Default response style

Lead with:

1. current conclusion
2. the required task card or compact review artifact for the current gate
3. risks/evidence gaps
4. only the next required confirmation, decision, or action

Use clear Chinese unless another language is requested. Prefer tables for comparisons and checklists for execution. Put detailed evidence in files or appendices.

## Quick natural-language triggers

- “我想做一个……先帮我整理需求，不要马上执行。”
- “先展示任务卡，等我确认后再调研。”
- “确认任务卡，开始调研现有产品、开源项目和可复用组件。”
- “不要把全文都丢给我，生成审阅包。”
- “我选方案 B；先验证关键能力，不要开始开发。”
- “先自检，再让独立 Reviewer 复核。”
- “只把黄灯、红灯和需要我决定的内容给我。”
- “验证方案 B 的关键能力，不要只看 README。”
- “根据当前结论生成第一阶段开发任务包。”
- “当前结果的问题是……我希望改成……”
- “按验收清单和黄金用例检查是否真的完成。”
