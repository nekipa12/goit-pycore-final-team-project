# How we work

Short rules for the team. Every Trello card repeats the ones that matter
for that task.

## Rules

1. **Nobody commits to `main`.** Every task is done in its own branch and
   gets into `main` only through a Pull Request (PR).
2. **One card = one branch = one PR.**
3. **Branch name** comes from the Trello card number:
   `feature/<card number>-<short-name>`. The exact name is written in the
   card.
4. **Commit message and PR title = the card title**, word for word.
5. **Change only the files and functions listed in your card.** Do not
   rename, move or reformat other code: that is what causes merge
   conflicts.
6. **Everyone reviews everyone.** A PR needs at least one approval and
   must have no merge conflicts. The card names the reviewer who answers
   first; anybody else is welcome too.
7. **Only the Team Lead merges PRs**, with "Squash and merge": `main`
   gets one commit per card, named by the card title.
8. **Keep Trello up to date** (see below).

## Trello

| List | The card is here when |
|---|---|
| Todo | nobody has started the task |
| In Progress | you have started: move the card yourself |
| Code Review | the PR is open: move the card and paste the PR link into it |
| Done | the Team Lead has merged the PR: the Team Lead moves the card |

## Step by step

Text in `<...>` is a placeholder: type the real name without the angle
brackets. Your card has the exact names.

### Once

1. Check Python: it must be 3.10 or newer.

   ```bash
   python --version
   ```

   On macOS and Linux type `python3` wherever our documents say `python`.
2. Tell git who you are (use the email of your GitHub account):

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

3. Accept the invitation to the repository (GitHub sends it by email).
4. Get the project and start it:

   ```bash
   git clone https://github.com/nekipa12/goit-pycore-final-team-project.git
   cd goit-pycore-final-team-project
   python -m personal_assistant
   ```

   The last command starts the assistant from the source code. Type
   `exit` to leave it. There is nothing else to install.

Run every command of this guide in the project folder. While you work on
the project, always start the assistant with `python -m personal_assistant`:
the installed command `personal-assistant` runs the installed copy and
does not see your changes.

### For every task

1. Move the card to **In Progress**.
2. Start from fresh `main` and create the branch named in the card:

   ```bash
   git checkout main
   git pull
   git status
   git checkout -b feature/<card number>-<short-name>
   ```

   Before the last command `git status` must say `On branch main` and
   `nothing to commit`.
3. Write the code described in the spec. Then delete the old data,
   start the assistant again and go through the "Check it" part of the
   spec (how: `docs/specs/00-overview.md`, chapter 7).
4. Look at what you changed. Only the files from your card may be
   listed, and all changed lines must be inside your functions:

   ```bash
   git status
   git diff
   ```

5. Commit and push. The message is the card title. Add files by name,
   not with `git add .`:

   ```bash
   git add <the files from your card>
   git commit -m "<card title>"
   git push -u origin feature/<card number>-<short-name>
   ```

   The first push asks you to sign in to GitHub: do it in the browser
   window that opens.
6. Open the PR on GitHub: base branch `main`, title = the card title.
   In the description say what you did and how to check it. Ask the
   reviewer from the card (and anybody else) for a review.
7. Move the card to **Code Review** and paste the PR link into it.
8. If a reviewer asks for changes: fix them in the same branch, then
   `git add`, `git commit -m "<card title>"`, `git push` again. The PR
   updates itself.
9. After the Team Lead has merged the PR, the branch is finished: do not
   use it again. Get the new `main`:

   ```bash
   git checkout main
   git pull
   ```

### If `main` has changed or GitHub shows a conflict

Bring `main` into your branch and push again. We merge, we do not rebase.

```bash
git checkout feature/<card number>-<short-name>
git pull --no-rebase --no-edit origin main
git push
```

If git reports a conflict, open the file, keep the right lines, delete
the `<<<<<<<`, `=======` and `>>>>>>>` markers, then:

```bash
git add <the fixed files>
git commit --no-edit
git push
```

Always create a branch from `main`, never from another feature branch.

### Reviewing

- A review request comes before your own task: the author is waiting.
- Put your unfinished work aside (`git stash`), get the branch
  (`git fetch`, then `git checkout <branch>`), run the "Check it" part of
  the spec and read the code against the spec. Then go back:
  `git checkout <your branch>` and `git stash pop`.
- Approve when it does what the spec says and nothing more.

### If something strange happens

The assistant keeps its data in the folder `.personal_assistant` of your
home folder, one for all branches. If the program reports an odd error
right after you switched branches, delete that folder and start again:

```bash
rm -r ~/.personal_assistant
```

## Code

- Everything is in English: names, comments, docstrings, messages.
- PEP 8, lines up to 79 characters. The Team Lead checks it with flake8
  before merging; you can do it yourself: `pip install flake8`, then
  `flake8 personal_assistant` must print nothing.
- Every module, class and function has a docstring.
- Only the Python standard library and only what we studied in the course.
- A mistake of the user is reported with `raise ValueError("clear text")`:
  the main loop prints the text and the program goes on.
- Check first, change after: if a command fails, the data stays exactly
  as it was.
- How a command is written and the full list of commands:
  `docs/specs/00-overview.md`.
