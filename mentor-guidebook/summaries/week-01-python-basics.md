# Week 1 — Python Basics (Mentor Summary)

**Environment this week:** Students work entirely in [online-python.com](https://www.online-python.com/) — no local install. Setup comes in Week 2. Work isn't auto-saved; they copy code out manually.

**Git thread:** Conceptual intro only (what/why of version control). Students create a *remote* GitHub repo (`firstname-lastname-python`) and submit via GitHub's web editor + a first PR. No local Git, no CLI yet — that's Weeks 2–3. Expect PR mechanics to feel like magic to them; that's by design.

---

## Key concepts taught

- **Variables & assignment** — `=` as "assign," naming rules, `#` comments.
- **Four core types** — `int`, `float`, `str`, `bool`; `type()` to inspect.
- **`print()` / `input()`** — multiple args to `print`; **`input()` always returns `str`**.
- **Type conversion** — `int()`, `float()`, `str()`, `bool()`; implicit vs. explicit; `ValueError` on bad casts (graceful handling deferred to Week 8).
- **Operators** — arithmetic (incl. `/` → float, `//`, `%`, `**`), comparison, logical (`and`/`or`/`not`).
- **Strings** — concatenation (`+` needs `str()` on numbers), **f-strings** incl. `:.2f` formatting, methods `.lower()/.upper()/.strip()/.replace()/.split()/.join()`.
- **Scripts** — top-to-bottom execution; build-test-build in small steps.
- **Debugging** — reading tracebacks bottom-up; recognizing `SyntaxError`, `NameError`, `TypeError`, `ValueError`, `IndentationError`; `print()` debugging.

## The assignment — "Profile Card Builder"

One script built up in five additive sections (students keep appending, not deleting):

1. Declare one variable of each core type; print value + `type()`.
2. `input()` name & birth year → compute approximate age → sentence.
3. Two numeric inputs → `float()` → multiply → f-string result.
4. Formatted ASCII "receipt" from variables only (no input); compute total.
5. **Mini-project:** profile card from 5 inputs, age computed from birth year, aligned labels.

Plus a **3–5 min video reflection**: what a variable is / data-type importance, a line-by-line walkthrough of one section, and one error they hit and fixed. Two submissions in CTD Learns: PR link (URL1) + video link (URL2).

## Likely trouble spots

- **`input()` returns a string** — the #1 stumble. Forgetting to `int()`/`float()` before math gives a `TypeError` (concatenation) or wrong result. Recurs in every section with input.
- **Age computation** — students often try to `input()` the age directly; the assignment requires computing it from birth year (`2026 - birth_year`, current year hardcoded — no `datetime` yet).
- **Output alignment** (Sections 4 & 5) — aligning labels/columns is fiddly with plain `print`. They only know manual spacing; f-string alignment specs (`{x:<10}`) aren't taught, so hand-padded spaces are acceptable.
- **`str()` in concatenation vs. f-strings** — f-strings auto-convert; `+` concatenation does not. Students mix these up.
- **Float display** — `0.1 + 0.2` surprises; `:.2f` is the intended fix.
- **Case-sensitive names** — `Name` vs. `name` `NameError` is a planted bug in the debugging lesson; watch for it in student code too.
- **Lost work** — online-python.com doesn't save. Some students will lose code before submitting; remind them to copy it out.
