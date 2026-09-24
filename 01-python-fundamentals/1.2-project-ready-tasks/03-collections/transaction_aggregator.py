transactions = [
    {"name": "Sam", "amount": 100},
    {"name": "John", "amount": 200},
    {"name": "Sam", "amount": 150},
    {"name": "Alex", "amount": 300}
]

total = 0

for transaction in transactions:
    total = total + transaction["amount"]

print("Total:", total)
