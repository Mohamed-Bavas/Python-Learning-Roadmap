expenses = []
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expense = {
        "name": name,
        "amount": amount
    }
    expenses.append(expense)
    print("Expense added successfully")
def display_expenses():
    if not expenses:
        print("No expenses found")
        return
    total = 0
    for expense in expenses:
        print(
            expense["name"],
            "- ₹",
            expense["amount"]
        )
        total += expense["amount"]
    print("----------------")
    print("Total Expense: ₹", total)
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        display_expenses()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice")