# Defensive Programming Patterns

**Objective**: By the end of this lesson, you will be able to:
  * Describe what defensive programming means and why it matters
  * Validate inputs at the start of a function before using them
  * Use guard clauses to return early when a precondition is not met
  * Check for `None` and empty values before accessing them
  * Explain why silently swallowing exceptions is dangerous
  * Use `assert` to check assumptions during development

---

## What Is Defensive Programming?

Error handling (last lesson) is about *reacting* to problems after they occur. Defensive programming is about *anticipating* problems before they happen.

The difference:
- **Reactive:** "Something went wrong — let me handle it."
- **Defensive:** "This might go wrong — let me check first."

Writing defensively means assuming that the data coming into your function might be wrong, missing, or unexpected — and writing code that fails clearly rather than silently, or produces confusing results.

---

## Input Validation

The most common form of defensive programming is **checking inputs at the start of a function** before doing anything with them.

Consider a function that calculates a percentage:

```python
# Fragile version — no validation
def calculate_percentage(value, total):
    return (value / total) * 100
```

This will crash with `ZeroDivisionError` if `total` is `0`, and produce a confusing `TypeError` if either argument is a string. A defensive version checks first:

```python
# Defensive version
def calculate_percentage(value, total):
    if not isinstance(value, (int, float)):
        raise TypeError(f"value must be a number, got {type(value).__name__}")
    if not isinstance(total, (int, float)):
        raise TypeError(f"total must be a number, got {type(total).__name__}")
    if total == 0:
        raise ValueError("total cannot be zero")
    return (value / total) * 100
```

The defensive version fails immediately with a clear, specific message instead of producing a confusing error several lines later.

Common things to validate:
- Is the value the right type?
- Is a number within a valid range?
- Is a string non-empty when it needs to be?
- Does a list have at least one item before you access the first one?

---

## Guard Clauses

A **guard clause** is an early `return` at the top of a function that exits immediately when a precondition is not met. This keeps the main logic of your function unindented and easy to read.

Without guard clauses (nested):

```python
def process_order(order):
    if order is not None:
        if order["quantity"] > 0:
            if order["price"] > 0:
                total = order["quantity"] * order["price"]
                print(f"Order total: ${total:.2f}")
            else:
                print("Invalid price.")
        else:
            print("Quantity must be greater than zero.")
    else:
        print("No order provided.")
```

With guard clauses (flat):

```python
def process_order(order):
    if order is None:
        print("No order provided.")
        return
    if order["quantity"] <= 0:
        print("Quantity must be greater than zero.")
        return
    if order["price"] <= 0:
        print("Invalid price.")
        return

    total = order["quantity"] * order["price"]
    print(f"Order total: ${total:.2f}")
```

Both versions do the same thing. The second is easier to read: each failure condition is handled at the top with a clear message and an immediate return. The main logic runs at the end without any nesting.

The pattern: **check conditions early, return fast, keep the happy path at the bottom.**

---

## Handling `None`

Functions don't always return a value. When a function can't find what it's looking for, returning `None` is often the right choice — but you have to handle it on the receiving end.

```python
def find_user(users, name):
    for user in users:
        if user["name"] == name:
            return user
    return None   # user not found
```

If you call `find_user()` without checking the result, you get a `TypeError` when you try to use the return value:

```python
user = find_user(users, "Alex")
print(user["email"])   # TypeError: 'NoneType' object is not subscriptable
```

Always check for `None` before using a value that might be it:

```python
user = find_user(users, "Alex")
if user is None:
    print("User not found.")
else:
    print(user["email"])
```

This is especially important when working with API responses — which you will in Week 9 — because failed requests and missing data often surface as `None`.

---

## Failing Loudly vs. Silently

**Silent failure** is when your code catches an error and does nothing:

```python
# Silent failure — dangerous
try:
    data = load_data("config.json")
except Exception:
    pass   # nothing happens
```

The program continues running as if everything is fine, but `data` was never assigned. The next time something tries to use `data`, it crashes — far from where the original problem happened, with a confusing error.

**Loud failure** tells you clearly what went wrong:

```python
# Loud failure — informative
try:
    data = load_data("config.json")
except FileNotFoundError as e:
    print(f"Could not load config: {e}")
    return
```

The rule: **never use `except: pass` or `except Exception: pass` in real code.** If you catch an exception, do something with it — print a message, log it, return a default value, or re-raise it. Silently swallowing errors makes bugs very difficult to find.

---

## `assert` for Development Checks

`assert` is a lightweight way to verify assumptions while you're building a program. If the condition is `False`, Python raises an `AssertionError` immediately:

