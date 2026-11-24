# Add help command

| | |
|---|---|
| Card, commit and PR title | `Add help command` |
| Branch | `feature/<card number>-help-command` |
| Files | `personal_assistant/commands/general.py`: `show_help` and the import line at the top |
| Depends on | nothing |
| Covers | criteria "convenient and logical command line", "the program offers the user to choose a command" |

## What to build

The function `show_help` in `commands/general.py` is declared, its body
is `raise NotImplementedError`. Replace the body.

`help` prints the list of all commands: what to type and what it does.
You do not write that list by hand. The assistant keeps all its commands
in the dictionary `COMMANDS` (file `personal_assistant/registry.py`). For
every command there is a pair: the function and the usage line. `help`
goes through this dictionary and builds the text.

Steps:

1. Change the existing import line at the top of the file so that it
   reads `from personal_assistant.registry import COMMANDS, command`.
   Do not add a second import line.
2. In `show_help` start the list of lines:
   `lines = ["Available commands:"]`
3. Write the loop exactly so:
   `for handler, usage in COMMANDS.values():`
   Every value is a pair: the function (`handler`) and its usage line.
4. Inside the loop take the description, which is the first line of the
   function's docstring, and add one line to the list:

   ```python
   description = handler.__doc__.splitlines()[0]
   lines.append(f"  {usage:<40}{description}")
   ```

   `{usage:<40}` prints the usage and then spaces up to 40 characters,
   so the descriptions stand in one column.
5. `exit` and `close` are not in `COMMANDS` (the main loop handles them),
   so add the last line yourself. After the loop write
   `usage = "exit, close"` and `description = "Leave the assistant."`,
   then repeat the `lines.append(...)` line from step 4.
6. Return all the lines joined into one text:
   `return "\n".join(lines)`. This `return` stands after the loop, at the
   same indentation as `for`.

## Check it

```text
Enter a command: help
Available commands:
  hello                                   Greet the user.
  help                                    Show this list of commands.
  add <name> <phone>                      Add a contact or one more phone to it.
  all                                     Show all contacts.
  change <name> <old phone> <new phone>   Replace a phone number.
  remove-phone <name> <phone>             Remove a phone number.
  delete <name>                           Delete a contact.
  add-email <name> <email>                Set or change the email.
  add-address <name> <address>            Set or change the address.
  find <text>                             Find contacts by any field.
  add-birthday <name> <DD.MM.YYYY>        Set or change the birthday.
  birthdays <days>                        Show birthdays in the coming days.
  add-note <text>                         Add a note.
  all-notes                               Show all notes.
  change-note <id> <new text>             Replace the text of a note.
  delete-note <id>                        Delete a note.
  find-note <text>                        Find notes by text.
  add-tag <id> <tag> [tag...]             Add tags to a note.
  find-tag <tag>                          Find notes by tag.
  sort-notes                              Show all notes sorted by tags.
  exit, close                             Leave the assistant.
```

The list is complete from the first day, because every command is
already declared. Some of them still answer
`This command is not implemented yet.`; that is fine, your teammates are
writing them.

If something goes wrong:

- `too many values to unpack`: `.values()` is missing in the loop line;
- only the first two lines are printed: `return` is inside the loop;
- the program does not start and prints `SyntaxError` or
  `IndentationError`: the last lines of that text name the line with the
  typo.

## Not in this task

Help for one command (`help add`), colours, grouping of commands.
