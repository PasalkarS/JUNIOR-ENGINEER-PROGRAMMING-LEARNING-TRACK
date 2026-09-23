# 19 - Advanced F-String Padding and Alignment
# Aligns text columns using format specifiers.

item1, price1 = "Coffee", 3.50
item2, price2 = "Sandwich", 8.25
item3, price3 = "Cheesecake", 5.00

print(f"{'Item':<15} {'Price':>8}")
print("-" * 24)
print(f"{item1:<15} ${price1:>7.2f}")
print(f"{item2:<15} ${price2:>7.2f}")
print(f"{item3:<15} ${price3:>7.2f}")
