# Personal Assistant

A command-line assistant that keeps your contacts and notes. You type a
command, the assistant answers.

It can:

- keep contacts with phones, an email, an address and a birthday;
- check phone numbers and emails when you enter them;
- find, change and delete contacts;
- show whose birthday is in the coming days;
- keep text notes, find, change and delete them;
- mark notes with tags, find and sort notes by tags;
- save everything to your home folder, so nothing is lost between runs.

This is the final team project of the GoIT course "Python Programming:
Foundations and Best Practices".

## How to install

You need Python 3.10 or newer. The assistant uses only the Python
standard library. On macOS and Linux type `python3` instead of `python`.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install git+https://github.com/nekipa12/goit-pycore-final-team-project.git
```

While this virtual environment is active, the command
`personal-assistant` works from any folder:

```bash
personal-assistant
```

To install from a copy of the repository instead, create and activate
the virtual environment as above, then:

```bash
git clone https://github.com/nekipa12/goit-pycore-final-team-project.git
cd goit-pycore-final-team-project
pip install .
```

## How to use

This chapter is written in the card "Write the user guide".
Until then the list of commands is in `docs/specs/00-overview.md`.

## For the team

- [CONTRIBUTING.md](CONTRIBUTING.md): our rules and the git steps for
  every task.
- [docs/specs/00-overview.md](docs/specs/00-overview.md): how the parts
  fit together and the full list of commands.
- [docs/specs](docs/specs): one spec for every Trello card after the
  first one (the template).
