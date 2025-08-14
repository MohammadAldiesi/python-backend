class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def display_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account[{self.account_number}] - Holder: {self.account_holder}, Balance: {self.__balance}"

    def __eq__(self, other):
        return self.account_number == other.account_number

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.display_balance() - amount >= 100:
            super().withdraw(amount)

class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.display_balance() - amount >= -self.overdraft_limit:
            super().withdraw(amount)

s1 = SavingsAccount(101, "Ali", 500, 0.03)
c1 = CheckingAccount(102, "Sara", 200, 150)
s1.withdraw(450)
c1.withdraw(300)
print(s1)
print(c1)
print(s1 == c1)
