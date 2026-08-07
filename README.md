# research-first-task-compiler

Version **1.3.1** adds an optional, non-gating "suggested runner model" hint to the task card (§0), so a task can carry a capability-matched model recommendation without adding a new approval gate. Version **1.3.0** makes both conversation gates version- and presentation-bound: only the current displayed task card can pass Gate A, and only a post-display selection of the current review package can pass Gate B.

The portable Agent Skill turns concise natural-language project requests into this workflow:

1. compile and display task card
2. **Gate A — user confirms the task card**
3. research existing solutions and open-source projects
4. self-check and independent review
5. generate and display a compact red/yellow/green/gray review package
6. **Gate B — user selects a direction**
7. run minimum validation
8. generate an execution package
9. execute with approval gates
10. evaluate with deterministic checks and golden cases
11. verify acceptance and compile feedback

Gate A blocks research, validation, packaging, and implementation. Gate B blocks validation, packaging, and implementation. Material task-card changes invalidate Gate A and downstream artifacts; material review-package changes invalidate Gate B and its selection. A Green risk grade never skips either gate; Red work additionally needs explicit approval.

## Folder structure

```text
research-first-task-compiler/
├── SKILL.md
├── README.md
├── LICENSE
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
│   ├── review-package-template.md
│   ├── decision-log-template.md
│   ├── workflow-state-template.md
│   ├── validation-report-template.md
│   ├── development-task-package-template.md
│   ├── acceptance-checklist.md
│   ├── golden-eval-cases.md
│   ├── chatgpt-project-instructions.md
│   └── quick-commands.md
├── examples/
│   ├── rss-daily-task-card.md
│   └── rss-daily-review-package.md
└── scripts/
    └── validate_package.py
```

## ChatGPT installation

Upload the packaged skill through the current Skills/plugin interface when available. For a Project fallback, copy `assets/chatgpt-project-instructions.md` into Project Instructions and upload the remaining files.

Test with this two-turn exchange:

```text
使用 research-first-task-compiler：我想做一个本地会议纪要管理工具。先整理需求和调查开源项目，不要写代码；最后只给我审阅包。

确认任务卡 TC-1。
```

## Claude Code / Codex

Place the folder in the tool's project-level Agent Skills directory, for example `.claude/skills/` or `.agents/skills/`, then invoke by natural language or slash command where supported.

## Output examples

- [Task-card confirmation gate](examples/rss-daily-task-card.md)
- [Review-package decision gate](examples/rss-daily-review-package.md)

## Validation

Run the included lightweight check:

```bash
python scripts/validate_package.py .
```

For full Agent Skills specification validation, use the official `skills-ref validate` command when available.

## Optional runtime layer

This package is deliberately framework-neutral. It can later be orchestrated with LangGraph, OpenAI Agents SDK, CrewAI Flows, or another runtime. Evaluation can be automated with tools such as Promptfoo or DeepEval, and traces can be stored in Langfuse. These are optional integrations, not hard dependencies.
