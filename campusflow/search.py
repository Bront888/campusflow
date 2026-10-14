"""Functions for searching and filtering CampusFlow tickets."""

from typing import Any, Iterable

Ticket = dict[str, Any]

CATEGORIES = ("Network", "Hardware", "Software", "Other")
STATUSES = ("open", "in_progress", "resolved")
PRIORITIES = ("critical", "high", "medium", "low")


def search_tickets(
    tickets: Iterable[Ticket],
    title_query: str = "",
    category: str | None = None,
    status: str | None = None,
    priority: str | None = None,
) -> list[Ticket]:

    if not isinstance(title_query, str):
        raise ValueError("Title search must be text.")

    if category is not None:
        category = category.strip().casefold()
        if category not in [item.casefold() for item in CATEGORIES]:
            raise ValueError("Invalid category.")

    if status is not None:
        status = status.strip().casefold()
        if status not in STATUSES:
            raise ValueError("Invalid status.")

    if priority is not None:
        priority = priority.strip().casefold()
        if priority not in PRIORITIES:
            raise ValueError("Invalid priority.")

    results = []

    for ticket in tickets:
        if title_query.casefold() not in ticket["title"].casefold():
            continue

        if category is not None:
            if ticket["category"].casefold() != category:
                continue

        if status is not None:
            if ticket["status"] != status:
                continue

        if priority is not None:
            if ticket["priority"] != priority:
                continue

        results.append(ticket)

    return results