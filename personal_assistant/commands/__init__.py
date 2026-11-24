"""Command handlers. Importing this package registers all the commands.

The modules are listed in the order in which ``help`` shows the commands.
"""

from personal_assistant.commands import (  # noqa: F401
    general,
    contacts,
    details,
    search,
    birthdays,
    notes,
    tags,
)
