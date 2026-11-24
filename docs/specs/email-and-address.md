# Add email and address commands

| | |
|---|---|
| Card, commit and PR title | `Add email and address commands` |
| Branch | `feature/<card number>-email-and-address` |
| Files | `personal_assistant/commands/details.py`: `add_email`, `add_address` |
| Depends on | nothing |
| Covers | "store contacts with addresses and emails", "edit records" |

## What to build

The file `commands/details.py` already has two functions. Each one has a
line that starts with `@command` (the decorator), a text in triple
quotes (the docstring) and one more line: `raise NotImplementedError`.
Replace only that last line with real code, in both functions. Every new
line starts with 4 spaces, exactly under the docstring.

| Function | Usage | Answer |
|---|---|---|
| `add_email` | `add-email <name> <email>` | `Email saved.` |
| `add_address` | `add-address <name> <address>` | `Address saved.` |

`args` is the list of words typed after the command. For
`add-email John john@example.com` it is `["John", "john@example.com"]`,
so `args[0]` is the name and `args[1]` is the email.

`add_email` is three lines:

1. Find the contact: `record = book.find(args[0])`. If there is no such
   contact, `find` reports it by itself; you check nothing.
2. Give the email to the record: `record.add_email(args[1])`. The method
   is ready in `address_book.py`. A new value replaces the old one, so
   the same command changes an email.
3. Return the answer: `return "Email saved."`

`add_address` is the same with `record.add_address(...)` and its own
answer. One difference: an address has several words
(`Kyiv, Khreshchatyk 1`), and `args` holds them one by one:
`["John", "Kyiv,", "Khreshchatyk", "1"]`. Everything after the name is
the address. Glue it back with `" ".join(args[1:])` and give that text to
`record.add_address`.

A finished command of the same kind is `add_contact` in
`commands/contacts.py`. Only look at it; do not change that file.

## Check it

Start with empty data (overview, chapter 7). Without that a repeated run
answers `Phone 0501234567 already exists.` to the first command.

```text
Enter a command: add John 0501234567
Contact added.
Enter a command: add-email John john@example.com
Email saved.
Enter a command: add-address John Kyiv, Khreshchatyk 1
Address saved.
Enter a command: all
Contact name: John, phones: 0501234567, email: john@example.com, address: Kyiv, Khreshchatyk 1
Enter a command: add-email John john.smith@example.com
Email saved.
Enter a command: all
Contact name: John, phones: 0501234567, email: john.smith@example.com, address: Kyiv, Khreshchatyk 1
Enter a command: add-email Ann ann@example.com
Contact Ann not found.
Enter a command: add-email John
Usage: add-email <name> <email>
Enter a command: add-address John
Usage: add-address <name> <address>
```

If the program does not start and prints a long text with `SyntaxError`
or `IndentationError`, its last lines name the file and the line with
the typo. If a command prints `None`, the `return` line is missing.

A wrong email (`add-email John abc`) may still be accepted when you test.
Checking the value is another card, `Add field validation`. When it is
merged, the answer becomes
`Invalid email abc. Use the form name@example.com.` and your code does
not change.

## Not in this task

Checking the email yourself, removing an email or an address.
