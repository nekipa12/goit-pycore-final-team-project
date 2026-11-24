# Add field validation

| | |
|---|---|
| Card, commit and PR title | `Add field validation` |
| Branch | `feature/<card number>-field-validation` |
| Files | `personal_assistant/fields.py` |
| Depends on | nothing |
| Covers | "check the phone number and the email when a record is created or edited"; criterion "correct validation for every field" |

## What to build

At the moment the field classes accept any text (only `Birthday` checks
that the date is real). Make each of the five classes of the table check
its value in `__init__`, the way `Phone` and `Birthday`
did in the homework, and raise `ValueError` with the message from the
table when the value is wrong.

| Class | The value is correct when | Message |
|---|---|---|
| `Name` | it has at least one letter: `any(char.isalpha() for char in value)` | `Name must have at least one letter.` |
| `Phone` | it is exactly 10 characters `0`-`9`: `re.fullmatch(r"[0-9]{10}", value)` | `Invalid phone number <value>. Use 10 digits, for example 0501234567.` |
| `Email` | the whole value matches `EMAIL_PATTERN` (below) | `Invalid email <value>. Use the form name@example.com.` |
| `Address` | it has at least one character that is not a space | `Address cannot be empty.` |
| `Birthday` | it is a real date `DD.MM.YYYY` | `Invalid date. Use DD.MM.YYYY, for example 24.08.1991.` (ready in the base, do not change) |
| `Birthday` | the date is from 01.01.1900 to today, both included | `Birthday must be between 01.01.1900 and today.` |

- `str.isdigit()` is not enough for a phone: it is also true for `²`.
- Keep the email pattern in a constant at the top of the file, otherwise
  the line does not fit into 79 characters. You also need `import re`
  and `date` from `datetime`.

  ```python
  EMAIL_PATTERN = (
      r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
  )
  ```

- Fields check, they do not change: `Name`, `Phone`, `Email` and
  `Address` store the value exactly as it was given (`Birthday` keeps a
  `date`, as in the base).
- An empty address cannot come from the command line (an argument is
  never empty); this check protects the class itself.

Nothing else changes: the class names, `value` and `__str__` stay as they
are, so the rest of the project does not notice anything except the new
errors. A value is checked both when a contact is created and when it is
edited, because both go through these classes. Values saved before this
card are not checked again.

## Check it

Start with empty data (overview, chapter 7).

```text
Enter a command: add John 12345
Invalid phone number 12345. Use 10 digits, for example 0501234567.
Enter a command: add John 05012345ab
Invalid phone number 05012345ab. Use 10 digits, for example 0501234567.
Enter a command: add 0501234567 John
Name must have at least one letter.
Enter a command: add John 0501234567
Contact added.
Enter a command: all
Contact name: John, phones: 0501234567
```

Try the other classes in the Python console (`python` in the project
folder). The console prints a `Traceback` block before every error; only
its last line is shown here.

```python
>>> from personal_assistant.fields import Address, Birthday, Email, Name
>>> Email("john@example.com").value
'john@example.com'
>>> Email("john@example")        # also: "john", "@example.com", "a b@c.de"
ValueError: Invalid email john@example. Use the form name@example.com.
>>> Birthday("31.02.2000")
ValueError: Invalid date. Use DD.MM.YYYY, for example 24.08.1991.
>>> Birthday("01.01.2999")
ValueError: Birthday must be between 01.01.1900 and today.
>>> Birthday("31.12.1899")
ValueError: Birthday must be between 01.01.1900 and today.
>>> str(Birthday("01.01.1900"))
'01.01.1900'
>>> Name("123")
ValueError: Name must have at least one letter.
>>> Address("   ")
ValueError: Address cannot be empty.
```

## Not in this task

Phone formats other than 10 digits, length limits, new fields.
