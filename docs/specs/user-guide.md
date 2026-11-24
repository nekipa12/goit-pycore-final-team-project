# Write the user guide

| | |
|---|---|
| Card, commit and PR title | `Write the user guide` |
| Branch | `feature/<card number>-user-guide` |
| Files | `README.md`: only the chapter `## How to use` |
| Depends on | nothing |
| Covers | criterion "a detailed instruction on how to install and use the application in Readme.md" |

## What to build

`README.md` already tells how to install the assistant. Write the
chapter that tells how to use it: replace the two placeholder lines under
`## How to use`. Do not touch the chapters above and below it. Write for
a person who sees the program for the first time.

The chapter has these parts, in this order. Make every part a `###`
heading.

1. **Start and exit**: how to start (`personal-assistant`; if it was
   installed into a virtual environment, that environment must be
   active), what the prompt looks like, how to leave (`exit` or `close`),
   and a small table of the general commands `hello`, `help`,
   `exit` / `close`.
2. **Rules of input**, as a short list:
   - a command is typed in one line: the command, then its values,
     separated by spaces; extra words at the end are ignored;
   - a name is one word, and letter case matters (`John` and `john` are
     two contacts);
   - a phone is 10 digits, e.g. `0501234567`;
   - a date is `DD.MM.YYYY`, e.g. `24.08.1991`; a birthday is a date from
     01.01.1900 to today;
   - an email looks like `name@example.com`;
   - an address and a note text may have several words;
   - a note is addressed by its number, which `all-notes` shows;
   - a tag is one word and is kept in lower case;
   - search ignores letter case and finds a part of a word.
3. **Contacts**: a table with three columns: the command, what it does,
   an example. One row for every contact command. Say that
   `birthdays <days>` shows the birthdays from today to the given number
   of days ahead (0 to 365), and that `find` looks into the name, the
   phones, the email, the address and the birthday.
4. **Editing a contact**: a small table "what to change / command":
   a phone (`change`, `remove-phone`), the email (`add-email` again),
   the address (`add-address` again), the birthday (`add-birthday`
   again).
5. **Notes**: the same kind of table as for contacts, for the note and
   tag commands. Say that `sort-notes` puts the notes without tags last.
6. **Example session**: 15-20 lines that show a typical use: add a
   contact, give it an email and a birthday, look at the upcoming
   birthdays, add a note with a tag, find it.
7. **Your data**: everything is saved automatically after every command
   to the file `data.pkl` in the folder `.personal_assistant` of the
   user's home folder; the data is there again at the next start; a
   damaged file is kept as `data.pkl.bak`.

How to write it:

- All commands, their usage lines and their answers are fixed in
  [00-overview.md](00-overview.md), chapter 6. The same list is in the
  "Check it" part of [help-command.md](help-command.md). Do not describe
  commands that are not there.
- You do not have to wait for the other cards. Most commands do not work
  in your branch yet, so write the example session by hand from the
  answers in chapter 6. Say above it which day is "today", because
  `birthdays` depends on it: on 24.11.2026 a contact born on 27.11.1990
  gives `27.11.2026 (Friday): John` for `birthdays 7`.
- In the tables put `delete` and `delete-note` last and choose examples
  that work when typed one after another.
- A table row looks like
  ``| `add <name> <phone>` | Adds a contact. | `add John 0501234567` |``
  under a header row and a `|---|---|---|` row. Put every command in
  backticks, otherwise GitHub hides the words in angle brackets.

## Check it

- Before the commit look at the preview in your editor (VS Code:
  Ctrl+Shift+V). After the push open `README.md` on GitHub in your
  branch: the tables and the code blocks are drawn correctly.
- Every command from chapter 6 of the overview is in your tables, with
  the same usage line.
- The examples use correct values: 10-digit phones, `DD.MM.YYYY` dates.

The comparison of the README with the finished program is a step of the
card `Prepare release 1.0`.

## Not in this task

The installation chapter (it is ready), changing the code.
