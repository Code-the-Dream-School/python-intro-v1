# try/except and Common Runtime Errors

**Objective**: By the end of this lesson, you will be able to:
  * Explain the difference between a syntax error and a runtime error
  * Use `try` and `except` to catch a specific exception by name
  * Use the `as e` syntax to inspect what went wrong
  * Use the `else` block to run code only when no exception occurred
  * Use `finally` for cleanup that must always run
  * Raise your own exceptions with `raise`
  * Name the most common Python runtime exceptions and what causes them
  * Use the `logging` module to record what your program is doing

---

## Two Kinds of Errors

Before we talk about handling errors, it helps to understand that Python errors come in two types.

**Syntax errors** happen before your program runs. Python reads your code and finds something it can't understand — a missing colon, mismatched parentheses, an unexpected indent. The program never starts.

```python
if x > 5
    print("big")   # SyntaxError: expected ':'
```

**Runtime errors** happen while your program is running. The code starts, but something goes wrong mid-execution — a user enters unexpected input, a file doesn't exist, a calculation produces an impossible result. Python calls these **exceptions**.

```python
number = int("hello")   # ValueError: invalid literal for int() with base 10: 'hello'
```

This week is about runtime errors: writing code that catches exceptions and responds clearly instead of crashing.

---

## Common Runtime Exceptions

Here are the exceptions you will encounter most often as you write Python programs:

| Exception | What causes it |
|-----------|----------------|
| `ValueError` | A value has the right type but the wrong content — e.g., `int("hello")` |
| `TypeError` | An operation is applied to the wrong type — e.g., `"hello" + 5` |
| `KeyError` | A key doesn't exist in a dict — e.g., `data["missing_key"]` |
| `IndexError` | An index is out of range — e.g., `my_list[10]` on a 3-item list |
| `FileNotFoundError` | A file you're trying to open doesn't exist |
| `ZeroDivisionError` | Division by zero — e.g., `10 / 0` |
| `AttributeError` | Calling a method that doesn't exist on an object — e.g., `42.upper()` |

You don't need to memorize all of these right now. The goal is to recognize them when you see them in error messages. Knowing the name makes debugging much faster!

---

## The try/except Block

The `try` block lets you run code that might fail. If an exception occurs, Python skips to the `except` block instead of crashing.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero.")
```

Without the `try/except`, this code crashes with `ZeroDivisionError: division by zero`. With it, Python catches the error and prints a helpful message.

**Name the specific exception you expect.** This is cleaner and safer than catching everything:

```python
# Specific — only catches ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero.")

# Too broad — catches every error, including bugs you didn't intend to hide
try:
    result = 10 / 0
except Exception:
    print("Something went wrong.")
```

Catching `Exception` (or the bare `except:` with no type) should be reserved for cases where you genuinely can't predict what might go wrong — like network calls where many different errors are possible.

---

## The `as e` Syntax

When you write `except SomeError as e:`, the variable `e` holds the actual exception object. You can print it to see the error message Python would have shown you:

```python
try:
    number = int("forty-two")
except ValueError as e:
    print(f"Conversion failed: {e}")
```

Output:
```
Conversion failed: invalid literal for int() with base 10: 'forty-two'
```

This is useful when you want to show the user (or yourself) what went wrong, without letting the full traceback crash the program.

---

## The `else` Block

The `else` block runs only if **no** exception occurred in the `try` block. It's a clean way to separate "success" logic from error-handling logic:

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero.")
else:
    print(f"Result: {result}")
```

Output:
```
Result: 5.0
```

You could put the `print` inside the `try` block and get the same result, but using `else` makes it clear that the print only runs when everything worked.

---

## The `finally` Block

The `finally` block always runs, whether an exception occurred or not. It's used for cleanup: releasing resources or running code that must happen no matter what:

```python
try:
    with open("data.txt", "r") as f:
        content = f.read()
    print("File read successfully.")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Attempted file read.")   # runs in either case
```

In practice, `with open()` already handles file closing automatically, so `finally` becomes more important when you work with database connections or other resources that need explicit cleanup.

---

## Raising Your Own Exceptions

You can raise an exception yourself using `raise`. This is useful inside functions where you want to signal that the caller passed invalid input:

```python
def get_discount(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError(f"Percent must be between 0 and 100, got {percent}.")
    return price * (1 - percent / 100)

try:
    discounted = get_discount(50, 150)
except ValueError as e:
    print(f"Invalid discount: {e}")
```

Output:
```
Invalid discount: Percent must be between 0 and 100, got 150.
```

When you `raise` an exception, the function stops immediately and the error travels up to whoever called the function. If nothing catches it, the program crashes with your message, which is exactly what you want during development.

---

## The `logging` Module

As your programs grow from small scripts to multi-function programs, `print()` statements become hard to manage. The `logging` module gives you structured output with **levels** that tell you how serious each message is:

