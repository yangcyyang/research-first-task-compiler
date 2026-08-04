#!/usr/bin/env python3
"""Deterministic regression checks for the v1.3 version-bound approval gates."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GateState:
    task_version: int = 0
    task_displayed: bool = False
    task_confirmed: int | None = None
    review_version: int = 0
    review_selected: int | None = None
    review_displayed: bool = False
    gray_blocker: bool = False

    def display_task(self, changed: bool = True) -> None:
        if changed or self.task_version == 0:
            self.task_version += 1
        self.task_displayed = True
        self.task_confirmed = None
        self.review_selected = None
        self.review_displayed = False

    def confirm_task(self, version: int) -> bool:
        if not self.task_displayed or version <= 0 or version != self.task_version:
            return False
        self.task_confirmed = version
        return True

    def display_review(self, changed: bool = True) -> bool:
        if not self.task_displayed or self.task_confirmed != self.task_version:
            return False
        if changed or self.review_version == 0:
            self.review_version += 1
        self.review_selected = None
        self.review_displayed = True
        return True

    def select_review(self, version: int) -> bool:
        if not self.review_displayed or version != self.review_version:
            return False
        self.review_selected = version
        return True

    def may_execute(self) -> bool:
        return (
            self.task_confirmed == self.task_version
            and self.review_selected == self.review_version
            and not self.gray_blocker
        )


CHECK_COUNT = 0


def check(condition: bool, message: str) -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    if not condition:
        raise AssertionError(message)


def main() -> None:
    fresh = GateState()
    check(not fresh.confirm_task(0), "unshown initial TC-0 confirmation must fail")
    check(not fresh.display_review(), "unshown initial TC-0 must not open the review gate")

    state = GateState()
    state.display_task()
    check(not state.may_execute(), "Gate A pending must block execution")
    check(not state.confirm_task(0), "old task-card confirmation must fail")
    check(state.confirm_task(1), "current task-card confirmation must pass")
    check(state.display_review(), "review may display only after Gate A")
    check(not state.select_review(2), "future or undisplayed review selection must fail")
    check(state.select_review(1), "current displayed review selection must pass")
    check(state.may_execute(), "both current gates should allow execution")

    state.display_task(changed=True)
    check(state.task_version == 2 and state.task_confirmed is None, "task modification must invalidate confirmation")
    check(not state.may_execute(), "task modification must invalidate downstream execution")
    check(state.confirm_task(2), "new task-card confirmation must pass")
    check(state.display_review(), "new review may display after new task confirmation")
    check(state.select_review(2), "current review selection must pass")
    state.display_review(changed=True)
    check(state.review_version == 3 and state.review_selected is None, "review revision must invalidate old selection")
    check(not state.may_execute(), "old review selection must not authorize revised package")
    check(state.select_review(3), "new review selection must pass")
    state.gray_blocker = True
    check(not state.may_execute(), "gray evidence must block execution")
    print(f"GATE CONTRACT PASSED: {CHECK_COUNT} transition assertions")


if __name__ == "__main__":
    main()
