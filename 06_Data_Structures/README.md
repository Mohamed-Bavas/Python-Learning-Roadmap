# 🐍 Day 06 – Python Data Structures

Welcome to **Day 06** of my **Python Programming Learning Journey** 🚀

Today I completed learning **Data Structures in Python**. Data structures are used to store, organize, and manage collections of data efficiently.

---

## 🎯 Topics Covered

* Lists
* Tuples
* Sets
* Dictionaries
* List Comprehension
* Dictionary Comprehension

---

## 📁 Files Created

```text
06_Data_Structures/
│
├── list.py
├── tuple.py
├── set.py
└── dictionary.py
```

---

## 🔹 1. Lists

A list is an ordered and mutable collection of elements.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(fruits[0])

fruits.append("Orange")

print(fruits)
```

Output:

```text
['Apple', 'Banana', 'Mango']
Apple
['Apple', 'Banana', 'Mango', 'Orange']
```

### Common List Methods

* `append()`
* `insert()`
* `remove()`
* `pop()`
* `sort()`
* `reverse()`
* `clear()`

---

## 🔹 2. Tuples

A tuple is an ordered and immutable collection of elements.

```python
numbers = (10, 20, 30, 40)

print(numbers)
print(numbers[1])
```

Output:

```text
(10, 20, 30, 40)
20
```

### Important Point

```text
List  → Mutable
Tuple → Immutable
```

---

## 🔹 3. Sets

A set is a collection that stores unique elements.

```python
numbers = {10, 20, 30, 20, 10}

print(numbers)

numbers.add(40)

print(numbers)
```

Output:

```text
{10, 20, 30}
{10, 20, 30, 40}
```

### Common Set Methods

* `add()`
* `remove()`
* `discard()`
* `union()`
* `intersection()`
* `difference()`

---

## 🔹 4. Dictionaries

A dictionary stores data as **key-value pairs**.

```python
student = {
    "name": "Bavas",
    "age": 20,
    "course": "Python"
}

print(student)
print(student["name"])
```

Output:

```text
{'name': 'Bavas', 'age': 20, 'course': 'Python'}
Bavas
```

### Common Dictionary Methods

* `keys()`
* `values()`
* `items()`
* `get()`
* `update()`
* `pop()`

---

## 🔹 5. List Comprehension

List comprehension provides a short way to create a list.

```python
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

### With Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

---

## 🔹 6. Dictionary Comprehension

Dictionary comprehension provides a short way to create dictionaries.

```python
numbers = [1, 2, 3, 4, 5]

squares = {x: x * x for x in numbers}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## 🧪 Practice Programs

I practiced the following programs:

* Create and modify a list
* Add and remove list elements
* Access list elements using indexes
* Create and access tuples
* Perform set operations
* Remove duplicate values using sets
* Create and update dictionaries
* Access dictionary values
* Loop through dictionaries
* Create lists using list comprehension
* Create dictionaries using dictionary comprehension

---

## 🧠 List vs Tuple vs Set vs Dictionary

| Data Structure | Ordered | Mutable | Duplicate Values | Key-Value |
| -------------- | ------- | ------- | ---------------- | --------- |
| List           | ✅       | ✅       | ✅                | ❌         |
| Tuple          | ✅       | ❌       | ✅                | ❌         |
| Set            | ❌       | ✅       | ❌                | ❌         |
| Dictionary     | ✅       | ✅       | Keys: ❌          | ✅         |

> Note: Python dictionaries preserve insertion order in modern Python versions.

---

## 🧠 What I Learned

* How to create and use lists
* How list methods work
* Difference between lists and tuples
* How sets store unique values
* How to perform set operations
* How dictionaries store key-value pairs
* How to access and update dictionary values
* How list comprehension works
* How dictionary comprehension works
* When to use different Python data structures

---

## 📊 Learning Progress

| Day    | Topic                  | Status        |
| ------ | ---------------------- | ------------- |
| Day 01 | Python Basics          | ✅ Completed   |
| Day 02 | Operators              | ✅ Completed   |
| Day 03 | Conditional Statements | ✅ Completed   |
| Day 04 | Loops                  | ✅ Completed   |
| Day 05 | Functions              | ✅ Completed   |
| Day 06 | Data Structures        | ✅ Completed   |
| Day 07 | Strings                | ⬜ Not Started |
| Day 08 | File Handling          | ⬜ Not Started |
| Day 09 | Exception Handling     | ⬜ Not Started |
| Day 10 | OOP                    | ⬜ Not Started |
| Day 11 | Modules & Packages     | ⬜ Not Started |
| Day 12 | Advanced Python        | ⬜ Not Started |
| Day 13 | SQLite                 | ⬜ Not Started |
| Day 14 | Practice Programs      | ⬜ Not Started |
| Day 15 | Mini Project           | ⬜ Not Started |

### 📈 Overall Progress

**6 / 15 Days Completed → 40%**

```text
████████░░░░░░░░░░░░ 40%
```

---

## 🔧 Tools Used

* 🐍 Python
* 💻 VS Code
* 🔧 Git
* 🌐 GitHub

---

## 📌 Git Commit

```bash
git add .
git commit -m "Complete Day 06 Python Data Structures"
git push origin main
```

### Example Commit Messages

```text
Complete Day 06 Python Data Structures
Add list examples
Add tuple examples
Add set examples
Add dictionary examples
Add list comprehension examples
Add dictionary comprehension examples
```

---

## 🚀 Next Step

### Day 07 – Strings

Topics planned:

* String Creation
* String Indexing
* String Slicing
* String Methods
* String Formatting
* String Programs

---

## 🎯 Learning Approach

**Learn → Practice → Build → Commit → Improve 🚀**

---

⭐ This repository documents my daily Python learning progress and practical coding journey.
