#!/usr/bin/env python3
"""Initialize a run workspace for the Human-AI Collaboration Gated Workflow."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "run"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="Human-readable run name")
    parser.add_argument("--out", default="./runs", help="Parent output directory")
    parser.add_argument("--run-id", help="Optional explicit run ID")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    skill_root = script_dir.parent
    templates = skill_root / "templates"
    if not templates.exists():
        raise SystemExit(f"Templates directory not found: {templates}")

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_id = args.run_id or f"{stamp}-{slugify(args.name)}"
    root = Path(args.out).resolve() / run_id

    dirs = [
        "00-intake",
        "01-task-card",
        "02-research",
        "02-solution-card",
        "03-validation",
        "04-execution/work-products",
        "05-result-card",
        "06-governance",
        "07-validation",
    ]
    for rel in dirs:
        (root / rel).mkdir(parents=True, exist_ok=True)

    mapping = {
        "task-card-screen.md": "01-task-card/task-card-screen.md",
        "task-card-record.md": "01-task-card/task-card-record.md",
        "research-report.md": "02-research/research-report.md",
        "solution-card-screen.md": "02-solution-card/solution-card-screen.md",
        "solution-card-record.md": "02-solution-card/solution-card-record.md",
        "decision-card.md": "02-solution-card/decision-cards.md",
        "validation-report.md": "03-validation/validation-report.md",
        "dev-task-package.md": "04-execution/dev-task-package.md",
        "result-card-screen.md": "05-result-card/result-card-screen.md",
        "result-card-record.md": "05-result-card/result-card-record.md",
        "source-index.md": "06-governance/source-index.md",
        "assumption-log.md": "06-governance/assumption-log.md",
        "baseline.md": "06-governance/baseline.md",
        "change-summary.md": "06-governance/changes.md",
    }
    for src, dst in mapping.items():
        shutil.copy2(templates / src, root / dst)

    (root / "00-intake/original-request.md").write_text(
        f"# 原始请求\n\n- 运行名称：{args.name}\n- 运行ID：{run_id}\n- 创建时间：{dt.datetime.now().isoformat(timespec='seconds')}\n\n{{{{ORIGINAL_USER_INPUT}}}}\n",
        encoding="utf-8",
    )
    (root / "04-execution/artifact-index.md").write_text(
        "# 成果文件索引\n\n| 产物 | 路径 | 状态 | 说明 |\n|---|---|---|---|\n",
        encoding="utf-8",
    )
    (root / "07-validation/final-validation-report.md").write_text(
        "# 终验报告\n\n## 方向检查\n\n## 完整性检查\n\n## 来源检查\n\n## 案例检查\n\n## 一致性检查\n",
        encoding="utf-8",
    )

    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
