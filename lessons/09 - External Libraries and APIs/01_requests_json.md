# The requests Library and JSON Parsing

**Objective**: By the end of this lesson, you will be able to:
  * Install a third-party library using `pip`
  * Make an HTTP GET request using `requests.get()`
  * Read a response status code to determine whether a request succeeded
  * Parse a JSON response using `.json()`
  * Describe the relationship between JSON and Python's built-in data structures

---

## Getting Started: Installing requests

In Week 8 you learned what `pip` is and how Python's package ecosystem works. Now you'll install your first third-party library for this project (`requests`) which makes it straightforward to fetch data from URLs.

Make sure your virtual environment is activated, then run:

```bash
pip install requests
```

Once installed, update your `requirements.txt` so anyone else running your project can install the same dependencies:

```bash
pip freeze > requirements.txt
```

Now you can use `requests` in any Python script by importing it at the top:

```python
import requests
```

---

## Making Your First Request

A **GET request** asks a server to send you some data. It's the same thing your browser does every time you navigate to a URL: the browser sends a GET request and the server sends back a web page. With `requests`, you do this in one line:

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response)
```

Output:
```
<Response [200]>
```

The `response` object contains everything the server sent back: the status code, the body, the headers. You'll be working with it a lot this week!

---

## HTTP Status Codes

Before you try to use the response data, it's worth checking whether the request actually worked. Every HTTP response includes a **status code** — a three-digit number that tells you the outcome.

```python
print(response.status_code)   # Output: 200
```

The most common codes you'll encounter:

| Code | Meaning | What it tells you |
|------|---------|-------------------|
| `200` | OK | Request succeeded — data is in the response body |
| `400` | Bad Request | Your request had a problem (wrong parameters, etc.) |
| `401` | Unauthorized | You need authentication (an API key) |
| `404` | Not Found | The URL or resource doesn't exist |
| `429` | Too Many Requests | You're making requests too quickly |
| `500` | Internal Server Error | Something went wrong on the server's side |

`200` means success. Codes starting with `4xx` indicate a client-side problem (something about your request). Codes starting with `5xx` indicate a server-side problem.

---

## Reading the Response Body

The server's response comes back as raw text. The `requests` library gives you two ways to access it:

### As raw text

```python
print(response.text)
```

Output (a string):
```
'{\n  "userId": 1,\n  "id": 1,\n  "title": "sunt aut facere...",\n  "body": "quia et suscipit..."\n}'
```

This is the response as a **string**. It looks like a Python dict, but it's just text that happens to be formatted as JSON.

### As a Python object

```python
data = response.json()
print(data)
```

Output (a Python dict):
```
{'userId': 1, 'id': 1, 'title': 'sunt aut facere...', 'body': 'quia et suscipit...'}
```

`.json()` parses the raw text and returns an actual Python object you can work with immediately — access its keys, loop over it, pass it to functions. Everything you've been doing with dicts and lists all course applies here.

---

## JSON and Python: The Connection

**JSON** (JavaScript Object Notation) is the most common format for exchanging data on the web. You'll encounter it in almost every API response. Fortunately, it maps almost perfectly onto Python's built-in data structures:

| JSON type | Python type | Example |
|-----------|-------------|---------|
| Object `{}` | `dict` | `{"name": "Jazmine"}` |
| Array `[]` | `list` | `[1, 2, 3]` |
| String | `str` | `"hello"` |
| Number | `int` or `float` | `42`, `3.14` |
| `true` / `false` | `True` / `False` | |
| `null` | `None` | |

When you call `.json()`, Python reads the raw JSON text and converts every value using this mapping. The result is a regular Python dict or list — use it exactly as you would any other.

---

### AI Prompt: Retrieval Practice

You've just learned how JSON maps to Python. Let's make sure it sticks.

1. Without looking at the table above, explain in your own words how JSON types map to Python types.
2. Open your preferred AI chatbot (ChatGPT, Microsoft Copilot, etc.) and share your explanation:

> "I just learned about the relationship between JSON data types and Python data types. Here's my understanding: [your explanation]. What did I get right, and what should I refine?"

---

## A Complete Working Example

Let's put it all together with a real API. The [Agify API](https://agify.io/) predicts a person's age based on their name.

```python
import requests

