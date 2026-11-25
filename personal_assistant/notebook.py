"""Notes and the notebook that keeps them."""

from collections import UserDict


class Note:
    """One note: a number (ID), a text and a list of tags."""

    def __init__(self, note_id: int, text: str) -> None:
        """Create a note without tags."""
        self.id = note_id
        self.text = text
        self.tags: list[str] = []

    def add_tags(self, tags: list[str]) -> None:
        """Add the tags that the note does not have yet."""
        raise NotImplementedError

    def __str__(self) -> str:
        """Return the note as one line: the ID, the text and the tags."""
        text = f"{self.id}: {self.text}"
        if self.tags:
            text += f" [{', '.join(self.tags)}]"
        return text


class NoteBook(UserDict):
    """All notes: the key is the note ID, the value is a Note."""

    def add(self, text: str) -> Note:
        """Create a note with the next free ID and return it."""
        note = Note(max(self.data, default=0) + 1, text)
        self.data[note.id] = note
        return note

    def find(self, note_id: str) -> Note:
        """Return the note with this ID or raise ValueError.

        ``note_id`` is the text typed by the user, so it is checked here.
        """
        if not note_id.isdecimal():
            raise ValueError("Note ID must be a number.")
        number = int(note_id)
        if number not in self.data:
            raise ValueError(f"Note {number} not found.")
        return self.data[number]

    def delete(self, note_id: str) -> Note:
        """Delete the note with this ID and return it."""
        note = self.find(note_id)
        del self.data[note.id]
        return note

    def search(self, text: str) -> list[Note]:
        """Return the notes that contain ``text``."""
        raise NotImplementedError

    def find_by_tag(self, tag: str) -> list[Note]:
        """Return the notes that have the tag."""
        raise NotImplementedError

    def sorted_by_tags(self) -> list[Note]:
        """Return all notes sorted by their tags."""
        raise NotImplementedError
