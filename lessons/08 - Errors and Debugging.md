# Lesson 8 — Errors & Debugging

**Lesson Overview**

Every program you've written so far assumed things would go right. The user enters a valid number. The file exists. The calculation makes sense. That assumption works fine while you're learning — but real programs can't make it.

This week you'll learn to write code that handles the unexpected: invalid input, missing files, network failures, and more. You'll meet Python's error-handling tools (`try`, `except`, `raise`) and learn a design philosophy — defensive programming — that shapes how you structure functions from the start. You'll also pick up two tools that will be with you for the rest of your career: the `logging` module for structured program output, and `pip` with virtual environments for managing the packages your projects depend on.

**Learning Objectives**

This week, I can...

* Use `try/except` to catch specific exceptions and handle errors without crashing.
* Apply defensive programming patterns: validating input, using guard clauses, and checking for `None`.
* Refactor a script to fail gracefully: returning safe defaults and logging errors instead of crashing.
* Create a virtual environment, install packages with `pip`, and generate a `requirements.txt`.

## Topics

1. **[`try`/`except` and Common Runtime Errors](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/lessons/08%20-%20Errors%20%26%20Debugging/01_try_except.md)**

   The difference between syntax errors and runtime errors; `try`, `except`, `else`, and `finally`; catching specific exceptions vs. broad `Exception`; the `as e` syntax for inspecting error messages; raising exceptions with `raise`; common runtime exceptions (`ValueError`, `TypeError`, `KeyError`, `IndexError`, `FileNotFoundError`, `ZeroDivisionError`); the `logging` module and its four levels (DEBUG, INFO, WARNING, ERROR)

2. **[Defensive Programming Patterns](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/lessons/08%20-%20Errors%20%26%20Debugging/02_defensive_programming.md)**

   What defensive programming means and why it matters; validating inputs before using them; guard clauses for early returns; checking for `None` and empty values; the difference between failing loudly and silently; `assert` for development-time checks

3. **[Writing Code That Fails Gracefully](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/lessons/08%20-%20Errors%20%26%20Debugging/03_failing_gracefully.md)**

   Crashing vs. graceful degradation; wrapping file reads and network calls in `try/except`; returning safe default values on failure; a complete worked example with CSV file reading; using `logging` in the context of error handling; refactoring an earlier script to be more robust

4. **[pip and Virtual Environments](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/lessons/08%20-%20Errors%20%26%20Debugging/04_pip_virtual_environments.md)**

   What `pip` is and how it connects to PyPI; why global package installation causes problems; what a virtual environment is and how it solves those problems; creating and activating `.venv`; `pip freeze > requirements.txt` and `pip install -r requirements.txt`
