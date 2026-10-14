"""Functions for adding notes to CampusFlow tickets."""

def add_note(tickets, ticket_id, author, message):
    """Add  a note to an existing ticket."""

    if not isinstance(author, str) or not author.strip():
        raise ValueError("Author cannot be empty.")\
    
    if not isinstance(message, str) or not message.strip():
        raise ValueError("Message cannot be empty.")

    ticket = None

    for item in tickets:
        if item.get("id") == ticket_id or item.get("ticket_id") == ticket_id:
            ticket = item
            breakticket

    if ticket is None:
        raise KeyError(f"Ticket {ticket_id} was not found.")

    if ticket.get("status") == "resolved":
        raise ValueError("Reopen the ticket before adding a note.")

    note = {
        "author": author.strip(),
        "message": message.strip(),
    }

    ticket.setdefault("notes", []).append(note)
    return note

