# Assignment 1 Answer Key — Python Basics

## File Setup

- One script, `assignment-1.py`, written in [online-python.com](https://www.online-python.com/) (no local setup this week).
- Submitted through GitHub's **web editor**: file committed to an `assignment-1` branch, then a pull request opened. **URL1** = the PR link; URL2 = video (not assessed).
- All five sections live in the **same file**, added in order — expect earlier sections to remain above later ones.

---

## Section 1: Variables and Types — **Objective**

One variable of each core type, each printed with `type()`. Values are the student's own; output pattern:

```
Alex <class 'str'>
27 <class 'int'>
5.9 <class 'float'>
True <class 'bool'>
```

**Correct if:** all four types present (`str`, `int`, `float`, `bool`), each printed alongside its `type()`. Watch for a number wrapped in quotes (`"27"`) misreported as an int, and `bool` values other than `True`/`False`.

## Section 2: User Input and Math — **Objective**

Asks for name + birth year, computes approximate age, prints a sentence:

```
Hi, Jordan! You are approximately 24 years old.
```

**Correct if:** birth year is converted with `int()` before subtracting (`2026 - birth_year` or similar), and the greeting uses the entered name.
**Common miss:** no `int()` → `TypeError` or string concatenation; asking for age directly instead of computing it from the birth year.

## Section 3: Type Conversion and f-strings — **Objective**

Two separate numeric inputs → `float` → product, shown with an f-string:

```
12.5 × 4.0 = 50.0
```

**Correct if:** both inputs cast to `float`, product is correct, output built with an f-string.
**Common miss:** casting to `int` (loses decimals), or string-concatenating instead of using an f-string. The `×` may be typed as `x` or `*` — accept any.

## Section 4: Formatted Receipt — **Objective**

Item, price, quantity stored in variables (no `input()` this section); total **computed** from them:

```
===========================
        RECEIPT
===========================
Item:      Python textbook
Price:     $29.99
Quantity:  2
---------------------------
Total:     $59.98
===========================
```

**Correct if:** `total` is calculated from the price/quantity variables (e.g. `29.99 * 2 == 59.98`), and money shows two decimals (`:.2f`).
**Common miss:** hard-coding the total as a literal instead of computing it. Border characters and exact spacing are free — don't dock for a different layout.

## Section 5: Mini-Project — Profile Card — **Objective** (with subjective formatting)

Five inputs (name, hometown, hobby, fun fact, birth year); age **computed** from birth year; card printed with f-strings and aligned labels.

```
╔══════════════════════════════╗
      PROFILE: Alex Rivera
╚══════════════════════════════╝
Hometown:   Chicago, IL
Hobby:      Rock climbing
Fun fact:   I've visited 12 countries.
Age:        27
```

**Correct if:** age is derived from the birth year (not asked directly), all five fields appear, and values are inserted via f-strings.
**Formatting (subjective):** labels should line up and the card should read cleanly — accept any border style or alignment approach. A working card with slightly ragged columns still passes; only messy, unreadable output is a problem.
