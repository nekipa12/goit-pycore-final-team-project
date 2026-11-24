# Add note tags

| | |
|---|---|
| Card, commit and PR title | `Add note tags` |
| Branch | `feature/<card number>-note-tags` |
| Files | `personal_assistant/notebook.py`: `Note.add_tags`, `NoteBook.find_by_tag`, `NoteBook.sorted_by_tags`<br>`personal_assistant/commands/tags.py`: `add_tag`, `find_tag`, `sort_notes` |
| Depends on | nothing |
| Covers | the extra task: "add tags to notes", "search and sort notes by tags" |

## What to build

Replace `raise NotImplementedError` in six bodies.

A tag is one word. Tags are kept in `note.tags` in lower case, without
duplicates, in alphabetical order. `str(note)` already prints them.

**Model, `notebook.py`**

- `Note.add_tags(tags)` gets the words as typed (`args[1:]`). For every
  word it removes commas at the ends (`tag.strip(",")`: people type
  `work, home`) and makes it lower case. It skips an empty tag and a tag
  the note already has (also one typed twice in the same command), and
  sorts `self.tags` at the end. The command does none of this itself.
- `NoteBook.find_by_tag(tag)`: the notes that have this tag. The whole
  tag must be equal, letter case is ignored. Commas are not removed
  here: `find-tag` takes one tag. The notes come in the order they have
  in the notebook: do not sort.
- `NoteBook.sorted_by_tags()`: a new list of all notes ordered by their
  lists of tags. Lists are compared the way Python compares lists: by
  the first tag, then by the second, and so on, so `[home]` goes before
  `[home, money]`. Notes without tags go last. Notes with equal lists
  keep the order of IDs (`sorted()` does not swap equal items).
  Hint: `key=lambda note: (not note.tags, note.tags)`.

**Commands, `commands/tags.py`**

| Function | Usage | Answer |
|---|---|---|
| `add_tag` | `add-tag <id> <tag> [tag...]` | `Tags added to note <id>.` |
| `find_tag` | `find-tag <tag>` | every found note on its own line, or `No notes with tag <tag>.` |
| `sort_notes` | `sort-notes` | all notes sorted by tags, each on its own line, or `No notes saved yet.` |

- The note is found with `notes.find(args[0])`, which already answers
  for a wrong ID. `<id>` in the answer is `note.id`.
- The answer of `add-tag` is the same when the note already had some or
  all of the tags.
- `<tag>` in `No notes with tag <tag>.` is the tag in lower case.

## Check it

Start with empty data (overview, chapter 7).

```text
Enter a command: sort-notes
No notes saved yet.
Enter a command: add-note Buy a present for John
Note 1 added.
Enter a command: add-note Call the bank
Note 2 added.
Enter a command: add-note Pay for the internet
Note 3 added.
Enter a command: add-tag 1 Shop birthday
Tags added to note 1.
Enter a command: add-tag 3 money
Tags added to note 3.
Enter a command: add-tag 3 money, home, HOME
Tags added to note 3.
Enter a command: all-notes
1: Buy a present for John [birthday, shop]
2: Call the bank
3: Pay for the internet [home, money]
Enter a command: find-tag SHOP
1: Buy a present for John [birthday, shop]
Enter a command: find-tag WORK
No notes with tag work.
Enter a command: sort-notes
1: Buy a present for John [birthday, shop]
3: Pay for the internet [home, money]
2: Call the bank
Enter a command: add-tag 2 alpha
Tags added to note 2.
Enter a command: add-note Water the flowers
Note 4 added.
Enter a command: add-tag 4 home
Tags added to note 4.
Enter a command: sort-notes
2: Call the bank [alpha]
1: Buy a present for John [birthday, shop]
4: Water the flowers [home]
3: Pay for the internet [home, money]
Enter a command: add-tag 9 x
Note 9 not found.
Enter a command: add-tag abc x
Note ID must be a number.
Enter a command: add-tag 1
Usage: add-tag <id> <tag> [tag...]
```

## Not in this task

Removing or renaming tags, checking the characters of a tag (any word is
a tag), a special alphabet for tags that are not English (plain `sort()`
is enough), tags for contacts, a list of all tags, search by several
tags at once.
