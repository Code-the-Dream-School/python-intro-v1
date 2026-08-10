# Week 9 — External Libraries and APIs (Mentor Summary)

## Key concepts taught
- **Installing `requests`** — first third-party lib for the project; `pip install requests`, then `pip freeze > requirements.txt`. Assumes venv active (introduced Week 8).
- **GET requests** — `requests.get(url)` returns a `Response` object (not a string, not a dict).
- **Status codes** — check `response.status_code` before parsing; table covers 200/400/401/404/429/500, with 4xx = client, 5xx = server.
- **Response body** — `.text` (raw string) vs `.json()` (parsed Python object). `.content` mentioned as raw bytes.
- **JSON ↔ Python mapping** — object→dict, array→list, string→str, number→int/float, true/false→True/False, null→None.
- **What an API is** — restaurant analogy (menu = docs, order = request, food = JSON); framed around reading docs and finding the example response first.
- **Query parameters** — pass via `params={}` (not manual f-string URL building); requests handles encoding. Examples: Open-Meteo, Agify.
- **Error handling** — wrap in `try/except requests.exceptions.RequestException` (the base class covering ConnectionError, Timeout, HTTPError); `raise_for_status()` as the professional pattern for 4xx/5xx.
- **API keys (conceptual only)** — key as param or `Authorization` header; store in `.env` with python-dotenv. Explicitly deferred: **this week is keyless public APIs only.**
- **Navigating nested JSON** — chain key/index lookups (`country["name"]["common"]`, `country["capital"][0]`); trace structure before coding.
- **Transform pattern** — loop raw response into a clean flat list-of-dicts (explicitly linked back to Week 7 CSV work).
- **`.get()` for missing keys** — safe access with fallback; the `capital` one-liner is the recurring example.
- **Fetch-and-return function** — network logic isolated in one function returning `[]` on failure; display logic kept separate. Framed as the direct structure of the Week 10 final project.

## The assignment — "Country Explorer CLI" (+ 4 warmups)
Build an interactive CLI over the REST Countries API. Work goes in `week-9/assignment-9/`; submit PR link + video reflection link.

- **Warmup 1** (`warmup1.py`) — GET Agify, print status code + full JSON.
- **Warmup 2** (`warmup2.py`) — access `name`/`age`; use `.get()` for a missing key with fallback.
- **Warmup 3** (`warmup3.py`) — loop a REST Countries list, print first 10 `name.common` values.
- **Warmup 4** (`warmup4.py`) — `try/except RequestException` + status check against a deliberately bad URL.
- **Mini-project** (`mini_project.py`) — fetch all countries into a list of dicts (`name`, `capital`, `region`, `population`); `while`-loop menu with search-by-name (case-insensitive partial match), filter-by-region (sorted by population desc), quit; `.get()` for missing capitals; error handling on the initial fetch. Sample JSON provided at `week-9/data/sample_countries.json`.
- **Video reflection** (3–5 min) — what JSON is / what `.json()` returns; raw response → list of dicts walkthrough; demo of handling missing data.

## Likely trouble spots
- **Network/environment friction** — live requests mean flaky wifi, timeouts, or a forgotten venv activation produce `ModuleNotFoundError: requests`. Confirm install + `requirements.txt` early.
- **REST Countries `/v3.1/all` requires `fields`** — the API rejects an unfiltered `/all` call (400). The assignment URL includes `?fields=...`; students who drop it will see failures.
- **Rate limiting (429)** — re-running scripts against the same API in a loop can trip limits; taught in the status table but easy to hit while debugging.
- **`Response` object vs data** — printing `response` (shows `<Response [200]>`) or forgetting `.json()` and indexing a string.
- **Nested-structure confusion** — `country["name"]` is a dict, not the name; `capital` is a list needing `[0]`. This is the core conceptual hurdle of the week.
- **KeyError on missing `capital`** — territories lack the key entirely; must use `.get()` not `["capital"]`.
- **Overwriting vs appending** — `result = {...}` inside the loop instead of `result.append({...})` (called out directly in a CFU).
- **Catching the wrong exception** — using `HTTPError` alone (misses connection errors) or bare `Exception` (too broad) instead of `RequestException`.
- **API keys / `.env`** — presented but NOT practiced this week; students asking how to authenticate should be pointed to keyless APIs for now, with the .env pattern coming in later courses.
