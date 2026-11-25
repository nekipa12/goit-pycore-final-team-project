"""Command that searches the contacts."""

from personal_assistant.registry import command


@command("find <text>")
def find_contacts(args, book, notes):
    """Find contacts by any field."""
    found = book.search(" ".join(args))
    if not found:
        return "No contacts found."
    return "\n".join(str(record) for record in found)
