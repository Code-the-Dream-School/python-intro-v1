# Connecting API Data to Dicts and Lists

> **Source:** New content — not in Python Essentials
>
> **Notes:** This section closes the loop between API responses and the data structures from Week 5. Cover:
> - Navigating nested JSON: a response is often a dict containing a list of dicts containing more dicts — students need to trace through multiple levels (e.g., `data["results"][0]["title"]`)
> - Extracting specific fields and building a clean list of dicts from raw response data
> - Writing a `fetch_and_parse()` function that takes a URL and query params, makes the request, and returns a structured list of dicts — connecting Week 6 (functions) and Week 9 (APIs)
> - Handling missing keys gracefully with `.get()` instead of direct `[]` access
> - A complete mini-project: fetch data from the week's chosen API, extract 3-5 fields per result, print a formatted summary
> This section directly previews the final project core requirements.

TBD
