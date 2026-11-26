# Personal Assistant

A command-line assistant that keeps your contacts and notes. You type a
command, the assistant answers.

It can:

- keep contacts with phones, an email, an address and a birthday;
- check phone numbers and emails when you enter them;
- find, change and delete contacts;
- show whose birthday is in the coming days;
- keep text notes, find, change and delete them;
- mark notes with tags, find and sort notes by tags;
- save everything to your home folder, so nothing is lost between runs.

This is the final team project of the GoIT course "Python Programming:
Foundations and Best Practices".

## How to install

You need Python 3.10 or newer. The assistant uses only the Python
standard library. On macOS and Linux type `python3` instead of `python`.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install git+https://github.com/nekipa12/goit-pycore-final-team-project.git
```

While this virtual environment is active, the command
`personal-assistant` works from any folder:

```bash
personal-assistant
```

To install from a copy of the repository instead, create and activate
the virtual environment as above, then:

```bash
git clone https://github.com/nekipa12/goit-pycore-final-team-project.git
cd goit-pycore-final-team-project
pip install .
```

## How to use

### Start and exit

Start the assistant with this command (if you installed it into a
virtual environment, that environment must be active):

```bash
personal-assistant
```

The assistant greets you and waits for a command:

```text
Welcome to the assistant bot! Type 'help' to see all commands.
Enter a command:
```

Type a command and press Enter. The assistant answers and waits for the
next command. To leave, type `exit` or `close`.

| Command | What it does |
|---|---|
| `hello` | Greets you: `How can I help you?` |
| `help` | Shows the list of all commands. |
| `exit` or `close` | Says `Good bye!` and closes the assistant. |

An unknown command gets the answer
`Unknown command. Type 'help' to see all commands.`

### Rules of input

- A command is typed in one line: the command, then its values,
  separated by spaces. Extra words at the end are ignored.
- A name is one word with at least one letter. Letter case matters:
  `John` and `john` are two different contacts.
- A phone is 10 digits, for example `0501234567`.
- A date is `DD.MM.YYYY`, for example `24.08.1991`. A birthday is a date
  from 01.01.1900 to today.
- An email looks like `name@example.com`.
- An address and a note text may have several words.
- A note is chosen by its number, which `all-notes` shows.
- A tag is one word and is kept in lower case. Tags are separated by
  spaces (a comma after a tag is dropped) and are shown in alphabetical
  order.
- Search ignores letter case and finds a part of a word.

If a value is wrong, the assistant says what is wrong and changes
nothing, for example
`Invalid phone number 123. Use 10 digits, for example 0501234567.`

### Contacts

| Command | What it does | Example |
|---|---|---|
| `add <name> <phone>` | Adds a contact. If the contact exists, adds one more phone to it. | `add John 0501234567` |
| `all` | Shows all contacts. | `all` |
| `change <name> <old phone> <new phone>` | Replaces a phone of the contact. | `change John 0501234567 0671234567` |
| `remove-phone <name> <phone>` | Removes a phone of the contact. | `remove-phone John 0671234567` |
| `add-email <name> <email>` | Sets the email of the contact. | `add-email John john@example.com` |
| `add-address <name> <address>` | Sets the address of the contact. | `add-address John Kyiv, Khreshchatyk 1` |
| `add-birthday <name> <DD.MM.YYYY>` | Sets the birthday of the contact. | `add-birthday John 24.08.1991` |
| `birthdays <days>` | Shows the birthdays from today to the given number of days ahead (0 to 365). | `birthdays 7` |
| `find <text>` | Finds contacts by the name, the phones, the email, the address and the birthday. | `find kyiv` |
| `delete <name>` | Deletes the contact. | `delete John` |

### Editing a contact

| What to change | Command |
|---|---|
| a phone | `change <name> <old phone> <new phone>` or `remove-phone <name> <phone>` |
| the email | `add-email <name> <email>` again: the new email replaces the old one |
| the address | `add-address <name> <address>` again: the new address replaces the old one |
| the birthday | `add-birthday <name> <DD.MM.YYYY>` again: the new date replaces the old one |

### Notes

| Command | What it does | Example |
|---|---|---|
| `add-note <text>` | Adds a note and shows its number. | `add-note Buy milk and bread` |
| `all-notes` | Shows all notes with their numbers and tags. | `all-notes` |
| `change-note <id> <new text>` | Replaces the text of the note. | `change-note 1 Buy milk, bread and eggs` |
| `find-note <text>` | Finds notes by their text. | `find-note milk` |
| `add-tag <id> <tag> [tag...]` | Adds one or more tags to the note. | `add-tag 1 shop food` |
| `find-tag <tag>` | Shows the notes that have the tag. | `find-tag shop` |
| `sort-notes` | Shows all notes sorted by their tags; notes without tags go last. | `sort-notes` |
| `delete-note <id>` | Deletes the note. | `delete-note 1` |

### Example session

Today is 24.11.2026, so the birthday on 27.11 is 3 days ahead.

```text
Welcome to the assistant bot! Type 'help' to see all commands.
Enter a command: add John 0501234567
Contact added.
Enter a command: add-email John john@example.com
Email saved.
Enter a command: add-birthday John 27.11.1990
Birthday saved.
Enter a command: birthdays 7
27.11.2026 (Friday): John
Enter a command: add-note Buy a present for John
Note 1 added.
Enter a command: add-tag 1 shop birthday
Tags added to note 1.
Enter a command: find-tag birthday
1: Buy a present for John [birthday, shop]
Enter a command: find john
Contact name: John, phones: 0501234567, email: john@example.com, birthday: 27.11.1990
Enter a command: exit
Good bye!
```

### Your data

Everything is saved automatically after every command to the file
`data.pkl` in the folder `.personal_assistant` of your home folder
(for example `C:\Users\<you>\.personal_assistant\data.pkl` on Windows or
`~/.personal_assistant/data.pkl` on macOS and Linux). At the next start
your contacts and notes are there again. If the file is damaged, the
assistant keeps it as `data.pkl.bak` and starts with empty data.

## For the team

- [CONTRIBUTING.md](CONTRIBUTING.md): our rules and the git steps for
  every task.
- [docs/specs/00-overview.md](docs/specs/00-overview.md): how the parts
  fit together and the full list of commands.
- [docs/specs](docs/specs): one spec for every Trello card after the
  first one (the template).
