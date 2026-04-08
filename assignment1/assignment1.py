# Task 1: Hello
def hello():
    return 'Hello!'

# Task 2: Greet with Strings
def greet(name):
    return f'Hello, {name}!'

# Task 3: Calculator
def calc(a, b, operation='multiply'):
    try:
        if operation == 'add':
            return a+b
        elif operation == 'subtract':
            return a-b
        elif operation == 'multiply':
            return a*b
        elif operation == 'divide':
            return a/b
        elif operation == 'modulo':
            return a%b
        elif operation == 'int_divide':
            return a//b
        elif operation == 'power':
            return a**b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
# Task 4: Data Type Conversion
# Task 4: Data Type Conversion
def data_type_conversion(value, type_name):
    try:
        if type_name == 'float':
            return float(value)
        elif type_name == 'str':
            return str(value)
        elif type_name == 'int':
            return int(value)
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type_name}."

# Task 5: Grading System
def grade(*args):
    try:
        if not args:
            return "Invalid data was provided."
        average = sum(args) / len(args)
        if average >= 90: return "A"
        elif average >= 80: return "B"
        elif average >= 70: return "C"
        elif average >= 60: return "D"
        else: return "F"
    except TypeError:
        return "Invalid data was provided."

# Task 6: Repeat      
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

# Task 7: Student Scores
def student_scores(mode, **kwargs):
    if not kwargs: return 0
    if mode == "best":
        return max(kwargs, key=kwargs.get)
    return sum(kwargs.values()) / len(kwargs)
# Task 8: Titleize
def titleize(text):
    words = text.split()
    little = ['a', 'on', 'an', 'the', 'of', 'and', 'is', 'in']
    res = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little:
            res.append(word.capitalize())
        else:
            res.append(word.lower())
    return " ".join(res)

# Task 9: Hangman
def hangman(secret, guess):
    return "".join([c if c in guess else "_" for c in secret])

# Task 10: Pig Latin
def pig_latin(text):
    vowels = "aeiou"
    res = []
    for word in text.split():
        if word[0] in vowels:
            res.append(word + "ay")
        # Fix for 'square', 'quiet', etc.
        elif "qu" in word:
            idx = word.find("qu") + 2
            res.append(word[idx:] + word[:idx] + "ay")
        else:
            idx = next((i for i, c in enumerate(word) if c in vowels), 0)
            res.append(word[idx:] + word[:idx] + "ay")
    return " ".join(res)