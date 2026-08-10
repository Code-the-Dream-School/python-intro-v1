# Assignment 6 Answer Key — Functions and Scope

## File Setup

- Forked `python-intro-homework` repo → `assignment-6` branch off `main` → all work in `week-6/assignment-6/` → PR into `main`. **URL1** = PR link; URL2 = video (not assessed).
- Expected files in `week-6/assignment-6/`: `warmup1.py`, `warmup2.py`, `warmup3.py`, `warmup4.py`, `mini_project.py`.
- Video reflection is NOT graded. Grade code only.

---

## Warmup 1: Default Parameters — `warmup1.py` — **Objective**

`greet(name, greeting="Hello")` prints, called three ways (positional-only, custom greeting, greeting as keyword).

Expected output:
```
Hello, Alex!
Good morning, Alex!
Hello, Alex!
```

**Correct if:** `greeting` has default `"Hello"`; three calls produce the three lines above; the third call uses keyword syntax, e.g. `greet("Alex", greeting="Hello")`.
**Common miss:** Keyword-argument call syntax is barely shown in the lessons — expect the third call to be a plain positional call (`greet("Alex", "Hello")`) instead of `greeting="Hello"`. Output looks identical, so read the source, not just the output. Also watch for `print` inside the function vs. returning the string.

---

## Warmup 2: Functions that Return Values — `warmup2.py` — **Objective**

`celsius_to_fahrenheit(c)` returns `(c * 9/5) + 32`; `fahrenheit_to_celsius(f)` returns `(f - 32) * 5/9`. Called with test values, printed via f-strings rounded to 1 decimal.

Expected output (using the assignment's sample values):
```
0°C = 32.0°F
100°C = 212.0°F
72°F = 22.2°C
```

**Correct if:** Both functions `return` (not `print`) the result; caller formats with `:.1f` (or `round(..., 1)`); values match.
**Common miss:** Function prints internally instead of returning, so f-string rounding is done wrong or not at all. Missing the `.0` / one-decimal formatting.

---

## Warmup 3: Scope in Action — `warmup3.py` — **Subjective (hybrid)**

- Part 1: a variable is defined inside a function; the outside access that raised `NameError` is shown/pasted in a comment, then the offending line is removed or commented out (file must still run cleanly).
- Part 2: the same value is `return`ed, assigned in the outer scope, and printed to prove it works.
- Correct if the file runs without error and clearly demonstrates the local-vs-returned contrast; exact wording of the pasted `NameError` doesn't matter.

---

## Warmup 4: Validation Function — `warmup4.py` — **Objective (logic) / hybrid (uses input)**

`is_valid_score(score)` returns `True` only when `score` is an int in `0..100` inclusive, else `False`. Program reads `input()`, calls the function in an `if`, and prints one of the two messages.

Expected messages (exact strings):
```
Valid score.
Invalid score — must be between 0 and 100.
```

**Correct if:** Function `return`s a boolean (not prints); range is inclusive on both ends; `input()` is converted to `int` before the check; both branches print the correct message. No fixed output — output depends on user input.
**Common miss:** Comparing a raw string from `input()` (never converting to `int`); exclusive bounds (`> 0 and < 100`); function prints instead of returning; the int-check requirement is dropped (e.g. accepting `50.5`). An `int()` conversion that crashes on non-numeric input is acceptable at this level.

---

## Part 2: Mini-Project — Refactor the Number Cruncher — `mini_project.py` — **Subjective (hybrid)**

Refactor of the Week 5 script into functions, each taking `numbers` as a parameter where noted:

- `find_min(numbers)` — returns min via a loop (no `min()`)
- `find_max(numbers)` — returns max via a loop (no `max()`)
- `search(numbers, target)` — returns index of `target`, or `-1` if not found (must NOT print)
- `bubble_sort(numbers)` — returns a NEW sorted list; original unchanged
- `show_menu()` — prints options, returns the user's choice as a string
- `main()` — while loop calling `show_menu()` and dispatching to each function
- `main()` called at the bottom of the file

**Correct if:**
- No logic lives outside a function except the `numbers` list definition and the `main()` call.
- `find_min`/`find_max` are loop-based (no built-in `min()`/`max()`).
- `search` returns the index and `-1`; the "Found at index X" / "Not found" printing happens in `main()`, not inside `search`.
- `bubble_sort` returns a new list and leaves the input unmodified (e.g. copies before sorting) — verify by checking `numbers` is unchanged after a sort.

**Common miss:** `bubble_sort` sorts in place and returns `None` (or returns the same mutated list); `search` prints its result instead of returning; using `min()`/`max()`; stray top-level logic (input handling outside `main()`); calling `main()` inside an `if __name__ == "__main__":` guard is fine and better — the assignment only requires it be called at the bottom.
