# Dictionaries and Sets

**Objective**: By the end of this lesson, you will be able to:
  * Create dictionaries and access values by key
  * Add, update, and remove key-value pairs
  * Use key dictionary methods: `keys()`, `values()`, `items()`, `get()`
  * Create sets and use common set operations
  * Choose the right data structure for different situations

---

## Dictionaries

A **dictionary** is a mutable collection of **key-value pairs**. Instead of accessing items by position (like a list), you access them by a unique key.

Think of a real dictionary: you look up a **word** (the key) to find its **definition** (the value). Python dictionaries work the same way.

```python
person = {"name": "Jazmine", "age": 28, "city": "Durham"}
print(person["name"])    # Output: Jazmine
print(person["age"])     # Output: 28
```

### Creating Dictionaries

Use curly braces `{}` with key-value pairs separated by colons:

```python
# A student record
student = {
    "name": "Carlos",
    "grade": "A",
    "score": 95
}
```

Keys must be unique and immutable (strings and numbers are most common). Values can be anything.

### Accessing Values

Use square brackets with the key name:

```python
student = {"name": "Carlos", "grade": "A", "score": 95}
print(student["name"])     # Output: Carlos
print(student["score"])    # Output: 95
```

If you use a key that doesn't exist, Python raises a `KeyError`:

```python
print(student["email"])    # KeyError: 'email'
```

To avoid this, use the `get()` method, which returns `None` (or a default you specify) if the key is missing:

```python
print(student.get("email"))              # Output: None
print(student.get("email", "N/A"))       # Output: N/A
```

### Adding and Updating

Add a new key-value pair or update an existing one with the same syntax:

```python
student = {"name": "Carlos", "grade": "A"}

student["email"] = "carlos@example.com"   # Add new key
student["grade"] = "A+"                   # Update existing key

print(student)
# Output: {'name': 'Carlos', 'grade': 'A+', 'email': 'carlos@example.com'}
```

### Removing Items

Use `del` to remove a key-value pair, or `pop()` to remove and return the value:

```python
student = {"name": "Carlos", "grade": "A", "score": 95}

del student["score"]
print(student)   # Output: {'name': 'Carlos', 'grade': 'A'}

grade = student.pop("grade")
print(grade)     # Output: A
print(student)   # Output: {'name': 'Carlos'}
```

### Key Dictionary Methods

| Method | What it returns | Example |
|--------|----------------|---------|
| `keys()` | All keys | `student.keys()` |
| `values()` | All values | `student.values()` |
| `items()` | All key-value pairs as tuples | `student.items()` |
| `get(key)` | Value for key, or None if missing | `student.get("name")` |

```python
student = {"name": "Carlos", "grade": "A", "score": 95}

print(list(student.keys()))     # Output: ['name', 'grade', 'score']
print(list(student.values()))   # Output: ['Carlos', 'A', 95]
print(list(student.items()))    # Output: [('name', 'Carlos'), ('grade', 'A'), ('score', 95)]
```

Notice that `items()` returns each pair as a tuple. This will be useful when we loop over dictionaries in the next lesson.

### When to Use Dictionaries

Dictionaries are ideal when you need to look up data by a label or identifier: a student's name to find their grade, a product ID to find its price, or a country code to find its name. If you find yourself thinking "I need to find X based on Y," a dictionary is probably the right choice.

### AI Prompt: Retrieval Practice

Open your preferred AI chatbot and explain in your own words:
- What makes a dictionary different from a list?
- When would you use `get()` instead of square brackets to access a value?

Ask the AI to give you feedback on your explanation.

---

## Sets

A **set** is an unordered collection of **unique** elements. If you add a duplicate, Python ignores it.

```python
colors = {"red", "green", "blue", "red"}
print(colors)   # Output: {'red', 'green', 'blue'} (no duplicate)
```

**Important:** Sets use curly braces like dictionaries, but without key-value pairs. An empty set must be created with `set()`, not `{}` (which creates an empty dictionary).

```python
empty_set = set()           # Correct
empty_dict = {}             # This is a dictionary, not a set
```

### Adding Items

```python
colors = {"red", "green", "blue"}
colors.add("yellow")
print(colors)   # Output includes 'yellow' (order may vary)
```

### Common Set Operations

Sets are great for comparing groups of data:

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a.union(set_b))          # Output: {1, 2, 3, 4, 5, 6}
print(set_a.intersection(set_b))   # Output: {3, 4}
print(set_a.difference(set_b))     # Output: {1, 2}
```

| Operation | What it returns |
|-----------|----------------|
| `union()` | All unique elements from both sets |
| `intersection()` | Elements common to both sets |
| `difference()` | Elements in the first set but not the second |

### When to Use Sets

Sets are perfect when you need to remove duplicates from a list or check membership quickly:

```python
# Remove duplicates
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = set(names)
print(unique_names)   # Output: {'Alice', 'Bob', 'Charlie'}

# Check membership (very fast with sets)
if "Alice" in unique_names:
    print("Found!")
```

---

## Choosing the Right Data Structure

Here's a summary of all four structures you've learned:

| Structure | Ordered? | Mutable? | Duplicates? | Key-Value? | Use when... |
|-----------|----------|----------|-------------|------------|-------------|
| **List** | Yes | Yes | Yes | No | Ordered collection that changes |
| **Tuple** | Yes | No | Yes | No | Fixed, ordered data |
| **Dictionary** | No | Yes | Keys: No | Yes | Looking up values by a label |
| **Set** | No | Yes | No | No | Unique items, comparisons |

---

## Videos

**"Python Tutorial for Beginners 5: Dictionaries"** (Corey Schafer)

[Watch the video](https://www.youtube.com/watch?v=daefaLgNkw0) for a detailed walkthrough of dictionaries, their methods, and practical use cases.

---

## Check for Understanding

**Question 1:** How do you access the value `"Jazmine"` from this dictionary?

```python
person = {"name": "Jazmine", "age": 28}
```

* A) `person[0]`
* B) `person["name"]`
* C) `person.name`
* D) `person("name")`

<details>
<summary>Answer</summary>

**B) `person["name"]`.** Dictionaries use keys (not indices) to access values. The key `"name"` maps to the value `"Jazmine"`.

</details>

**Question 2:** What happens when you add a duplicate value to a set?

* A) Python raises an error
* B) The duplicate is added anyway
* C) Python ignores the duplicate
* D) The original value is replaced

<details>
<summary>Answer</summary>

**C) Python ignores the duplicate.** Sets only store unique elements. Adding a value that already exists has no effect.

</details>

**Question 3:** Which method safely returns `None` if a dictionary key doesn't exist?

* A) `dict[key]`
* B) `dict.find(key)`
* C) `dict.get(key)`
* D) `dict.search(key)`

<details>
<summary>Answer</summary>

**C) `dict.get(key)`.** Using `get()` returns `None` (or a default value) if the key doesn't exist, instead of raising a `KeyError`.

</details>

**Question 4:** You need to store student names and their grades. Which data structure is the best choice?

* A) List
* B) Tuple
* C) Dictionary
* D) Set

<details>
<summary>Answer</summary>

**C) Dictionary.** A dictionary lets you map each student name (key) to their grade (value), making it easy to look up any student's grade.

</details>

---

## Further Reading

- [W3Schools: Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
- [W3Schools: Python Sets](https://www.w3schools.com/python/python_sets.asp)
- [Python Official Documentation: Mapping Types](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
