"""Saving and loading the data: the address book and the notebook.

Everything is kept in one file in the user's home folder.
"""

import pickle
from pathlib import Path

from personal_assistant.address_book import AddressBook
from personal_assistant.notebook import NoteBook

DATA_FILE = Path.home() / ".personal_assistant" / "data.pkl"


def save_data(book: AddressBook, notes: NoteBook) -> None:
    """Save the address book and the notebook to the data file."""
    # Write a new file first and then put it in place of the old one:
    # if writing fails, the old data stays untouched.
    temp_file = DATA_FILE.with_name(DATA_FILE.name + ".tmp")
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(temp_file, "wb") as file:
            pickle.dump((book, notes), file)
        temp_file.replace(DATA_FILE)
    except OSError as error:
        # No rights, full disk: tell the user and let the program go on.
        print(f"Could not save the data: {error}")


def load_data() -> tuple[AddressBook, NoteBook]:
    """Return the saved address book and notebook (empty on first run)."""
    if not DATA_FILE.exists():
        return AddressBook(), NoteBook()
    try:
        with open(DATA_FILE, "rb") as file:
            book, notes = pickle.load(file)
    except Exception:
        # A damaged file can raise almost any exception while it is read.
        book, notes = None, None
    if isinstance(book, AddressBook) and isinstance(notes, NoteBook):
        return book, notes
    # Keep the damaged file: the next save must not write over it.
    backup = DATA_FILE.with_name(DATA_FILE.name + ".bak")
    try:
        DATA_FILE.replace(backup)
        print(f"The data file is damaged, it was moved to {backup}.")
    except OSError as error:
        print(f"The data file is damaged and could not be moved: {error}")
    print("Starting with empty data.")
    return AddressBook(), NoteBook()
