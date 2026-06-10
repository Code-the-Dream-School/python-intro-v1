# Connecting API Data to Dicts and Lists

**Objective**: By the end of this lesson, you will be able to:
  * Navigate nested JSON structures by chaining key lookups
  * Extract specific fields from a raw API response
  * Build a clean list of dicts from API data using a loop
  * Handle missing keys safely using `.get()`
  * Write a reusable function that fetches and returns structured data

---

## Navigating Nested JSON

A real API response is rarely a flat dictionary. Most responses are **nested** — dicts containing lists containing more dicts. Learning to trace through this structure is the main challenge of working with APIs.

Here's a simplified version of what one entry looks like from the [REST Countries API](https://restcountries.com/):

```json
{
  "name": {
    "common": "Finland",
    "official": "Republic of Finland"
  },
  "capital": ["Helsinki"],
  "region": "Europe",
  "population": 5530719
}
```

Notice:
- `"name"` is itself a dict with multiple keys — it's nested one level deep
- `"capital"` is a **list** (some countries have multiple capitals)
- `"region"` and `"population"` are flat values you can access directly

If Python stored one of these entries in a variable called `country`, here's how you'd reach each field:

```python
country["name"]["common"]     # "Finland"  — access the nested dict, then the key
country["name"]["official"]   # "Republic of Finland"
country["capital"][0]         # "Helsinki"  — capital is a list, take index 0
country["region"]             # "Europe"
country["population"]         # 5530719
```

When you encounter a new API response, **slow down and trace the structure before writing code**. Ask yourself: *is this value a dict, a list, or a plain value? What keys or indices do I need to get where I'm going?*

---

## Extracting Fields from a Response

Once you understand the structure, extracting the fields you need is straightforward. Here's how you fetch a list of European countries and look at the raw response:

```python
import requests

response = requests.get(
    "https://restcountries.com/v3.1/region/europe",
    params={"fields": "name,capital,region,population"}
)
response.raise_for_status()
countries = response.json()   # countries is a list of dicts

print(type(countries))        # <class 'list'>
print(len(countries))         # 44 (number of countries returned)
print(countries[0])           # the first country dict, raw from the API
```

The full response is a **list**, so `countries[0]` gives you the first item — one country dict in its raw nested form.

---

## Building a Clean List of Dicts

Raw API data often contains more fields than you need and can be awkward to work with (like that nested `"name"` dict or the `"capital"` list). A common pattern is to **transform** the raw data into a cleaner, flatter structure before using it elsewhere in your program:

```python
cleaned = []

for country in countries:
    cleaned.append({
        "name": country["name"]["common"],
        "capital": country["capital"][0] if country.get("capital") else "N/A",
        "region": country["region"],
        "population": country["population"]
    })

print(cleaned[0])
# Output: {'name': 'Finland', 'capital': 'Helsinki', 'region': 'Europe', 'population': 5530719}
```

Now `cleaned` is a list of flat, consistent dicts. Notice how similar this is to the list-of-dicts you built when parsing CSV files in Week 7 — the pattern shows up everywhere data comes from an external source.

---

## Handling Missing Data with `.get()`

Not every country in the API response has a capital. Some territories have no capital city, so the `"capital"` key is absent entirely. Accessing a missing key with `country["capital"]` raises a `KeyError` and crashes your program.

`.get()` provides a safe alternative:

```python
# Risky — raises KeyError if "capital" is missing
capital = country["capital"][0]

# Safe — returns None if "capital" is missing, then we handle it
capital_list = country.get("capital")
capital = capital_list[0] if capital_list else "N/A"
```

The second version reads as: *"if the country has a capital list and it's not empty, take the first item; otherwise use 'N/A'."*

You can write this as a one-liner:

```python
capital = country["capital"][0] if country.get("capital") else "N/A"
```

Whenever you're pulling data out of an API response, ask: *could this key be missing?* If there's any chance it could be, use `.get()`.

---

### AI Prompt: Scaffold Removal

Before moving on, try this on your own.

Write a function called `largest_by_population` that takes a list of country dicts in the cleaned format (with keys `"name"`, `"capital"`, `"region"`, `"population"`) and returns the **name** of the most populated country.

1. Try writing it without help first.
2. If you're stuck, open your preferred AI chatbot:
   - *"I'm writing a Python function that finds the country with the highest population from a list of dicts. Each dict has keys 'name', 'capital', 'region', 'population'. Can you give me 3 hints without giving me the answer?"*
   - *"I wrote this function: [paste your code]. What's wrong with it? Point me to the concept I should review instead of just fixing it."*

---

## Wrapping It in a Function

Once the fetch-and-clean logic is working, put it in a function. A function that makes a request and returns structured data is the core building block of the final project:

```python
import requests

def fetch_european_countries():
    url = "https://restcountries.com/v3.1/region/europe"
    params = {"fields": "name,capital,region,population"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        countries = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    cleaned = []
    for country in countries:
        capital_list = country.get("capital")
        cleaned.append({
            "name": country["name"]["common"],
            "capital": capital_list[0] if capital_list else "N/A",
            "region": country["region"],
            "population": country["population"]
        })

    return cleaned
```

