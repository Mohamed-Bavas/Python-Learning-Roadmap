# 🐍 Day 09 – Python Exception Handling

Welcome to **Day 09** of my Python Programming Learning Journey 🚀

Today I learned about **Exception Handling in Python**, including handling errors using `try`, `except`, `else`, and `finally`.

Exception handling is useful for preventing programs from crashing when unexpected errors occur and allows us to handle errors safely.

---

# 📚 Topics Covered

## 1. `try`

The `try` block contains code that may cause an exception.

```python
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input")
```

---

## 2. `except`

The `except` block is used to handle an exception.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 3. Handling Multiple Exceptions

Python allows us to handle different types of exceptions separately.

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print(result)

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 4. `else`

The `else` block runs when no exception occurs in the `try` block.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", number)
```

---

## 5. `finally`

The `finally` block always executes whether an exception occurs or not.

```python
try:
    print("Program is running")

except:
    print("An error occurred")

finally:
    print("Program completed")
```

---

# 📂 Exception Handling Structure

Python exception handling generally follows this structure:

```python
try:
    # Code that may cause an error

except:
    # Handle the error

else:
    # Runs when there is no error

finally:
    # Always runs
```

---

# 6. Common Python Exceptions

Python provides many built-in exceptions.

| Exception           | Description              |
| ------------------- | ------------------------ |
| `ValueError`        | Invalid value            |
| `TypeError`         | Incorrect data type      |
| `ZeroDivisionError` | Division by zero         |
| `IndexError`        | Invalid list index       |
| `KeyError`          | Dictionary key not found |
| `FileNotFoundError` | File does not exist      |
| `NameError`         | Variable is not defined  |
| `AttributeError`    | Invalid object attribute |

---

# 7. Raising Exceptions

The `raise` keyword is used to manually generate an exception.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

# 8. Custom Exceptions

Python allows us to create our own exception classes.

```python
class AgeError(Exception):
    pass

age = 15

if age < 18:
    raise AgeError("Age must be 18 or above")
```

Custom exceptions are useful when we want to create meaningful errors for our applications.

---

# 💻 Exception Handling Practice

I practiced exception handling using two Python programs:

* Handling exceptions using `try` and `except`
* Creating and using a custom exception

---

# 📂 Repository Structure

```text
09_Exception_Handling/
│
├── try_except.py
└── custom_exception.py
```

---

# 📄 Files Description

### `try_except.py`

Contains basic examples of handling exceptions using `try` and `except`.

Topics:

* `try`
* `except`
* `ValueError`
* `ZeroDivisionError`
* Basic exception handling

---

### `custom_exception.py`

Contains an example of creating and using a custom exception.

Topics:

* Custom exception class
* `Exception`
* `raise`
* Error handling

---

# 📝 Practice Programs

I practiced the following two exception handling programs:

```text
1. try_except.py
   → Basic exception handling using try and except

2. custom_exception.py
   → Creating and raising a custom exception
```

---

# 🧠 What I Learned

Through Day 09, I learned:

* What exceptions are
* How to use `try`
* How to use `except`
* How to handle common exceptions
* How `else` works with exception handling
* How `finally` works
* How to raise exceptions using `raise`
* How to create custom exceptions
* How exception handling helps prevent program crashes

---

# 📈 Learning Progress

**Overall Progress:** `60%` 🎯

**9 / 15 Days Completed**

```text
Python Basics          ✅
Operators              ✅
Conditions             ✅
Loops                  ✅
Functions              ✅
Data Structures        ✅
Strings                ✅
File Handling          ✅
Exception Handling     ✅
OOP                    ⬜
Modules & Packages     ⬜
Advanced Python        ⬜
SQLite                 ⬜
Practice Programs      ⬜
Mini Projects          ⬜
```

### Progress Bar

```text
████████████░░░░░░░░ 60%
```

---

# 🎯 Day 09 Goal

The goal of Day 09 was to understand how Python programs can **detect and handle errors using exception handling**.

I learned the basic concepts of `try`, `except`, `else`, `finally`, `raise`, and custom exceptions.

**Status:** ✅ Completed

---

# 🚀 Next Step

### Day 10 – Object-Oriented Programming

Topics to learn:

* Classes
* Objects
* Constructors
* Instance Variables
* Methods
* Inheritance
* Polymorphism
* Encapsulation
* Abstraction

---

## 👨‍💻 Learning Journey

**Learn → Practice → Build → Improve 🚀**

**Day 09 Completed Successfully! 🎉**

**9 / 15 Days Completed → 60% Progress 🐍**
