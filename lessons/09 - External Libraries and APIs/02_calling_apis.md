# Calling a Public API and Handling the Response

**Objective**: By the end of this lesson, you will be able to:
  * Explain what an API is and how client-server communication works
  * Read API documentation to find endpoints and query parameters
  * Pass query parameters to a GET request using `requests.get(url, params={})`
  * Wrap an API call in `try/except` to handle network errors
  * Use `raise_for_status()` to catch unsuccessful responses

---

## What is an API?

You've now made a GET request and parsed a JSON response. But what exactly are you communicating with?

An **API** (Application Programming Interface) is a defined way for programs to talk to each other. In the context of web APIs, a server publishes a set of URLs you can call to request data or trigger actions — and it promises to respond in a predictable format.

Think of it like a restaurant:
- You (the client) don't go into the kitchen to make your food.
- Instead, you look at a **menu** (the API documentation) that describes what's available.
- You place an **order** (the HTTP request) through the waiter (the API endpoint).
- The waiter returns with your **food** (the JSON response).

When you called `https://api.agify.io/?name=michael` in the previous lesson, you were sending a request to Agify's servers asking for data about that name. The server processed it and returned a structured JSON response. You didn't need to know anything about how Agify stores or calculates that data — you just needed to know the URL and what to send.

---

## Reading API Documentation

Every well-designed API comes with **documentation** that describes what endpoints exist, what parameters they accept, and what the response looks like. Learning to read API docs quickly is a skill you'll use constantly as a developer.

Let's look at a real example: the **Open-Meteo Weather API** (`open-meteo.com`). It's free, requires no API key, and returns real weather forecast data.

From the Open-Meteo docs, you learn:
- **Base URL:** `https://api.open-meteo.com/v1/forecast`
- **Required parameters:** `latitude` and `longitude` (the location you want weather for)
- **Optional parameters:** `current_weather=true` to include current conditions in the response
- **Response format:** A JSON object with a `current_weather` key containing temperature, wind speed, and more

The docs also show a sample response so you can plan how to parse it before writing any code. Always read the example response first — it's the most important part of any API doc.

---

## Query Parameters

A URL can carry additional information using **query parameters** — key-value pairs appended after a `?` in the URL:

```
https://api.open-meteo.com/v1/forecast?latitude=35.78&longitude=-78.64&current_weather=true
```

Breaking this down:
- `?` marks the start of the query string
- `latitude=35.78` is one parameter
- `&` separates multiple parameters
- `longitude=-78.64` and `current_weather=true` are additional parameters

You *could* build this URL manually as a string, but `requests` gives you a cleaner way — the `params` argument:

```python
import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 35.78,
    "longitude": -78.64,
    "current_weather": True
}

response = requests.get(url, params=params)
print(response.url)   # requests builds the full URL for you
```

Output:
```
https://api.open-meteo.com/v1/forecast?latitude=35.78&longitude=-78.64&current_weather=True
```

Using `params={}` keeps your code readable and handles URL encoding automatically (like converting spaces to `%20`). Always prefer this over manually concatenating strings into a URL.

---

### AI Prompt: Predict-Then-Check

Look at this code before running it:

```python
import requests

url = "https://api.agify.io/"
params = {"name": "sofia"}

response = requests.get(url, params=params)
print(response.status_code)
print(response.json())
```

1. Predict what the status code and JSON output will be. What age do you think the API will predict for the name "sofia"?
2. Open your preferred AI chatbot and share your prediction:

> "I'm learning Python's `requests` library and query parameters. I predict this code will output [your prediction] because [your reasoning]. Am I correct? If not, what am I misunderstanding?"

3. Then run the code to verify.

---

## Handling Errors Robustly

Network requests can fail in two distinct ways:

1. **The request never reaches the server** — your internet is down, the URL is wrong, or the server is unreachable. This raises a `requests.exceptions.RequestException`.
2. **The server responds, but with an error code** — the request reached the server, but something went wrong on either end. The status code tells you what happened.

You need to handle both.

### Catching Network Errors with try/except

Wrap your `requests.get()` call to handle connection problems gracefully:

```python
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 35.78, "longitude": -78.64, "current_weather": True}

try:
    response = requests.get(url, params=params)
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
```

`requests.exceptions.RequestException` is the parent class for all requests-related errors — including `ConnectionError`, `Timeout`, and `TooManyRedirects`. Catching this one exception covers all network-level failures.

### Checking the Status Code

After a successful connection, check the status code before parsing the response:

```python
try:
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Request failed: status {response.status_code}")
    else:
        data = response.json()
        # work with data here
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
```

### Using raise_for_status()

`raise_for_status()` is a shortcut: it automatically raises an `HTTPError` for any 4xx or 5xx status code, so you don't have to check manually.

```python
try:
    response = requests.get(url, params=params)
    response.raise_for_status()   # raises HTTPError for 4xx or 5xx
    data = response.json()
    # work with data here
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

This is the pattern you'll see in professional code and the one you'll use for the rest of this course. A single `except requests.exceptions.RequestException` catches both connection errors and HTTP errors raised by `raise_for_status()`.

---

## A Practical Walkthrough

Let's put everything together. The goal: fetch the current temperature and wind speed for a given location using Open-Meteo.

```python
import requests

