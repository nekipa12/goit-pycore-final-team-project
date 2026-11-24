# Overview: what we build and how the parts fit

Read this once before your first task. Every task has its own short spec
in this folder; this file holds what all tasks share.

## 1. The product

A command-line "Personal assistant": an address book and a notebook.
The user types a command, the assistant answers, and so on until `exit`.

It is the bot from the homework, made bigger: the same `Field`, `Record`,
`AddressBook`, the same `add <name> <phone>` style of commands. We add
email, address, search, deletion, birthdays for a given number of days, notes
with tags, storage in the user's home folder and installation as a
package.

We keep it simple on purpose: only the standard library, only what was
studied in the course, and only the commands listed below.

## 2. What is already in `main`

The base is a working program. `hello`, `add`, `all`, `add-note`,
`all-notes` and `exit`/`close` work, and the data is saved after every
command to `.personal_assistant/data.pkl` in your home folder.

Every other command is already declared: its usage line, its function
and its description are in place, and the body is
`raise NotImplementedError`. The same is true for the methods of the
classes. **A task is "replace these bodies with real code".** Until a
command is written, the program answers
`This command is not implemented yet.` to it.

```
personal_assistant/
  __init__.py          the package                                       (finished)
  __main__.py          starts main() for `python -m personal_assistant`  (finished)
  main.py              the loop: read a command, run it, print, save     (finished)
  registry.py          the table of commands, the @command decorator     (finished)
  storage.py           load_data() and save_data(): one pickle file      (finished)
  fields.py            Field, Name, Phone, Email, Address, Birthday
  address_book.py      Record and AddressBook
  notebook.py          Note and NoteBook
  commands/
    __init__.py        imports the modules below                         (finished)
    general.py         hello, help
    contacts.py        add, all, change, remove-phone, delete
    details.py         add-email, add-address
    search.py          find
    birthdays.py       add-birthday, birthdays
    notes.py           add-note, all-notes, change-note, delete-note, find-note
    tags.py            add-tag, find-tag, sort-notes
```

Every card lists its files and, inside a file, its functions. Nobody
else works there, so two people never change the same lines. To keep it
that way:

- Do not change the files marked "finished".
- Do not change usage lines, function names, parameters or docstrings.
  `help` prints the first line of a handler's docstring.
- If you need a helper function, put it right above the function that
  uses it, never at the end of a file.
- Do not add imports: every file already imports what its cards need.
  The two exceptions are written in `field-validation.md` and
  `help-command.md`.
- Do not add attributes to `Record`, `Note` or the books and do not
  rename classes or modules: the saved data file depends on them.

## 3. How a command is written

A command is one function with the `@command` decorator; in these
documents such a function is called a handler. This is a finished one
from `commands/contacts.py`:

```python
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
```

- The text in `@command(...)` is the usage line. Its first word is the
  command name. Every `<word>` is a required argument, `[word]` is an
  optional one.
- The function always takes `(args, book, notes)`: the list of words typed
  after the command, the `AddressBook` and the `NoteBook`. It returns the
  text to print. It never calls `print()` or `input()`.
- You do not check the number of arguments. If the user gives fewer than
  the usage requires, the loop prints `Usage: ...` and does not call you.
- Take arguments by index (`args[0]`, `args[1]`), not by unpacking
  (`name, phone = args`): extra words typed by the user must not break
  the command. They are simply ignored.
- An argument that may contain spaces (an address, a note text, a search
  text) is always the last one. Take it as `" ".join(args[1:])`, or as
  `" ".join(args)` when it is the only argument.
- A name is one word, exactly as typed (`John` and `john` are different
  contacts), as in the homework.

## 4. Errors

One rule for the whole project: **a mistake of the user is a `ValueError`
with a ready message.**

```python
raise ValueError("Phone 0501234567 not found.")
```

The loop catches it and prints the message; the program goes on. So:

- field classes raise `ValueError` when a value is wrong;
- `book.find(name)` and `notes.find(note_id)` raise `ValueError` when
  there is no such contact or note, so you never check their result for
  `None`;
- you do not write `try/except` in a handler just to print an error.

Python raises `ValueError` too, with texts that mean nothing to the
user. Do not let them out:

- check `text.isdecimal()` before `int(text)`;
- check that a value is in a list before `list.remove(value)`.

**Check first, change after.** Create the new field object (it checks
the value) and do all your own checks before you change a record. If a
command answers with an error, the data must stay exactly as it was.

The loop also catches every other exception and prints
`Unexpected error: ...`, so a bug in one command cannot close the
program. That is protection against bugs, not a way to report errors.

What happens when the user types `add-email John abc`:

1. `main()` reads the line with `input()`.
2. `parse_input` splits it: the command `add-email`, the arguments
   `["John", "abc"]`.
3. `execute` finds the handler in `COMMANDS` and checks that there are
   enough arguments.
4. The handler `add_email` calls `book.find("John")` and then
   `record.add_email("abc")`.
5. `Record.add_email` creates `Email("abc")`; the class sees a wrong
   value and raises `ValueError("Invalid email abc. ...")`.
6. `execute` catches it and returns the text; `main()` prints it and
   saves the data.

