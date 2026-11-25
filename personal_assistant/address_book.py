"""Contacts (records) and the address book that keeps them."""

from collections import UserDict
from datetime import date

from personal_assistant.fields import Address, Birthday, Email, Name, Phone


class Record:
    """One contact: a name, phones and optional email, address, birthday."""

    def __init__(self, name: str) -> None:
        """Create a contact that has only a name."""
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.email = None
        self.address = None
        self.birthday = None

    def find_phone(self, phone: str):
        """Return the stored Phone equal to ``phone`` or None."""
        for stored in self.phones:
            if stored.value == phone:
                return stored
        return None

    def add_phone(self, phone: str) -> None:
        """Add a phone number; the same number cannot be added twice."""
        new_phone = Phone(phone)
        if self.find_phone(new_phone.value) is not None:
            raise ValueError(f"Phone {new_phone} already exists.")
        self.phones.append(new_phone)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Replace the phone ``old_phone`` with ``new_phone``."""
        old = self.find_phone(old_phone)
        if old is None:
            raise ValueError(f"Phone {old_phone} not found.")
        new = Phone(new_phone)
        existing = self.find_phone(new.value)
        if existing is not None and existing is not old:
            raise ValueError(f"Phone {new} already exists.")
        self.phones[self.phones.index(old)] = new

    def remove_phone(self, phone: str) -> None:
        """Remove the phone number from the contact."""
        stored = self.find_phone(phone)
        if stored is None:
            raise ValueError(f"Phone {phone} not found.")
        self.phones.remove(stored)

    def add_email(self, email: str) -> None:
        """Set the email; a new value replaces the old one."""
        self.email = Email(email)

    def add_address(self, address: str) -> None:
        """Set the address; a new value replaces the old one."""
        self.address = Address(address)

    def add_birthday(self, birthday: str) -> None:
        """Set the birthday; a new value replaces the old one."""
        self.birthday = Birthday(birthday)

    def __str__(self) -> str:
        """Return the contact as one line; empty fields are left out."""
        parts = [f"Contact name: {self.name}"]
        if self.phones:
            phones = "; ".join(phone.value for phone in self.phones)
            parts.append(f"phones: {phones}")
        if self.email is not None:
            parts.append(f"email: {self.email}")
        if self.birthday is not None:
            parts.append(f"birthday: {self.birthday}")
        if self.address is not None:
            parts.append(f"address: {self.address}")
        return ", ".join(parts)


class AddressBook(UserDict):
    """All contacts: the key is the contact name, the value is a Record."""

    def add_record(self, record: Record) -> None:
        """Add a new contact to the book."""
        name = record.name.value
        if name in self.data:
            raise ValueError(f"Contact {name} already exists.")
        self.data[name] = record

    def find(self, name: str) -> Record:
        """Return the contact called ``name`` or raise ValueError."""
        if name not in self.data:
            raise ValueError(f"Contact {name} not found.")
        return self.data[name]

    def delete(self, name: str) -> None:
        """Delete the contact called ``name``."""
        self.find(name)
        del self.data[name]

    def search(self, text: str) -> list[Record]:
        """Return the contacts that have ``text`` in any of their fields."""
        raise NotImplementedError

    def upcoming_birthdays(self, days: int) -> list[tuple[date, Record]]:
        """Return (date, contact) pairs for birthdays in the next ``days``."""
        raise NotImplementedError
