# Lesson 9 — External Libraries & APIs

**Lesson Overview**
Up to this point, all the data your programs have worked with came from inside the program itself — values you typed, files you saved, input you collected. This week that changes. You'll learn how to reach out to the internet and pull in live data from public APIs: weather, countries, predictions, and more.

The tools are new (the `requests` library, JSON, HTTP status codes) but the underlying structures aren't. Once you fetch an API response and parse it, you'll find yourself right back in familiar territory: dicts, lists, loops, and functions. Everything you've built over the past eight weeks comes together here, and it's a direct preview of the final project.

**Learning Objectives**

This week, I can...

* Mke a GET request with `requests.get()` and parse the JSON response.
* Read API documentation, construct a request with query parameters, and handle common HTTP status codes.
* Navigate nested JSON and build a clean list of dictionaries from raw API response data.

## Topics

1. **[The requests Library and JSON Parsing](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/lessons/09%20-%20External%20Libraries%20%26%20APIs/01_requests_json.md)**
   
   Installing `requests` via pip; making a GET request with `requests.get()`; understanding HTTP status codes (200, 404, etc.); parsing a JSON response with `.json()`; the relationship between JSON and Python dicts/lists

2. **[Calling a Public API and Handling the Response](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/lessons/09%20-%20External%20Libraries%20%26%20APIs/02_calling_apis.md)**
   
   What an API is and how public APIs work; reading API documentation to find endpoints and parameters; query parameters in URLs; combining `requests` with `try/except` for robust API calls; working with API keys (conceptual, using a keyless public API for practice)

3. **[Connecting API Data to Dicts and Lists](https://github.com/Code-the-Dream-School/python-intro-v1/blob/main/lessons/09%20-%20External%20Libraries%20%26%20APIs/03_api_data_structures.md)**
   
   Navigating nested JSON (dicts inside lists inside dicts); extracting and transforming relevant fields; building a clean list of dicts from raw API response data; writing a function that fetches and returns structured data
