---
name: research-first-task-compiler
aliases: [rftc, research-first, task-compiler, 先查再造]
description: |
  先查再造 — 把模糊需求编译成清晰的任务卡，先调研现有产品和开源项目再决定复用还是自研，用一屏方案卡呈现推荐与备选，两个人工卡点后生成计划模式交接包。适用于想复用而非从零造轮子、且希望阅读负担最小的场景。
  触发方式：「先查再造」「先查再造师」「research-first」「task-compiler」
  Turns brief natural-language product, workflow, prototype, automation, research, or software requests into a clear task card, researches existing products and open-source projects before inventing, presents a one-screen option card with a recommendation and 1–2 genuine alternatives, and hands the chosen direction to plan mode for execution. Use when the user wants practical reuse, reduced prompt-writing effort, minimal reading burden, or repeatable human-agent collaboration.
license: MIT
compatibility: "Works with Agent Skills-compatible tools. Research needs web or GitHub access; runtime validation needs repository, shell, and relevant runtimes. When tools are unavailable, mark claims and tests as unverified and return an executable plan instead."
triggers:
  - 先查再造
  - 先查再造师
  - research-first
  - task-compiler
metadata:
  author: generated-for-user
  version: "1.4.0"
  language: zh-CN
---

# Research-First Task Compiler（先查再造）

## Purpose

Convert short, imperfect natural-language requests into reliable, evidence-driven work with the smallest possible reading burden for the user.

Use this operating model:

```text
模糊需求
→ 任务卡 TC-N（一屏内，直接展示）
→ Gate A：用户确认任务卡
→ 调研现有产品与开源项目（快速阅读入围项目；完整证据写入文件）
→ 方案卡 RP-N（推荐结论 + 1~2 个方案目录 + 风险灯，直接展示）
→ Gate B：用户选择方向
→ 计划模式交接包
→ 进入计划模式制定执行计划并实施（计划首个任务：30 分钟熔断的验证 spike）
→ 按任务卡验收标准检查
```

The user owns intent, priorities, trade-offs, and high-risk approvals. This skill owns structure, research discipline, evidence tracking, output compression, and the plan-mode handoff. **Planning and implementation belong to plan mode; this skill ends at a well-formed handoff.**

## Core rules

