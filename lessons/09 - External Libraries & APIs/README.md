# Lesson 9 — External Libraries & APIs

**Lesson Overview**
Students use the `requests` library to fetch real data from the web, parse JSON responses, and connect that data back to the Python structures they already know. This week is the direct foundation for the final project.

## Topics

1. **[The requests Library and JSON Parsing](01_requests_json.md)**
   *New content*
   Installing `requests` via pip; making a GET request with `requests.get()`; understanding HTTP status codes (200, 404, etc.); parsing a JSON response with `.json()`; the relationship between JSON and Python dicts/lists

2. **[Calling a Public API and Handling the Response](02_calling_apis.md)**
   *New content*
   What an API is and how public APIs work; reading API documentation to find endpoints and parameters; query parameters in URLs; combining `requests` with `try/except` for robust API calls; working with API keys (conceptual, using a keyless public API for practice)

3. **[Connecting API Data to Dicts and Lists](03_api_data_structures.md)**
   *New content*
   Navigating nested JSON (dicts inside lists inside dicts); extracting and transforming relevant fields; building a clean list of dicts from raw API response data; writing a function that fetches and returns structured data
