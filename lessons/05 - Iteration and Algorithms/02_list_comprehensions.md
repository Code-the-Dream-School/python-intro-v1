# List Comprehensions

**Objective**: By the end of this lesson, you will be able to:
  * Write a basic list comprehension to create a new list
  * Add a condition to filter items in a comprehension
  * Convert between a `for` loop and a list comprehension
  * Recognize when a comprehension improves readability and when a loop is better

---

## What Is a List Comprehension?

In the previous lesson, you wrote loops like this to create new lists:

```python
numbers = [1, 2, 3, 4, 5]
doubled = []
for n in numbers:
    doubled.append(n * 2)
print(doubled)   # Output: [2, 4, 6, 8, 10]
```

A **list comprehension** is a shorter way to write the same thing in one line:

```python
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)   # Output: [2, 4, 6, 8, 10]
```

Both produce the same result. The comprehension just puts the expression, loop, and new list all in one line.

---

## Basic Syntax

The pattern is:

```python
new_list = [expression for item in iterable]
```

Breaking it down:
- `expression`: what you want in the new list (e.g., `n * 2`)
- `item`: the variable name for each element (e.g., `n`)
- `iterable`: the collection you're looping over (e.g., `numbers`)

Here are a few more examples:

```python
# Squares of numbers 0-9
squares = [x ** 2 for x in range(10)]
print(squares)   # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Convert names to uppercase
names = ["jazmine", "carlos", "amir"]
upper_names = [name.upper() for name in names]
print(upper_names)   # Output: ['JAZMINE', 'CARLOS', 'AMIR']

# Get the length of each word
words = ["python", "is", "fun"]
lengths = [len(word) for word in words]
print(lengths)   # Output: [6, 2, 3]
```

---

## Adding a Filter with `if`

You can add a condition to include only certain items:

```python
new_list = [expression for item in iterable if condition]
```

The `if` at the end filters out items that don't match the condition.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)   # Output: [2, 4, 6, 8, 10]

# Only scores above 80
scores = [85, 42, 91, 67, 73, 55, 88]
high_scores = [s for s in scores if s >= 80]
print(high_scores)   # Output: [85, 91, 88]
```

### Side-by-Side Comparison

Here's the same logic written as a loop and as a comprehension:

**Loop version:**
```python
scores = [85, 42, 91, 67, 73, 55, 88]
passing = []
for score in scores:
    if score >= 70:
        passing.append(score)
```

**Comprehension version:**
```python
scores = [85, 42, 91, 67, 73, 55, 88]
passing = [score for score in scores if score >= 70]
```

Both produce `[85, 91, 67, 73, 88]`. The comprehension is shorter and easier to scan once you're comfortable with the syntax.

### AI Prompt: Predict-Then-Check

Study this code without running it:

```python
words = ["hello", "world", "hi", "python", "go"]
long_words = [w.upper() for w in words if len(w) > 3]
print(long_words)
```

Predict the output, then check:

> "I'm learning list comprehensions in Python. I predict this will output [your prediction] because the filter keeps words longer than 3 characters and .upper() transforms them. Am I right?"

---

## When to Use Comprehensions (and When Not To)

List comprehensions are great when the logic is simple: one transformation, maybe one filter. They make your code shorter AND clearer.

But if the logic is complex, a regular `for` loop is better. A comprehension that's hard to read defeats the purpose.

**Good use (clear and short):**
```python
prices = [10, 20, 30, 40]
discounted = [p * 0.9 for p in prices]
```

**Bad use (too complex, use a loop instead):**
```python
# Don't do this, too hard to read
result = [x * 2 + 1 for x in range(100) if x % 3 == 0 and x % 5 != 0 and x > 10]
```

**Rule of thumb:** If your comprehension doesn't fit on one line or takes more than 5 seconds to understand, use a regular loop instead.

---

## Videos

**"Python Tutorial: Comprehensions"** (Corey Schafer)

[Watch the video](https://www.youtube.com/watch?v=3dt4OGnU5sM) for a thorough explanation of list comprehensions, including filtering and when to use them.

---

## Check for Understanding

**Question 1:** Which list comprehension produces `[2, 4, 6, 8, 10]`?

* A) `[n for n in range(1, 11)]`
* B) `[n * 2 for n in range(1, 6)]`
* C) `[n for n in range(1, 11) if n > 5]`
* D) `[n + 2 for n in range(5)]`

<details>
<summary>Answer</summary>

**B) `[n * 2 for n in range(1, 6)]`.** `range(1, 6)` gives `[1, 2, 3, 4, 5]`, and each is multiplied by 2.

</details>

**Question 2:** What does this comprehension produce?

```python
[x for x in [3, 6, 9, 12] if x > 5]
```

* A) `[3, 6, 9, 12]`
* B) `[6, 9, 12]`
* C) `[3]`
* D) `[True, True, True, False]`

<details>
<summary>Answer</summary>

**B) `[6, 9, 12]`.** The `if x > 5` filter keeps only items greater than 5.

</details>

**Question 3:** When should you use a regular `for` loop instead of a list comprehension?

* A) When the list is short
* B) When you need to filter items
* C) When the logic is complex and hard to read in one line
* D) Always, comprehensions are bad practice

<details>
<summary>Answer</summary>

**C) When the logic is complex and hard to read in one line.** Comprehensions are great for simple transformations, but complex logic is clearer as a regular loop.

</details>

---

## Further Reading

- [W3Schools: Python List Comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)
- [Real Python: When to Use a List Comprehension](https://realpython.com/list-comprehension-python/)
- [Python Official Documentation: List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
