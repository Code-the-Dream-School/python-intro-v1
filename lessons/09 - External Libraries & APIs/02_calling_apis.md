# Calling a Public API and Handling the Response

> **Source:** New content — not in Python Essentials
>
> **Notes:** Students go deeper on working with APIs. Cover:
> - What an API is at a conceptual level (a defined interface for requesting data from a server)
> - Reading API documentation: how to find an endpoint, what query parameters it accepts, what the response structure looks like
> - Adding query parameters to a request: `requests.get(url, params={"q": "weather"})`
> - Wrapping the call in `try/except` to handle `requests.exceptions.RequestException`
> - Checking response status and raising for bad responses: `response.raise_for_status()`
> - A practical walkthrough: pick a specific public API (e.g., Open-Meteo for weather, NASA Astronomy Picture of the Day, or PokeAPI) and walk through finding the docs, making the call, and reading the response
> - Brief conceptual mention of API keys and authentication (students use a keyless API for practice)

TBD
