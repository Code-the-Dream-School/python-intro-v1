# The requests Library and JSON Parsing

> **Source:** New content — not in Python Essentials
>
> **Notes:** Students install `requests` (their first real third-party package install in this course) and make their first HTTP call. Cover:
> - Installing `requests` with `pip install requests`
> - Making a GET request: `response = requests.get(url)`
> - Checking `response.status_code` and what 200/404/500 mean
> - Parsing the response body: `response.json()` returns a Python dict or list
> - The relationship between JSON and Python: JSON objects → dicts, JSON arrays → lists, JSON null → None
> - A minimal but complete working example using a simple public API (e.g., `https://api.open-meteo.com` or `https://jsonplaceholder.typicode.com`)
> - Common errors: `ConnectionError`, `JSONDecodeError`, non-200 status

TBD
