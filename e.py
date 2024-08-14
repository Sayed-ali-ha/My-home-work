class BankAccount:
    def __init__(self, account_name, initial_balance=0):
        self.__account_name = account_name  # ویژگی خصوصی برای نام حساب
        self.__balance = initial_balance    # ویژگی خصوصی برای موجودی

    # متدهای عمومی برای دریافت مقادیر
    def get_account_name(self):
        return self.__account_name

    def get_balance(self):
        return self.__balance

    # متدهای عمومی برای تنظیم مقادیر
    def set_account_name(self, account_name):
        self.__account_name = account_name

    # متد واریز پول
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited {amount}. Current balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # متد برداشت پول
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew {amount}. Current balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# مثال از استفاده
my_account = BankAccount("John Doe", 1000)

# دریافت اطلاعات حساب
print("Account Name:", my_account.get_account_name())
print("Initial Balance:", my_account.get_balance())

# واریز پول
my_account.deposit(500)

# برداشت پول
my_account.withdraw(300)

# دریافت موجودی نهایی
print("Final Balance:", my_account.get_balance())
