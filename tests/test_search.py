import unittest

from campusflow.search import search_tickets


class SearchTests(unittest.TestCase):

    def setUp(self):
        self.tickets = [
            {
                "id": 1,
                "title": "Campus WiFi Problem",
                "category": "Network",
                "status": "open",
                "priority": "critical",
            },
            {
                "id": 2,
                "title": "Broken Laptop",
                "category": "Hardware",
                "status": "in_progress",
                "priority": "high",
            },
            {
                "id": 3,
                "title": "WiFi Password Help",
                "category": "Network",
                "status": "resolved",
                "priority": "low",
            },
        ]

    def test_empty_search_returns_all_tickets(self):
        result = search_tickets(self.tickets)
        self.assertEqual(len(result), 3)

    def test_title_search_is_case_insensitive(self):
        result = search_tickets(self.tickets, title_query="WIFI")
        self.assertEqual(len(result), 2)

    def test_no_match_returns_empty_list(self):
        result = search_tickets(self.tickets, title_query="printer")
        self.assertEqual(result, [])

    def test_category_filter(self):
        result = search_tickets(self.tickets, category="Network")
        self.assertEqual(len(result), 2)

    def test_status_filter(self):
        result = search_tickets(self.tickets, status="open")
        self.assertEqual(len(result), 1)

    def test_priority_filter(self):
        result = search_tickets(self.tickets, priority="high")
        self.assertEqual(len(result), 1)

    def test_combined_filters(self):
        result = search_tickets(
            self.tickets,
            title_query="wifi",
            category="Network",
            status="open",
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)

    def test_invalid_category_is_rejected(self):
        with self.assertRaises(ValueError):
            search_tickets(self.tickets, category="Food")

    def test_invalid_status_is_rejected(self):
        with self.assertRaises(ValueError):
            search_tickets(self.tickets, status="waiting")

    def test_invalid_priority_is_rejected(self):
        with self.assertRaises(ValueError):
            search_tickets(self.tickets, priority="urgent")


if __name__ == "__main__":
    unittest.main()