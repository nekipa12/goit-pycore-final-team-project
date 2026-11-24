# Add note editing and deletion

| | |
|---|---|
| Card, commit and PR title | `Add note editing and deletion` |
| Branch | `feature/<card number>-note-editing` |
| Files | `personal_assistant/notebook.py`: `NoteBook.delete`<br>`personal_assistant/commands/notes.py`: `change_note`, `delete_note` |
| Depends on | nothing |
| Covers | "edit and delete notes" |

## What to build

Adding and showing notes is ready (`add-note`, `all-notes`,
`NoteBook.add`, `NoteBook.find`). Replace `raise NotImplementedError` in
three bodies.

- `NoteBook.delete(note_id)`: remove the note and return it. `note_id` is
  the text typed by the user; `self.find(note_id)` already checks it and
  answers `Note ID must be a number.` or `Note <id> not found.` The keys
  of the notebook are numbers, so delete by `note.id` of the found note.

| Function | Usage | Answer |
|---|---|---|
| `change_note` | `change-note <id> <new text>` | `Note <id> updated.` |
| `delete_note` | `delete-note <id>` | `Note <id> deleted.` |

- The new text is everything after the ID: join those arguments with a
  space. `change_note` puts it into `note.text` itself; `Note` gets no
  new method. The ID and the tags of the note do not change.
- `<id>` in an answer is `note.id`, not the typed text.
- A new note gets the biggest ID plus one, so the number of a deleted
  last note is given out again. That is expected: do not change
  `NoteBook.add`.

## Check it

Start with empty data (overview, chapter 7).

```text
Enter a command: add-note Buy a present for John
Note 1 added.
Enter a command: add-note Call the bank
Note 2 added.
Enter a command: change-note 2 Call the bank before 18:00
Note 2 updated.
Enter a command: all-notes
1: Buy a present for John
2: Call the bank before 18:00
Enter a command: change-note 02 Call the bank before 17:00
Note 2 updated.
Enter a command: change-note two New text
Note ID must be a number.
Enter a command: change-note 2
Usage: change-note <id> <new text>
Enter a command: delete-note 5
Note 5 not found.
Enter a command: delete-note 1
Note 1 deleted.
Enter a command: all-notes
2: Call the bank before 17:00
Enter a command: add-note One more
Note 3 added.
```

## Not in this task

Search (`find-note`) and tags: they have their own cards. Titles, dates,
confirmation questions.