| Level | When to use it |
|-------|----------------|
| `DEBUG` | Detailed information useful during development — variable values, function calls |
| `INFO` | Confirmation that things are working as expected |
| `WARNING` | Something unexpected happened, but the program can continue |
| `ERROR` | A serious problem prevented part of the program from running |

Basic setup and usage:

```python
import logging

logging.basicConfig(level=logging.DEBUG)

def divide(a, b):
    logging.debug(f"divide() called with a={a}, b={b}")
    if b == 0:
        logging.error("Division by zero attempted.")
        return None
    result = a / b
    logging.info(f"Result: {result}")
    return result

divide(10, 2)
divide(5, 0)
```

Output:
```
DEBUG:root:divide() called with a=10, b=2
INFO:root:Result: 5.0
DEBUG:root:divide() called with a=5, b=0
ERROR:root:Division by zero attempted.
```

The key advantage over `print`: you can change `level=logging.DEBUG` to `level=logging.ERROR` and the DEBUG and INFO messages disappear entirely — without deleting a single line of code. Your production code can be quieter than your development code with one change.

---

### AI Prompt: Predict-Then-Check

Look at this code before running it:

```python
import logging

logging.basicConfig(level=logging.WARNING)

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error(f"Error: {e}")
        return None
    else:
        logging.info(f"Result: {result}")
        return result

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

1. Before running the code: what will appear in the console? The logging level is set to `WARNING`. What does that mean for the `INFO` and `ERROR` messages?
2. Share your prediction with an AI chatbot:

> "I'm learning `try/except` and the `logging` module in Python. Here's my prediction for what this code outputs: [your prediction]. Can you tell me if I'm right, and explain why each line is or isn't printed?"

3. Then run the code to verify.

---

## Videos

**"Python Tutorial: Using Try/Except Blocks for Error Handling"** (Corey Schafer)

[Watch the video](https://youtu.be/NIWwJbo-9_8?si=pIW22bVWi2xl7kot) — walks through try, except, else, finally, and raising exceptions. 

**"Python Tutorial: Logging Basics - Logging to Files, Setting Levels, and Formatting"** (Corey Schafer)

[Watch the video](https://youtu.be/-ARI4Cz-awo?si=Ad7k5QpSU3in3TXb) — covers the logging module in depth, including setting levels and formatting output. Search YouTube for the title above to find it.

---

## Check for Understanding

**Question 1:** What is the difference between a syntax error and a runtime error?

* A) Syntax errors occur while the program is running; runtime errors occur before it starts
* B) Syntax errors prevent the program from starting; runtime errors occur while the program is running
* C) Syntax errors are always more serious than runtime errors
* D) They are the same thing — Python uses both terms for the same situation

<details>
<summary>Answer</summary>

**B) Syntax errors prevent the program from starting; runtime errors occur while the program is running** — A syntax error means Python can't parse your code at all (a missing colon, bad indentation). A runtime error means Python understood your code but something went wrong during execution — bad input, missing file, division by zero.

</details>

**Question 2:** Which `except` clause is best for catching a `ValueError` specifically?

* A) `except Exception:`
* B) `except:`
* C) `except ValueError:`
* D) `except Error:`

<details>
<summary>Answer</summary>

**C) `except ValueError:`** — Naming the specific exception type is almost always better than catching `Exception` or using a bare `except:`. Specific catching means you only handle errors you actually expected; other unexpected bugs will still surface rather than being silently hidden.

</details>

**Question 3:** When does the `else` block in a try/except statement run?

* A) When an exception is raised
* B) After `finally`, regardless of what happened
* C) Only if no exception was raised in the `try` block
* D) Only if an exception was raised and caught

<details>
<summary>Answer</summary>

**C) Only if no exception was raised in the `try` block** — `else` is the "success" branch: it runs when the `try` block completed normally. If any exception occurred (caught or not), `else` is skipped.

</details>

**Question 4:** What does `except ValueError as e:` let you do?

* A) Rename the `ValueError` to a simpler name
* B) Access the exception's error message via the variable `e`
* C) Catch multiple exception types at once
* D) Suppress the error without printing anything

<details>
<summary>Answer</summary>

**B) Access the exception's error message via the variable `e`** — The `as e` syntax binds the exception object to `e`. You can print it (`print(e)`) or include it in a string (`f"Error: {e}"`) to show what specifically went wrong.

</details>

**Question 5:** You set `logging.basicConfig(level=logging.WARNING)`. Which calls will produce output?

* A) Only `logging.debug()` calls
* B) `logging.debug()` and `logging.info()` calls
* C) `logging.warning()`, `logging.error()`, and above
* D) All logging calls, regardless of level

<details>
<summary>Answer</summary>

**C) `logging.warning()`, `logging.error()`, and above** — The level setting is a minimum threshold. With `level=logging.WARNING`, messages at WARNING, ERROR, and CRITICAL are shown; DEBUG and INFO are suppressed. This lets you write detailed logging during development and quiet it down for production by changing one line.

</details>

---

## Further Reading

- [Python Documentation — Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Python Documentation — Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Real Python — Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)
- [Real Python — Logging in Python](https://realpython.com/python-logging/)
