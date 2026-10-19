# Assignment 5 — Iteration & Algorithms

## Submission Instructions

1. **Make sure main is up to date:** 
      a. If your assignment last week was successful, be sure that you have merged your open Pull Request.  This will update the `main` branch with your `assignment-4` work so your main branch has a record of all your completed assignments to date. 
      b. In your terminal, use the `git pull origin main` command so your local `main` matches your GitHub `main`.
2. **Create your branch:** From `main`, create a new `assignment-5` branch in your `python-intro-homework` repo.
3. **Create your folder:** Inside `week-5/`, create a new `assignment-5/` folder and do all your work there.
4. **Submit two links in CTD Learns:**
   - **URL1:** A link to your pull request from `assignment-5` into `main`
   - **URL2:** A link to your video reflection

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file.

---

### Warmup 1: Sum with a For Loop

Use a `for` loop with `range()` to calculate the sum of all integers from 1 to 100. Print the result.

Example output — your message wording might differ:

```
The sum of 1 to 100 is 5050.
```

**Save as:** `warmup1.py`

---

### Warmup 2: Input Validation with a While Loop

Use a `while` loop that repeatedly asks the user to enter a positive integer. If the user enters anything that isn't a positive integer, print a message and ask again. Once valid input is received, print it and stop. The example session below shows the format — your inputs and message wording might differ:

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

Start with a hardcoded list of names. Ask the user to enter a name. Loop through the list and print whether the name was found and at what index — or a not-found message if it isn't in the list. The examples below show the format for two different searches — your names, index, and message wording might differ:

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

Build a menu-driven program using a `while` loop. Each time the menu displays, the user picks an option. The menu below shows the format — your wording and layout might differ, but all five options must be present:

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
4. **Sort** — implement **[bubble sort](https://www.w3schools.com/python/python_dsa_bubblesort.asp)**: repeatedly loop through adjacent pairs, swap if out of order, and repeat until no swaps occur. Print the sorted list. Do not use `sorted()` or `.sort()`.
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

Include the video link in the `URL2` field in the submission form.

---

## Review: The GitHub Cycle

This is your repeatable workflow for every assignment. Wherever you see `assignment-N`, replace `N` with the current assignment number (e.g. `assignment-5`) and use the same branch name in every command for that assignment. 

**Get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-N   # replace N: e.g. assignment-5
```

`origin` is your fork. `git pull origin main` syncs your local main with your fork on GitHub; it's normal to see "Already up to date."

**Save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin assignment-N  # send your branch to GitHub
```

Repeat `add → commit → push` as often as you like. Committing often gives you more points to return to if something goes wrong.

**Open your pull request:**

On GitHub, open a pull request from `assignment-N` into main. Confirm the base repository is your own fork (`your-username/python-intro-homework`), not `Code-the-Dream-School`.

**Submit your assignment:**

Use the button on the bottom of your lesson page to submit the link to your pull request.

**Close the loop:**

Assignment successful? You can merge your Pull Request.  

Assignment needs revisions?  Make your corrections on your local branch, and be sure to add, commit, and push them.  No need for a new pull request, when you push the changes your open pull request will reflect those new changes.  Resubmit your work the same way you first submitted - same pull request link too! - and you should see success.  

Problems?  Remember to connect with 1:1 mentors if you are experiencing any trouble with this GitHub Cycle.

Once you merge your pull request, be sure your local `main` branch also gets updated by running the following locally in your terminal:

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```

**If something looks off:**

* Committed to main by accident? (You forgot to create your branch first.) Make the branch now: `git checkout -b assignment-N` carries your latest commits with it, then continue. Your work isn't lost.
* `git push` says your branch has "no upstream"? You haven't pushed this branch before. Run `git push origin assignment-N` to create it on your fork.

---

<details>
<summary>Rubric (for AirHub reviewer and mentors)</summary>

### Required Deliverables/Tasks

Work happens in the student's forked `python-intro-homework` repo, on an
`assignment-5` branch, with files inside a `week-5/assignment-5/` folder.
`Example — adapt to your own layout`: the folder path and repo location are
organizational conventions — do NOT fail correct code for sitting in a different
folder or path; the reviewer cannot see the student's filesystem. Submission
mechanics (branch, PR base) are not graded from the code. This repo is
cumulative — folders from earlier weeks are expected to remain; do not tell the
student to remove prior-week work. Expected files: `warmup1.py`, `warmup2.py`,
`warmup3.py`, `warmup4.py`, `mini_project.py`.

- **Warmup 1 — Sum with a For Loop** — a `for` loop with `range()` that sums the
  integers 1 through 100 and prints the result. `Use exactly as written`: the sum
  is 5050. `Example — adapt to your own layout`: the message wording ("The sum of
  1 to 100 is 5050.") is the student's own.
- **Warmup 2 — Input Validation with a While Loop** — a `while` loop that keeps
  asking until it receives a positive integer, printing a message on invalid input
  and printing the value once valid. Required: non-numeric input is handled without
  crashing (`try`/`except` or `.isdigit()` — either is fine), and negatives and
  zero are rejected. `Example — adapt to your own layout`: the sample transcript
  (-3, hello, 7) and all prompt and message wording are the student's own — grade
  the behavior, not the strings.
- **Warmup 3 — Linear Search** — a hardcoded list of names; ask for a name; find
  it with the student's own loop, printing the index when found and a not-found
  message otherwise. Required: **no `.index()` and no `in` operator** — the search
  is written as a loop. `Example — adapt to your own layout`: the names (Marcus,
  Zara), the index (3), and the message wording all depend on the student's list.
- **Warmup 4 — FizzBuzz** — a loop from 1 to 30 printing one word per line:
  FizzBuzz for multiples of both 3 and 5, Fizz for 3 only, Buzz for 5 only, and
  the number itself otherwise. `Use exactly as written`: the strings `FizzBuzz`,
  `Fizz`, and `Buzz`. Required: the combined case is checked first, so 15 and 30
  print `FizzBuzz`.
- **Mini-Project — Number Cruncher (`mini_project.py`)** — the `numbers` list
  copied in from the provided `week-5/data/numbers.py`, then a `while`-loop menu
  with five options (1 minimum, 2 maximum, 3 search, 4 sort, 5 quit) that
  redisplays after each operation until the user quits. Required: **no `min()`, no
  `max()`, no `sorted()` and no `.sort()`** — the minimum and maximum are tracked
  in loops, the search is written as a linear search loop (`.index()` and the `in`
  operator are not allowed here either), and the sort is bubble sort (repeated
  passes over adjacent pairs, swapping, until a pass makes no swaps). The
  assignment states each of these constraints, so hold the line on them. `Example
  — adapt to your own layout`: the menu text and layout, the option wording, and
  all messages are the student's own, and the list's contents come from the
  provided data file — do not fail on specific values, on menu formatting, or on
  the data file's path (the reviewer cannot see the provided file or the student's
  filesystem).
- **Video reflection (URL2)** — a required submission, but it is not part of the
  code and is not assessed here. Do not fail the code submission for anything
  about the video.

### Optional Deliverables/Tasks

**None.**

</details>
