"""The main loop: reads a command, runs it and prints the answer."""

from personal_assistant import commands  # noqa: F401 (registers commands)
from personal_assistant.address_book import AddressBook
from personal_assistant.notebook import NoteBook
from personal_assistant.registry import COMMANDS
from personal_assistant.storage import load_data, save_data

try:
    # On macOS and Linux this makes the arrow keys work in input().
    import readline  # noqa: F401
except ImportError:
    # Windows has no such module: its console edits the line itself.
    pass

EXIT_COMMANDS = ("close", "exit")


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Split a line into the command (in lower case) and its arguments."""
    parts = user_input.split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]


def execute(
    command: str, args: list[str], book: AddressBook, notes: NoteBook
) -> str:
    """Run one command and return the text to show to the user."""
    if command not in COMMANDS:
        return "Unknown command. Type 'help' to see all commands."
    handler, usage = COMMANDS[command]
    if len(args) < usage.count("<"):
        return f"Usage: {usage}"
    try:
        return handler(args, book, notes)
    except NotImplementedError:
        # The command is declared, but its card is not merged yet.
        return "This command is not implemented yet."
    except ValueError as error:
        # The user's mistake: the message already says what is wrong.
        return str(error)
    except Exception as error:
        # A bug in one command must not close the whole program.
        return f"Unexpected error: {error!r}"


def main() -> None:
    """Run the assistant until the user types 'exit' or 'close'."""
    book, notes = load_data()
    print("Welcome to the assistant bot! Type 'help' to see all commands.")
    try:
        while True:
            command, args = parse_input(input("Enter a command: "))
            if not command:
                continue
            if command in EXIT_COMMANDS:
                break
            print(execute(command, args, book, notes))
            save_data(book, notes)
    except (EOFError, KeyboardInterrupt):
        # Ctrl+D or Ctrl+C: leave like 'exit'; the data is already saved.
        print()
    print("Good bye!")


if __name__ == "__main__":
    main()
