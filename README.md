# research-first-task-compiler（先查再造）

Version **1.4.0** — 两卡点 + 一屏方案卡 + 计划模式交接。Both conversation gates remain version- and presentation-bound: only the current displayed task card can pass Gate A, and only a post-display selection of the current option card can pass Gate B.

The portable Agent Skill turns concise natural-language project requests into this workflow:

1. compile and display a one-screen task card
2. **Gate A — user confirms the task card**
3. research existing solutions: quick-read finalist open-source projects (README, docs, code structure, license, issues); full evidence goes to files
4. display a one-screen option card: 概要结论（推荐+理由）→ 方案目录（1~2 个方案，每行定位｜复用/自研｜选它如果…｜风险灯）→ 需要决定的唯一问题 → 详情文件位置
5. **Gate B — user selects a direction**
6. generate a plan-mode handoff package and stop; planning and implementation happen in plan mode (first plan task: a 30-minute time-boxed validation spike; red-line actions still need explicit approval during execution)

Gate A blocks research, handoff generation, and implementation. Gate B blocks the handoff and implementation. Material task-card changes invalidate Gate A and downstream artifacts; material option-card changes invalidate Gate B and its selection. A Green risk grade never skips either gate; Red work additionally needs explicit approval.

What's new in 1.4.0:

- review package redesigned as 方案卡 (option card): progressive disclosure — conclusion → option directory → on-demand expansion from files, never improvised
- 1–2 genuine options only; filler options forbidden; every option must state reused foundation, self-built scope, and evidence basis
- standalone minimum-validation and execution-package phases removed; runtime validation becomes the first execution-plan task (30-minute circuit breaker)
- execution phase replaced by plan-mode handoff + execution guardrails
- independent reviewer is risk-triggered instead of default
- frontmatter `name` fixed to spec-compliant `research-first-task-compiler`
- keeps v1.3.1's optional, non-gating "suggested runner model" hint on the task card (§0)

## Folder structure

```text
research-first-task-compiler/
├── SKILL.md
├── README.md
├── LICENSE
├── manifest.json
├── agents/
│   └── interface.yaml
├── references/
│   ├── research-protocol.md
│   ├── review-protocol.md
│   ├── risk-and-approval-policy.md
│   ├── validation-protocol.md
│   ├── evaluation-protocol.md
│   └── execution-protocol.md
├── assets/
│   ├── task-card-template.md
│   ├── research-report-template.md
│   ├── review-package-template.md   （方案卡模板）
│   ├── plan-handoff-template.md     （计划模式交接包）
│   ├── decision-log-template.md
│   ├── workflow-state-template.md
│   ├── validation-report-template.md
│   ├── acceptance-checklist.md
│   ├── golden-eval-cases.md
│   ├── chatgpt-project-instructions.md
│   ├── gate-transition-contract.md
│   └── quick-commands.md
├── examples/
│   ├── rss-daily-task-card.md
│   └── rss-daily-review-package.md  （方案卡示例）
└── scripts/
    ├── validate_package.py
    ├── validate_gate_contract.py
    └── test_gate_contract.py
```

## ChatGPT installation

Upload the packaged skill through the current Skills/plugin interface when available. For a Project fallback, copy `assets/chatgpt-project-instructions.md` into Project Instructions and upload the remaining files.

Test with this two-turn exchange:

```text
使用 research-first-task-compiler：我想做一个本地会议纪要管理工具。先整理需求和调查开源项目，不要写代码；最后只给我方案卡。

确认任务卡 TC-1。
```

## Claude Code / Codex

Place the folder in the tool's user- or project-level Agent Skills directory, for example `~/.codex/skills/`, `.claude/skills/` or `.agents/skills/`, then invoke by natural language or slash command where supported.

## Output examples

- [Task-card confirmation gate](examples/rss-daily-task-card.md)
- [Option-card decision gate](examples/rss-daily-review-package.md)

## Validation

Run the included lightweight check:

```bash
python scripts/validate_package.py .
```

For full Agent Skills specification validation, use the official `skills-ref validate` command when available.

## Optional runtime layer

This package is deliberately framework-neutral. It can later be orchestrated with LangGraph, OpenAI Agents SDK, CrewAI Flows, or another runtime. Evaluation can be automated with tools such as Promptfoo or DeepEval, and traces can be stored in Langfuse. These are optional integrations, not hard dependencies.

## Design references

- snarktank/ai-dev-tasks (Apache-2.0): clarifying-questions style for task intake; one-step-at-a-time execution rhythm
- github/spec-kit (MIT): structured clarification before planning; checklists as unit tests for requirements
