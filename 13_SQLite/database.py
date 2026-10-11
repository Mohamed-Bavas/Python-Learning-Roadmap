import sqlite3
connection = sqlite3.connect("student.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
cursor.execute(
    "INSERT INTO students (name, age) VALUES (?, ?)",
    ("Mohamed", 20)
)
connection.commit()
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
for student in students:
    print(student)
connection.close()