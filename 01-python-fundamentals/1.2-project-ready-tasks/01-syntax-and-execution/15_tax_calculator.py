# 15 - Sales Tax Calculation
# Computes tax and grand total with clean rounding.

subtotal = 149.99
tax_rate = 0.0825  # 8.25%

tax_amount = round(subtotal * tax_rate, 2)
grand_total = round(subtotal + tax_amount, 2)

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8.25%): ${tax_amount:.2f}")
print(f"Grand Total: ${grand_total:.2f}")
