# Assignment 9 Answer Key — External Libraries and APIs

## File Setup

- Forked `python-intro-homework` repo, `assignment-9` branch, work in `week-9/assignment-9/`. PR from `assignment-9` into `main`. **URL1** = PR link; URL2 = video (not assessed).
- `requests` must be pip-installed (`pip install requests`) and reflected in `requirements.txt`. An `import requests` at the top of each file is expected.
- Five files: `warmup1.py`–`warmup4.py`, `mini_project.py`.
- API output is live and varies (ages, populations, country counts, order). Grade on shape and correct parsing, not exact values.
- `week-9/data/sample_countries.json` is provided as a **structure reference only** (to understand the response shape before writing a parser) — students still fetch live from the API; a submission that reads the sample file instead of calling the API misses the point of the assignment.

## Warmup 1: Make Your First API Request — **Objective (hybrid)**

`requests.get("https://api.agify.io/?name=michael")`, then print status code and full JSON.

```
Status code: 200
Response: {'name': 'michael', 'age': 40, 'count': 112758}
```

**Correct if:** uses `requests.get`, prints `response.status_code`, and prints `response.json()` (the parsed dict — printed with single quotes, not `response.text`). `age`/`count` values will vary.
**Common miss:** printing `response.text` (a string with double-quoted JSON) or the raw `<Response [200]>` object instead of the parsed dict.

## Warmup 2: Access Specific JSON Fields — **Objective (hybrid)**

Same endpoint; pull `name` and `age`, then a missing key via `.get()` with a fallback.

```
Name: michael
Predicted age: 40
Birthday: Not available
```

**Correct if:** `data["name"]` / `data["age"]` accessed directly, and the missing key uses `.get("birthday", "Not available")` (or `.get()` + conditional) so no `KeyError`.
**Common miss:** using `data["birthday"]` (crashes with `KeyError`), or catching the error with try/except instead of using `.get()` as instructed.

## Warmup 3: Loop Through a JSON List — **Objective (hybrid)**

`GET https://restcountries.com/v3.1/region/europe?fields=name,population`, loop the list, print `item["name"]["common"]`, first 10 only.

```
Albania
Andorra
Austria
...
```

**Correct if:** response treated as a **list**, name reached via nested `item["name"]["common"]`, and output sliced to 10 (`[:10]` or a counter). Exact names/order vary by API.
**Common miss:** `item["name"]` (prints the whole nested dict), forgetting the 10-item limit, or indexing the top level as a dict.

## Warmup 4: Handle Request Errors — **Objective (hybrid)**

`requests.get` in `try`/`except requests.exceptions.RequestException`; also check status code before parsing. Test against a bad URL.

```
Error: Could not reach the server. Check your connection and try again.
```

**Correct if:** unreachable host caught by `except requests.exceptions.RequestException` and a friendly message printed; and a non-200 status is handled (`status_code != 200` check or `raise_for_status()`) rather than blindly parsing.
**Common miss:** bare `except:` or catching `Exception`; catching only `ConnectionError` (misses timeouts/HTTP errors); no status check so `.json()` runs on error responses.

## Part 2: Mini-Project — Country Explorer CLI — **Subjective (hybrid)**

`GET https://restcountries.com/v3.1/all?fields=name,capital,region,population`, parsed into a list of dicts with keys `name`, `capital`, `region`, `population`; menu loop with search-by-name, filter-by-region, quit.

- **Fetch + parse:** initial request wrapped in `try`/`except` with a status/`raise_for_status()` check; JSON transformed into clean flat dicts (name from `country["name"]["common"]`). Failure prints a message and exits rather than crashing.
- **`/all` endpoint trap:** the `fields` param is **required** — `https://restcountries.com/v3.1/all` with no `fields` returns **400 Bad Request**, not data. A submission that drops `fields` (or a bare status check that then calls `.json()`/exits without explanation) is a real correctness failure, not just style.
- **Search (option 1):** case-insensitive partial match (`term.lower() in name.lower()`); prints each match with capital, region, population.
- **Filter (option 2):** region match (case-insensitive is fine) sorted by population descending (`sorted(..., key=..., reverse=True)`).
- **Missing capital:** countries with no `capital` key/empty list show `"N/A"` (via `.get()` or conditional) instead of raising `KeyError`/`IndexError`.
- **Menu loop:** `while` loop with options 1–3; option 3 exits cleanly; invalid input handled without crashing (nice-to-have).

**Common miss:** omitting `fields` on `/all` (400); indexing `capital[0]` unguarded (crashes on capital-less territories); search not case-insensitive; region results unsorted or ascending.
