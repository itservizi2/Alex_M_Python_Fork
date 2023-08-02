class BankAccountError(Exception):
    pass


class BankAccount:
    def __init__(self, account_number, account_holder_name):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = 0

    def get_account_number(self):
        return self.__account_number

    def get_account_holder_name(self):
        return self.__account_holder_name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise BankAccountError("Insufficient balance")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, interest_rate):
        super().__init__(account_number, account_holder_name)
        self.__interest_rate = interest_rate

    def get_interest_rate(self):
        return self.__interest_rate


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, overdraft_limit):
        super().__init__(account_number, account_holder_name)
        self.__overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self.__overdraft_limit

    def withdraw(self, amount):
        if amount > self.__overdraft_limit:
            raise BankAccountError("Overdraft limit exceeded")
        super().withdraw(amount)


# Cream conturile mai intii
savings = SavingsAccount("1234", "Petre Marinescu", 0.05)
current = CurrentAccount("4567", "Petre Marinescu", 1000)

# Testam deposit and withdraw pe contul de economii savings
print("Savings Account Balance:", savings.get_balance())
savings.deposit(500)
print("Savings Account Balance:", savings.get_balance())

try:
    savings.withdraw(700)
except BankAccountError as e:
    print(e)
print("Savings Account Balance:", savings.get_balance())

# Testam overdraft protectie  pe cont current
print("Current Account Balance:", current.get_balance())

try:
    current.withdraw(2000)
except BankAccountError as e:
    print(e)

print("Current Account Balance:", current.get_balance())

