price = float(input("Enter price: "))
tax_rate = float(input("Enter tax rate: "))

tax = price * tax_rate / 100
total = price + tax

print("Tax:", tax)
print("Total price:", total)
