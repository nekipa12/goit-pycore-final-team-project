"""Fields of a contact: every field keeps one value."""

import re
from datetime import date, datetime

EMAIL_PATTERN = (
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
)


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

    def __init__(self, value: str) -> None:
        """Check that the name has at least one letter."""
        if not any(char.isalpha() for char in value):
            raise ValueError("Name must have at least one letter.")
        super().__init__(value)


class Phone(Field):
    """Phone number of a contact."""

    def __init__(self, value: str) -> None:
        """Check that the phone is exactly 10 digits."""
        if not re.fullmatch(r"[0-9]{10}", value):
            raise ValueError(
                f"Invalid phone number {value}. "
                "Use 10 digits, for example 0501234567."
            )
        super().__init__(value)


class Email(Field):
    """E-mail address of a contact."""

    def __init__(self, value: str) -> None:
        """Check that the email looks like name@example.com."""
        if not re.fullmatch(EMAIL_PATTERN, value):
            raise ValueError(
                f"Invalid email {value}. Use the form name@example.com."
            )
        super().__init__(value)


class Address(Field):
    """Postal address of a contact."""

    def __init__(self, value: str) -> None:
        """Check that the address is not empty."""
        if not value.strip():
            raise ValueError("Address cannot be empty.")
        super().__init__(value)


class Birthday(Field):
    """Birthday of a contact, kept as a ``datetime.date``."""

    def __init__(self, value: str) -> None:
        """Turn the text DD.MM.YYYY into a date."""
        message = "Invalid date. Use DD.MM.YYYY, for example 24.08.1991."
        if not re.fullmatch(r"[0-9]{2}\.[0-9]{2}\.[0-9]{4}", value):
            raise ValueError(message)
        try:
            birthday = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError(message)
        if not date(1900, 1, 1) <= birthday <= date.today():
            raise ValueError("Birthday must be between 01.01.1900 and today.")
        super().__init__(birthday)

    def __str__(self) -> str:
        """Return the date as DD.MM.YYYY."""
        return self.value.strftime("%d.%m.%Y")
