# Topic 02: Encapsulation & Invariant Protection
# Demonstrates protecting object state using properties and validation setters.

class BankAccount:
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_number = account_number
        self._balance = initial_balance
        self._is_frozen = False

    @property
    def balance(self) -> float:
        """Read-only access to account balance."""
        return self._balance

    @property
    def is_frozen(self) -> bool:
        return self._is_frozen

    def freeze(self):
        self._is_frozen = True

    def unfreeze(self):
        self._is_frozen = False

    def deposit(self, amount: float) -> None:
        if self._is_frozen:
            raise PermissionError("Account is frozen. Transactions disabled.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if self._is_frozen:
            raise PermissionError("Account is frozen. Transactions disabled.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds: Balance is ${self._balance:.2f}, tried to withdraw ${amount:.2f}")
        self._balance -= amount

if __name__ == "__main__":
    acc = BankAccount("ACC-9988", 250.0)
    print(f"Account: {acc.account_number} | Balance: ${acc.balance:.2f}")

    acc.deposit(100.0)
    print("Deposited $100 -> New balance:", acc.balance)

    acc.withdraw(50.0)
    print("Withdrew $50 -> New balance:", acc.balance)

    try:
        acc.withdraw(500.0)
    except ValueError as e:
        print("[CAUGHT]:", e)

    acc.freeze()
    try:
        acc.deposit(10.0)
    except PermissionError as e:
        print("[CAUGHT]:", e)
