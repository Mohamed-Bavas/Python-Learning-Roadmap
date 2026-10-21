students = []
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    student = {
        "name": name,
        "age": age
    }
    students.append(student)
    print("Student added successfully")
def display_students():
    if not students:
        print("No students found")
        return
    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("----------------")
while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")