## 5. The data

```python
record = book.find("John")   # Record, or ValueError "Contact John not found."
record.name                  # Name
record.phones                # list of Phone
record.email                 # Email or None
record.address               # Address or None
record.birthday              # Birthday or None; birthday.value is a date
str(record)                  # "Contact name: John, phones: 0501234567; ..."

note = notes.find("3")       # Note, or ValueError "Note 3 not found."
note.id                      # int
note.text                    # str
note.tags                    # list of str
str(note)                    # "3: Buy a present for John [birthday, shop]"
```

- `Record` has `add_phone`, `find_phone`, `add_email`, `add_address` and
  `add_birthday`. Every `add_*` method creates the field object, so a
  value is checked in one place: the field class.
- `record.find_phone(phone)` is the homework method: it returns the
  `Phone` object or `None`, it does not raise.
- Every field prints itself: `str(record.birthday)` is `24.08.1991`,
  while `record.birthday.value` is a `date`.
- `notes.find` takes the ID as the user typed it and checks it itself.
  The keys of the notebook are numbers (`note.id`).

## 6. All commands

This chapter is the contract for the texts the user sees. Use these
answers exactly.

### General

| Usage | Answer |
|---|---|
| `hello` | `How can I help you?` |
| `help` | the list of all commands |
| `exit` or `close` | `Good bye!` |
| anything else | `Unknown command. Type 'help' to see all commands.` |

### Contacts

| Usage | Answer |
|---|---|
| `add <name> <phone>` | `Contact added.` or, for an existing contact, `Contact updated.` |
| `all` | every contact on its own line, or `No contacts saved yet.` |
| `change <name> <old phone> <new phone>` | `Contact updated.` |
| `remove-phone <name> <phone>` | `Phone removed.` |
| `delete <name>` | `Contact deleted.` |
| `add-email <name> <email>` | `Email saved.` |
| `add-address <name> <address>` | `Address saved.` |
| `find <text>` | the contacts that have the text in any field, or `No contacts found.` |
| `add-birthday <name> <DD.MM.YYYY>` | `Birthday saved.` |
| `birthdays <days>` | lines `DD.MM.YYYY (Weekday): Name`, or `No birthdays in the next <days> days.` |

`add-email`, `add-address` and `add-birthday` also replace the old value:
that is how these fields are edited. `<days>` is a number from 0 to 365.

### Notes

| Usage | Answer |
|---|---|
| `add-note <text>` | `Note <id> added.` |
| `all-notes` | every note on its own line, or `No notes saved yet.` |
| `change-note <id> <new text>` | `Note <id> updated.` |
| `delete-note <id>` | `Note <id> deleted.` |
| `find-note <text>` | the notes that contain the text, or `No notes found.` |
| `add-tag <id> <tag> [tag...]` | `Tags added to note <id>.` |
| `find-tag <tag>` | the notes that have the tag, or `No notes with tag <tag>.` |
| `sort-notes` | all notes sorted by their tags, or `No notes saved yet.` |

In an answer `<id>` is the number of the note (`note.id`), `<tag>` is the
tag in lower case and `<days>` is the number, not the text as typed:
`change-note 01 Hi` answers `Note 1 updated.`

### Error messages

| When | Message |
|---|---|
| too few arguments | `Usage: <usage of the command>` |
| no such contact | `Contact <name> not found.` |
| the contact has no such phone | `Phone <phone> not found.` |
| the contact already has this phone | `Phone <phone> already exists.` |
| a name without letters | `Name must have at least one letter.` |
| a wrong phone | `Invalid phone number <phone>. Use 10 digits, for example 0501234567.` |
| a wrong email | `Invalid email <email>. Use the form name@example.com.` |
| a wrong date | `Invalid date. Use DD.MM.YYYY, for example 24.08.1991.` |
| a birthday before 1900 or in the future | `Birthday must be between 01.01.1900 and today.` |
| a wrong number of days | `Days must be a number from 0 to 365.` |
| no such note | `Note <id> not found.` |
| the note ID is not a number | `Note ID must be a number.` |

A contact is printed as
`Contact name: John, phones: 0501234567; 0671234567, email: john@example.com, birthday: 24.08.1991, address: Kyiv, Khreshchatyk 1`
(the parts that are not set are left out). A note is printed as
`3: Buy a present for John [birthday, shop]`.

## 7. How to check your work

Every task spec has a "Check it" part: what to type and what the
assistant must answer (the welcome line is left out). Start the
assistant from the project folder:

```bash
python -m personal_assistant
```

On macOS and Linux type `python3` instead of `python`.

The expected answers assume that there is no saved data, and the
assistant remembers everything between runs. So before every check
leave the assistant with `exit` and delete the data file:

```bash
rm -f ~/.personal_assistant/data.pkl                 # macOS, Linux
del $HOME\.personal_assistant\data.pkl               # Windows PowerShell
```

A message that there is no such file is fine: there was nothing to
delete.

## 8. Done means

- The code does what the spec says and nothing more.
- Only the files and functions of your card are changed.
- Every new function, class and module has a docstring.
- The "Check it" part of your spec gives the expected output.
- The program starts, and `exit` leaves it without errors.
