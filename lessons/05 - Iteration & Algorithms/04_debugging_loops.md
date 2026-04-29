# Debugging Loops

> **Source:** New content (builds on print-statement debugging approach from Week 1 / PE 1.7)
>
> **Notes:** Students now encounter a new class of bugs specific to iteration. Cover the most common loop bugs with concrete examples of each:
> - **Off-by-one errors:** `range(n)` vs. `range(1, n+1)`; `<` vs. `<=`
> - **Infinite loops:** forgetting to update the loop variable in a `while` loop
> - **Wrong accumulator initialization:** starting a sum at 1 instead of 0
> - **Mutating a list while iterating over it** (brief mention of why this is dangerous)
> Strategy: insert `print(f"i={i}, value={value}")` inside loops to trace state. Encourage students to trace loops on paper before running.

TBD
