# Add contact search

| | |
|---|---|
| Card, commit and PR title | `Add contact search` |
| Branch | `feature/<card number>-contact-search` |
| Files | `personal_assistant/address_book.py`: `AddressBook.search`<br>`personal_assistant/commands/search.py`: `find_contacts` |
| Depends on | nothing |
| Covers | "search contacts in the address book", "search by different criteria (for example, by name)" |

## What to build

Replace `raise NotImplementedError` in two bodies.

**`AddressBook.search(text)`** returns the list of records that have
`text` in at least one field value: the name, any phone, the email, the
address or the birthday.

- Letter case is ignored: `john` finds `John`.
- A part of a value is enough: `050` finds `0501234567`, `gmail` finds
  `john@gmail.com`.
- Look at the values only, not at the printed line of a record, otherwise
  `find email` would find every contact that has an email.
- The birthday is searched as the text `DD.MM.YYYY`: use
  `str(record.birthday)`, because `record.birthday.value` is a `date`.
- Fields that are not set (`None`) are skipped.
- The records come in the order they have in the book: do not sort.

**`find_contacts`**, usage `find <text>`: every found contact on its own
line (`str(record)`), or `No contacts found.`

The text may consist of several words (`find Main Street`): join all the
arguments with a space. The words are searched as one phrase.

## Check it

Start with empty data (overview, chapter 7).

```text
Enter a command: add John 0501234567
Contact added.
Enter a command: add Joanna 0671112233
Contact added.
Enter a command: add Bob 0930000000
Contact added.
Enter a command: find jo
Contact name: John, phones: 0501234567
Contact name: Joanna, phones: 0671112233
Enter a command: find 0930
Contact name: Bob, phones: 0930000000
Enter a command: find phones
No contacts found.
Enter a command: find John 050
No contacts found.
Enter a command: find
Usage: find <text>
```

Email, address and birthday are set by other cards, so this part of the
check is done in the Python console (`python` in the project folder). It
is required: a mistake with the birthday shows up only here.

```python
>>> from personal_assistant.address_book import AddressBook, Record
>>> book = AddressBook()
>>> record = Record("John")
>>> record.add_email("john@gmail.com")
>>> record.add_address("Kyiv, Khreshchatyk 1")
>>> record.add_birthday("24.08.1991")
>>> book.add_record(record)
>>> [str(found.name) for found in book.search("GMAIL")]
['John']
>>> [str(found.name) for found in book.search("khresh")]
['John']
>>> [str(found.name) for found in book.search("08.1991")]
['John']
>>> book.search("email")
[]
```

## Not in this task

Search by one chosen field, regular expressions, sorting of the result.
