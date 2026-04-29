# Assignment 5 — Iteration & Algorithms

## Submission Instructions

1. **Create your branch:** From `main`, create a new `assignment-5` branch in your `python-intro-homework` repo.
2. **Create your folder:** Inside `week-5/`, create a new `assignment-5/` folder and do all your work there.
3. **Submit two links in CTD Learns:**
   - **URL1:** A link to your video reflection
   - **URL2:** A link to your pull request from `assignment-5` into `main`

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file.

---

### Warmup 1: Sum with a For Loop

Use a `for` loop with `range()` to calculate the sum of all integers from 1 to 100. Print the result.

```
The sum of 1 to 100 is 5050.
```

**Save as:** `warmup1.py`

---

### Warmup 2: Input Validation with a While Loop

Use a `while` loop that repeatedly asks the user to enter a positive integer. If the user enters anything that isn't a positive integer, print a message and ask again. Once valid input is received, print it and stop:

```
Enter a positive integer: -3
That's not a positive integer. Try again.
Enter a positive integer: hello
That's not a positive integer. Try again.
Enter a positive integer: 7
Got it: 7
```

> **Hint:** You'll need `try`/`except` to handle non-numeric input — or you can check `str.isdigit()`.

**Save as:** `warmup2.py`

---

### Warmup 3: Linear Search

Start with a hardcoded list of names. Ask the user to enter a name. Loop through the list and print whether the name was found and at what index — or "Not found" if it isn't in the list:

```
Enter a name to search for: Marcus
Found "Marcus" at index 3.
```

```
Enter a name to search for: Zara
"Zara" was not found in the list.
```

Do not use Python's `.index()` method or the `in` operator — implement the search yourself with a loop.

**Save as:** `warmup3.py`

---

### Warmup 4: FizzBuzz

Loop from 1 to 30 and print one word per line:
- `"FizzBuzz"` if the number is divisible by both 3 and 5
- `"Fizz"` if divisible by 3 only
- `"Buzz"` if divisible by 5 only
- The number itself otherwise

Check the combined case first.

**Save as:** `warmup4.py`

---

## Part 2: Mini-Project — Number Cruncher

A data file is provided in `week-5/data/numbers.py`. Copy the `numbers` list from that file into your script.

Build a menu-driven program using a `while` loop. Each time the menu displays, the user picks an option:

```
=== Number Cruncher ===
1. Find minimum
2. Find maximum
3. Search for a number
4. Sort the list
5. Quit
Choose an option (1-5):
```

**Requirements for each option:**

1. **Find minimum** — loop through the list and track the smallest value. Do not use Python's built-in `min()`.
2. **Find maximum** — same approach, tracking the largest value. Do not use `max()`.
3. **Search** — ask the user for a number, then implement a linear search loop. Print the index if found, or a "not found" message.
4. **Sort** — implement **bubble sort**: repeatedly loop through adjacent pairs, swap if out of order, and repeat until no swaps occur. Print the sorted list. Do not use `sorted()` or `.sort()`.
5. **Quit** — print a goodbye message and exit the loop.

The menu should redisplay after each operation until the user chooses Quit.

> **Bubble sort hint:** One pass through the list looks at pairs — `numbers[i]` and `numbers[i+1]` — and swaps them if the first is larger. You need to repeat this process until a full pass produces zero swaps.
>
> Pseudocode:
> ```
> repeat:
>     swapped = False
>     for each adjacent pair:
>         if left > right:
>             swap them
>             swapped = True
> until swapped is False
> ```

**Save as:** `mini_project.py`

---

## Video Reflection

Record a short video (3–5 minutes) on YouTube, Loom, or a similar platform and share the link in your submission.

Your video should address the following questions. You don't need to cover every sub-point in depth — aim for clear, conversational explanations over a polished script.

1. Explain the difference between a `for` loop and a `while` loop. When would you choose one over the other?
2. Walk through one of the sorting or searching algorithms you implemented. Explain how it works step by step — without just reading the code aloud.
3. Describe a bug you hit in a loop this week. How did you find it and fix it?

**Requirements:**
- Keep it to 3–5 minutes
- Use screen sharing to walk through your code when relevant
- Speak in your own words — no need to read from a script

Include the video link in your pull request description or the `URL1` field in the submission form.

---

## Review: The GitHub Cycle

**At the start of each week — get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-5
```

**As you work — save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin assignment-5  # send your branch to GitHub
```

You can repeat the `add → commit → push` steps as many times as you like within a week. Committing often gives you more points to return to if something goes wrong — you don't have to wait until you're finished.

**After your PR is merged on GitHub — close the loop:**

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```