def get_current_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Could not fetch weather data: {e}")
        return

    weather = data["current_weather"]
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Wind speed:  {weather['windspeed']} km/h")

get_current_weather(35.78, -78.64)   # Raleigh, NC
```

Sample output:
```
Temperature: 14.2°C
Wind speed:  11.3 km/h
```

Notice the structure: build the URL and params → make the request → raise for status → parse the JSON → access the data you need. This is the pattern for nearly every API call you'll write.

---

## API Keys (Conceptual)

Many APIs require **authentication** to identify who is making requests and to limit usage. The most common method is an **API key** — a unique string you include with every request, either as a query parameter or in a request header:

```python
# API key as a query parameter
params = {"api_key": "your-key-here", "city": "Raleigh"}

# API key as a header
headers = {"Authorization": "Bearer your-key-here"}
response = requests.get(url, params=params, headers=headers)
```

API keys let the server identify your account, enforce rate limits, and charge you if the service isn't free.

**This week you'll use keyless public APIs**. But as you build bigger projects with CTD, you'll encounter APIs that require keys. When you do: **never paste an API key directly into your Python file.** Instead, store them in a .env file at the root of your project and read them with the python-dotenv library. This will be our standard practice in future Python courses.

---

## Videos

**"What is a REST API?"** (IBM Technology)

[Watch the video](https://youtu.be/lsMQRaeKNDk?si=WaOmFTTduUjiVgpa) — a short conceptual explainer that will deepen your mental model of how APIs work before you dig into more complex code.

---

## Check for Understanding

**Question 1:** You want to call `https://example-api.com/data?city=Raleigh&limit=10`. What is the best way to pass those query parameters using `requests`?

* A) Build the full URL manually as an f-string
* B) `requests.get(url, params={"city": "Raleigh", "limit": 10})`
* C) `requests.post(url, data={"city": "Raleigh"})`
* D) There's no way to pass parameters with `requests`

<details>
<summary>Answer</summary>

**B) `requests.get(url, params={"city": "Raleigh", "limit": 10})`** — The `params` argument is the cleanest approach. `requests` handles URL encoding automatically, whereas manually building the URL as an f-string is fragile and can break with special characters.

</details>

**Question 2:** What does `response.raise_for_status()` do?

* A) Raises an exception for any response, successful or not
* B) Prints the status code to the console
* C) Raises an `HTTPError` if the response status code is 4xx or 5xx
* D) Returns the status code as an integer

<details>
<summary>Answer</summary>

**C) Raises an `HTTPError` if the response status code is 4xx or 5xx** — `raise_for_status()` does nothing for successful 2xx responses, but raises an `HTTPError` for client errors (4xx) and server errors (5xx). Because `HTTPError` is a subclass of `RequestException`, your existing `except requests.exceptions.RequestException` block catches it.

</details>

**Question 3:** Your code raises `requests.exceptions.ConnectionError`. What most likely happened?

* A) The server returned a 404 status code
* B) The JSON response was malformed
* C) Your code had a syntax error
* D) The request couldn't reach the server at all

<details>
<summary>Answer</summary>

**D) The request couldn't reach the server at all** — `ConnectionError` means the network request failed before getting any response. This can happen if the URL is wrong, your internet is down, or the server is unreachable. A 404 response, by contrast, *did* reach the server — it just told you the resource doesn't exist.

</details>

**Question 4:** Which exception should you catch to handle all requests-related errors — including both `ConnectionError` and errors raised by `raise_for_status()`?

* A) `Exception`
* B) `requests.exceptions.RequestException`
* C) `requests.exceptions.HTTPError`
* D) `ValueError`

<details>
<summary>Answer</summary>

**B) `requests.exceptions.RequestException`** — This is the base class for all exceptions in the `requests` library. Catching it handles `ConnectionError`, `Timeout`, `TooManyRedirects`, and `HTTPError` (raised by `raise_for_status()`) with one `except` clause. `HTTPError` alone would miss connection problems, and catching bare `Exception` is too broad.

</details>

**Question 5:** An API requires a query parameter `units` with the value `"metric"`. Without it, the server returns a 400 error. What is missing from this code?

```python
response = requests.get("https://example-api.com/weather")
```

* A) A `headers` argument
* B) A `params={"units": "metric"}` argument
* C) A `try/except` block
* D) Nothing — the code is correct

<details>
<summary>Answer</summary>

**B) A `params={"units": "metric"}` argument** — The request is missing the required query parameter. The corrected version: `requests.get("https://example-api.com/weather", params={"units": "metric"})`.

</details>

---

## Further Reading

- [requests Documentation — Passing Parameters In URLs](https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls)
- [requests Documentation — Errors and Exceptions](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions)
- [Open-Meteo API Documentation](https://open-meteo.com/en/docs)
- [MDN Web Docs — What is an API?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-server_websites/Introduction_to_APIs)
