"""Command that searches the contacts."""

from personal_assistant.registry import command


@command("find <text>")
def find_contacts(args, book, notes):
    """Find contacts by any field."""
    raise NotImplementedError
