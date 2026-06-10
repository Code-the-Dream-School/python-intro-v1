# Boolean Operators

**Operators** are special symbols that perform operations on variables and values. Some of the most commonly used operators are:

1. **Arithmetic Operators**: For mathematical calculations
   * `+` (addition): `3 + 2` → `5`
   * `-` (subtraction): `5 - 3` → `2`
   * `*` (multiplication): `4 * 2` → `8`
   * `/` (division): `9 / 3` → `3.0`
   * `//` (integer division): `9 // 3` → `3`
   * `%` (modulus, remainder): `7 % 3` → `1`
   * `**` (exponentiation): `2 ** 3` → `8`

2. **Comparison Operators**: Compare two values and return a Boolean (`True` or `False`)
   * `==` (equal to): `5 == 5` → `True`
   * `!=` (not equal to): `5 != 4` → `True`
   * `<` (less than): `3 < 4` → `True`
   * `>` (greater than): `10 > 5` → `True`
   * `<=` (less than or equal to): `5 <= 5` → `True`
   * `>=` (greater than or equal to): `7 >= 3` → `True`

3. **Logical Operators**: Combine or invert conditions
   * `and`: Both conditions must be `True`
   * `or`: At least one condition must be `True`
   * `not`: Inverts the result

```python
# Arithmetic
result = 10 + 5   # 15
remainder = 9 % 4  # 1

# Comparison
print(5 > 3)  # True

# Logical
print(True and False)  # False
```

---

## Logical Operators in Depth

Logical operators let you combine or invert conditions inside an `if` statement. This section covers how each one works and how to use them together.

### `and`

`and` returns `True` only when **both** conditions are `True`. If either one is `False`, the whole expression is `False`.

| A | B | A and B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

```python
age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").lower()

if age >= 18 and has_id == "yes":
    print("You may enter.")
else:
    print("Entry denied.")
```

Both conditions must be satisfied — being old enough isn't enough if you don't have ID, and having ID isn't enough if you're underage.

### `or`

`or` returns `True` when **at least one** condition is `True`. It only returns `False` when both conditions are `False`.

| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | **False** |

```python
day = input("What day is it? ").lower()

if day == "saturday" or day == "sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")
```

### `not`

`not` **inverts** a boolean value — `True` becomes `False`, and `False` becomes `True`.

| A | not A |
|---|-------|
| True | False |
| False | True |

```python
is_raining = False

if not is_raining:
    print("Good day for a walk!")
else:
    print("You might want an umbrella.")
```

---

## Operator Precedence

When you combine multiple logical operators in one expression, Python evaluates them in this order:

1. `not` (evaluated first)
2. `and`
3. `or` (evaluated last)

```python
# Python reads this as: (not False) and True → True and True → True
result = not False and True
print(result)  # True
```

When in doubt, use parentheses to make the order explicit and your code easier to read:

```python
# Clear and unambiguous
if (age >= 13 and age < 18) or has_permission:
    print("Access granted.")
```

---

## Truthy and Falsy Values

In Python, values don't have to be literally `True` or `False` to work in an `if` statement. Some values are considered **falsy** — they behave like `False` when used as a condition:

| Falsy value | What it represents |
|-------------|-------------------|
| `0` | The integer zero |
| `""` | An empty string |
| `None` | The absence of a value |
| `[]` | An empty list |

Everything else is **truthy**.

```python
name = input("Enter your name: ")

if name:
    print("Hello,", name)
else:
    print("You didn't enter a name.")
```

If the user presses Enter without typing anything, `name` will be `""` (an empty string), which is falsy — so the `else` branch runs.

---

## Check for Understanding

**Question:** What will the following code output?

```python
x = 5
y = 10

if x > 3 and y > 8:
    print("Both conditions are true.")
else:
    print("At least one condition is false.")
```

* A) `Both conditions are true.`
* B) `At least one condition is false.`
* C) Nothing
* D) An error

<details>

<summary>View answer</summary>

**Answer**: A) `Both conditions are true.`

`5 > 3` is `True` and `10 > 8` is `True`. Since both conditions are `True`, `and` evaluates to `True` and the first branch runs.

</details>

**Question:** What will the following code output?

```python
is_member = False
has_coupon = True

if is_member or has_coupon:
    print("Discount applied.")
else:
    print("No discount available.")
```

* A) `Discount applied.`
* B) `No discount available.`
* C) Nothing
* D) An error

<details>

<summary>View answer</summary>

**Answer**: A) `Discount applied.`

`is_member` is `False`, but `has_coupon` is `True`. Since at least one condition is `True`, `or` evaluates to `True`.

</details>

**Question:** What is the value of `result`?

```python
result = not True
print(result)
```

* A) `True`
* B) `False`
* C) `None`
* D) An error

<details>

<summary>View answer</summary>

**Answer**: B) `False`

`not` inverts the boolean value: `not True` → `False`.

</details>

**Question:** Which of the following values is **falsy** in Python?

* A) `1`
* B) `"hello"`
* C) `[]`
* D) `True`

<details>

<summary>View answer</summary>

**Answer**: C) `[]`

An empty list is falsy. Non-empty strings, non-zero numbers, and `True` are all truthy.

</details>
