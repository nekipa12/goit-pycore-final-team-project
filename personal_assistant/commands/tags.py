"""Commands that work with the tags of notes."""

from personal_assistant.registry import command


@command("add-tag <id> <tag> [tag...]")
def add_tag(args, book, notes):
    """Add tags to a note."""
    raise NotImplementedError


@command("find-tag <tag>")
def find_tag(args, book, notes):
    """Find notes by tag."""
    raise NotImplementedError


@command("sort-notes")
def sort_notes(args, book, notes):
    """Show all notes sorted by tags."""
    raise NotImplementedError
