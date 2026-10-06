
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = 0
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be greater than zero")
        else:
            self._balance += amount
            print("Deposit successful")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be greater than zero")
        elif amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
            print("Withdrawal successful")

    def show_account(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)


account1 = BankAccount("Rahul", 5000)

account1.deposit(1000)
account1.withdraw(2000)
account1.show_account()

"""
Deposit successful
Withdrawal successful
Owner: Rahul
Balance: 4000
"""
