# 🐍 Day 08 – Python File Handling

Welcome to **Day 08** of my Python Programming Learning Journey 🚀

Today I learned about **File Handling in Python**, including opening, reading, writing, appending, and working with different file modes.

File handling is useful for storing and retrieving data from files using Python programs.

---

# 📚 Topics Covered

## 1. Opening Files

Python provides the `open()` function to open a file.

```python
file = open("example.txt", "r")

print(file.read())

file.close()
```

---

## 2. Reading Files

I learned different ways to read data from a file.

### `read()`

Reads the complete file.

```python
file = open("example.txt", "r")

data = file.read()

print(data)

file.close()
```

### `readline()`

Reads one line from the file.

```python
file = open("example.txt", "r")

line = file.readline()

print(line)

file.close()
```

### `readlines()`

Reads all lines and returns them as a list.

```python
file = open("example.txt", "r")

lines = file.readlines()

print(lines)

file.close()
```

---

## 3. Writing to Files

The `"w"` mode is used to write data to a file.

```python
file = open("example.txt", "w")

file.write("Hello Python")

file.close()
```

> `w` mode creates a new file if it does not exist and overwrites existing content.

---

## 4. Appending Data

The `"a"` mode is used to add data at the end of an existing file.

```python
file = open("example.txt", "a")

file.write("\nLearning File Handling")

file.close()
```

---

# 📂 File Modes

Python provides different modes for working with files.

| Mode | Description       |
| ---- | ----------------- |
| `r`  | Read              |
| `w`  | Write             |
| `a`  | Append            |
| `x`  | Create a new file |
| `r+` | Read and Write    |
| `w+` | Write and Read    |
| `a+` | Append and Read   |

---

# 5. Using `with open()`

The `with` statement automatically closes the file after completing the operation.

```python
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
```

This is the recommended way to work with files in Python.

---

# 6. Working with CSV Files

CSV stands for **Comma-Separated Values**.

Python provides the built-in `csv` module to work with CSV files.

Example:

```python
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

# 💻 File Handling Practice

I practiced basic file handling operations such as:

* Creating a file
* Writing data
* Reading data
* Appending data
* Reading individual lines
* Reading multiple lines
* Working with file modes
* Using `with open()`
* Reading CSV files

---

# 📂 Repository Structure

```text
08_File_Handling/
│
├── file_read.py
├── file_write.py
└── file_append.py
```

---

# 📄 Files Description

### `file_read.py`

Contains examples for reading data from files.

Topics:

* `read()`
* `readline()`
* `readlines()`

---

### `file_write.py`

Contains examples for creating and writing data to files.

Topics:

* `open()`
* `"w"` mode
* `write()`

---

### `file_append.py`

Contains examples for adding new data to existing files.

Topics:

* `"a"` mode
* `write()`
* Appending multiple lines

---

### `csv_file.py`

Contains basic examples of working with CSV files using Python's `csv` module.

---

# 🧠 What I Learned

Through Day 08, I learned:

* How to open files using `open()`
* How to read file contents
* How to write data to files
* How to append data to files
* How different file modes work
* How to use `with open()`
* How to work with CSV files
* How to safely close files

---

# 📝 Practice Programs

I practiced the following file handling programs:

```text
1. Create a File
2. Write Data to a File
3. Read a File
4. Append Data to a File
5. Read File Line by Line
6. Count Number of Lines
7. Count Number of Words
8. Copy File Contents
9. Store Student Details in a File
10. Read CSV File
```

---

# 🔧 Git Workflow

I use Git and GitHub to track my learning progress.

```bash
git add .
git commit -m "Complete Day 08 Python File Handling"
git push origin main
```

### Example Commit Messages

```text
Complete Day 08 Python File Handling
Add file reading examples
Add file writing examples
Add file append examples
Add file mode examples
Add with open examples
Add CSV file examples
Add file handling practice programs
```

---

# 📈 Learning Progress

**Overall Progress:** `53.33%` 🎯

**8 / 15 Days Completed**

```text
Python Basics          ✅
Operators              ✅
Conditions             ✅
Loops                  ✅
Functions              ✅
Data Structures        ✅
Strings                ✅
File Handling          ✅
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
██████████░░░░░░░░░░ 53.33%
```

---

# 🎯 Day 08 Goal

The goal of Day 08 was to understand how Python programs can **create, read, write, modify, and manage data stored in files**.

**Status:** ✅ Completed

---

# 🚀 Next Step

### Day 09 – Exception Handling

Topics to learn:

* `try`
* `except`
* `else`
* `finally`
* Raising Exceptions
* Custom Exceptions

---

## 👨‍💻 Learning Journey

**Learn → Practice → Build → Commit → Improve 🚀**

**Day 08 Completed Successfully! 🎉**

**8 / 15 Days Completed → 53.33% Progress 🐍**
