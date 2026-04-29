# Building the CLI

In Phase 1, you created a program that fetches and parses data. Now you'll turn it into a *tool*, something a user can run and interact with, asking questions of the data in real time.

This phase has two parts: 
* choosing how to accept user input
* implementing at least one meaningful interaction.

Start simple! You can always add more interactions once the first one works.

---

## Two Approaches to User Input

You have two options for how your CLI accepts input. Pick one:

> **Tip:** If you're not sure which to choose, start with `input()`. You can always switch to `argparse` later! The logic for filtering, looking up, and displaying results is identical between the two. The only thing that changes is how the user provides input.

### Option 1 — `input()` prompts

`input()` pauses the program and waits for the user to type something. It's simpler to write and easier to understand at first.

```python
def main():
    data = fetch_data()
    records = process_data(data)

    query = input("Enter a region to filter by: ")
    results = [r for r in records if r["region"].lower() == query.lower()]
    display_results(results)
```

**Good for:** interactive, conversational programs where the user runs the script and types responses.

**Limitation:** harder to automate or script. Every run requires manual input.

### Option 2 — `argparse`

`argparse` reads arguments passed on the command line when the script is run. It's the standard approach for real CLI tools.

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Query country data by region.")
    parser.add_argument("region", help="The region to filter by (e.g., Europe)")
    args = parser.parse_args()

    data = fetch_data()
    records = process_data(data)
    results = [r for r in records if r["region"].lower() == args.region.lower()]
    display_results(results)
```

Run it like this:
```bash
python main.py Europe
```

**Good for:** professional-style tools that can be run with different arguments without editing code.

**Limitation:** slightly more code to write, and less intuitive to set up at first.

---

## What "At Least One Meaningful Interaction" Looks Like

The project requires at least one interaction where the user provides input and gets back a useful result. Here are the three patterns that work well with list-of-dicts data:

### Pattern 1 — Filter by a field value

Show all records where a field matches what the user typed.

```python
query = input("Enter a region: ").strip().lower()
results = [r for r in records if r.get("region", "").lower() == query]
```

Works well for: countries by region, Pokémon by type, books by decade.

### Pattern 2 — Look up a record by name or ID

Find and display one specific record.

```python
query = input("Enter a name: ").strip().lower()
results = [r for r in records if r.get("name", "").lower() == query]
```

Works well for: looking up a specific country, a specific Pokémon, a specific book title.

### Pattern 3 — Compare two records side by side

Find two records and display them next to each other so the user can compare.

```python
name1 = input("First name: ").strip().lower()
name2 = input("Second name: ").strip().lower()

match1 = next((r for r in records if r.get("name", "").lower() == name1), None)
match2 = next((r for r in records if r.get("name", "").lower() == name2), None)
```

Works well for: comparing two countries' populations, comparing two Pokémon's stats.

You only need to implement **one** of these to meet the requirement. Implement whichever fits your API best. If you finish one and want to add a second, do that after the first is working and tested.

---

## Formatting Output

A list of raw dictionaries is hard to read in the terminal. Take a few minutes to format your output before submitting.

**Before:**
```
{'name': 'France', 'population': 67391582, 'region': 'Europe', 'area': 551695.0}
```

**After:**
```
France
  Region:     Europe
  Population: 67,391,582
  Area:       551,695 km²
```

Here's how to write a `display_results()` function that produces the "after" version:

```python
def display_results(results):
    if not results:
        print("No results found.")
        return

    print(f"\n{len(results)} result(s) found:")
    print("-" * 40)

    for r in results:
        print(r["name"])
        print(f"  Region:     {r.get('region', 'Unknown')}")
        print(f"  Population: {r.get('population', 0):,}")
        print("-" * 40)
```

**A few things in this example worth noting:**

- **Check for empty results at the top.** If no records matched, tell the user that instead of printing nothing.
- **Separator lines** (`"-" * 40`) make it easy to see where one record ends and the next begins.
- **`{value:,}` formatting** adds comma separators to large numbers: `67391582` becomes `67,391,582`.

You don't need to match this format exactly. The goal is output that's easy to read — not raw dict output.

<details>
<summary>Stuck on formatting output? Click here for an example.</summary>

Here's a minimal pattern for iterating over a list of dicts and printing selected fields with f-strings. Replace the field names with your own:

```python
def display_results(results):
    if not results:
        print("No results found.")
        return

    for item in results:
        name = item.get("name", "Unknown")
        field1 = item.get("field1", "N/A")
        field2 = item.get("field2", "N/A")
        print(f"{name}: {field1} | {field2}")
```

This works for any list of dicts. Change `"field1"` and `"field2"` to the actual keys in your data.

</details>

---

## Handling Unexpected Input

Users will type things you didn't expect. Your program shouldn't crash when they do.

Three scenarios to handle:

**1. No matching results**

The query was valid, but nothing matched. Tell the user, don't crash.

```python
results = [r for r in records if r.get("region", "").lower() == query]
if not results:
    print(f"No results found for '{query}'.")
    return
```

**2. Empty input**

The user pressed Enter without typing anything.

```python
query = input("Enter a region: ").strip()
if not query:
    print("Please enter a value.")
    return
```

**3. Non-numeric input where a number is expected**

If you're asking for something like a minimum population, the input might not be a valid number.

```python
raw = input("Minimum population: ").strip()
try:
    min_pop = int(raw)
except ValueError:
    print(f"'{raw}' is not a valid number.")
    return
```

You don't need to handle every possible bad input, just the ones that would cause a crash or a confusing error. The rubric requires that "unexpected input is handled without crashing."

---

## Putting It All Together in `main()`

`main()` is where all the pieces connect. Its job is to orchestrate: fetch the data, process it, get input from the user, and display results.

```python
def main():
    # Phase 1: fetch and process
    data = fetch_data()
    if not data:
        return  # fetch_data() already printed an error message

    records = process_data(data)

    # Phase 2: interact
    query = input("Enter a region to filter by: ").strip()
    if not query:
        print("Please enter a value.")
        return

    results = [r for r in records if r.get("region", "").lower() == query.lower()]
    display_results(results)
```

This is the outline, your `main()` will look different depending on your API and which interaction pattern you chose. The important thing is that each function does one job: `fetch_data()` fetches, `process_data()` transforms, `display_results()` prints. `main()` calls them in order and handles the user input in between.

> **Note:** If you add a second interaction (for example, a menu that lets the user choose between filter, lookup, or compare), that logic lives in `main()` too. A `while True` loop with a menu and a `break` condition is a common pattern for this.

---

## Phase 2 Checkpoint

Before moving on, check these off:

- [ ] Your program accepts at least one form of user input (via `input()` or `argparse`)
- [ ] At least one meaningful interaction is implemented and returns formatted results
- [ ] Unexpected input (empty input, no matching results) is handled without crashing
- [ ] `display_results()` prints output that's readable — not raw dicts
- [ ] `main()` calls `fetch_data()`, `process_data()`, and `display_results()` in the right order

If all five are true, your Week 10 project is complete. Commit your work and submit your pull request, then head to Week 11.
