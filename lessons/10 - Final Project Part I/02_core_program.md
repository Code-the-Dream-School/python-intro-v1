# Building the Core Program

You already know how to use `requests`, write `try/except` blocks, and organize code into functions. Phase 1 is about putting those pieces together in the context of your own project, with real data.

This lesson walks you through each step. **Work through it sequentially**. The most common mistake in a phase like this is writing too much code at once before testing any of it.

---

## Step 1 — Write `fetch_data()`

The job of `fetch_data()` is simple: make an HTTP request to your API and return the raw data.

Here's the basic pattern:

```python
import requests

API_URL = "https://restcountries.com/v3.1/all"  # replace with your URL

def fetch_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()
```

**Three things to notice:**

1. **Put the URL in a variable, not directly in the call.** `requests.get(API_URL)` is easier to update and test than `requests.get("https://restcountries.com/v3.1/all")` buried inside a call. When you change APIs or update an endpoint, you change one line at the top.

2. **`response.raise_for_status()`** checks whether the server returned an error (a 4xx or 5xx status code). If it did, it raises an exception automatically. Without this line, a 404 or 500 response would look like a success — your program would just crash later when it tried to parse the bad response.

3. **Return the raw response, not a print statement.** `fetch_data()` shouldn't print anything. It should return data that another function can use. Functions that return values are far more flexible than functions that print directly.

### Test it now

Before you write `process_data()`, test that `fetch_data()` works:

```python
def main():
    data = fetch_data()
    print(data)
```

Run the program. You should see a large blob of JSON printed to the terminal. That's good — it means the request worked and the raw data is coming back. Read a few records before moving on; this is your first look at the shape of your actual data.

---

## Step 2 — Parse the Response into a List of Dicts

The raw response from `fetch_data()` might be:

- **A list directly**: `[{...}, {...}, {...}]` — REST Countries returns this.
- **A dict with a list inside it**: `{"results": [{...}, {...}]}` — Open Library returns this.

Your job in `process_data()` is to pull out the list, then extract just the fields you'll use.

**If the response is already a list:**

```python
def process_data(records):
    result = []
    for record in records:
        result.append({
            "name": record.get("name", {}).get("common", "Unknown"),
            "population": record.get("population", 0),
            "region": record.get("region", "Unknown"),
        })
    return result
```

**If the response is a dict with a list inside:**

```python
def process_data(data):
    records = data.get("docs", [])  # or "results", depending on your API
    result = []
    for record in records:
        result.append({
            "title": record.get("title", "Unknown"),
            "author": record.get("author_name", ["Unknown"])[0],
            "year": record.get("first_publish_year", "Unknown"),
        })
    return result
```

**Replacing the field names:** The field names in the examples above are specific to REST Countries and Open Library. Replace them with the fields you identified in Phase 0. Use the exact key names from the JSON you read in your browser.

### Using `.get()` for fields that might be missing

Public APIs don't always return every field for every record. If a field is missing and you try to access it with `record["field"]`, your program will crash with a `KeyError`.

Use `.get()` instead:

```python
record.get("population", 0)      # returns 0 if "population" is missing
record.get("region", "Unknown")  # returns "Unknown" if "region" is missing
```

The second argument to `.get()` is the default — choose one that makes sense for the field.

### Test it now

Update `main()` to call both functions and print the result:

```python
def main():
    data = fetch_data()
    records = process_data(data)
    print(records[:3])  # just the first three, to keep the output manageable
```

Run the program. You should see a list of small, clean dictionaries with just the fields you care about. If something looks wrong — a missing field, a `None` where you expected a value, an extra level of nesting — fix it now, before you write the CLI.

<details>
<summary>Stuck on parsing? Click here for help.</summary>

The most common confusion is figuring out where the list of records actually lives in the response. Here's a pattern for finding it:

```python
def main():
    data = fetch_data()

    # What type is the top-level response?
    print(type(data))

    # If it's a dict, what keys does it have?
    if isinstance(data, dict):
        print(data.keys())

    # If it's a list, how many items?
    if isinstance(data, list):
        print(len(data))
        print(data[0])  # look at the first record
```

Work through this step by step until you can see one clean record. Once you know the shape, write `process_data()`.

</details>

---

## Step 3 — Add Error Handling

Right now, if the network is down or the API returns an error, your program will crash with an unhelpful traceback. Wrap the risky parts with `try/except` so the user sees a clear message instead.

```python
def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: could not fetch data. {e}")
        return []
```

**A few things to notice:**

- **Catch at the right level.** The `try/except` wraps the network call and the status check — the two lines that can fail due to connection problems or bad server responses. It doesn't wrap the whole program. If `process_data()` crashes, that's a different bug and you want to see that traceback.

- **Return an empty list on failure.** This lets the rest of the program keep running gracefully. When `main()` calls `process_data([])`, it will return an empty list, and the CLI can tell the user "no results" rather than crashing.

- **`requests.exceptions.RequestException`** is the base class for all `requests` errors — timeouts, connection errors, bad status codes raised by `.raise_for_status()`. Catching this one type handles all of them.

> **Tip:** Test your error handling by temporarily changing `API_URL` to something invalid (like `"https://this-does-not-exist.example.com"`). Your program should print the error message and exit gracefully rather than crashing with a traceback.

---

## Step 4 — Test Incrementally

Before writing the CLI, confirm that your core program works end-to-end:

```python
def main():
    data = fetch_data()
    records = process_data(data)

    if not records:
        print("No data returned.")
        return

    print(f"Fetched {len(records)} records.")
    print(records[0])  # inspect the first record
```

Run this. If you see a count and a well-shaped dictionary, you're ready for Phase 2.

If something is wrong, fix it now. A bug in `fetch_data()` or `process_data()` will be harder to track down once there's CLI code running on top of it.

---

## PokeAPI: Fetching Multiple Records

If you chose PokeAPI, there's one important difference: each request returns data for exactly one Pokémon. To build a dataset, you need to make multiple requests, one per Pokémon.

This is a common real-world pattern. Many APIs let you list resources (with IDs or names) separately from fetching details about each one.

```python
POKEMON_NAMES = ["bulbasaur", "charmander", "squirtle", "pikachu", "eevee"]

def fetch_data():
    records = []
    for name in POKEMON_NAMES:
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{name}"
            response = requests.get(url)
            response.raise_for_status()
            records.append(response.json())
        except requests.exceptions.RequestException as e:
            print(f"Could not fetch {name}: {e}")
    return records
```

Notice that the error handling is inside the loop. If one request fails, the program continues and collects data for the rest. This is more useful than stopping at the first error.

You can start with a small list (5–10 Pokémon) and expand it later. The project doesn't require a specific number — focus on getting clean data for the ones you have.

---

## Phase 1 Checkpoint

Before moving to Phase 2, you should be able to answer yes to all of these:

- [ ] `fetch_data()` successfully calls your API and returns data
- [ ] `process_data()` returns a list of clean dictionaries with the fields you need
- [ ] A connection error or bad status code shows a helpful message, not a traceback
- [ ] You've confirmed the output by printing a few records from `main()`

If all four are true, move to [Building the CLI](03_cli_tool.md).