```python
def calculate_average(numbers):
    assert len(numbers) > 0, "numbers list cannot be empty"
    return sum(numbers) / len(numbers)
```

`assert` is best for catching **programmer mistakes** — wrong assumptions about how your own code works — rather than bad user input. For user-facing validation, use explicit `if/raise` checks as shown above.

One important note: `assert` statements can be disabled when running Python with the `-O` (optimize) flag. Don't use them for checks that must always run in production.

---

### AI Prompt: Scaffold Removal

Try writing a defensive version of this function on your own:

```python
def get_first_item(items):
    return items[0]
```

This crashes if `items` is `None`, if it's empty, or if it's not a list at all. Your goal:
1. Add guard clauses for `None` and an empty list
2. Return a meaningful message or `None` in each failure case

Then try it:

```python
print(get_first_item(None))     # should not crash
print(get_first_item([]))       # should not crash
print(get_first_item([42, 7]))  # should return 42
```

If you get stuck, ask an AI chatbot:

> "I'm learning guard clauses in Python. My function `get_first_item(items)` crashes when `items` is None or empty. Can you give me two hints for how to add guard clauses — without giving me the solution?"

---

## Videos

**"LBYL vs EAFP: Preventing or Handling Errors in Python"** (Real Python)

[Watch the video](https://youtu.be/TotBLX6rQw8?si=DJPhm7RmyeaQRhL6) — covers two competing philosophies for handling errors in Python: Look Before You Leap (defensive checking) vs. Easier to Ask Forgiveness than Permission (try/except). 

---

## Check for Understanding

**Question 1:** What is the main difference between error handling (try/except) and defensive programming?

* A) Error handling uses `try/except`; defensive programming uses `assert`
* B) Error handling reacts to problems after they occur; defensive programming anticipates and prevents them
* C) Error handling is for beginners; defensive programming is for advanced developers
* D) They are the same thing with different names

<details>
<summary>Answer</summary>

**B) Error handling reacts to problems after they occur; defensive programming anticipates and prevents them** — `try/except` catches an error that already happened. Defensive programming (input validation, guard clauses, None checking) stops you from getting there in the first place by checking conditions before running risky code. Both techniques are used together.

</details>

**Question 2:** What is a guard clause?

* A) A `try/except` block that prevents all errors
* B) An early `return` at the top of a function that exits when a precondition is not met
* C) A variable that stores the last error message
* D) A comment that explains what a function expects as input

<details>
<summary>Answer</summary>

**B) An early `return` at the top of a function that exits when a precondition is not met** — Guard clauses check each failure condition at the top and return immediately if something is wrong. This keeps the main logic unindented and readable, avoiding deeply nested if/else chains.

</details>

**Question 3:** A function returns `None` when a user is not found. What happens if you write `user["email"]` without checking for `None` first?

* A) Python returns an empty string
* B) Python skips the line silently
* C) Python raises a `TypeError` because `None` cannot be subscripted
* D) Python raises a `KeyError`

<details>
<summary>Answer</summary>

**C) Python raises a `TypeError` because `None` cannot be subscripted** — `None["email"]` raises `TypeError: 'NoneType' object is not subscriptable`. Always check `if user is None:` before using a value that might be `None`, especially from functions that return `None` on failure.

</details>

**Question 4:** Why is `except Exception: pass` considered dangerous?

* A) It only catches `ValueError` and misses other errors
* B) It crashes the program immediately
* C) It silently hides errors, making bugs very hard to find later
* D) It causes an infinite loop

<details>
<summary>Answer</summary>

**C) It silently hides errors, making bugs very hard to find later** — When you catch an exception and do nothing, the program continues in a broken state. The bug may not surface until much later, with a confusing error far from the original problem. Always do something with a caught exception: log it, print a message, return a default value, or re-raise it.

</details>

**Question 5:** When should you use `assert` instead of an explicit `if/raise` check?

* A) For validating user input in production code
* B) For security-critical checks that must always run
* C) For checking programmer assumptions during development
* D) Whenever you want to print a helpful error message

<details>
<summary>Answer</summary>

**C) For checking programmer assumptions during development** — `assert` is a development tool: it flags impossible states that shouldn't happen if your code logic is correct. For user-facing validation (handling bad input), use explicit `if/raise` because `assert` can be disabled with the `-O` flag and won't protect users in production.

</details>

---

## Further Reading

- [Real Python — Python's assert: Debug and Test Your Code Like a Pro](https://realpython.com/python-assert-statement/)
- [Real Python — LBYL vs EAFP: Preventing or Handling Errors in Python](https://realpython.com/python-lbyl-vs-eafp/)
- [PEP 8 — Programming Recommendations](https://peps.python.org/pep-0008/#programming-recommendations)
