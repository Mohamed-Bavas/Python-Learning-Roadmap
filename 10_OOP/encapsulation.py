class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def display_balance(self):
        print("Balance:", self.__balance)
account = BankAccount(1000)
account.deposit(500)
account.display_balance()