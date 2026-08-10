# Assignment 5 Answer Key — Iteration and Algorithms

## File Setup

- Forked `python-intro-homework` repo, `assignment-5` branch, work inside `week-5/assignment-5/`.
- Submitted as a PR from `assignment-5` into `main`. **URL1** = the PR link; URL2 = video (not assessed).
- Separate `.py` files: `warmup1.py`, `warmup2.py`, `warmup3.py`, `warmup4.py`, plus `mini_project.py`.
- The mini-project copies the provided `numbers` list from `week-5/data/numbers.py` into the script — expect the list pasted near the top.

---

## Warmup 1: Sum with a For Loop — **Objective**

For loop over `range()` summing integers 1–100.

```
The sum of 1 to 100 is 5050.
```

**Correct if:** total is `5050`, produced by a loop (e.g. `for n in range(1, 101): total += n`).
**Common miss:** `range(1, 100)` (off-by-one — stops at 99, gives 4950) or `range(100)` (0–99). Only `range(1, 101)` is correct.

## Warmup 2: Input Validation with a While Loop — **Objective**

`while` loop that re-prompts until a positive integer is entered, then reports it and stops.

```
Enter a positive integer: -3
That's not a positive integer. Try again.
Enter a positive integer: hello
That's not a positive integer. Try again.
Enter a positive integer: 7
Got it: 7
```

**Correct if:** the loop repeats on bad input and exits only on a valid positive integer; non-numeric input (`hello`) is handled without crashing — via `try`/`except` or `str.isdigit()`.
**Common miss:** no guard against non-numeric text → `ValueError` crash; accepting `0` or negatives as valid; validating only once instead of looping.

## Warmup 3: Linear Search — **Objective**

Hardcoded list of names; prompt for a name; hand-rolled loop reports found index or "not found."

```
Enter a name to search for: Marcus
Found "Marcus" at index 3.
```

```
Enter a name to search for: Zara
"Zara" was not found in the list.
```

**Correct if:** the search is a manual loop (e.g. `for i in range(len(names))` comparing `names[i]`), reporting the index on a match and a not-found message otherwise.
**Common miss:** using `.index()` or the `in` operator — the assignment forbids both; flag as a correctness issue. Also watch for printing "not found" inside the loop on every mismatch instead of once after the loop ends.

## Warmup 4: FizzBuzz — **Objective**

Loop 1–30, one word per line, combined case checked first.

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
```

**Correct if:** divisible-by-both check (`n % 3 == 0 and n % 5 == 0` → `FizzBuzz`) comes before the individual checks; range is 1–30 inclusive (`range(1, 31)`).
**Common miss:** checking `% 3` or `% 5` first, so 15/30 print `Fizz`/`Buzz` instead of `FizzBuzz`; off-by-one range stopping at 29.

## Mini-Project: Number Cruncher — **Objective** (with subjective menu formatting)

Menu-driven `while` loop over the provided `numbers` list; redisplays until Quit.

```
=== Number Cruncher ===
1. Find minimum
2. Find maximum
3. Search for a number
4. Sort the list
5. Quit
Choose an option (1-5):
```

Each option must be **hand-rolled** — the assignment forbids `min()`, `max()`, `.index()`, `in`, `sorted()`, and `.sort()`:

1. **Minimum** — loop tracking the smallest value seen.
2. **Maximum** — loop tracking the largest value seen.
3. **Search** — prompt for a number, linear-search loop, print index or a not-found message.
4. **Sort** — **bubble sort** using the swap-until-no-swaps flag: `swapped = False` per pass, set `True` on each swap, repeat until a pass makes zero swaps. Print the sorted list.
5. **Quit** — goodbye message, exit the loop.

**With the shipped `numbers` list** (`week-5/data/numbers.py`): min = `3`, max = `93`, and sorted ascending:

```
[3, 5, 8, 14, 17, 22, 29, 31, 40, 42, 47, 55, 59, 61, 66, 74, 78, 83, 86, 93]
```

**Correct if:** all five options work; min/max/search/sort are implemented manually; sort is bubble sort with the `swapped` flag terminating the passes; the menu reappears after each operation and exits only on Quit.
**Common miss (flag as correctness issue):** any banned built-in (`min`, `max`, `.index()`, `in`, `sorted`, `.sort()`); a sort that isn't bubble sort (e.g. selection sort or a fixed pass count instead of the swap-flag loop). Also watch for a menu that doesn't loop back, or option-3 search reusing the forbidden `in`.
**Menu formatting (subjective):** exact banner/spacing is free — accept any readable layout; only invalid-choice handling and clean redisplay matter.
