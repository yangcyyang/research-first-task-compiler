#!/usr/bin/env python3
"""Validate the structure and required headings of this skill package."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "manifest.txt",
    "references/workflow-and-artifacts.md",
    "references/progressive-disclosure.md",
    "references/human-review-and-decisions.md",
    "references/self-check-and-drift.md",
    "references/baseline-and-delta.md",
    "references/research-gate.md",
    "references/validation-gate.md",
    "references/delivery-package.md",
    "templates/task-card-screen.md",
    "templates/task-card-record.md",
    "templates/solution-card-screen.md",
    "templates/solution-card-record.md",
    "templates/result-card-screen.md",
    "templates/result-card-record.md",
    "templates/decision-card.md",
    "templates/baseline.md",
    "templates/change-summary.md",
    "templates/source-index.md",
    "templates/assumption-log.md",
    "templates/research-report.md",
    "templates/validation-report.md",
    "templates/dev-task-package.md",
]

REQUIRED_TEMPLATE_HEADINGS = {
    "templates/task-card-screen.md": [
        "## 一句话任务", "## 目标", "## 本轮产物", "## 本轮范围",
        "## 明确不做", "## 需要你确认", "## AI建议动作",
    ],
    "templates/solution-card-screen.md": [
        "## 一句话结论", "## AI推荐方案", "## 执行抽象模型",
        "## 预期成效", "## 主要风险", "## 需要你确认",
    ],
    "templates/result-card-screen.md": [
        "## 一句话结果", "## 整体完成情况", "## 核心成果",
        "## 与已确认方案的差异", "## 需要你验收",
    ],
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    errors: list[str] = []

    for rel in REQUIRED_FILES:
        path = root / rel
        if not path.exists():
            errors.append(f"Missing required file: {rel}")
        elif path.stat().st_size == 0:
            errors.append(f"Empty required file: {rel}")

    skill_path = root / "SKILL.md"
    if skill_path.exists():
        text = read(skill_path)
        frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not frontmatter:
            errors.append("SKILL.md is missing YAML frontmatter")
        else:
            fm = frontmatter.group(1)
            if not re.search(r"^name:\s*[a-z0-9-]+\s*$", fm, re.M):
                errors.append("SKILL.md frontmatter needs a lowercase hyphenated name")
            if not re.search(r"^description:\s*.+$", fm, re.M):
                errors.append("SKILL.md frontmatter needs a description")

    for rel, headings in REQUIRED_TEMPLATE_HEADINGS.items():
        path = root / rel
        if not path.exists():
            continue
        text = read(path)
        for heading in headings:
            if heading not in text:
                errors.append(f"{rel} missing heading: {heading}")

    manifest_path = root / "manifest.txt"
    if manifest_path.exists():
        listed = {
            line.strip()
            for line in read(manifest_path).splitlines()
            if line.strip() and not line.startswith("#")
        }
        actual = {
            str(path.relative_to(root)).replace("\\", "/")
            for path in root.rglob("*")
            if path.is_file() and path.name != ".DS_Store"
        }
        missing_from_manifest = sorted(actual - listed)
        extra_in_manifest = sorted(listed - actual)
        if missing_from_manifest:
            errors.append("Files missing from manifest: " + ", ".join(missing_from_manifest))
        if extra_in_manifest:
            errors.append("Manifest references missing files: " + ", ".join(extra_in_manifest))

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
