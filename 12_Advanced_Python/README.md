# 🐍 Day 12 – Advanced Python

Welcome to **Day 12** of my Python Programming Learning Journey 🚀

Today I practiced advanced Python concepts that help me understand how functions can be extended, values can be generated one at a time, and objects can be accessed through iteration.

The main focus was on **Decorators, Generators, and Iterators**.

---

## 📚 Topics Covered

### 1. Iterators

An **iterator** is an object that allows us to access elements one at a time.

Python provides two built-in functions for working with iterators:

* `iter()` – Creates an iterator from an iterable.
* `next()` – Returns the next item from an iterator.

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
30
```

Practice file: `iterators.py`

---

### 2. Generators

A **generator** is a special type of iterator that produces values one at a time using the `yield` keyword.

Generators can help save memory when working with large sequences because they do not need to store all generated values at once.

Example:

```python
def count_numbers():
    yield 1
    yield 2
    yield 3

for number in count_numbers():
    print(number)
```

Output:

```text
1
2
3
```

Practice file: `generators.py`

---

### 3. Decorators

A **decorator** is a function that adds or modifies the behavior of another function without changing its original code directly.

Decorators are commonly written using the `@` symbol.

Example:

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def greet():
    print("Hello Python")

greet()
```

Output:

```text
Before function
Hello Python
After function
```

Practice file: `decorators.py`

---

## 📂 Repository Structure

```text
12_Advanced_Python/
│
├── decorators.py
├── generators.py
└── iterators.py
```

---

## 📄 Files Description

### `decorators.py`

Practiced how decorators wrap functions and add behavior before or after a function call.

### `generators.py`

Practiced creating generators and producing values using the `yield` keyword.

### `iterators.py`

Practiced creating iterators using `iter()` and retrieving values using `next()`.

---

## 💻 Practice Programs

The following three Python files were practiced:

1. **`decorators.py`** – Understanding and using decorators.
2. **`generators.py`** – Creating generators with `yield`.
3. **`iterators.py`** – Working with iterators using `iter()` and `next()`.

---

## 🧠 What I Learned

Through Day 12, I learned:

* How iterators work in Python
* How to use `iter()` and `next()`
* How generators produce values using `yield`
* How generators can help reduce memory usage
* What decorators are
* How decorators modify function behavior
* How these concepts help in writing reusable Python code

---

## 📊 Learning Progress

**Day 12 Progress:** `100%`

**Overall Progress:** `80%`

**12 / 15 Days Completed**

```text
████████████████░░░░ 80%
```

---

## 🏆 Current Status

* ✅ Completed: **12 / 15 Days**
* 📈 Current Progress: **80%**
* 📚 Current Level: **Python Fundamentals + OOP + Modules + Advanced Python**
* 🚀 Next Step: **Day 13 – Database Programming / SQLite**

---

## 🎯 Goal

My goal is to strengthen my Python programming fundamentals and gradually develop the skills needed to build practical applications for **Software Development, Automation, Scripting, and Embedded Systems**.

---

## 🚀 Next Step

### Day 13 – Database Programming / SQLite

Next, I plan to learn:

* SQLite Introduction
* Creating a Database
* Creating Tables
* Inserting Data
* Reading Data
* Updating Data
* Deleting Data
* SQL Queries
* Connecting Python with SQLite

---

## 🔥 Learning Journey

> **Learn → Practice → Build → Improve → Repeat**

⭐ Continuing my Python Programming Learning Journey step by step.
