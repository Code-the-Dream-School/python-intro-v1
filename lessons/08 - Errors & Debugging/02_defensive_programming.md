# Defensive Programming Patterns

> **Source:** New content — expands on PE 1.8
>
> **Notes:** PE 1.8 teaches error handling syntax but not defensive *design*. This section teaches students to anticipate problems before they happen. Cover:
> - **Input validation:** check types, ranges, and emptiness before using a value
> - **Guard clauses:** return early with a clear message if preconditions aren't met, rather than deep nesting
> - **`None` checking:** explicitly handle the case where a function might return `None`
> - **Failing loudly vs. silently:** why swallowing exceptions with a bare `except: pass` is dangerous
> - **Assertion-based checks** (brief): `assert condition, "message"` for invariants during development
> Use a before/after refactoring example to show the difference between fragile and defensive code.

TBD