This function:
- Makes the request inside a `try/except` block
- Returns an empty list if something goes wrong (so the caller doesn't crash)
- Transforms the raw data before returning it
- Has a clear, predictable return type: a list of dicts with consistent keys

You can now call it from anywhere in your program without thinking about HTTP details:

```python
countries = fetch_european_countries()
print(f"Found {len(countries)} countries")
```

This separation — network logic in one function, display logic somewhere else — is what makes programs maintainable. It also directly mirrors how the final project is structured.

---

## Putting It All Together

Here's a complete script that fetches data, cleans it, and prints a formatted summary. This is the same structure you'll use for the assignment mini-project and the final project:

```python
import requests


def fetch_european_countries():
    url = "https://restcountries.com/v3.1/region/europe"
    params = {"fields": "name,capital,region,population"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        countries = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    cleaned = []
    for country in countries:
        capital_list = country.get("capital")
        cleaned.append({
            "name": country["name"]["common"],
            "capital": capital_list[0] if capital_list else "N/A",
            "region": country["region"],
            "population": country["population"]
        })

    return cleaned


def print_summary(countries):
    print(f"\n{'Country':<20} {'Capital':<20} {'Population':>15}")
    print("-" * 56)
    sorted_countries = sorted(countries, key=lambda c: c["population"], reverse=True)
    for c in sorted_countries[:10]:
        print(f"{c['name']:<20} {c['capital']:<20} {c['population']:>15,}")


if __name__ == "__main__":
    countries = fetch_european_countries()
    if countries:
        print_summary(countries)
```

Sample output:
```
Country              Capital              Population
--------------------------------------------------------
Russia               Moscow               144,444,359
Germany              Berlin                83,294,633
France               Paris                 68,042,591
United Kingdom       London                67,215,293
Italy                Rome                  59,037,798
...
```

Notice the two separate functions: one that knows how to fetch and parse data, and one that knows how to display it. This division of responsibility makes each piece easier to test, debug, and reuse.

---

## Videos & Further Practice

**"Working with JSON Data using the json Module"** (Corey Schafer)

[Watch the video](https://youtu.be/9N6a-VLBa2I?si=Zad1rg7c-F9i5hqq) — covers JSON parsing, reading and writing JSON, and working with nested structures in Python.

**"Python API Tutorial: Getting Started with APIs"** (Dataquest)

[Watch the video](https://youtu.be/Na8h09Goovk?si=vqnwf73rxQRKAWG1) — a practical walkthrough of fetching and parsing real API data, including nested JSON navigation.

---

## Check for Understanding

**Question 1:** A country dict from the REST Countries API looks like this:

```python
{"name": {"common": "Germany"}, "capital": ["Berlin"], "region": "Europe"}
```

How do you access the string `"Germany"`?

* A) `country["name"]`
* B) `country["name"]["common"]`
* C) `country["name"][0]`
* D) `country["common"]`

<details>
<summary>Answer</summary>

**B) `country["name"]["common"]`** — `country["name"]` returns the inner dict `{"common": "Germany"}`. You then access `"common"` on that dict to get the string. `country["name"][0]` would try to use integer index `0` on a dict, which raises a `KeyError`.

</details>

**Question 2:** You want to safely access the `"nickname"` key from a dict that might not have it. Which options are safe?

* A) `data["nickname"]`
* B) `data.get("nickname")`
* C) `data.get("nickname", "Unknown")`
* D) Both B and C are safe

<details>
<summary>Answer</summary>

**D) Both B and C are safe** — `.get("nickname")` returns `None` if the key is missing (no `KeyError`). `.get("nickname", "Unknown")` returns `"Unknown"` as the default. Both avoid crashing. Direct access with `data["nickname"]` will raise a `KeyError` if the key doesn't exist.

</details>

**Question 3:** You call `response.json()` on a REST Countries API response and get a list of 250 dicts. What expression gives you the `"region"` of the first country?

* A) `response.json()["region"]`
* B) `response.json()[0]["region"]`
* C) `response.json()["0"]["region"]`
* D) `response.json().region`

<details>
<summary>Answer</summary>

**B) `response.json()[0]["region"]`** — The response is a list, so you index it with `[0]` to get the first dict, then `["region"]` to access the field. It's often cleaner to store the parsed list first: `countries = response.json()`, then `countries[0]["region"]`.

</details>

**Question 4:** What does the following function return if the network request raises a `RequestException`?

```python
def fetch_data():
    try:
        response = requests.get("https://example-api.com/data")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return []
```

* A) `None`
* B) `{}`
* C) `[]`
* D) It re-raises the exception

<details>
<summary>Answer</summary>

**C) `[]`** — When a `RequestException` occurs, the `except` block runs and returns an empty list. This is a deliberate design choice: the caller gets back an empty list instead of a crash, and can check `if data:` before using the result.

</details>

**Question 5:** You're building a list of dicts from an API response. What is wrong with this code?

```python
result = []
for item in api_data:
    result = {"name": item["name"], "count": item["count"]}
```

* A) `api_data` should be parsed with `.json()` first
* B) `result` is being overwritten on each iteration instead of appended to
* C) The dict keys should be integers, not strings
* D) Nothing — the code is correct

<details>
<summary>Answer</summary>

**B) `result` is being overwritten on each iteration instead of appended to** — `result = {...}` replaces the variable each time through the loop, so you end up with only the last item. The fix is `result.append({...})` to add each dict to the list.

</details>

---

## Further Reading

- [requests Documentation — JSON Response Content](https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content)
- [REST Countries API Documentation](https://restcountries.com/)
- [W3Schools — Python JSON](https://www.w3schools.com/python/python_json.asp)
- [Real Python — Working with JSON Data in Python](https://realpython.com/python-json/)
