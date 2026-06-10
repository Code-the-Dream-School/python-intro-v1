# Writing Code That Fails Gracefully

**Objective**: By the end of this lesson, you will be able to:
  * Explain the difference between crashing and graceful degradation
  * Wrap risky operations in `try/except` with specific exception types
  * Return a meaningful fallback value when something goes wrong
  * Print a user-friendly error message instead of letting Python crash
  * Use `logging` to record errors in a structured way
  * Apply these patterns to refactor a script from an earlier week

---

## Crashing vs. Graceful Degradation

So far in this course, when something went wrong your program crashed: Python printed a traceback and stopped. That's fine during development — the traceback tells you exactly what happened.

But programs that run for real users need to handle failure differently. A program that crashes on unexpected input or a missing file is not a finished program.

**Crashing** (unhandled exception):

```python
def load_scores(filename):
    with open(filename, "r") as f:
        return f.read()

scores = load_scores("scores.txt")   # FileNotFoundError if file is missing
print(scores)
```

If `scores.txt` doesn't exist, the program crashes immediately. The user sees a raw Python traceback.

**Graceful degradation** (handled exception):

```python
def load_scores(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Could not find '{filename}'. Starting with no scores.")
        return ""

scores = load_scores("scores.txt")
print(scores)
```

Now the program catches the error, tells the user what happened in plain language, and continues with a safe default value. The user never sees a traceback.

---

## Wrapping Risky Operations

Any time your program does something that depends on the outside world, you should treat it as risky. The two most common risky operations at this stage of the course:

1. **Reading a file** — the file might not exist, might be unreadable, or might be in an unexpected format
2. **Making a network request** — the server might be unreachable, or might return an error (you'll use this pattern extensively in Week 9)

The general pattern:

```python
try:
    # risky operation here
except SpecificError as e:
    # handle it here
```

For file reading, the most common exceptions to handle are:

| Exception | What caused it |
|-----------|----------------|
| `FileNotFoundError` | The file path doesn't exist |
| `PermissionError` | The file exists but can't be read |
| `IsADirectoryError` | The path points to a folder, not a file |

You can catch multiple exceptions in one block:

```python
try:
    with open(filename, "r") as f:
        content = f.read()
except (FileNotFoundError, PermissionError) as e:
    print(f"Could not read file: {e}")
    content = ""
```

---

## Meaningful Fallback Behavior

When something goes wrong, you have three options:

1. **Return a safe default value** (empty list, empty string, `0`, `None`) and let the caller continue
2. **Print a user-friendly message** and stop that operation
3. **Re-raise the exception** to let the caller decide what to do

Which one is right depends on context. For functions that return data, returning a safe default is usually the most useful approach:

```python
def read_student_list(filename):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Warning: '{filename}' not found. Using empty list.")
        return []
```

A function that returns `[]` on failure is much easier to work with than one that sometimes crashes. The caller can always check `if students:` before proceeding:

```python
students = read_student_list("students.txt")
if not students:
    print("No students to process.")
else:
    for student in students:
        print(student)
```

---

## A Complete Worked Example

Here's a realistic pattern: reading a CSV file, handling failure gracefully, and returning clean structured data.

```python
import csv

def load_grades(filename):
    try:
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"Could not find '{filename}'.")
        return []
    except csv.Error as e:
        print(f"Could not parse '{filename}': {e}")
        return []

def print_grades(grades):
    if not grades:
        print("No grade data available.")
        return
    for row in grades:
        print(f"{row['name']}: {row['grade']}")

if __name__ == "__main__":
    grades = load_grades("grades.csv")
    print_grades(grades)
```

Notice the structure:
- `load_grades()` handles all the risky work and always returns a list — either with data, or empty
- `print_grades()` checks for the empty case before doing anything
- Neither function crashes regardless of what happens to the file

This separation — one function owns the risky work, another owns the display — is the same pattern you'll use for API calls in Week 9.

---

## Using `logging` for Errors

In the last lesson you learned what `logging` is. Here's how it fits into graceful failure: instead of (or in addition to) printing a message, log it. This is especially useful in longer programs where you want to track what went wrong without cluttering the user-facing output.

```python
import logging

logging.basicConfig(level=logging.WARNING)

def load_grades(filename):
    try:
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return []
```

With `level=logging.WARNING`, this ERROR message will appear in the console during development. In a larger program, you might send it to a log file instead of the screen — the logging module supports that with a few extra lines of configuration.

The key idea: **use `print()` for messages the user needs to see; use `logging` for messages developers need to see.**

---

### AI Prompt: Retrieval Practice

Before moving on, close this lesson and answer these questions from memory:

1. What is the difference between crashing and graceful degradation?
2. What are two risky operations that should always be wrapped in `try/except`?
3. If a function is supposed to return a list, what should it return when something goes wrong?

Then open your preferred AI chatbot and share your answers:

> "I'm learning to write Python code that fails gracefully. Here's what I remember about the key ideas: [your answers]. What did I get right? What should I add or clarify?"

---

## Applying These Patterns: Refactoring

One of the best ways to practice graceful failure is to go back to code you've already written and make it more robust. Think about a script from Week 7 that reads a file.

Before (fragile):

```python
with open("products.txt", "r") as f:
    for line in f:
        name, price = line.strip().split(",")
        print(f"{name}: ${price}")
```

After (graceful):

```python
def load_products(filename):
    try:
        with open(filename, "r") as f:
            products = []
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    products.append({"name": parts[0], "price": parts[1]})
                else:
                    logging.warning(f"Skipping malformed line: {line.strip()}")
            return products
    except FileNotFoundError:
        print(f"Could not find '{filename}'.")
        return []

products = load_products("products.txt")
for p in products:
    print(f"{p['name']}: ${p['price']}")
```

The refactored version:
- Wraps the file read in `try/except`
- Skips malformed lines instead of crashing on them
- Returns an empty list on failure
- Separates the data-loading logic from the display logic

This kind of refactoring — taking working-but-fragile code and making it robust — is a skill you'll use throughout your programming career.

---

## Videos

**"Python Tutorial: File Objects - Reading and Writing to Files"** (Corey Schafer)

[Watch the video](https://youtu.be/Uh2ebFW8OYM?si=mGHJ7pcDWIGewcMn) — includes handling `FileNotFoundError` and working safely with file operations. Search YouTube for the title above.

---

## Check for Understanding

**Question 1:** What is graceful degradation?

* A) Making your program run faster by removing unnecessary code
* B) Handling an exception so the program can continue with a safe fallback instead of crashing
* C) Printing a traceback to the user when something goes wrong
* D) Ignoring all errors with `except: pass`