url = "https://api.agify.io/?name=michael"
response = requests.get(url)

print("Status code:", response.status_code)
# Output: Status code: 200

data = response.json()
print(data)
# Output: {'name': 'michael', 'age': 40, 'count': 112758}

print("Predicted age:", data["age"])
# Output: Predicted age: 40
```

Try changing `"michael"` to your own name and see what the API predicts. How close was it? Post the result in your #class-discussion channel!

---

## Common Errors

Things can go wrong when making network requests. Here are the three situations you'll most often encounter:

### ConnectionError: Can't reach the server

If the URL is wrong, your internet is down, or the server is unreachable, you'll get a `requests.exceptions.ConnectionError`:

```
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='...')
```

### Non-200 status code: Request failed

If the server responds with a 404 or 500, `.json()` might still run (some APIs return JSON error messages), but the data won't be what you wanted. Always check `status_code` before parsing:

```python
if response.status_code != 200:
    print(f"Something went wrong: {response.status_code}")
else:
    data = response.json()
```

### JSONDecodeError: Response isn't valid JSON

If the server sends back HTML (like an error page) instead of JSON, calling `.json()` raises a `JSONDecodeError`. This usually happens alongside a non-200 status code.

In the next lesson, you'll learn how to wrap all of this in `try/except` for clean, robust error handling. For now, just know these errors exist and what causes them.

---

## Videos

**"Python Requests Tutorial: Request Web Pages, Download Images, POST Data, Read JSON, and More"** (Corey Schafer)

[Watch the video](https://youtu.be/tb8gHvYlCFs?si=MhcNUpU6CV9Bk-9v) — covers making GET requests, reading responses, and working with JSON data.

**"APIs for Beginners — How to use an API (Full Course / Tutorial)"** (freeCodeCamp.org)

[Watch the video](https://youtu.be/WXsD0ZgxjRw?si=-6Bgl7YQdepwlUbP) — a longer conceptual overview of how APIs work. Good background to have before diving deeper into the code.

---

## Check for Understanding

**Question 1:** What does `requests.get()` return?

* A) A string containing the server's response
* B) A dict with the JSON data
* C) A Response object
* D) An HTTP status code

<details>
<summary>Answer</summary>

**C) A Response object** — `requests.get()` returns a `Response` object that contains the status code, body, headers, and more. You access the body with `.text` (raw string) or `.json()` (parsed Python object).

</details>

**Question 2:** A server responds with status code `404`. What does this mean?

* A) The request succeeded
* B) You're not authenticated
* C) The resource was not found
* D) The server had an internal error

<details>
<summary>Answer</summary>

**C) The resource was not found** — `404 Not Found` means the URL you requested doesn't exist or the resource isn't available. `200` is success, `401` is unauthorized, and `500` is a server-side error.

</details>

**Question 3:** You call `response.json()` and get back a list. What did the server's JSON response look like?

* A) A JSON object: `{}`
* B) A JSON array: `[]`
* C) A JSON string
* D) It could be any type

<details>
<summary>Answer</summary>

**B) A JSON array: `[]`** — `.json()` converts raw JSON to Python using the type mapping. A JSON array becomes a Python `list`, and a JSON object becomes a Python `dict`.

</details>

**Question 4:** How do you access the raw text of a response without parsing it?

* A) `response.json()`
* B) `response.body`
* C) `response.text`
* D) `response.content()`

<details>
<summary>Answer</summary>

**C) `response.text`** — `.text` gives you the response body as a plain string. `.json()` parses that string into a Python object. (Note: `.content` with no parentheses gives you the raw bytes, which is useful for binary files like images.)

</details>

**Question 5:** What Python value does JSON `null` become after calling `.json()`?

* A) `0`
* B) `False`
* C) `"null"`
* D) `None`

<details>
<summary>Answer</summary>

**D) `None`** — JSON `null` maps to Python's `None`. Similarly, JSON `true` becomes `True` and JSON `false` becomes `False`.

</details>

---

## Further Reading

- [requests Documentation — Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [MDN Web Docs — HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)
- [W3Schools — Python JSON](https://www.w3schools.com/python/python_json.asp)
- [json.org — Introducing JSON](https://www.json.org/json-en.html)
