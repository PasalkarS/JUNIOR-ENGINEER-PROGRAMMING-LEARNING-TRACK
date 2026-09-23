# 10 - Simple Interest Calculator
# Formula: (Principal * Rate * Time) / 100

principal = 10000.0  # Dollars
rate = 5.5           # Annual rate %
time_years = 3       # Years

interest = (principal * rate * time_years) / 100
total_balance = principal + interest

print(f"Principal: ${principal:.2f}")
print(f"Interest Earned: ${interest:.2f}")
print(f"Total Balance: ${total_balance:.2f}")
