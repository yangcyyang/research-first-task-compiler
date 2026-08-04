#!/usr/bin/env python3
"""Regression tests for the two conversation gates.

The skill is a Markdown workflow, so this test verifies its executable policy
contract: version-bound approvals, presentation-before-approval, and
invalidation after a material artifact change.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


@dataclass
class GateState:
    task_card_version: int = 0
    task_card_presented: bool = False
    gate_a_passed_version: int | None = None
    review_package_version: int = 0
    review_package_presented: bool = False
    gate_b_selected_version: int | None = None

    def show_task_card(self) -> None:
        self.task_card_version += 1
        self.task_card_presented = True
        self.gate_a_passed_version = None
        self.invalidate_review()

    def confirm_task_card(self, version: int) -> bool:
        if self.task_card_presented and version == self.task_card_version:
            self.gate_a_passed_version = version
            return True
        return False

    def show_review_package(self) -> None:
        if self.gate_a_passed_version != self.task_card_version:
            raise PermissionError("Gate A is not passed for the current task card")
        self.review_package_version += 1
        self.review_package_presented = True
        self.gate_b_selected_version = None

    def select_direction(self, version: int) -> bool:
        if self.review_package_presented and version == self.review_package_version:
            self.gate_b_selected_version = version
            return True
        return False

    def invalidate_review(self) -> None:
        self.review_package_version = 0
        self.review_package_presented = False
        self.gate_b_selected_version = None


class GateTransitionTests(unittest.TestCase):
    def test_task_card_edit_invalidates_gate_a_and_gate_b(self) -> None:
        state = GateState()
        state.show_task_card()
        self.assertTrue(state.confirm_task_card(1))
        state.show_review_package()
        self.assertTrue(state.select_direction(1))

        state.show_task_card()

        self.assertIsNone(state.gate_a_passed_version)
        self.assertIsNone(state.gate_b_selected_version)
        self.assertFalse(state.confirm_task_card(1))
        with self.assertRaises(PermissionError):
            state.show_review_package()

    def test_early_or_stale_review_choice_cannot_open_gate_b(self) -> None:
        state = GateState()
        self.assertFalse(state.select_direction(1))
        state.show_task_card()
        self.assertTrue(state.confirm_task_card(1))
        state.show_review_package()
        self.assertTrue(state.select_direction(1))

        state.show_review_package()

        self.assertIsNone(state.gate_b_selected_version)
        self.assertFalse(state.select_direction(1))
        self.assertTrue(state.select_direction(2))


class PolicyDocumentTests(unittest.TestCase):
    def test_skill_declares_version_bound_gate_a(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Only an explicit confirmation of the current displayed task-card version passes Gate A.", text)
        self.assertIn("A modification or addition never passes Gate A", text)

    def test_skill_declares_presentation_bound_gate_b(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("only after that exact review-package version has been displayed", text)
        self.assertIn("invalidate Gate B", text)

    def test_templates_record_versions_and_invalidation(self) -> None:
        state = (ROOT / "assets/workflow-state-template.md").read_text(encoding="utf-8")
        decision = (ROOT / "assets/decision-log-template.md").read_text(encoding="utf-8")
        self.assertIn("Task card presentation evidence", state)
        self.assertIn("Review package presentation evidence", state)
        self.assertIn("Invalidated", state)
        self.assertIn("Task card version", decision)
        self.assertIn("Review package version", decision)


if __name__ == "__main__":
    unittest.main(verbosity=2)
