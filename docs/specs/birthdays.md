# Add birthday commands

| | |
|---|---|
| Card, commit and PR title | `Add birthday commands` |
| Branch | `feature/<card number>-birthdays` |
| Files | `personal_assistant/address_book.py`: `AddressBook.upcoming_birthdays`<br>`personal_assistant/commands/birthdays.py`: `add_birthday`, `birthdays` |
| Depends on | nothing |
| Covers | "store contacts with birthdays", "show the contacts whose birthday is in a given number of days from today" |

## What to build

Replace `raise NotImplementedError` in three bodies.

**`AddressBook.upcoming_birthdays(days)`** returns a list of
`(date, record)` pairs: the contacts whose next birthday is today or
within the next `days` days, with the date of that birthday.

- "Next birthday" is the birthday in this year or, if it has already
  passed, in the next year.
- Both ends count: `days = 0` is today only, `days = 7` is today and the
  seven days after it.
- A birthday on 29 February is celebrated on 1 March in a year that has
  no 29 February. `date.replace(year=...)` raises `ValueError` there:
  catch it, do not let it reach the user. The rule applies to the date
  in the next year too.
- Contacts without a birthday are skipped.
- The list is sorted by date: `result.sort(key=lambda pair: pair[0])`.
  Always give `key`: without it Python compares two records with the
  same date and crashes. Contacts with the same date stay in the order
  of the book.
- No new import is needed: `date.today()` gives today and
  `(birthday - today).days` is the number of days left.

**Commands, `commands/birthdays.py`**

| Function | Usage | Answer |
|---|---|---|
| `add_birthday` | `add-birthday <name> <DD.MM.YYYY>` | `Birthday saved.` |
| `birthdays` | `birthdays <days>` | one line per contact: `DD.MM.YYYY (Weekday): Name`, or `No birthdays in the next <days> days.` |

- `add_birthday` uses `Record.add_birthday`, which is ready; a new date
  replaces the old one.
- `<days>` must be a whole number from 0 to 365, otherwise the answer is
  `Days must be a number from 0 to 365.` Check it with `isdecimal()`
  before `int()`.
- In `No birthdays in the next <days> days.` print the number, not the
  typed text; the wording is the same for 0 and 1.
- The weekday is the English name from `date.strftime("%A")`.

## Check it

Start with empty data (overview, chapter 7).

Take a date whose day and month are three days from now, with a past
year (a future date is rejected once `Add field validation` is merged).
If today is 24.11.2026:

```text
Enter a command: add John 0501234567
Contact added.
Enter a command: add-birthday John 27.11.1990
Birthday saved.
Enter a command: add-birthday John 2026-11-27
Invalid date. Use DD.MM.YYYY, for example 24.08.1991.
Enter a command: birthdays 2
No birthdays in the next 2 days.
Enter a command: birthdays 3
27.11.2026 (Friday): John
Enter a command: add Bob 0671234567
Contact added.
Enter a command: add-birthday Bob 27.11.2001
Birthday saved.
Enter a command: birthdays 3
27.11.2026 (Friday): John
27.11.2026 (Friday): Bob
Enter a command: birthdays week
Days must be a number from 0 to 365.
Enter a command: birthdays 400
Days must be a number from 0 to 365.
Enter a command: birthdays
Usage: birthdays <days>
Enter a command: add-birthday Ann 01.01.2000
Contact Ann not found.
```

Also check:

- a birthday that was yesterday: it is not in `birthdays 300`, it is in
  `birthdays 365`;
- a birthday today: it is in `birthdays 0`;
- a contact born on `29.02.2000`: `birthdays 365` shows it with a real
  date and nothing crashes.

## Not in this task

Moving birthdays from weekends to Monday (that was the homework rule;
here we show the real date), ages, reminders.
