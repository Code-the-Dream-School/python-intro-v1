# Assignment 3 Answer Key — Control Flow

## File Setup

- Work done in the forked `python-intro-homework` repo, on an `assignment-3` branch, inside `week-3/assignment-3/`.
- Each warmup and the mini-project is a **separate `.py` file**: `warmup1.py`, `warmup2.py`, `warmup3.py`, `warmup4.py`, `mini_project.py`.
- Submitted via a pull request from `assignment-3` into `main`. **URL1** = the PR link; URL2 = video (not assessed).

---

## Warmup 1: Letter Grades — **Objective**

Hardcoded `score`, `if`/`elif`/`else` chain printing the letter grade. Output for `score = 84`:

```
Score: 84
Grade: B
```

**Correct if:** branches are ordered so ranges don't overlap incorrectly — top-down (`>= 90`, `>= 80`, ...) or bottom-up (`< 60`, `< 70`, ...) both work as long as the order matches the direction of the comparison. Boundaries land right: 90→A, 80→B, 70→C, 60→D, below 60→F.
**Common miss:** wrong branch order (e.g. checking `>= 60` before `>= 90`, so everything above 60 prints D); using `if`/`if`/`if` instead of `elif` so multiple branches fire; off-by-one at the boundaries (89 → A).

## Warmup 2: Age Categories — **Objective**

`input()` → `int()`, then `if`/`elif`/`else` using `and` to bound the ranges. Output for `16`:

```
Enter your age: 16
You are a Teen.
```

**Correct if:** ranges are bounded with `and` (e.g. `age >= 13 and age <= 17`), categories map correctly (0–12 Child, 13–17 Teen, 18–64 Adult, 65+ Senior), and input is converted with `int()`.
**Common miss:** no `int()` (comparisons on a string); missing `and` so ranges are open-ended and overlap; boundary errors (12 → Teen, 65 → Adult).

## Warmup 3: Boolean Expression Practice — **Objective** (results) + **Subjective** (reasoning)

Prints five expressions with a `#` comment on each explaining *why*. Literal results:

```
False
True
False
False
True
```

**Correct if:** all five results match above (`not True and False`→False; `True or False and False`→True; `not (5 > 3)`→False; `10 == 10 and 4 != 4`→False; `not False or not True`→True), **and** each line carries a comment whose reasoning is sound. Check the precedence explanations: #2 must note `and` binds before `or`; #5 must note `not` applies to each operand first.
**Common miss:** correct output but missing/hand-wavy comments; reasoning that ignores precedence (e.g. reading #2 left-to-right as `(True or False) and False`→False — wrong result and wrong logic).

## Warmup 4: Sign and Parity — **Objective**

`input()` → number, then **two separate** `if`/`elif`/`else` blocks (one for sign, one for parity), printing two lines. Output for `-7` and `0`:

```
Enter a number: -7
-7 is negative.
-7 is odd.
```

```
Enter a number: 0
0 is zero.
0 is even.
```

**Correct if:** sign block treats `0` as its own case (positive / negative / zero — not folded into either), parity uses `% 2`, and the two decisions live in **two independent blocks** (not one combined chain).
**Common miss:** `0` reported as positive or negative instead of zero; a single merged if-chain instead of two; parity computed only for positives (negative odds like `-7` misclassified).

## Mini-Project: Day Planner — **Objective** (with subjective suggestions)

Asks for a day and a time of day, normalizes input, and prints an activity suggestion. Output shape:

```
What day is it? Tuesday
What time of day? morning
Suggestion: Morning Python class — great time to focus!
```

```
What day is it? blah
What time of day? morning
Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...
```

**Correct if:** at least **9 day×time combinations** (≥3 days × 3 times) with distinct suggestions; input case-normalized (`.lower()` so `"Monday"` and `"monday"` both match); and a fallback message for any unrecognized day or time.
**Common miss:** no `.lower()` (only exact capitalization matches); no fallback (unrecognized input prints nothing or crashes); fewer than 9 combinations or duplicated suggestions.
**Suggestions (subjective):** the specific activity text is the student's own — any sensible, distinct suggestions pass. Don't dock for wording or theme.
