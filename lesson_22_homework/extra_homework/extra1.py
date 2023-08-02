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
            print("Insufficient balance")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, interest_rate):
        super().__init__(account_number, account_holder_name)
        self.__interest_rate = interest_rate


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, overdraft_limit):
        super().__init__(account_number, account_holder_name)
        self.__overdraft_limit = overdraft_limit

# Cream conturile mai intii
savings = SavingsAccount("1234", "Petre Marinescu", 0.05)
current = CurrentAccount("4567", "Petre Marinescu", 1000)

# Testam deposit and withdraw pe contul de economii savings
def test_savings_deposit():
    print("Savings Account Balance:", savings.get_balance())
    savings.deposit(500)
    print("Savings Account Balance:", savings.get_balance())

def test_savings_withdraw():
    print("Savings Account Balance:", savings.get_balance())
    savings.withdraw(200)
    print("Savings Account Balance:", savings.get_balance())

# Testam overdraft protectie  pe cont current
def test_current_overdraft():
    print("Current Account Balance:", current.get_balance())
    current.withdraw(2000)
    print("Current Account Balance:", current.get_balance())

# Rulam testele
test_savings_deposit()
test_savings_withdraw()
test_current_overdraft()
