# Lists and Tuples

**Objective**: By the end of this lesson, you will be able to:
  * Create and modify lists using indexing, slicing, and key methods
  * Understand the difference between mutable and immutable data
  * Use tuples for fixed collections of data
  * Choose between a list and a tuple based on whether the data should change

---

## What Are Data Structures?

So far, your variables have stored single values: one number, one string, one boolean. But real programs work with collections of data: a list of student names, a set of unique tags, a mapping of product names to prices.

Python has four built-in **data structures** for storing collections. This week covers all four. This lesson starts with the two that are ordered: **lists** and **tuples**.

---

## Mutable vs. Immutable

Before diving into lists and tuples, you need to understand two terms: **mutable** and **immutable**.

Something that is **mutable** can be changed after it's created. Something that is **immutable** cannot be changed after it's created.

Think of it like this:
- **Clay (mutable)**: you can reshape, add to, or remove pieces after it's formed
- **Ceramic statue (immutable)**: once it's fired in a kiln, you can't change it without breaking it

Lists are mutable. Tuples are immutable. This one difference determines when you use each one.

---

## Lists

A **list** is a mutable, ordered collection of items. You create a list using square brackets `[]`:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)   # Output: ['apple', 'banana', 'cherry']
```

Lists can hold any data type, and you can mix types (though you usually won't):

```python
mixed = ["hello", 42, 3.14, True]
```

### Accessing Items by Index

Each item in a list has a position number called an **index**. Indexing starts at `0`, not `1`:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # Output: apple
print(fruits[1])    # Output: banana
print(fruits[2])    # Output: cherry
```

You can also use negative indices to count from the end:

```python
print(fruits[-1])   # Output: cherry (last item)
print(fruits[-2])   # Output: banana (second to last)
```

### Modifying Items

Since lists are mutable, you can change items by their index:

```python
fruits = ["apple", "banana", "cherry"]
fruits[0] = "orange"
print(fruits)   # Output: ['orange', 'banana', 'cherry']
```

### Key List Methods

| Method | What it does | Example |
|--------|-------------|---------|
| `append(item)` | Adds an item to the end | `fruits.append("grape")` |
| `remove(item)` | Removes the first occurrence | `fruits.remove("banana")` |
| `sort()` | Sorts the list in place | `fruits.sort()` |
| `len(list)` | Returns the number of items | `len(fruits)` |
| `pop()` | Removes and returns the last item | `fruits.pop()` |
| `insert(i, item)` | Inserts item at position i | `fruits.insert(1, "kiwi")` |

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("grape")
print(fruits)   # Output: ['apple', 'banana', 'cherry', 'grape']

fruits.remove("banana")
print(fruits)   # Output: ['apple', 'cherry', 'grape']

print(len(fruits))   # Output: 3

fruits.sort()
print(fruits)   # Output: ['apple', 'cherry', 'grape']
```

Note that `len()` is a function (not a method), so you call it as `len(fruits)`, not `fruits.len()`.

### Slicing

**Slicing** lets you grab a portion of a list. The syntax is `list[start:end]`, where `start` is included and `end` is not:

```python
letters = ["A", "B", "C", "D", "E"]

print(letters[1:3])    # Output: ['B', 'C']
print(letters[:3])     # Output: ['A', 'B', 'C'] (from the beginning)
print(letters[2:])     # Output: ['C', 'D', 'E'] (to the end)
print(letters[-2:])    # Output: ['D', 'E'] (last two items)
```

Slicing creates a **new list**. The original list is not changed.

### Iterating Over a List

You can loop through a list using a `for` loop:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Output:
```
apple
banana
cherry
```

This pattern is so common in Python that it will feel natural very quickly.

### AI Prompt: Predict-Then-Check

Study this code without running it:

```python
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.remove(20)
print(numbers)
print(numbers[1:4])
```

Predict both outputs, then check with your preferred AI chatbot:

> "I'm learning Python lists. I predict this code will output [your predictions]. Can you walk me through what happens at each step?"

---

## Tuples

A **tuple** is an immutable, ordered collection. You create a tuple using parentheses `()`:

```python
dimensions = (1920, 1080)
print(dimensions[0])   # Output: 1920
print(dimensions[1])   # Output: 1080
```

You can access items by index, just like a list. But you **cannot** change, add, or remove items:

```python
dimensions = (1920, 1080)
dimensions[0] = 2560   # TypeError: 'tuple' object does not support item assignment
```

### When to Use Tuples

Use a tuple when:
- The data should not change (coordinates, RGB colors, database records)
- You want to signal to other developers that this collection is fixed
- You're returning multiple values from a function (you'll learn this in Week 6)

```python
# Good uses of tuples
coordinates = (37.7749, -122.4194)      # Latitude, longitude
rgb_red = (255, 0, 0)                    # Color values
person = ("Jazmine", 28, "Engineer")     # A fixed record
```

### Tuple Unpacking

You can assign each item in a tuple to its own variable in one line:

```python
dimensions = (1920, 1080)
width, height = dimensions
print(width)    # Output: 1920
print(height)   # Output: 1080
```

This also works with lists, but it's most commonly used with tuples.

---

## Lists vs. Tuples: When to Use Which

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable? | Yes | No |
| Can add/remove items? | Yes | No |
| Use when... | Data changes (shopping cart, to-do list) | Data is fixed (coordinates, config values) |

When in doubt, use a list. Tuples are for specific situations where immutability matters.

---

## Videos

**"Python Tutorial for Beginners 4: Lists, Tuples, and Sets"** (Corey Schafer)

[Watch the video](https://www.youtube.com/watch?v=W8KRzm-HUcc) for a thorough walkthrough of lists, tuples, and their methods.

---

## Check for Understanding

**Question 1:** What is the output of this code?

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
```

* A) `apple`
* B) `banana`
* C) `cherry`
* D) An error

<details>
<summary>Answer</summary>

**B) `banana`.** List indexing starts at 0, so index 1 is the second item.

</details>

**Question 2:** What happens when you try to modify a tuple?

```python
colors = ("red", "green", "blue")
colors[0] = "yellow"
```

* A) It changes "red" to "yellow"
* B) It creates a new tuple
* C) It raises a `TypeError`
* D) It does nothing

<details>
<summary>Answer</summary>

**C) It raises a `TypeError`.** Tuples are immutable, so you cannot change their elements after creation.

</details>

**Question 3:** What does `fruits.append("grape")` do?

* A) Adds "grape" to the beginning of the list
* B) Adds "grape" to the end of the list
* C) Replaces the last item with "grape"
* D) Creates a new list with "grape"

<details>
<summary>Answer</summary>

**B) Adds "grape" to the end of the list.** `append()` always adds to the end.

</details>

**Question 4:** What is the output of `letters[1:3]` where `letters = ["A", "B", "C", "D"]`?

* A) `["A", "B"]`
* B) `["B", "C"]`
* C) `["B", "C", "D"]`
* D) `["A", "B", "C"]`

<details>
<summary>Answer</summary>

**B) `["B", "C"]`.** Slicing with `[1:3]` starts at index 1 (included) and stops before index 3 (excluded).

</details>

---

## Further Reading

- [W3Schools: Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [W3Schools: Python Tuples](https://www.w3schools.com/python/python_tuples.asp)
- [Python Official Documentation: Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
