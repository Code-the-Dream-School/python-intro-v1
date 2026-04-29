# Writing Code That Fails Gracefully

> **Source:** New content
>
> **Notes:** This section connects defensive programming to the kinds of programs students are building (file I/O scripts and, soon, API clients). Cover:
> - Wrapping file reads and network calls in `try/except` with specific exceptions
> - Providing a meaningful fallback: returning a default value, logging the error, or printing a user-friendly message
> - The difference between *crashing* (unhandled exception) and *graceful degradation* (handled exception with useful feedback)
> - A worked example: a function that reads a CSV file, catches `FileNotFoundError`, and returns an empty list with a warning message instead of crashing
> - Applying patterns from this week to refactor a script from an earlier week to be more robust
> - Brief mention of the `logging` module at different levels (DEBUG for development, ERROR for production)

TBD
