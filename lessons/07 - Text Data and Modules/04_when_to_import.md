# When to Write Your Own Code vs. Import a Module

One of the most common questions new Python developers face is: *should I write this myself, or find a module that already does it?*

A useful way to think about this is in three tiers:

**Tier 1 — Check the standard library first**

If you need to do something common — work with dates, read a file, generate a random number — there's a good chance Python already includes a module for it. The standard library is well-tested, well-documented, and requires no installation. Always check here first.

**Tier 2 — Look for a well-known third-party package**

For tasks the standard library doesn't cover well, the Python community has likely built something. Third-party packages are installed via `pip` and hosted on [PyPI](https://pypi.org/) (the Python Package Index). PyPI has hundreds of thousands of packages — but that also means quality varies widely.

**Tier 3 — Write it yourself**

When what you need is small, specific to your situation, or not well served by existing packages, writing your own code is the right call.

#### Finding and Evaluating a Package on PyPI

[PyPI.org](https://pypi.org/) is where third-party Python packages live. You can search by name or keyword. Once you find a candidate, check:

- **Recent activity**: When was it last updated? A package untouched since 2017 may not work with current Python versions.
- **Download counts and GitHub stars**: High numbers suggest the package is trusted and widely used.
- **Documentation quality**: If the docs are sparse or hard to follow, using the package will be frustrating.
- **License**: Make sure the license allows your intended use. MIT and Apache 2.0 are common and permissive; GPL has restrictions.

#### Three Examples

**Clearly better to import**

You need to parse a date string like `"April 15, 2024"` into something your code can work with. Writing a date parser from scratch — handling different formats, leap years, edge cases — could take weeks. This is exactly what `datetime` (and third-party libraries like `dateutil`) exist for.

```python
from datetime import datetime
date = datetime.strptime("April 15, 2024", "%B %d, %Y")
print(date.year)  # 2024
```

**Clearly better to write your own**

You need a function that filters a list of filenames to only the `.csv` ones. That's two or three lines of Python — adding a dependency for something this small would be overkill.

```python
def get_csv_files(filenames):
    return [f for f in filenames if f.endswith(".csv")]
```

**In between**

You need to send a request to a web API. Python's standard library has `urllib` for this, but it's verbose and low-level. The third-party `requests` library does the same thing with much cleaner syntax and is widely trusted. Most developers reach for `requests` here — it's a reasonable judgment call.

```python
# Standard library — works, but verbose
import urllib.request
with urllib.request.urlopen("https://api.example.com/data") as response:
    data = response.read()

# requests — cleaner and more readable
import requests
data = requests.get("https://api.example.com/data").json()
```

The mental model: *standard library first, established package second, roll your own when the task is small or highly specific to your project.*
