"""Fields of a contact: every field keeps one value."""

from datetime import datetime


class Field:
    """Base class of all fields."""

    def __init__(self, value):
        """Keep the value of the field."""
        self.value = value

    def __str__(self) -> str:
        """Return the value as text."""
        return str(self.value)


class Name(Field):
    """Name of a contact."""


class Phone(Field):
    """Phone number of a contact."""


class Email(Field):
    """E-mail address of a contact."""


class Address(Field):
    """Postal address of a contact."""


class Birthday(Field):
    """Birthday of a contact, kept as a ``datetime.date``."""

    def __init__(self, value: str) -> None:
        """Turn the text DD.MM.YYYY into a date."""
        try:
            birthday = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError(
                "Invalid date. Use DD.MM.YYYY, for example 24.08.1991."
            )
        super().__init__(birthday)

    def __str__(self) -> str:
        """Return the date as DD.MM.YYYY."""
        return self.value.strftime("%d.%m.%Y")
