# Assignment 10 Answer Key — Final Project Part I

## File Setup

- Forked `python-intro-homework` repo, feature branch `week-10-final-project`, PR into their own fork's `main`. **URL1** = PR link; URL2 = video demo (not assessed).
- Deliverables: `main.py` (CLI entry point), `requirements.txt` (must list `requests` at minimum), `README.md` (title, which API, install/run steps, description of the CLI interaction).
- **Incremental commits are a graded expectation** — expect at least three commits reflecting stages: API working, parsing, CLI. A single squashed "final project" commit is a Version Control miss.
- No single correct output — this is a project. Grade each section against the requirement. Recommended APIs: REST Countries, Open Library, PokeAPI. Any other API requires Cohort Instructional Leader sign-off (must be free, no API key, returns records that fit a list of dicts).

---

## Section 1: API Integration — **Objective + Subjective**

**Objective (hard rule):** The program must actually call the API with `requests` and use live data. Hardcoded/pasted JSON or a canned list fails outright.

**Passing has:** `requests.get(URL)`, `response.raise_for_status()`, and `response.json()`; URL held in a variable (or built from args), not buried inline.

**Failing misses:** no `raise_for_status()` (bad status silently treated as success); URL/params hardcoded inside the call with no clear organization.

**Note for PokeAPI:** each request returns one Pokémon, so a passing submission must **loop** and make one request per name/ID, appending each result. A single `requests.get` for PokeAPI cannot produce a dataset — flag it.

## Section 2: JSON → List-of-Dicts Transformation — **Subjective**

**Passing has:** a transformation that pulls the record list from wherever it lives and builds a list of clean dicts with only the relevant fields (3–5). `.get()` (or equivalent guard) used for fields that may be missing so a `KeyError` can't crash it.

**Failing misses:** returns the raw response untouched; crashes on a missing/`null` field via `record["key"]`; or never isolates the record list.

**Response-shape confusion to watch:** REST Countries returns a list directly; Open Library nests records under `docs`; PokeAPI returns one dict per request. A common bug is iterating the top-level dict instead of the inner list — check they located the list correctly.

## Section 3: Error Handling — **Subjective**

**Passing has:** `try/except requests.exceptions.RequestException` around the network call + status check, showing a clear message instead of a traceback, and returning `[]` (or similar) so the program degrades gracefully.

**Failing misses:** no error handling (raw traceback on connection failure); bare `except:`; or catching something too narrow to cover connection/status errors.

**Watch the level:** the `try/except` should wrap only the request/status lines — not the whole program, and not `process_data()`. Over-broad wrapping that swallows parsing/CLI bugs is a code-smell worth noting even if it technically passes.

## Section 4: Modular Functions — **Subjective**

**Passing has:** logic split into functions with clear names, parameters, and return values — fetch, process/transform, display, and `main()` orchestrating them. Each function does one job; `fetch`/`process` return values rather than printing.

**Failing misses:** one long `main()` (or top-level script) doing everything; functions with no parameters/returns that just mutate globals or print inline.

**Watch:** stubs renamed or split across files is fine (allowed by the lesson). What matters is genuine separation of responsibilities — a "refactor" that's still one giant function with helper names doesn't count.

## Section 5: CLI Tool — **Subjective**

**Passing has:** at least one form of user input (`input()` prompts **or** `argparse`) driving **at least one meaningful interaction** — filter by a field, look up a record, or compare two records — with readable, formatted output (not raw dict dumps) and graceful handling of unexpected input (empty input, no matches).

**Failing misses:** no interaction (just prints all data with no input); crashes on empty input or a no-match query; output is raw `{...}` dicts.

**Note:** only one meaningful interaction is required; multiple modes / a menu loop is an "Exceeds," not a baseline. Either input style is fully acceptable.
