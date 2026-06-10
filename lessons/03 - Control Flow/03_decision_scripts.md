# Decision-Making Scripts

So far you've learned `if`/`elif`/`else`, comparison operators, boolean operators, and `input()`. This section puts them all together to build a short program that does something real: it takes information from the user and makes decisions based on it.

---

## Worked Example: Library Card Eligibility

The city library issues different card types based on a visitor's age and whether they live in the city. Let's build a script that asks for that information and tells the user what they qualify for.

### The complete script

```python
name = input("What is your name? ")
age = int(input("How old are you? "))
is_resident = input("Do you live in the city? (yes/no): ").lower()

if age < 5:
    print("Sorry, " + name + ", you must be at least 5 years old to get a library card.")
elif age < 18 and is_resident == "yes":
    print("Welcome, " + name + "! You qualify for a free Youth Card.")
elif age < 18 and is_resident == "no":
    print("Welcome, " + name + "! You qualify for a Youth Card ($5/year).")
elif is_resident == "yes":
    print("Welcome, " + name + "! You qualify for a free Adult Card.")
else:
    print("Welcome, " + name + "! You qualify for an Adult Card ($25/year).")
```

### Walkthrough

**Step 1 — Collect input**

```python
name = input("What is your name? ")
age = int(input("How old are you? "))
is_resident = input("Do you live in the city? (yes/no): ").lower()
```

* `input()` always returns a string. For `age`, we wrap it in `int()` so we can use it in numeric comparisons like `age < 18`.
* `.lower()` converts the user's answer to lowercase (`"Yes"`, `"YES"`, and `"yes"` all become `"yes"`), so the comparison works regardless of how they type it.

**Step 2 — Check age first**

```python
if age < 5:
    print("Sorry, " + name + ", you must be at least 5 years old to get a library card.")
```

The age-5 rule applies regardless of residency, so we handle it before any other conditions.

**Step 3 — Use `and` to check two conditions at once**

```python
elif age < 18 and is_resident == "yes":
    print("Welcome, " + name + "! You qualify for a free Youth Card.")
elif age < 18 and is_resident == "no":
    print("Welcome, " + name + "! You qualify for a Youth Card ($5/year).")
```

Each branch combines an age check with a residency check using `and`. Both conditions have to be true for the branch to run.

**Step 4 — Handle the adult cases**

```python
elif is_resident == "yes":
    print("Welcome, " + name + "! You qualify for a free Adult Card.")
else:
    print("Welcome, " + name + "! You qualify for an Adult Card ($25/year).")
```

By the time Python reaches these lines, we already know the user is 18 or older (because all the `age < 18` branches were skipped). So we only need to check residency. The final `else` catches any remaining case — an adult non-resident.

---

## Extension Challenge

The library also offers a **Senior Card** (free for residents, $10/year for non-residents) for visitors aged 65 and older.

Add two new branches to the script to handle senior visitors. Make sure they appear in the right order — think about which age checks need to come first.

<details>

<summary>Hint</summary>

The `age >= 65` check needs to come **before** the general adult check, otherwise Python will match adults first and never reach the senior branch.

</details>

---

## Practice Assignment

Write your own eligibility or decision script. It can check anything — event admission, a discount, a quiz result, a recommendation — as long as it meets these requirements:

- [ ] Collects input from the user with at least **two** `input()` calls
- [ ] Uses at least one `if`/`elif`/`else` chain with **at least three branches**
- [ ] Uses at least one **boolean operator** (`and`, `or`, or `not`)
- [ ] Prints a different, meaningful message for at least **three** different combinations of input

Share your work in the Slack #[class]-discussion channel!
