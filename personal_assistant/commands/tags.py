"""Commands that work with the tags of notes."""

from personal_assistant.registry import command


@command("add-tag <id> <tag> [tag...]")
def add_tag(args, book, notes):
    """Add tags to a note."""
    note = notes.find(args[0])
    note.add_tags(args[1:])
    return f"Tags added to note {note.id}."


@command("find-tag <tag>")
def find_tag(args, book, notes):
    """Find notes by tag."""
    tag = args[0].lower()
    found = notes.find_by_tag(tag)
    if not found:
        return f"No notes with tag {tag}."
    return "\n".join(str(note) for note in found)


@command("sort-notes")
def sort_notes(args, book, notes):
    """Show all notes sorted by tags."""
    if not notes:
        return "No notes saved yet."
    return "\n".join(str(note) for note in notes.sorted_by_tags())
