class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # ویژگی خصوصی

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited {amount}. Current balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew {amount}. Current balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance

# مثال از استفاده
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Final Balance:", account.get_balance())

