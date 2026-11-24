"""Commands that set the email and the address of a contact."""

from personal_assistant.registry import command


@command("add-email <name> <email>")
def add_email(args, book, notes):
    """Set or change the email."""
    raise NotImplementedError


@command("add-address <name> <address>")
def add_address(args, book, notes):
    """Set or change the address."""
    raise NotImplementedError
