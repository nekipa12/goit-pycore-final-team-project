"""The table of commands that the assistant understands.

A handler adds itself to the table with the ``@command`` decorator, so no
file has to list all the commands by hand.
"""

COMMANDS = {}


def command(usage: str):
    """Register the decorated function as the handler of a command.

    ``usage`` is the line shown to the user, for example
    ``"change <name> <old phone> <new phone>"``. Its first word is the
    command name and every ``<word>`` is a required argument.
    """

    def register(handler):
        """Put the handler into the table and return it unchanged."""
        COMMANDS[usage.split()[0]] = (handler, usage)
        return handler

    return register
