# Week 4 — Data Structures and Loops (Mentor Summary)

## Key concepts taught

- **Mutable vs. immutable** — framed up front (clay vs. fired ceramic) as the single distinction that drives list-vs-tuple choice.
- **Lists** — square brackets, zero-based and negative indexing, item reassignment; methods `append`, `remove`, `sort`, `pop`, `insert`, and `len()` (flagged as a function, not a method).
- **Slicing** — `list[start:end]` (start inclusive, end exclusive), open ends, negative slices; noted that slicing returns a *new* list.
- **Tuples** — parentheses, immutable, index access, unpacking (`w, h = dims`); "when in doubt use a list."
- **Dictionaries** — key-value pairs, `[]` access (raises `KeyError`) vs. `get()` (returns `None`/default), add/update by assignment, `del` and `pop()`; methods `keys()`, `values()`, `items()` (items returns tuples — bridge to looping).
- **Sets** — unordered, unique-only; empty set is `set()` not `{}`; `add()`, `union`, `intersection`, `difference`; used for dedup and fast membership.
- **for loops** — over sequences and strings; `range(stop)`, `range(start, stop)`, `range(start, stop, step)`, counting backwards.
- **while loops** — condition-driven; the `count += 1` / infinite-loop warning (`Ctrl+C`); input-validation and `while True` + `break` menu patterns.
- **break / continue** — exit vs. skip-iteration.
- **Looping structured data** — `enumerate()`; filter / accumulate / transform patterns; three ways to loop a dict (keys, `.values()`, `.items()`); **list of dictionaries** framed as tabular data and explicitly previewed for Weeks 7 (CSV), 9 (API), and the final project.
- **Choosing a structure** — recurring comparison tables (ordered? mutable? duplicates? key-value?).

## The assignment — "Core Data Structures"

Normal Git workflow: `assignment-4` branch, `week-4/assignment-4/` folder, submit PR link + video reflection link in CTD Learns. Assignment reprints the full GitHub cycle as a reference at the bottom.

- **Part 1 — three warmups, separate files.** `warmup1.py`: list indexing/slicing/reverse, no loops. `warmup2.py`: student dict (incl. a `subjects` list), loop with `.items()`, add a key. `warmup3.py`: two lists → sets → union/intersection/difference.
- **Part 2 — `mini_project.py`, "Student Roster Analyzer."** Copy a provided `students` list (dicts with `name`, `score`, `subject`) from `week-4/data/roster.py`. Must: find top scorer (loop-tracked — **`max()` on the list explicitly disallowed**), compute class average by accumulation, collect unique subjects into a set, and append names of students scoring above 75.
- **Video reflection (3–5 min):** list vs. dict tradeoff, walk through the manual top-scorer loop, and what was confusing about nested data.

## Likely trouble spots

- **Manual top-scorer loop** — the assignment bans `max()`, so students must hand-roll the max-tracking pattern (init a best score + name, compare each iteration). Common bug: not updating both variables together, or initializing badly.
- **`{}` is a dict, not a set** — empty-set gotcha called out in the lesson; watch for it in warmup3.
- **`[]`/`KeyError` vs. `.get()`** — students reach for bracket access and crash on missing keys.
- **Nested access `books[0]["title"]`** — index-then-key on lists of dicts is the week's conceptual peak; the reflection question implies it's expected to confuse.
- **Slicing off-by-one / new-list** — end-exclusive slicing and the fact that slices don't mutate the original.
- **Infinite `while`** — forgotten increment / bad termination condition.
- **Set unordered-ness** — output order not guaranteed; students may expect a fixed order (and the example roster output shows a set literal whose order they shouldn't try to match exactly).
- **Deferred / not yet taught:** returning tuples from functions and tuple unpacking as return values (Week 6); reading lists-of-dicts from CSV (Week 7) and APIs (Week 9); list comprehensions are *not* introduced — all filter/transform work is explicit loops + `.append()`.