<details>
<summary>Answer</summary>

**B) Handling an exception so the program can continue with a safe fallback instead of crashing** — Graceful degradation means the program catches a failure, tells the user or developer what happened in clear language, and continues (or exits cleanly) instead of crashing with a raw Python traceback.

</details>

**Question 2:** A function is supposed to return a list of records read from a file. What should it return if the file is not found?

* A) `None`
* B) `False`
* C) `[]` (an empty list)
* D) It should crash so the caller knows something went wrong

<details>
<summary>Answer</summary>

**C) `[]` (an empty list)** — Returning an empty list is the most useful fallback because the caller can always check `if records:` before processing. It also means the caller's code doesn't need a special case for `None`. Returning `None` requires the caller to handle two different types (`None` or `list`), which is messier.

</details>

**Question 3:** Which two operations are most commonly wrapped in `try/except` at this stage of the course?

* A) Loops and list comprehensions
* B) File reads and network requests
* C) Variable assignments and print statements
* D) Function definitions and return statements

<details>
<summary>Answer</summary>

**B) File reads and network requests** — Both depend on the outside world and can fail for reasons outside your control (missing file, network error, server error). Both should be wrapped in `try/except` with specific exception types.

</details>

**Question 4:** When is it better to use `logging.error()` rather than `print()` for an error message?

* A) When you want the message to be visible to the user
* B) When the error is in a loop
* C) When you want to record what went wrong for developers, not display it to the user
* D) `logging.error()` and `print()` are identical

<details>
<summary>Answer</summary>

**C) When you want to record what went wrong for developers, not display it to the user** — `print()` always shows output to the user; `logging` gives you control over what's shown and when. You can suppress DEBUG and INFO messages in production while keeping ERROR messages, or redirect all log output to a file. Use `print()` for user-facing messages and `logging` for developer-facing ones.

</details>

**Question 5:** What is wrong with this code?

```python
def get_config(filename):
    try:
        with open(filename) as f:
            return f.read()
    except Exception:
        pass
```

* A) `open()` is not the right function for reading files
* B) The `try` block should be outside the function
* C) The function silently returns `None` on failure, hiding the error
* D) Nothing — this is a good pattern for handling file errors

<details>
<summary>Answer</summary>

**C) The function silently returns `None` on failure, hiding the error** — `except Exception: pass` swallows the error and lets the function return `None` implicitly. The caller has no idea anything went wrong. A better version would catch a specific exception, log or print a message, and return a safe default like an empty string — so the caller knows what happened and gets a usable value.

</details>

---

## Further Reading

- [Python Documentation — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python — Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)
- [Real Python — Reading and Writing Files in Python](https://realpython.com/read-write-files-python/)
- [Python Documentation — logging — Logging facility for Python](https://docs.python.org/3/library/logging.html)
