# Assignment 9 — External Libraries & APIs

## Submission Instructions

1. **Create your branch:** From `main`, create a new `assignment-9` branch in your `python-intro-homework` repo.
2. **Create your folder:** Inside `week-9/`, create a new `assignment-9/` folder and do all your work there.
3. **Submit two links in CTD Learns:**
   - **URL1:** A link to your video reflection
   - **URL2:** A link to your pull request from `assignment-9` into `main`

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

> **Note:** This assignment makes live network requests. Make sure your virtual environment has `requests` installed (`pip install requests`) and your `requirements.txt` is up to date.

---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file.

---

### Warmup 1: Make Your First API Request

Use `requests.get()` to fetch from this endpoint:

```
https://api.agify.io/?name=michael
```

Print the HTTP status code and the full JSON response:

```
Status code: 200
Response: {'name': 'michael', 'age': 40, 'count': 112758}
```

**Save as:** `warmup1.py`

---

### Warmup 2: Access Specific JSON Fields

Using the same API from Warmup 1, access and print just the `name` and `age` fields from the response. Then try accessing a key that doesn't exist (e.g., `"birthday"`) — use `.get()` to avoid a `KeyError` and print a fallback message instead:

```
Name: michael
Predicted age: 40
Birthday: Not available
```

**Save as:** `warmup2.py`

---

### Warmup 3: Loop Through a JSON List

Fetch from this endpoint, which returns a list of countries in Europe:

```
https://restcountries.com/v3.1/region/europe?fields=name,population
```

Loop through the response list and print the common name of each country on its own line. Print only the first 10 results.

```
Albania
Andorra
Austria
...
```

> **Hint:** Each item in the list is a dict. The country name is nested: `item["name"]["common"]`.

**Save as:** `warmup3.py`

---

### Warmup 4: Handle Request Errors

Write a script that wraps a `requests.get()` call in `try`/`except requests.exceptions.RequestException` to handle network errors. Also check the response status code — if it's not 200, print an error message instead of trying to parse the response.

Test it by using a URL you know will fail (e.g., `https://thisurldoesnotexist.example.com`).

```
Error: Could not reach the server. Check your connection and try again.
```

**Save as:** `warmup4.py`

---

## Part 2: Mini-Project — Country Explorer CLI

Use the REST Countries API to build an interactive command-line tool. This is the same API recommended for the final project, so treat this as a practice run.

**Fetch URL:**
```
https://restcountries.com/v3.1/all?fields=name,capital,region,population
```

Your program should:

1. Fetch all countries from the API when the script starts. Parse the JSON into a list of dictionaries, each with these keys: `name`, `capital`, `region`, `population`.
2. Display a menu in a `while` loop:

```
=== Country Explorer ===
1. Search by name
2. Filter by region
3. Quit
Choose an option (1-3):
```

3. **Search by name (option 1):** Ask for a search term and do a case-insensitive partial match against country names. Print all matches with their capital, region, and population.

```
Search: land
Finland — Capital: Helsinki | Region: Europe | Population: 5,530,719
Iceland — Capital: Reykjavik | Region: Europe | Population: 366,425
...
```

4. **Filter by region (option 2):** Ask for a region name (e.g., "Africa", "Asia", "Europe"). Print all countries in that region sorted by population (largest first).

5. **Handle missing data:** Some countries in the API response don't have a capital. Use `.get()` or a conditional to display `"N/A"` instead of crashing.

6. **Handle errors:** Wrap the initial API request in `try`/`except` and check the status code. If the request fails, print a useful message and exit.

A sample JSON excerpt for reference is available in `week-9/data/sample_countries.json` — you can open it to understand the response structure before writing your parser.

**Save as:** `mini_project.py`

---

## Video Reflection

Record a short video (3–5 minutes) on YouTube, Loom, or a similar platform and share the link in your submission.

Your video should address the following questions. You don't need to cover every sub-point in depth — aim for clear, conversational explanations over a polished script.

1. What is JSON, and how does Python's `requests` library let you work with it? What does `response.json()` actually return?
2. Walk through how your script goes from a raw API response to a list of dictionaries. What does each step do?
3. Show how your script handles a case where the API returns unexpected or missing data — for example, a country without a capital.

**Requirements:**
- Keep it to 3–5 minutes
- Use screen sharing to walk through your code when relevant
- Speak in your own words — no need to read from a script

Include the video link in your pull request description or the `URL1` field in the submission form.

---

## Need a GitHub Review?

<details>
<summary>Weekly Git workflow reference (click to expand)</summary>

**At the start of each week — get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-9
```

**As you work — save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin assignment-9  # send your branch to GitHub
```

You can repeat the `add → commit → push` steps as many times as you like within a week. Committing often gives you more points to return to if something goes wrong — you don't have to wait until you're finished.

**After your PR is merged on GitHub — close the loop:**

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```
</details>
