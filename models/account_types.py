from .bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient balance")

    def check_balance(self):
        print(f"Savings Account {self.account_number} balance: UGX {self.balance}")

    def calculate_interest(self):
        interest = self.balance * self._interest_rate
        self.deposit(interest)

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=50000):
        super().__init__(account_number, balance)
        self._overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self._overdraft_limit:
            self.balance -= amount
        else:
            print("Withdrawal amount exceeds overdraft limit")

    def check_balance(self):
        print(f"Checking Account {self.account_number} balance: UGX {self.balance}")

# Dictionary to hold account instances
accounts = {}

def create_account(account_type, account_number):
    if account_number in accounts:
        print("Account number already exists.")
        return
    if account_type == "savings":
        accounts[account_number] = SavingsAccount(account_number)
    elif account_type == "checking":
        accounts[account_number] = CheckingAccount(account_number)
    else:
        print("Invalid account type.")
        return

def deposit(account_number, amount):
    if account_number in accounts:
        accounts[account_number].deposit(amount)
    else:
        print("Account not found.")

def withdraw(account_number, amount):
    if account_number in accounts:
        accounts[account_number].withdraw(amount)
    else:
        print("Account not found.")

def check_balance(account_number):
    if account_number in accounts:
        accounts[account_number].check_balance()
    else:
        print("Account not found.")
