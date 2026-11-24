# Add contact editing and deletion

| | |
|---|---|
| Card, commit and PR title | `Add contact editing and deletion` |
| Branch | `feature/<card number>-contact-editing` |
| Files | `personal_assistant/address_book.py`: `Record.edit_phone`, `Record.remove_phone`, `AddressBook.delete`<br>`personal_assistant/commands/contacts.py`: `change_phone`, `remove_phone`, `delete_contact` |
| Depends on | nothing |
| Covers | "edit and delete records of the address book" |

## What to build

Replace `raise NotImplementedError` in six bodies.

**Model, `address_book.py`**

- `Record.edit_phone(old_phone, new_phone)`: put the new number in the
  place of the old one, at the same position in the list. Check in this
  order:
  1. `self.find_phone(old_phone)` returns `None` (it does not raise):
     `Phone <old_phone> not found.`
  2. create `Phone(new_phone)`: the class raises the error for a wrong
     number itself;
  3. the record has `new_phone` as another number:
     `Phone <new_phone> already exists.` Changing a number to itself is
     not an error.

  Only then replace the old `Phone` object. If anything is wrong, the
  record stays exactly as it was.
- `Record.remove_phone(phone)`: remove the number;
  `Phone <phone> not found.` if the record does not have it. The last
  number can be removed too; the contact stays.
- `AddressBook.delete(name)`: remove the contact. For a missing contact
  the answer is `Contact <name> not found.`; `self.find(name)` already
  raises it.

**Commands, `commands/contacts.py`**

| Function | Usage | Answer |
|---|---|---|
| `change_phone` | `change <name> <old phone> <new phone>` | `Contact updated.` |
| `remove_phone` | `remove-phone <name> <phone>` | `Phone removed.` |
| `delete_contact` | `delete <name>` | `Contact deleted.` |

## Check it

Start with empty data (overview, chapter 7).

```text
Enter a command: add John 0501234567
Contact added.
Enter a command: add John 0671234567
Contact updated.
Enter a command: change John 0501234567 0931234567
Contact updated.
Enter a command: all
Contact name: John, phones: 0931234567; 0671234567
Enter a command: change John 0931234567 0931234567
Contact updated.
Enter a command: change John 0000000000 0931234567
Phone 0000000000 not found.
Enter a command: change John 0931234567 0671234567
Phone 0671234567 already exists.
Enter a command: change John
Usage: change <name> <old phone> <new phone>
Enter a command: remove-phone John 0671234567
Phone removed.
Enter a command: remove-phone John 0671234567
Phone 0671234567 not found.
Enter a command: all
Contact name: John, phones: 0931234567
Enter a command: delete Ann
Contact Ann not found.
Enter a command: delete John
Contact deleted.
Enter a command: all
No contacts saved yet.
```

One more check works only when the card `Add field validation` is in
`main` too; it is repeated in the release card:

```text
Enter a command: add John 0501234567
Contact added.
Enter a command: change John 0501234567 abc
Invalid phone number abc. Use 10 digits, for example 0501234567.
Enter a command: all
Contact name: John, phones: 0501234567
```

## Not in this task

Renaming a contact, confirmation questions, undo.
