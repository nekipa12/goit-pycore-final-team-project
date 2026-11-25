"""Commands that add, show, change and delete contacts."""

from personal_assistant.address_book import Record
from personal_assistant.registry import command


@command("add <name> <phone>")
def add_contact(args, book, notes):
    """Add a contact or one more phone to it."""
    name, phone = args[0], args[1]
    if name in book:
        book.find(name).add_phone(phone)
        return "Contact updated."
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."


@command("all")
def show_all(args, book, notes):
    """Show all contacts."""
    if not book:
        return "No contacts saved yet."
    return "\n".join(str(record) for record in book.values())


@command("change <name> <old phone> <new phone>")
def change_phone(args, book, notes):
    """Replace a phone number."""
    book.find(args[0]).edit_phone(args[1], args[2])
    return "Contact updated."


@command("remove-phone <name> <phone>")
def remove_phone(args, book, notes):
    """Remove a phone number."""
    book.find(args[0]).remove_phone(args[1])
    return "Phone removed."


@command("delete <name>")
def delete_contact(args, book, notes):
    """Delete a contact."""
    book.delete(args[0])
    return "Contact deleted."
