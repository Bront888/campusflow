"""Tests for ticket reporting."""

import unittest

from campusflow.reports import generate_report


class GenerateReportTests(unittest.TestCase):
    def test_report_counts_statuses_and_priorities(self):
        tickets = [
            {"status": "open", "priority": "critical"},
            {"status": "in_progress", "priority": "high"},
            {"status": "resolved", "priority": "high"},
            {"status": "open", "priority": "low"},
        ]

        report = generate_report(tickets)

        self.assertEqual(report["total"], 4)
        self.assertEqual(
            report["by_status"],
            {"open": 2, "in_progress": 1, "resolved": 1},
        )
        self.assertEqual(
            report["by_priority"],
            {"critical": 1, "high": 2, "medium": 0, "low": 1},
        )

    def test_empty_report_includes_all_zero_counts(self):
        report = generate_report([])

        self.assertEqual(report["total"], 0)
        self.assertEqual(
            report["by_status"],
            {"open": 0, "in_progress": 0, "resolved": 0},
        )
        self.assertEqual(
            report["by_priority"],
            {"critical": 0, "high": 0, "medium": 0, "low": 0},
        )

    def test_unknown_status_is_rejected(self):
        with self.assertRaises(ValueError):
            generate_report([{"status": "closed", "priority": "low"}])

    def test_unknown_priority_is_rejected(self):
        with self.assertRaises(ValueError):
            generate_report([{"status": "open", "priority": "urgent"}])

    def test_report_counts_categories(self):
        tickets = [
            {
                "status": "open",
                "priority": "high",
                "category": "Network",
            },
            {
                "status": "resolved",
                "priority": "low",
                "category": "Hardware",
            },
            {
                "status": "open",
                "priority": "medium",
                "category": "Network",
            },
        ]

        report = generate_report(tickets)

        self.assertEqual(
            report["by_category"],
            {
                "Network": 2,
                "Hardware": 1,
                "Software": 0,
                "Other": 0,
            },
        )

    def test_report_counts_unresolved_tickets(self):
        tickets = [
            {"status": "open", "priority": "high"},
            {"status": "in_progress", "priority": "medium"},
            {"status": "resolved", "priority": "low"},
        ]

        report = generate_report(tickets)

        self.assertEqual(report["unresolved"], 2)

    def test_resolution_percentage(self):
        tickets = [
            {"status": "resolved", "priority": "high"},
            {"status": "resolved", "priority": "low"},
            {"status": "open", "priority": "medium"},
            {"status": "in_progress", "priority": "high"},
        ]

        report = generate_report(tickets)

        self.assertEqual(report["resolution_percentage"], 50.0)

    def test_empty_report_has_zero_resolution_percentage(self):
        report = generate_report([])

        self.assertEqual(report["resolution_percentage"], 0.0)
        self.assertEqual(report["unresolved"], 0)

    def test_unknown_category_is_rejected(self):
        tickets = [
            {
                "status": "open",
                "priority": "low",
                "category": "Food",
            }
        ]

        with self.assertRaises(ValueError):
            generate_report(tickets)

if __name__ == "__main__":
    unittest.main()
