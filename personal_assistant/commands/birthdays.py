"""Commands that set a birthday and show the upcoming birthdays."""

from personal_assistant.registry import command


@command("add-birthday <name> <DD.MM.YYYY>")
def add_birthday(args, book, notes):
    """Set or change the birthday."""
    book.find(args[0]).add_birthday(args[1])
    return "Birthday saved."


@command("birthdays <days>")
def birthdays(args, book, notes):
    """Show birthdays in the coming days."""
    if not args[0].isdecimal() or int(args[0]) > 365:
        raise ValueError("Days must be a number from 0 to 365.")
    days = int(args[0])
    upcoming = book.upcoming_birthdays(days)
    if not upcoming:
        return f"No birthdays in the next {days} days."
    return "\n".join(
        f"{birthday.strftime('%d.%m.%Y (%A)')}: {record.name}"
        for birthday, record in upcoming
    )
