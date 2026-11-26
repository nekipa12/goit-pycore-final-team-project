"""General commands: the greeting and the list of commands."""

from personal_assistant.registry import COMMANDS, command


@command("hello")
def hello(args, book, notes):
    """Greet the user."""
    return "How can I help you?"


@command("help")
def show_help(args, book, notes):
    """Show this list of commands."""
    lines = ["Available commands:"]
    for handler, usage in COMMANDS.values():
        description = handler.__doc__.splitlines()[0]
        lines.append(f"  {usage:<40}{description}")
    usage = "exit, close"
    description = "Leave the assistant."
    lines.append(f"  {usage:<40}{description}")
    return "\n".join(lines)
