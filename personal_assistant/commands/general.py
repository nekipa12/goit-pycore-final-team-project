"""General commands: the greeting and the list of commands."""

from personal_assistant.registry import command


@command("hello")
def hello(args, book, notes):
    """Greet the user."""
    return "How can I help you?"


@command("help")
def show_help(args, book, notes):
    """Show this list of commands."""
    raise NotImplementedError
