# Lesson 8 — Errors & Debugging

**Lesson Overview**
Students learn to write code that handles the unexpected gracefully. This week brings together error handling from Python Essentials with new defensive programming patterns that prepare students for working with external data and APIs.

## Topics

1. **[try/except and Common Runtime Errors](01_try_except.md)**
   *Ported from Python Essentials — PE 1.8 (Error Handling)*
   `try`, `except`, `else`, `finally`; catching specific exceptions vs. broad `Exception`; raising exceptions with `raise`; common runtime errors: `ValueError`, `TypeError`, `FileNotFoundError`, `ZeroDivisionError`

2. **[Defensive Programming Patterns](02_defensive_programming.md)**
   *New content (expands on PE 1.8)*
   Validating inputs before using them; checking for `None` and empty values; writing functions that fail loudly with informative messages; guard clauses; the principle of failing early

3. **[Writing Code That Fails Gracefully](03_failing_gracefully.md)**
   *New content*
   Wrapping risky operations (file reads, network calls) in `try/except`; providing meaningful fallback behavior or user-facing error messages; the difference between crashing and graceful degradation; applying these patterns to scripts from earlier weeks

   > **Note:** The `logging` module from PE 1.7 is intentionally moved here from Week 1. Students are now writing larger programs where structured logging is more relevant.

4. **[pip and Virtual Environments (Conceptual)](04_pip_virtual_environments.md)**
   *Ported from Python Essentials — PE 2.6 (Virtual Environments)*
   What `pip` is and how to install a package; what a virtual environment is and why it matters; creating and activating a `.venv`; `requirements.txt`

   > **Note:** Virtual environments were introduced in Week 2 setup; this section deepens the conceptual understanding and covers `requirements.txt` for the first time.
