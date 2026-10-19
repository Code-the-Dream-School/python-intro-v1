# Assignment 9 — External Libraries & APIs

## Submission Instructions

1. **Make sure main is up to date:** 
      a. If your assignment last week was successful, be sure that you have merged your open Pull Request.  This will update the `main` branch with your `assignment-8` work so your main branch has a record of all your completed assignments to date. 
      b. In your terminal, use the `git pull origin main` command so your local `main` matches your GitHub `main`.
2. **Create your branch:** From `main`, create a new `assignment-9` branch in your `python-intro-homework` repo.
3. **Create your folder:** Inside `week-9/`, create a new `assignment-9/` folder and do all your work there.
4. **Submit two links in CTD Learns:**
   - **URL1:** A link to your pull request from `assignment-9` into `main`
   - **URL2:** A link to your video reflection

The PR URL should look like `github.com/your-username/python-intro-homework/pull/[number]`, *not the link to your repo homepage*.

---

## Before You Start: Get Your API Key

The REST Countries API used in Warmup 3 and the mini-project requires a free API key. Real-world APIs almost always work this way, so this is good practice for the kind of setup you will do on the job.

**Set up your key:**

1. Go to [restcountries.com/sign-up](https://restcountries.com/sign-up) and create a free account with your email and a password.
2. Confirm your email address by clicking the link that REST Countries sends you.
3. Sign in, open your account dashboard, and copy your API key.

Your free account includes **1,000 requests per month**. That is plenty for this assignment, as long as you fetch the data once when your script starts instead of fetching inside a loop.

**Keep your key out of your code.** Your key is tied to your account, and your repository is public — anyone could copy a key that you push to GitHub. Store it in an environment variable instead, and read it with the `os` module from Week 7:

```python
import os

API_KEY = os.environ.get("RESTCOUNTRIES_API_KEY")

if not API_KEY:
    print("No API key found. Set RESTCOUNTRIES_API_KEY and try again.")
    exit()
```

Set the variable in your terminal before you run your script:

- **macOS / Linux:** `export RESTCOUNTRIES_API_KEY="your_key_here"`
- **Windows PowerShell:** `$env:RESTCOUNTRIES_API_KEY="your_key_here"`

This lasts for your current terminal session, so set it again each time you open a new terminal.

**Send your key with every request.** The API expects your key in an `Authorization` header. Without it, every request comes back with a `401` status code and no data:

```python
headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get(url, headers=headers)
```

You also need `requests` installed in your virtual environment (`pip install requests`), and your `requirements.txt` should be up to date.

---

## Part 1: Warmup Exercises

Complete each of the following short exercises as a separate Python file.

---

### Warmup 1: Make Your First API Request

Use `requests.get()` to fetch from this endpoint:

```
https://api.agify.io/?name=michael
```

Print the HTTP status code and the full JSON response. The example below shows the format — this is a live API whose data changes, so your age and count will differ:

```
Status code: 200
Response: {'name': 'michael', 'age': 40, 'count': 112758}
```

**Save as:** `warmup1.py`

---

### Warmup 2: Access Specific JSON Fields

Using the same API from Warmup 1, access and print just the `name` and `age` fields from the response. Then try accessing a key that doesn't exist (e.g., `"birthday"`) — use `.get()` to avoid a `KeyError` and print a fallback message instead. The example below shows the format — the predicted age comes from a live API and will differ, and your fallback wording is your own:

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
https://api.restcountries.com/countries/v5/region/Europe?response_fields=names.common,population
```

Loop through the response list and print the common name of each country on its own line. Print only the first 10 results. The example below shows the format — it is truncated, and your results come from a live API, so they might differ:

```
Albania
Andorra
Austria
...
```

> **Hint:** The countries come back inside the response, at `response.json()["data"]["objects"]`. Each item in that list is a dict, and the country name is nested: `item["names"]["common"]`.

**Save as:** `warmup3.py`

---

### Warmup 4: Handle Request Errors

Write a script that wraps a `requests.get()` call in `try`/`except requests.exceptions.RequestException` to handle network errors. Also check the response status code — if it's not 200, print an error message instead of trying to parse the response.

Test it by using a URL you know will fail (e.g., `https://thisurldoesnotexist.example.com`). The example below shows the format — your message wording might differ:

```
Error: Could not reach the server. Check your connection and try again.
```

**Save as:** `warmup4.py`

---

## Part 2: Mini-Project — Country Explorer CLI

Use the REST Countries API to build an interactive command-line tool. This is the same API recommended for the final project, so treat this as a practice run.

**Fetch URL:**
```
https://api.restcountries.com/countries/v5?response_fields=names.common,capitals,region,population
```

**Sample Response:**
```
{
    "data": {
        "objects": [
            {
                "names": {
                    "official": "Republic of Albania"
                },
                "capitals": [
                    {
                        "attributes": {
                            "administrative": false,
                            "constitutional": false,
                            "executive": false,
                            "judicial": false,
                            "legislative": false,
                            "primary": true
                        },
                        "coordinates": {
                            "lat": 41.32,
                            "lng": 19.82
                        },
                        "name": "Tirana"
                    }
                ],
                "region": "Europe",
                "population": 2335930,
                "_match": [
                    {
                        "path": "region",
                        "value": "Europe"
                    }
                ],
                "_meta": {
                    "lastUpdatedTimestamp": 1783787495
                }
            },
            {
                "names": {
                    "official": "Principality of Andorra"
                },
                "capitals": [
                    {
                        "attributes": {
                            "administrative": false,
                            "constitutional": false,
                            "executive": false,
                            "judicial": false,
                            "legislative": false,
                            "primary": true
                        },
                        "coordinates": {
                            "lat": 42.5,
                            "lng": 1.52
                        },
                        "name": "Andorra la Vella"
                    }
                ],
                "region": "Europe",
                "population": 89752,
                "_match": [
                    {
                        "path": "region",
                        "value": "Europe"
                    }
                ],
                "_meta": {
                    "lastUpdatedTimestamp": 1786028454
                }
            },...
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

Include the video link in the `URL2` field in the submission form.

---

## Need a GitHub Review?

<details>
<summary>Weekly Git workflow reference (click to expand)</summary>

## Review: The GitHub Cycle

This is your repeatable workflow for every assignment. Wherever you see `assignment-N`, replace `N` with the current assignment number (e.g. `assignment-9`) and use the same branch name in every command for that assignment.

**Get a clean starting point:**

```bash
git checkout main
git pull origin main
git checkout -b assignment-N   # replace N: e.g. assignment-9
```

`origin` is your fork. `git pull origin main` syncs your local main with your fork on GitHub; it's normal to see "Already up to date."

**Save your progress:**

```bash
git status                    # see what's changed (run this often)
git add .                     # stage all changes
git commit -m "describe what you did and why"
git push origin assignment-N  # send your branch to GitHub
```

Repeat `add → commit → push` as often as you like. Committing often gives you more points to return to if something goes wrong.

**Open your pull request:**

On GitHub, open a pull request from `assignment-N` into main. Confirm the base repository is your own fork (`your-username/python-intro-homework`), not `Code-the-Dream-School`.

**Submit your assignment:**

Use the button on the bottom of your lesson page to submit the link to your pull request.

**Close the loop:**

Assignment successful? You can merge your Pull Request.  

Assignment needs revisions?  Make your corrections on your local branch, and be sure to add, commit, and push them.  No need for a new pull request, when you push the changes your open pull request will reflect those new changes.  Resubmit your work the same way you first submitted - same pull request link too! - and you should see success.  

Problems?  Remember to connect with 1:1 mentors if you are experiencing any trouble with this GitHub Cycle.

Once you merge your pull request, be sure your local `main` branch also gets updated by running the following locally in your terminal:

```bash
git checkout main
git pull origin main          # bring the merged changes back to your local machine
```

**If something looks off:**

* Committed to main by accident? (You forgot to create your branch first.) Make the branch now: `git checkout -b assignment-N` carries your latest commits with it, then continue. Your work isn't lost.
* `git push` says your branch has "no upstream"? You haven't pushed this branch before. Run `git push origin assignment-N` to create it on your fork.
</details>

---

<details>
<summary>Rubric (for AirHub reviewer and mentors)</summary>

### Required Deliverables/Tasks

Work happens in the student's forked `python-intro-homework` repo, on an
`assignment-9` branch, with files inside a `week-9/assignment-9/` folder.
`Example — adapt to your own layout`: the folder path and repo location are
organizational conventions — do NOT fail correct code for sitting in a different
folder or path; the reviewer cannot see the student's filesystem. Submission
mechanics (branch, PR base) are not graded from the code. This repo is
cumulative — folders from earlier weeks are expected to remain; do not tell the
student to remove prior-week work. The assignment assumes the virtual environment
and `requirements.txt` from Assignment 8; the reviewer cannot see either, so do
not fail their absence. Expected files: `warmup1.py`, `warmup2.py`, `warmup3.py`,
`warmup4.py`, `mini_project.py`.

**This assignment calls live APIs, so almost nothing about the returned data can
be verified.** Every value in every example — ages, counts, country names,
capitals, populations — comes from a live service and changes over time. Grade the
code's structure and behavior, never the specific values it prints. **Do not fail a
student for which key names they used to reach the data** — any reasonable parsing
of the response they actually received is correct.

**On the API key:** the REST Countries endpoints require a free key that each student
signs up for themselves. **The reviewer cannot see a student's key**, because the
assignment tells them to keep it in an environment variable rather than in the code —
so an absent key value is expected and must NEVER be failed, and neither is a missing
`.env` file, dashboard, or terminal setup. What *can* be checked in the code: that the
request sends an `Authorization` header carrying the key, and that the key is read from
the environment (for example with `os.environ.get()`) instead of being written
literally in the file. A key hardcoded into a committed file is worth flagging, since
the assignment explicitly tells students not to do that.

- **Warmup 1 — Make Your First API Request** — uses `requests.get()` against the
  agify endpoint and prints both the HTTP status code and the full JSON response.
  `Use exactly as written`: `requests.get()`. Required: both the status code and
  the parsed response body are printed. `Example — adapt to your own layout`: the
  age and count values (live data — the example's `age: 40, count: 112758` is
  already out of date), and all label wording.
- **Warmup 2 — Access Specific JSON Fields** — prints the `name` and `age` fields
  from the same API, then uses `.get()` for a key that does not exist and prints a
  fallback instead of raising `KeyError`. `Use exactly as written`: `.get()` for
  the missing key. Required: two real fields printed, plus a fallback for the
  missing one. `Example — adapt to your own layout`: the age value, the choice of
  missing key, and the fallback wording ("Not available").
- **Warmup 3 — Loop Through a JSON List** — fetches the region endpoint, loops the
  returned list, and prints one country name per line, limited to the first 10.
  Required: a loop over the response list, one name per line, and a limit of 10
  results. `Example — adapt to your own layout`: the country names and their order
  (live data), and which name field was used. Required: the request sends the
  student's API key in an `Authorization` header — without it this endpoint returns
  `401` and no data.
- **Warmup 4 — Handle Request Errors** — wraps `requests.get()` in
  `try`/`except requests.exceptions.RequestException` and also checks the status
  code, printing an error message rather than parsing when the request fails or
  the code is not 200. `Use exactly as written`: `except
  requests.exceptions.RequestException`, and a status-code check against 200.
  Required: both guards are present — the exception handler and the status check.
  `Example — adapt to your own layout`: the failing URL used for the test and the
  error message wording.
- **Mini-Project — Country Explorer CLI (`mini_project.py`)** — fetches all
  countries once at startup, parses them into a list of dictionaries carrying a
  name, capital, region, and population for each, then runs a `while`-loop menu
  with three options (1 search by name, 2 filter by region, 3 quit) that
  redisplays until the user quits. Required, because the assignment states each
  one: option 1 does a **case-insensitive partial** match and prints each match
  with capital, region, and population; option 2 filters by region and prints the
  results **sorted by population, largest first**; countries with no capital
  display `N/A` rather than crashing; and the initial request is wrapped in
  `try`/`except` with a status-code check that prints a message and exits on
  failure. `Example — adapt to your own layout`: the menu text and layout, all
  separators and message wording, the number formatting (thousands separators are
  not required), and every country value shown — names, capitals, regions, and
  populations all come from a live API. The dictionary keys the student chooses
  are their own, so do not fail a different key structure. Required: the request
  sends the student's API key in an `Authorization` header, and the data is fetched
  once at startup rather than on every menu action (the free plan allows 1,000
  requests per month).
- **Video reflection (URL2)** — a required submission, but it is not part of the
  code and is not assessed here. Do not fail the code submission for anything
  about the video.

### Optional Deliverables/Tasks

**None.**

</details>
