# Sorting and Searching Algorithms

**Objective**: By the end of this lesson, you will be able to:
  * Implement a linear search to find an item in a list
  * Explain how binary search works and why it requires a sorted list
  * Implement a simple sorting algorithm (selection sort)
  * Understand that different algorithms have different performance characteristics

---

## What Is an Algorithm?

An **algorithm** is a step-by-step procedure for solving a problem. You've already been writing algorithms without calling them that: every loop that filters a list or builds a total follows a set of repeatable steps.

This lesson focuses on two classic categories: **searching** (finding an item in a collection) and **sorting** (putting items in order). These are foundational problems in computer science, and understanding them will help you think more clearly about how to break any problem into steps.

**Important note:** Python has built-in tools for searching (`in`, `list.index()`) and sorting (`list.sort()`, `sorted()`). Those built-in tools are faster and better for production code. The point of this lesson is to understand how searching and sorting work under the hood, not to replace the built-in tools.

---

## Linear Search

**Linear search** is the simplest search algorithm: start at the beginning and check each item, one by one, until you find a match or reach the end.

```python
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

numbers = [4, 7, 2, 9, 1, 5, 8]
result = linear_search(numbers, 9)
print(result)   # Output: 3

result = linear_search(numbers, 6)
print(result)   # Output: -1
```

The function returns the **index** of the target if found, or `-1` if not found. Returning `-1` is a common convention meaning "not found."

### How It Works

For `linear_search([4, 7, 2, 9, 1, 5, 8], 9)`:

| Step | Index | Value | Match? |
|------|-------|-------|--------|
| 1 | 0 | 4 | No |
| 2 | 1 | 7 | No |
| 3 | 2 | 2 | No |
| 4 | 3 | 9 | Yes, return 3 |

Linear search works on any list, sorted or not. The downside is that if the list has 1,000,000 items and the target is last, you have to check all 1,000,000.

---

## Binary Search

**Binary search** is much faster, but it only works on a **sorted** list. The idea is to repeatedly cut the search space in half.

Think of it like looking up a word in a physical dictionary: you don't start at page 1. You open to the middle, see if your word comes before or after that page, then flip to the middle of the remaining half. Each step eliminates half the pages.

```python
def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15]
result = binary_search(sorted_numbers, 7)
print(result)   # Output: 3

result = binary_search(sorted_numbers, 6)
print(result)   # Output: -1
```

### How It Works

For `binary_search([1, 3, 5, 7, 9, 11, 13, 15], 7)`:

| Step | low | high | mid | data[mid] | Action |
|------|-----|------|-----|-----------|--------|
| 1 | 0 | 7 | 3 | 7 | Found! Return 3 |

That found it in just 1 step. If we searched for 13:

| Step | low | high | mid | data[mid] | Action |
|------|-----|------|-----|-----------|--------|
| 1 | 0 | 7 | 3 | 7 | 13 > 7, set low = 4 |
| 2 | 4 | 7 | 5 | 11 | 13 > 11, set low = 6 |
| 3 | 6 | 7 | 6 | 13 | Found! Return 6 |

3 steps instead of 6 (which linear search would need). With a list of 1,000,000 items, binary search needs at most about 20 steps. That's the power of halving the search space each time.

### AI Prompt: Predict-Then-Check

Trace through `binary_search([2, 4, 6, 8, 10, 12, 14], 10)` on paper. Write down the values of `low`, `high`, and `mid` at each step. Then check with your AI chatbot:

> "I traced through a binary search for 10 in the list [2, 4, 6, 8, 10, 12, 14]. Here are my steps: [your trace]. Can you verify whether I tracked low, high, and mid correctly?"

---

## Selection Sort

**Selection sort** sorts a list by repeatedly finding the smallest item and moving it to the front.

The algorithm:
1. Find the smallest item in the entire list
2. Swap it with the first item
3. Find the smallest item in the remaining (unsorted) portion
4. Swap it with the next position
5. Repeat until the list is sorted

```python
def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

numbers = [64, 25, 12, 22, 11]
print(selection_sort(numbers))   # Output: [11, 12, 22, 25, 64]
```

### How It Works

For `[64, 25, 12, 22, 11]`:

| Pass | Action | List after pass |
|------|--------|-----------------|
| 1 | Find smallest (11), swap with position 0 | `[11, 25, 12, 22, 64]` |
| 2 | Find smallest in remaining (12), swap with position 1 | `[11, 12, 25, 22, 64]` |
| 3 | Find smallest in remaining (22), swap with position 2 | `[11, 12, 22, 25, 64]` |
| 4 | Find smallest in remaining (25), already in place | `[11, 12, 22, 25, 64]` |

Notice the nested loop: the outer loop picks each position, and the inner loop finds the smallest item to put there. This is why sorting is generally slower than searching.

---

## Built-in Tools vs. Manual Algorithms

Python's built-in `sort()` and `sorted()` are much faster than selection sort. For any real project, use the built-in tools:

```python
numbers = [64, 25, 12, 22, 11]
numbers.sort()
print(numbers)   # Output: [11, 12, 22, 25, 64]

# Or create a new sorted list without changing the original
original = [64, 25, 12, 22, 11]
ordered = sorted(original)
print(ordered)    # Output: [11, 12, 22, 25, 64]
print(original)   # Output: [64, 25, 12, 22, 11] (unchanged)
```

The value of implementing search and sort manually is understanding **how** they work. This helps you:
- Think about problems step by step
- Understand why some approaches are faster than others
- Debug code that processes data in loops

---

## Videos

**"Linear and Binary Search Algorithms Explained in Python"**

[Watch the video](https://www.youtube.com/watch?v=u46nNK4lmeE) for a clear visual explanation of how linear search and binary search work, with full Python implementations.

---

## Check for Understanding

**Question 1:** You have an unsorted list of 100 items. Which search algorithm can you use?

* A) Only binary search
* B) Only linear search
* C) Either one
* D) Neither

<details>
<summary>Answer</summary>

**B) Only linear search.** Binary search requires the list to be sorted first. Linear search works on any list, sorted or not.

</details>

**Question 2:** What does `return -1` mean in a search function?

* A) The item is at the last position
* B) The item was not found
* C) There was an error
* D) The list is empty

<details>
<summary>Answer</summary>

**B) The item was not found.** Returning `-1` is a common convention to indicate that the search target doesn't exist in the list.

</details>

**Question 3:** In selection sort, what happens during each pass?

* A) The largest item is moved to the end
* B) The smallest remaining item is moved to the next sorted position
* C) Two random items are swapped
* D) The list is split in half

<details>
<summary>Answer</summary>

**B) The smallest remaining item is moved to the next sorted position.** Each pass finds the minimum value in the unsorted portion and swaps it into place.

</details>

**Question 4:** For production code, what should you use instead of writing your own sort?

* A) `list.selection_sort()`
* B) `list.sort()` or `sorted()`
* C) A while loop
* D) `list.order()`

<details>
<summary>Answer</summary>

**B) `list.sort()` or `sorted()`.** Python's built-in sorting is highly optimized and should be used for any real project. Manual implementations are for learning how algorithms work.

</details>

---

## Further Reading

- [W3Schools: Python sort()](https://www.w3schools.com/python/ref_list_sort.asp)
- [Python Official Documentation: Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)
- [Khan Academy: Intro to Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms)
