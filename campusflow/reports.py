"""Aggregate ticket counts for the CampusFlow CLI."""

from __future__ import annotations

from typing import Any, Iterable

Ticket = dict[str, Any]

_STATUSES = ("open", "in_progress", "resolved")
_PRIORITIES = ("critical", "high", "medium", "low")
_CATEGORIES = ("Network", "Hardware", "Software", "Other")


def generate_report(tickets: Iterable[Ticket]) -> dict[str, Any]:
    """Return ticket counts and resolution statistics."""

    status_counts = {status: 0 for status in _STATUSES}
    priority_counts = {priority: 0 for priority in _PRIORITIES}
    category_counts = {category: 0 for category in _CATEGORIES}

    total = 0

    for ticket in tickets:
        total += 1

        status = ticket.get("status")
        priority = ticket.get("priority")
        category = ticket.get("category")

        if status not in status_counts:
            raise ValueError(f"Unknown ticket status: {status!r}.")

        if priority not in priority_counts:
            raise ValueError(f"Unknown ticket priority: {priority!r}.")

        status_counts[status] += 1
        priority_counts[priority] += 1

        # Older test records may not have a category.
        if category is not None:
            matching_category = next(
                (
                    item
                    for item in _CATEGORIES
                    if item.casefold() == category.casefold()
                ),
                None,
            )

            if matching_category is None:
                raise ValueError(f"Unknown ticket category: {category!r}.")

            category_counts[matching_category] += 1

    resolved = status_counts["resolved"]
    unresolved = status_counts["open"] + status_counts["in_progress"]

    if total == 0:
        resolution_percentage = 0.0
    else:
        resolution_percentage = (resolved / total) * 100

    return {
        "total": total,
        "by_status": status_counts,
        "by_priority": priority_counts,
        "by_category": category_counts,
        "unresolved": unresolved,
        "resolution_percentage": resolution_percentage,
    }
