# 🐍 Day 07 – Python Strings

Welcome to **Day 07** of my Python Programming Learning Journey 🚀

Today I learned about **Strings in Python**, including string creation, indexing, slicing, string methods, string formatting, and basic string programming problems.

---

# 📚 Topics Covered

## 1. String Creation

* Creating strings
* Single quotes
* Double quotes
* Multi-line strings
* String variables

Example:

```python
name = "Mohamed"
message = 'Hello Python'

print(name)
print(message)
```

---

## 2. String Indexing

String indexing is used to access individual characters from a string.

```python
text = "Python"

print(text[0])
print(text[1])
print(text[-1])
```

---

## 3. String Slicing

String slicing is used to extract a portion of a string.

```python
text = "Python Programming"

print(text[0:6])
print(text[7:])
print(text[:6])
print(text[::-1])
```

---

## 4. String Methods

I practiced commonly used Python string methods.

### Common Methods

* `upper()`
* `lower()`
* `capitalize()`
* `title()`
* `strip()`
* `replace()`
* `split()`
* `find()`
* `count()`
* `startswith()`
* `endswith()`

Example:

```python
text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("python", "Python"))
print(text.count("p"))
```

---

## 5. String Formatting

I learned how to insert variables into strings using string formatting.

### f-string

```python
name = "Mohamed"
age = 20

print(f"My name is {name}")
print(f"I am {age} years old")
```

### `format()` Method

```python
name = "Mohamed"
course = "Python"

print("My name is {} and I am learning {}".format(name, course))
```

---

# 💻 String Programs

I practiced basic programming problems using strings.

### Programs Practiced

* Reverse a String
* Check Palindrome
* Count Characters
* Count Vowels
* Count Words
* Find String Length
* Remove Spaces
* Convert Uppercase / Lowercase
* Count Occurrences of a Character

Example:

```python
text = input("Enter a string: ")

reverse = text[::-1]

print("Reverse:", reverse)
```

---

# 📂 Repository Structure

```text
07_Strings/
│
├── string_methods.py
└── string_programs.py
```

---

# 📄 Files Description

### `string_methods.py`

Contains examples and practice programs for commonly used Python string methods.

Topics include:

* `upper()`
* `lower()`
* `capitalize()`
* `title()`
* `strip()`
* `replace()`
* `split()`
* `find()`
* `count()`
* `startswith()`
* `endswith()`

### `string_programs.py`

Contains basic string programming problems and practice exercises.

Examples:

* Reverse a String
* Palindrome Check
* Count Vowels
* Count Characters
* Count Words
* String Length
* Remove Spaces

---

# 🧠 What I Learned

Through Day 07, I learned:

* How to create strings in Python
* How string indexing works
* How to use positive and negative indexes
* How to slice strings
* How to use common string methods
* How to format strings using f-strings
* How to solve basic string programming problems
* How to manipulate and process strings

---

# 🔧 Git Workflow

I use Git and GitHub to track my learning progress.

```bash
git add .
git commit -m "Complete Day 07 Python Strings"
git push origin main
```

### Example Commit Messages

```text
Complete Day 07 Python Strings
Add string methods examples
Add string programs
Add palindrome program
Add reverse string program
Add string practice programs
```

---

# 📈 Learning Progress

**Overall Progress:** `46.67%` 🎯

**7 / 15 Days Completed**

```text
Python Basics          ✅
Operators              ✅
Conditions             ✅
Loops                  ✅
Functions              ✅
Data Structures        ✅
Strings                ✅
File Handling          ⬜
Exception Handling     ⬜
OOP                    ⬜
Modules & Packages     ⬜
Advanced Python        ⬜
SQLite                 ⬜
Practice Programs      ⬜
Mini Projects          ⬜
```

### Progress Bar

```text
█████████░░░░░░░░░░░ 46.67%
```

---

# 🎯 Day 07 Goal

The goal of Day 07 was to understand **Python Strings** and practice different string operations and programming problems.

**Status:** ✅ Completed

---

# 🚀 Next Step

### Day 08 – File Handling

Topics to learn:

* Open Files
* Read Files
* Write Files
* Append Data
* File Modes
* CSV Files

---

## 👨‍💻 Learning Journey

**Learn → Practice → Build → Commit → Improve 🚀**

**Day 07 Completed Successfully! 🎉**

**7 / 15 Days Completed → 46.67% Progress 🐍**