1. Accept concise, fragmented, or conversational input. Do not require a long form.
2. Infer reasonable details and label assumptions. Ask only questions that materially change architecture, cost, legal/compliance risk, data access, or irreversible actions.
3. For product, tool, workflow, system, prototype, automation, research, or development tasks, do not default to inventing or coding from scratch.
4. Before substantial design or implementation, investigate existing products, open-source projects, and reusable components unless the user explicitly skips research.
5. Separate sourced facts, agent inference, assumptions, and runtime-verified evidence.
6. Never claim a repository, feature, or workflow was tested unless it was actually inspected or run with sufficient evidence.
7. **Keep the main response minimal.** The task card and the option card are the only two artifacts always displayed in full. Full research reports, candidate analyses, and evidence ledgers are written to files first (default: `99_workspace/rftc/<任务名>/` or the project's workspace convention); when the user asks for detail, read it back from those files — never regenerate from memory.
8. Human review focuses on decisions, high-risk items, evidence gaps, and irreversible actions — not every line of low-risk output.
9. Use deterministic checks, schemas, tests, and source verification before LLM-based judgment whenever possible.
10. A producer's self-check is the default. Use an independent reviewer agent/model only when risk-triggered (see [references/review-protocol.md](references/review-protocol.md)).
11. Preserve workflow state, evidence, decisions, and unresolved risks in files so another agent can continue without rereading the full chat.
12. User feedback may be plain language. Compile it into a structured change request automatically.
13. **Gate A — task-card confirmation is mandatory and version-bound.** Every displayed task card has a `Task-card version` (for example `TC-2`). Only an explicit confirmation of the current displayed task-card version passes Gate A. A modification or addition never passes Gate A: compile a new version, display it, invalidate all downstream artifacts, and remain pending.
14. **Gate B — review-package decision is mandatory and version-bound.** Every displayed option card (review package) has a `Review-package version` (for example `RP-3`). A selection or delegated choice passes Gate B only after that exact review-package version has been displayed and is recorded against it. A prior authorization, an old selection, or a selection for an undisplayed version is invalid. A material review-package change must invalidate Gate B, clear its selected direction, and require a new displayed package plus a new selection.
15. Green is a risk grade, not permission to bypass Gate A or Gate B. Red actions always require explicit approval; gray evidence is never treated as a pass.

## Detect the current phase

| User intent | Phase |
|---|---|
| "我想做一个……" | Intake and task compilation |
| "先整理需求" | Task card only |
| "先找开源项目/调研现有方案" | Research (after Gate A) |
| "给我方案卡/别输出太多" | Option card |
| "方案 A 具体讲讲" | Expand from files, do not regenerate |
| "我选择方案 A（RP-N）" | Decision recording, then plan-mode handoff |
| "生成计划/进入计划模式" | Plan-mode handoff package |
| "开始开发/实施" | Execution under plan (spike first) |
| "结果有这些问题" | Change compilation |
| "检查是否完成" | Acceptance verification |

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

When information is missing, first try labeled assumptions. If assumptions are not enough, list the 3–5 most material clarifying questions inside the task card (borrowed from ai-dev-tasks' PRD style) — but only questions that materially change the solution may block; everything else becomes an assumption.

Do not block on missing details unless they materially affect the solution. **Always display the completed task card in the main response with a new task-card version, then set workflow state to `Gate A — approval pending` and stop.** End with exactly one bounded request: `请回复：确认任务卡 TC-N / 修改：… / 补充：…`.

**Optional model-runner suggestion（可选元数据，非 gate）**：任务卡可附带一行「建议执行模型」字段（见 [assets/task-card-template.md](assets/task-card-template.md) §0），按任务能力缺口给匹配建议：调研/聚合型 → 联网检索能力强的模型；视觉/出图型 → 图像能力模型；代码验证/执行型 → 代码能力模型；默认 → 当前模型不切换。它是可跳过的元数据，不是确认门槛；用户可在 Gate A 确认时一并决定（如 `确认任务卡 TC-N，用 XX 模型`），或保持当前模型。若切换执行者，应先读取 workflow-state 文件再继续，避免上下文断裂。推荐映射会随模型能力变化而过时，只作示例、不硬编码为规则。

**Forbidden before Gate A passes:** web or repository research, candidate comparison, runtime validation, handoff-package generation, implementation, or any external side effect. A request to "先调研" still produces the task card first; it does not skip Gate A. `修改` or `补充` creates a new task-card version and keeps Gate A pending; it cannot be interpreted as approval.

## Phase 2 — Research existing solutions

Follow [references/research-protocol.md](references/research-protocol.md). Enter this phase only after Gate A is recorded as approved.

Research in layers:

1. comparable products and public implementations
2. complete open-source projects suitable for reuse
3. reusable components, libraries, templates, or infrastructure
4. adjacent-domain patterns that can transfer
5. architecture and implementation references

Candidate funnel:

- **Broad discovery** — collect enough candidates to understand the solution space; never present this raw list.
- **Hard filter** — reject critical mismatches (wrong problem, incompatible license, no extension path, unacceptable deployment/privacy model).
- **Quick reading of finalists (≤3)** — actually read README, official docs, code structure, license file, recent issues/releases for each finalist. README claims alone are not evidence of capability.

Write the full research report and evidence ledger to files using [assets/research-report-template.md](assets/research-report-template.md). Classify each candidate as: use directly / fork and modify / extract a component / combine / architecture reference only / reject.

Do not manufacture candidates to hit a quota. If one direction clearly satisfies all hard constraints, record why additional alternatives would not change the decision.

## Phase 3 — Present the option card (review package)

Follow [references/review-protocol.md](references/review-protocol.md). See the completed style reference at [examples/rss-daily-review-package.md](examples/rss-daily-review-package.md).

Compress everything into [assets/review-package-template.md](assets/review-package-template.md) and display it in full. The card contains only:

1. **概要结论** — recommended direction in one sentence plus 1–2 sentences of reasoning
2. **方案目录** — one line per option: positioning ｜ what is reused vs self-built ｜ choose-it-if condition ｜ risk light
3. **需要你决定的** — the single core trade-off question
4. **风险灯** — red/yellow/gray items with content (omit empty lights)
5. **详细材料位置** — file paths for the full report and evidence ledger

Hard rules for options:

- Present **1–2 genuine directions, never filler**. If only one direction is reasonable, present it and state why no second option exists.
- An option may be presented only if it explicitly states its reused foundation, self-built scope, and evidence basis. Missing any of these, it is not a selectable option.
- When the user asks about an option, expand from the written files; do not improvise new content.

**Always display the completed option card in the main response with a new review-package version, then set workflow state to `Gate B — decision pending` and stop.** End with a bounded selection such as `请选择：方案 A（RP-N）/ 方案 B（RP-N）/ 退回调研`. The user may also explicitly delegate the selection for `RP-N`.

**Forbidden before Gate B passes:** implementation, deployment, external side effects, or plan-mode handoff generation. Do not infer a choice from silence, praise, a prior authorization, or a request for more detail. If research or the option card materially changes, issue a new review-package version and invalidate Gate B together with the prior selection.

## Phase 4 — Hand off to plan mode

Enter this phase only after Gate B records a selected direction or an explicit delegated choice.

Generate the handoff package using [assets/plan-handoff-template.md](assets/plan-handoff-template.md):

- confirmed goal, constraints, and acceptance signals (from the task card)
- selected direction and its reuse/self-build boundaries
- suggested first plan task: a validation spike (see [references/validation-protocol.md](references/validation-protocol.md)) — smallest falsifiable checks first, **30-minute hard timebox**, timeout means mark gray and record the blocker
- red-line items that still need explicit approval during execution

Display the handoff package, recommend entering plan mode, and stop. **This skill does not generate its own development task package or implementation plan — that is plan mode's territory.**

## Phase 5 — Execution guardrails (apply inside plan mode / execution)

Follow [references/execution-protocol.md](references/execution-protocol.md) and [references/risk-and-approval-policy.md](references/risk-and-approval-policy.md):

- work one small reviewable step at a time; report and continue (borrowed from ai-dev-tasks' rhythm)
- run the validation spike first; a failed critical assumption returns to research as a material change (new RP version, Gate B re-opens)
- inspect the repository before editing; preserve conventions; do not silently broaden scope
- test after each meaningful change; document deviations and evidence
- Red actions (external publication, paid operations, production deployment, credential changes, deletion, migrations, irreversible actions) require explicit approval naming the action and its impact — silence is not approval
- gray evidence is never reported as passed

## Phase 6 — Acceptance and feedback

Follow [references/evaluation-protocol.md](references/evaluation-protocol.md) and [assets/acceptance-checklist.md](assets/acceptance-checklist.md). Verify against the task card's acceptance signals, preferring deterministic checks over LLM judgment. Never equate "content/code generated" with "task completed".

Plain-language feedback is compiled into a structured change request: current behavior, problem, desired behavior, constraints, affected components, acceptance criteria, regression checks, risk grade and required approval. Do not make the user rewrite feedback as a formal prompt.

## State and evidence discipline

For multi-step work, maintain [assets/workflow-state-template.md](assets/workflow-state-template.md) and record decisions with [assets/decision-log-template.md](assets/decision-log-template.md).

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

Stop research and move to the option card when:

- finalists have been quick-read and at least one direction plausibly satisfies the core requirement; or
- further search is unlikely to change the decision.

Stop execution when:

- Gate A or Gate B is pending;
- a red approval is pending;
- spike evidence contradicts the chosen approach (return to research as a material change);
- scope materially changes;
- tests reveal a critical regression;
- the required tools or data are unavailable.

Skip the research phase only when:

- the task is a small change in an existing system;
- the user mandates a specific implementation;
- the user explicitly asks not to browse; or
- research cost clearly exceeds task value.

When skipping, state the reason.

## Default response style

Lead with:

1. current conclusion
2. the required task card or option card for the current gate
3. risks/evidence gaps
4. only the next required confirmation, decision, or action

Use clear Chinese unless another language is requested. Prefer tables for comparisons and checklists for execution. Put detailed evidence in files, not in the main response.

## Quick natural-language triggers

- "我想做一个……先帮我整理需求，不要马上执行。"
- "先展示任务卡，等我确认后再调研。"
- "确认任务卡，开始调研现有产品、开源项目和可复用组件。"
- "不要把全文都丢给我，给我方案卡。"
- "方案 A 具体讲讲。"（从文件展开）
- "我选方案 A（RP-1）；生成计划模式交接包。"
- "只把推荐结论、备选目录和需要我决定的内容给我。"
- "当前结果的问题是……我希望改成……"
- "按任务卡验收标准检查是否真的完成。"
