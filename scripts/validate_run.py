#!/usr/bin/env python3
"""Validate a generated run workspace."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED = [
    "00-intake/original-request.md",
    "01-task-card/task-card-screen.md",
    "01-task-card/task-card-record.md",
    "02-solution-card/solution-card-screen.md",
    "02-solution-card/solution-card-record.md",
    "05-result-card/result-card-screen.md",
    "05-result-card/result-card-record.md",
    "06-governance/source-index.md",
    "06-governance/assumption-log.md",
    "06-governance/baseline.md",
    "07-validation/final-validation-report.md",
]

SCREEN_LIMITS = {
    "01-task-card/task-card-screen.md": ("需要你确认", 3),
    "02-solution-card/solution-card-screen.md": ("需要你确认", 3),
    "05-result-card/result-card-screen.md": ("需要你验收", 3),
}


def unresolved_placeholders(text: str) -> list[str]:
    found = []
    start = 0
    while True:
        i = text.find("{{", start)
        if i < 0:
            break
        j = text.find("}}", i + 2)
        if j < 0:
            break
        found.append(text[i:j + 2])
        start = j + 2
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_root")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Do not fail on unresolved template placeholders",
    )
    args = parser.parse_args()
    root = Path(args.run_root).resolve()

    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED:
        path = root / rel
        if not path.exists():
            errors.append(f"Missing: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"Empty: {rel}")
        if not args.allow_placeholders:
            placeholders = unresolved_placeholders(text)
            if placeholders:
                warnings.append(
                    f"{rel} still has {len(placeholders)} unresolved placeholders"
                )

    for rel in SCREEN_LIMITS:
        path = root / rel
        if path.exists():
            chars = len(path.read_text(encoding="utf-8"))
            if chars > 1600:
                warnings.append(
                    f"{rel} is {chars} characters; review whether it still fits one screen"
                )

    if errors:
        print("RUN VALIDATION FAILED")
        for item in errors:
            print(f"- ERROR: {item}")
    else:
        print("RUN STRUCTURE PASSED")

    for item in warnings:
        print(f"- WARNING: {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
