# Week 5 — Iteration and Algorithms (Mentor Summary)

## Key concepts taught
- **Three loop patterns** — counter (start at 0, increment on condition), accumulator (build up a total/list/string), and search (`for` + `break`, or `while`). Framed as a reusable mental toolkit: recognize the pattern, reach for the structure.
- **Nested loops** — inner loop runs fully per outer iteration; shown with a multiplication table (`end="\t"`) and lists-of-dicts. Explicitly capped at 2 levels for readability.
- **List comprehensions** — `[expr for item in iterable if cond]`. Taught as a shorter equivalent to accumulator loops, with side-by-side loop-vs-comprehension. Rule of thumb: if it doesn't fit on one line or takes >5 seconds to read, use a loop.
- **Search algorithms** — linear search (works on any list, returns index or `-1`) vs. binary search (requires sorted list, halves the search space, ~20 steps for 1M items). Step-by-step trace tables provided.
- **Selection sort & bubble sort** — selection: scan for the min of the unsorted portion, one swap per pass; bubble: swap adjacent out-of-order pairs, largest values "bubble" to the end. Both nested-loop, both contrasted against built-in `sort()`.
- **Built-ins vs. manual** — repeatedly stresses that `in`, `.index()`, `.sort()`, `sorted()`, `min()`, `max()` are the right choice for real code; manual implementations are for understanding mechanics only.
- **Debugging loops** — off-by-one (`range` bounds, `<` vs `<=`), infinite `while` loops (forgotten/wrong-direction update, `Ctrl+C` to stop), accumulator init bugs (wrong start value, reset inside loop, uninitialized list), mutating a list while iterating, and tracing via paper tables + labeled debug prints.

## The assignment — "Number Cruncher"
Students build a set of warmup scripts plus a menu-driven data tool. Work goes in `week-5/assignment-5/`; submit a PR link plus a video reflection link.

- **Part 1 — Warmups (4 separate files):** `warmup1.py` sum 1–100 with `for`/`range`; `warmup2.py` `while`-loop input validation for a positive integer (hint: `try`/`except` or `.isdigit()`); `warmup3.py` linear search over a name list, hand-rolled (no `.index()` / `in`); `warmup4.py` FizzBuzz 1–30 (check combined case first).
- **Part 2 — Mini-Project (`mini_project.py`):** copy a provided `numbers` list from `week-5/data/numbers.py`; `while`-loop menu with 5 options — min, max, linear search, sort, quit. Min/max/search must be hand-rolled (no `min()`/`max()`/`in`). Sort must be **bubble sort** (swap-until-no-swaps); pseudocode is provided. Menu redisplays until Quit.
- **Video reflection (3–5 min):** `for` vs `while` and when to choose each; walk through one algorithm implemented; describe a loop bug hit this week and how it was found/fixed.

## Likely trouble spots
- **Bubble sort termination** — lesson and assignment now both use the **swap-until-no-swaps** flag version (`swapped = False` at the top of each pass; repeat until a pass makes zero swaps). Sticking points: forgetting to reset `swapped = False` inside the loop (infinite loop), dropping the final zero-swap confirmation pass, or conflating bubble with selection sort.
- **`while`-loop input validation** — `warmup2` needs `try`/`except` or `.isdigit()`; note `.isdigit()` alone rejects negatives but also can't parse them, and returns False for non-numeric — students often mishandle the "hello" vs "-3" cases separately.
- **Off-by-one on sum/search** — `range(1, 101)` for 1–100 is a classic miss; also index vs value confusion in linear search (must report index).
- **Infinite menu / validation loops** — forgetting to update the loop variable or to `break`/exit on Quit; watch for menus that never re-prompt or never stop.
- **Bubble sort in place vs. returning** — mutating the shared `numbers` list across menu operations; some students sort a copy and the change doesn't persist.
- **Comprehension overreach** — after learning comprehensions, students force complex multi-condition logic into one line where a loop is clearer.
- **Manual-vs-built-in slip** — assignment explicitly forbids `min`/`max`/`.index()`/`in`/`sorted()`/`.sort()`; students reach for them reflexively.
- **List-mutation-while-iterating** — taught as a pitfall; may surface if students filter the numbers list during a menu operation.
