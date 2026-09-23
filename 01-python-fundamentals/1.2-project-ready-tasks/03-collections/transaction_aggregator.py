# Transaction Aggregator
# Aggregates debit/credit transactions by category.

transactions = [
    {"id": "TX1", "type": "DEBIT", "category": "Food", "amount": 42.50},
    {"id": "TX2", "type": "DEBIT", "category": "Transport", "amount": 15.00},
    {"id": "TX3", "type": "CREDIT", "category": "Salary", "amount": 3200.00},
    {"id": "TX4", "type": "DEBIT", "category": "Food", "amount": 18.25},
    {"id": "TX5", "type": "DEBIT", "category": "Utilities", "amount": 120.00},
    {"id": "TX6", "type": "DEBIT", "category": "Food", "amount": 65.00},
]

category_totals = {}
total_expenses = 0.0
total_income = 0.0

for tx in transactions:
    amt = tx["amount"]
    if tx["type"] == "DEBIT":
        total_expenses += amt
        cat = tx["category"]
        category_totals[cat] = category_totals.get(cat, 0.0) + amt
    elif tx["type"] == "CREDIT":
        total_income += amt

net_savings = total_income - total_expenses

print(f"Total Income:   ${total_income:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Net Savings:    ${net_savings:.2f}")
print("\nExpenses by Category:")
for cat, total in category_totals.items():
    print(f" - {cat:<12}: ${total:.2f}")
