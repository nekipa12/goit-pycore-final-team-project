"""Commands that add, show, change, delete and search notes."""

from personal_assistant.registry import command


@command("add-note <text>")
def add_note(args, book, notes):
    """Add a note."""
    note = notes.add(" ".join(args))
    return f"Note {note.id} added."


@command("all-notes")
def show_notes(args, book, notes):
    """Show all notes."""
    if not notes:
        return "No notes saved yet."
    return "\n".join(str(note) for note in notes.values())


@command("change-note <id> <new text>")
def change_note(args, book, notes):
    """Replace the text of a note."""
    note = notes.find(args[0])
    note.text = " ".join(args[1:])
    return f"Note {note.id} updated."


@command("delete-note <id>")
def delete_note(args, book, notes):
    """Delete a note."""
    note = notes.delete(args[0])
    return f"Note {note.id} deleted."


@command("find-note <text>")
def find_notes(args, book, notes):
    """Find notes by text."""
    found = notes.search(" ".join(args))
    if not found:
        return "No notes found."
    return "\n".join(str(note) for note in found)
