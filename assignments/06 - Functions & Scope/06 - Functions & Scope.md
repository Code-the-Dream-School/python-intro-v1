# Assignment 6 — Functions & Scope

## Submission Instructions

1. **Create your branch:** From `main`, create a new `assignment-6` branch in your `python-intro-homework` repo.
2. **Create your folder:** Inside `week-6/`, create a new `assignment-6/` folder and do all your work there.
3. **Submit two links in CTD Learns:**
   - **URL1:** A link to your video reflection
   - **URL2:** A link to your pull request from `assignment-6` into `main`

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file.

---

### Warmup 1: Default Parameters

Write a function `greet(name, greeting="Hello")` that prints a greeting. Call it three different ways:

1. With only a name argument
2. With both a name and a custom greeting
3. With the greeting passed as a keyword argument

Expected output:
```
Hello, Alex!
Good morning, Alex!
Hello, Alex!
```

**Save as:** `warmup1.py`

---

### Warmup 2: Functions that Return Values

Write two functions:
- `celsius_to_fahrenheit(c)` — converts Celsius to Fahrenheit using `(c * 9/5) + 32`
- `fahrenheit_to_celsius(f)` — converts Fahrenheit to Celsius using `(f - 32) * 5/9`

Call each with a few test values and print the results. Use f-strings and round to one decimal place.

```
0°C = 32.0°F
100°C = 212.0°F
72°F = 22.2°C
```

**Save as:** `warmup2.py`

---

### Warmup 3: Scope in Action

Demonstrate variable scope with two short examples in one file:

1. Define a variable inside a function. Try to access it outside the function and show the `NameError` — paste the error in a comment, then remove or comment out the line that causes it.
2. Show how `return` solves the problem: return the value from the function and assign it to a variable in the outer scope. Print it to confirm it worked.

**Save as:** `warmup3.py`

---

### Warmup 4: Validation Function

Write a function `is_valid_score(score)` that returns `True` if `score` is an integer between 0 and 100 (inclusive), and `False` otherwise. Then use `input()` to ask the user for a score. Call your function inside an `if` statement and print either `"Valid score."` or `"Invalid score — must be between 0 and 100."`.

**Save as:** `warmup4.py`

---

## Part 2: Mini-Project — Refactor the Number Cruncher

Open your `mini_project.py` from Assignment 5. You're going to refactor it so that each operation lives in its own function.

**Create a new file** (don't modify your Week 5 submission). Pull a copy of the `numbers` list from `week-5/data/numbers.py` into your new script.

Define the following functions, each taking `numbers` (a list) as a parameter:

- `find_min(numbers)` — returns the minimum value (your loop-based implementation, no `min()`)
- `find_max(numbers)` — returns the maximum value (your loop-based implementation, no `max()`)
- `search(numbers, target)` — returns the index of `target`, or `-1` if not found
- `bubble_sort(numbers)` — returns a **new sorted list** (do not modify the original)
- `show_menu()` — prints the menu options and returns the user's choice as a string
- `main()` — the while loop that calls `show_menu()` and dispatches to the right function

Call `main()` at the bottom of the file.

**Requirements:**
- No logic should live outside of a function (except the `numbers` list definition and the `main()` call)
- `bubble_sort` should return a new list, not sort in place
- Your `search` function should print "Found at index X" or "Not found" from inside `main()`, not inside `search()` itself — `search` just returns the index

**Save as:** `mini_project.py`

> **Why revisit Week 5?** This is exactly how real software gets built — you write something that works, then return to make it cleaner and easier to change. Your git history now shows both versions, which is version control doing its job.

---

## Video Reflection

Record a short video (3–5 minutes) on YouTube, Loom, or a similar platform and share the link in your submission.

Your video should address the following questions. You don't need to cover every sub-point in depth — aim for clear, conversational explanations over a polished script.

1. What does `return` do — how is it different from `print()`?
2. Walk through one function you wrote: what are its inputs, what does it do, and what does it return?
3. Show a place where breaking your code into functions made it cleaner or easier to understand. How does this connect to why Git history is useful?

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
git checkout -b assignment-6
```

**As you work — save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin assignment-6  # send your branch to GitHub
```

You can repeat the `add → commit → push` steps as many times as you like within a week. Committing often gives you more points to return to if something goes wrong — you don't have to wait until you're finished.

**After your PR is merged on GitHub — close the loop:**

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```
