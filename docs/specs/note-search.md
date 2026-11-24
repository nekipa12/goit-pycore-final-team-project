# Add note search

| | |
|---|---|
| Card, commit and PR title | `Add note search` |
| Branch | `feature/<card number>-note-search` |
| Files | `personal_assistant/notebook.py`: `NoteBook.search`<br>`personal_assistant/commands/notes.py`: `find_notes` |
| Depends on | nothing |
| Covers | "search the notes" |

## What to build

Replace `raise NotImplementedError` in two bodies.

- `NoteBook.search(text)`: return the list of notes whose `note.text`
  contains `text`. Only the text is searched: not the ID and not the
  tags, so do not look in `str(note)`. Letter case is ignored, a part of
  a word is enough. The notes come in the order they have in the
  notebook (that is already the order of IDs: do not sort).
- `find_notes`, usage `find-note <text>`: every found note on its own
  line (`str(note)`), or `No notes found.`

The text may consist of several words: join all the arguments with a
space. The words are searched as one phrase.

## Check it

Start with empty data (overview, chapter 7).

```text
Enter a command: add-note Buy a present for John
Note 1 added.
Enter a command: add-note Call the bank
Note 2 added.
Enter a command: find-note BANK
2: Call the bank
Enter a command: find-note a present
1: Buy a present for John
Enter a command: find-note pizza
No notes found.
Enter a command: find-note 2
No notes found.
Enter a command: find-note
Usage: find-note <text>
```

## Not in this task

Search by tags (that is `find-tag` in the tags card), regular
expressions.
