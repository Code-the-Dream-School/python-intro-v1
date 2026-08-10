# Assignment 4 Answer Key — Data Structures and Loops

## File Setup

- Forked `python-intro-homework` repo, `assignment-4` branch, all work inside `week-4/assignment-4/`.
- **Four separate files** (not one script): `warmup1.py`, `warmup2.py`, `warmup3.py`, `mini_project.py`.
- Submitted as a PR from `assignment-4` into `main`. **URL1** = the PR link; URL2 = video (not assessed).

---

## Warmup 1: List Operations — **Objective**

Hardcoded list of 8 numbers; four prints, **no loops**. Values differ per student; pattern:

```
First:   42
Last:    40
Middle:  [83, 5, 61, 29]
Reversed: [40, 86, 22, 59, 3, 78, 47, 14]
```

**Correct if:** first via `[0]`; last via a **negative index** (`[-1]`); middle is a 4-item slice of the center (`[2:6]` on an 8-item list); reverse via `[::-1]` or `reversed()`. No loops used.
**Common miss:** using `[7]` instead of `[-1]`; a middle slice that isn't the center four; reversing with a loop instead of a slice.

## Warmup 2: Dictionary Operations — **Objective**

Hardcoded student dict with `name`, `grade`, `subjects` (a list); iterate with `.items()`, add a key, reprint. Pattern:

```
name: Alex
grade: 11
subjects: ['Python', 'Math', 'Art']
graduated: False
```

**Correct if:** loop uses `.items()` to unpack key/value pairs; `"graduated"` added with value `False` (boolean, not the string `"False"`); updated dict printed and includes the new key.
**Common miss:** iterating keys only (`for k in d:`) instead of `.items()`; adding `"False"` as a string; printing before adding the key.

## Warmup 3: Set Operations — **Objective**

Two hardcoded language lists with partial overlap, converted to sets; print union, intersection, difference. Pattern (order within a set is not fixed):

```
Union:        {'Python', 'JavaScript', 'Go', 'Rust', 'C'}
Intersection: {'Python', 'JavaScript'}
Difference:   {'Go', 'Rust'}
```

**Correct if:** both lists converted with `set()`; union (`|` / `.union()`), intersection (`&` / `.intersection()`), and difference (`-` / `.difference()`) each correct. Difference is **first minus second**.
**Common miss:** reversing operands on the difference (second − first); using list logic instead of set operations; lists with no actual overlap so intersection is empty.

## Part 2: Mini-Project — Student Roster Analyzer — **Objective**

Copies the provided `students` list from `week-4/data/roster.py`, then computes four results with loops. Correct output for the shipped roster:

```
Top scorer:       Priya (95)
Class average:    81.25
Subjects offered: {'Python', 'Data', 'Web'}
High scorers:     ['Jazmine', 'Sara', 'Priya', 'Mia', 'Eli']
```

> **Two notes on the assignment's own example output** (it disagrees with the shipped data): it prints `Top scorer: Sara (91)`, but `roster.py` has **Priya at 95** — Priya is correct. It also shows `81.3`, but `650 / 8 = 81.25`; Python's `round(avg, 1)` and `f"{avg:.1f}"` both yield `81.2` (banker's rounding), not `81.3`. Accept `81.25`, `81.2`, or `81.3` — but the honest value is `81.25`.

**Correct if:**
- Top scorer found by a **manual loop** tracking highest score + name — **not** `max()` on the list.
- Class average accumulated in a loop then divided (rounding to one decimal is fine).
- Subjects collected into a **set** (deduped).
- High scorers built with a loop + `.append()`, threshold **strictly above 75**.

**Common miss:** calling `max(students, ...)` or `max()` on scores directly; averaging with `sum()`/`len()` only (acceptable for the divide, but the total must still come from a loop per the instructions); using a list instead of a set for subjects (duplicates remain); using `>= 75` instead of `> 75`.
