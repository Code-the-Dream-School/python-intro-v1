# Week 10 — Final Project Part I (Mentor Summary)

This is the mandatory core of the two-week final project: fetch from a public API, transform JSON into structured Python, and wrap it in a CLI. No new syntax — students integrate Weeks 6–9 skills into their own project. Delivered in two phases (core program, then CLI) plus planning (Phase 0).

## Key concepts taught
- **API integration via `requests`** — `requests.get(url)` + `response.raise_for_status()` + `response.json()`; URL stored in a module-level constant, not hard-coded in the call.
- **JSON → list-of-dicts transformation** — pull the record list out of the response (top-level list vs. dict-with-a-key), then extract 3–5 chosen fields into clean dicts. `.get(key, default)` for missing/`null` fields (avoids `KeyError`).
- **`try/except` error handling** — wrap only the network call + status check; catch `requests.exceptions.RequestException`; return `[]` on failure so the program degrades gracefully instead of crashing.
- **Modular functions** — `fetch_data()`, `process_data(records)`, `display_results(results)`, `main()`. One responsibility each; return values, not prints (except display). Students may rename/split.
- **Required CLI tool with argument-based behavior** — accept input via `input()` prompts or `argparse`; implement at least one meaningful interaction (filter / lookup / compare); formatted output; unexpected input handled without crashing.

## The assignment — "Final Project Part I"
Build a CLI tool over a free, no-key public API. Recommended APIs: **REST Countries**, **Open Library**, **PokeAPI** (other APIs need Cohort Instructional Leader sign-off). Two-phase build:
- **Phase 1 (core):** connect via `requests`, parse JSON into a list of dicts, handle connection/status errors with `try/except`, organize into functions.
- **Phase 2 (CLI):** accept user input, implement one meaningful interaction (filter a field / look up a record / compare two), display readable formatted output, handle bad input gracefully.

Starter repo provides `main.py` stubs, `requirements.txt`, `README.md`. **Deliverables:** those three files (README must name the API + install/run steps + interaction description); PR from branch `week-10-final-project` with incremental commits (API / parse / CLI as separate commits); 3–5 min video walking through `fetch_data()`, a live CLI demo, and one code-organization decision.

## Likely trouble spots
- **Scope creep** — students over-plan (multiple interactions, menus, extra APIs) before one interaction works. Rubric needs only *one* meaningful interaction; push them to ship the minimal path first, add later.
- **API choice / PokeAPI trap** — PokeAPI returns one record per request, so `fetch_data()` needs a loop over a name list with per-iteration `try/except`. Students who pick it expecting a single list-returning call get stuck; steer beginners to REST Countries or Open Library.
- **Response shape confusion** — the biggest Phase 1 blocker is finding where the record list lives (top-level list vs. `data["docs"]`/`["results"]`) and handling nested fields (`name.common`, `author_name[0]`). Have them inspect `type(data)` / `data.keys()` before writing `process_data()`.
- **Error handling at the wrong level** — wrapping the whole program in one `try/except` (hides real bugs) or catching too narrowly. It should wrap only the request+status lines and return `[]`; test by pointing `API_URL` at a bad host.
- **Refactoring into functions** — treating functions as decoration: printing inside `fetch_data()`, no return values, or one giant `main()`. Rubric rewards clean separation (fetch/parse/display) and passing query params as arguments.
- **CLI arg parsing** — `argparse` positional-vs-optional args and case-sensitive matching (`.lower()` both sides). Remind them `input()` is a valid, simpler choice; the filter/lookup/compare logic is identical either way.
- **Version control** — single-commit submissions and forgetting the feature branch. Rubric explicitly grades incremental commits; nudge commit-per-phase early.
