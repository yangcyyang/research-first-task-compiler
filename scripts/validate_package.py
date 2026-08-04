#!/usr/bin/env python3
"""Lightweight structural validation for research-first-task-compiler."""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

REQUIRED = [
    "SKILL.md", "README.md", "LICENSE",
    "references/research-protocol.md",
    "references/review-protocol.md",
    "references/risk-and-approval-policy.md",
    "references/validation-protocol.md",
    "references/evaluation-protocol.md",
    "references/execution-protocol.md",
    "assets/task-card-template.md",
    "assets/review-package-template.md",
    "assets/workflow-state-template.md",
    "assets/golden-eval-cases.md",
    "assets/gate-transition-contract.md",
    "examples/rss-daily-task-card.md",
    "examples/rss-daily-review-package.md",
]

def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []
    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f"missing: {rel}")
    skill = root / "SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append("SKILL.md frontmatter missing or malformed")
        else:
            front = match.group(1)
            for key in ("name:", "description:", "license:"):
                if key not in front:
                    errors.append(f"frontmatter missing {key[:-1]}")
            name_match = re.search(r"^name:\s*([^\n]+)$", front, re.M)
            if name_match and not re.fullmatch(r"[a-z0-9-]+", name_match.group(1).strip()):
                errors.append("name must use lowercase letters, numbers, and hyphens")
        lines = text.count("\n") + 1
        if lines > 500:
            errors.append(f"SKILL.md has {lines} lines; recommended maximum is 500")
        for rel in re.findall(r"\]\(([^)]+\.md)\)", text):
            if rel.startswith("http"):
                continue
            if not (root / rel).exists():
                errors.append(f"broken SKILL.md reference: {rel}")
        if 'version: "1.3.0"' not in front:
            errors.append("SKILL.md must declare version 1.3.0")
        for trigger in ("先查再造", "research-first", "task-compiler"):
            if f"  - {trigger}" not in front:
                errors.append(f"SKILL.md missing trigger: {trigger}")
        for required_rule in (
            "Gate A — task-card confirmation is mandatory and version-bound",
            "Gate B — review-package decision is mandatory and version-bound",
            "Forbidden before Gate A passes",
            "Forbidden before Gate B passes",
        ):
            if required_rule not in text:
                errors.append(f"SKILL.md missing version-bound gate rule: {required_rule}")
    for gate_test in (
        root / "scripts" / "validate_gate_contract.py",
        root / "scripts" / "test_gate_contract.py",
    ):
        if not gate_test.is_file():
            errors.append(f"missing gate validation: {gate_test.name}")
            continue
        result = subprocess.run([sys.executable, str(gate_test)], capture_output=True, text=True, check=False)
        if result.returncode:
            errors.append(f"gate transition contract failed: {result.stdout}{result.stderr}".strip())
    if errors:
        print("VALIDATION FAILED")
        for e in errors:
            print(f"- {e}")
        return 1
    print("VALIDATION PASSED")
    print(f"Root: {root}")
    print(f"Required files: {len(REQUIRED)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
