"""Commands that set the email and the address of a contact."""

from personal_assistant.registry import command


@command("add-email <name> <email>")
def add_email(args, book, notes):
    """Set or change the email."""
    record = book.find(args[0])
    record.add_email(args[1])
    return "Email saved."


@command("add-address <name> <address>")
def add_address(args, book, notes):
    """Set or change the address."""
    record = book.find(args[0])
    record.add_address(" ".join(args[1:]))
    return "Address saved."
