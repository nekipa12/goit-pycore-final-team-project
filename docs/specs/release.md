# Prepare release 1.0

| | |
|---|---|
| Card, commit and PR title | `Prepare release 1.0` |
| Branch | `feature/<card number>-release` |
| Files | `personal_assistant/main.py` (one `except` branch) and whatever the checks below show; normally `README.md` |
| Depends on | all the other cards are in `Done` |
| Covers | the final check against all acceptance criteria |

## What to do

The Team Lead's last card: make sure that the whole thing works as one
product, the way the mentor will check it.

1. **No stubs.** `NotImplementedError` is not found anywhere in
   `personal_assistant`. Then remove the `except NotImplementedError`
   branch from `execute()` in `main.py`: it was needed only while the
   commands were being written.
2. **Clean install.** In an empty folder outside the project:

   ```bash
   python -m venv check-env
   source check-env/bin/activate          # Windows: check-env\Scripts\activate
   pip install git+https://github.com/nekipa12/goit-pycore-final-team-project.git
   cd ~
   personal-assistant
   ```

   The assistant starts from any folder.
3. **All commands.** Go through the "Check it" part of every spec in
   this folder. Delete the data file before each one (overview,
   chapter 7). Include the second block of `contact-editing.md`: a wrong
   new phone must leave the contact as it was.
4. **Restart.** Leave with `exit`, start again: contacts and notes are
   still there. Do the same after closing the terminal window instead of
   `exit`.
5. **Bad input.** Empty line, unknown command, too few arguments, wrong
   phone, wrong email, wrong date, a note ID that is not a number,
   Ctrl+C: the program answers and keeps running (Ctrl+C says good bye).
   No answer starts with `Unexpected error`.
6. **README.** Every command from `help` is in the README and the other
   way round; the installation steps are the ones you have just done.
7. **Code.** `flake8 personal_assistant` reports nothing; every module,
   class and function has a docstring; no `print` for debugging or
   commented-out code is left.
8. **Repository.** It is public; `main` has one commit per card; there
   are no data files, virtual environments or editor folders in it.

Anything that fails goes back to the owner of that card as a comment, or
is fixed in the release branch if it is small.

## Done when

All eight points pass and the link to the repository is ready to be sent
to the mentor.
