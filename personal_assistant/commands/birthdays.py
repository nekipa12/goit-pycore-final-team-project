"""Commands that set a birthday and show the upcoming birthdays."""

from personal_assistant.registry import command


@command("add-birthday <name> <DD.MM.YYYY>")
def add_birthday(args, book, notes):
    """Set or change the birthday."""
    raise NotImplementedError


@command("birthdays <days>")
def birthdays(args, book, notes):
    """Show birthdays in the coming days."""
    raise NotImplementedError
