import sqlite3

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY,
    account_holder TEXT NOT NULL,
    balance REAL NOT NULL CHECK (balance >= 0)
)
""")

cursor.execute("""
INSERT OR IGNORE INTO accounts
(account_id, account_holder, balance)
VALUES (1, 'Alice', 5000.00)
""")

cursor.execute("""
INSERT OR IGNORE INTO accounts
(account_id, account_holder, balance)
VALUES (2, 'Bob', 2000.00)
""")

connection.commit()


def show_accounts():
    cursor.execute("SELECT * FROM accounts")

    accounts = cursor.fetchall()

    for account in accounts:
        print(account)


def transfer_money(from_account, to_account, amount):
    try:
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")

        cursor.execute("BEGIN")

        cursor.execute(
            "SELECT balance FROM accounts WHERE account_id = ?",
            (from_account,)
        )
        sender = cursor.fetchone()

        cursor.execute(
            "SELECT balance FROM accounts WHERE account_id = ?",
            (to_account,)
        )
        receiver = cursor.fetchone()

        if sender is None:
            raise ValueError("Sender account does not exist.")

        if receiver is None:
            raise ValueError("Receiver account does not exist.")

        if sender[0] < amount:
            raise ValueError("Insufficient balance.")

        cursor.execute(
            "UPDATE accounts SET balance = balance - ? "
            "WHERE account_id = ?",
            (amount, from_account)
        )

        cursor.execute(
            "UPDATE accounts SET balance = balance + ? "
            "WHERE account_id = ?",
            (amount, to_account)
        )

        connection.commit()
        print("Transfer completed successfully.")

    except (ValueError, sqlite3.Error) as error:
        connection.rollback()
        print("Transfer failed:", error)
        print("All transfer changes have been rolled back.")


print("Accounts before transfer:")
show_accounts()

print("\nAttempting transfer of 1000 from Alice to Bob:")
transfer_money(1, 2, 1000)

print("\nAccounts after transfer:")
show_accounts()

print("\nAttempting transfer of 10000 from Alice to Bob:")
transfer_money(1, 2, 10000)

print("\nAccounts after failed transfer:")
show_accounts()

connection.close()
