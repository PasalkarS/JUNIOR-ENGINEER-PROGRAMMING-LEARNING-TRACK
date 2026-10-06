import pandas as pd

customers = pd.DataFrame({
    "Customer_ID": [1, 2, 3, 4],
    "Customer": ["Rahul", "Priya", "Amit", "Sneha"],
    "City": ["Pune", "Mumbai", "Delhi", "Pune"]
})

sales = pd.DataFrame({
    "Sale_ID": [101, 102, 103, 104, 105],
    "Customer_ID": [1, 2, 1, 3, 4],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop"],
    "Quantity": [1, 2, 1, 2, 1],
    "Price": [50000, 1000, 1500, 12000, 50000]
})

# Calculate total
sales["Total"] = sales["Quantity"] * sales["Price"]

print("----- SALES DATA -----")
print(sales)

# Sort sales
print("\n----- SORTED BY TOTAL -----")
print(sales.sort_values("Total", ascending=False))

# Filter sales
print("\n----- SALES ABOVE 10000 -----")
print(sales[sales["Total"] > 10000])

# Group and aggregate
print("\n----- CUSTOMER SALES SUMMARY -----")

customer_summary = sales.groupby("Customer_ID").agg(
    Total_Sales=("Total", "sum"),
    Total_Quantity=("Quantity", "sum")
)

print(customer_summary)

# Merge customers and sales
merged_data = pd.merge(
    sales,
    customers,
    on="Customer_ID",
    how="left"
)

print("\n----- MERGED DATA -----")
print(merged_data)

# City summary
city_summary = merged_data.groupby("City").agg(
    Total_Sales=("Total", "sum"),
    Total_Orders=("Sale_ID", "count")
)

print("\n----- CITY SUMMARY -----")
print(city_summary)

# Pivot table
pivot = pd.pivot_table(
    merged_data,
    values="Total",
    index="City",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)

print("\n----- PIVOT TABLE -----")
print(pivot)

"""
----- SALES DATA -----
   Sale_ID  Customer_ID   Product  Quantity  Price  Total
0      101            1    Laptop         1  50000  50000
1      102            2     Mouse         2   1000   2000
2      103            1  Keyboard         1   1500   1500
3      104            3   Monitor         2  12000  24000
4      105            4    Laptop         1  50000  50000

----- SORTED BY TOTAL -----
   Sale_ID  Customer_ID   Product  Quantity  Price  Total
0      101            1    Laptop         1  50000  50000
4      105            4    Laptop         1  50000  50000
3      104            3   Monitor         2  12000  24000
1      102            2     Mouse         2   1000   2000
2      103            1  Keyboard         1   1500   1500

----- SALES ABOVE 10000 -----
   Sale_ID  Customer_ID  Product  Quantity  Price  Total
0      101            1   Laptop         1  50000  50000
3      104            3  Monitor         2  12000  24000
4      105            4   Laptop         1  50000  50000

----- CUSTOMER SALES SUMMARY -----
             Total_Sales  Total_Quantity
Customer_ID                             
1                  51500               2
2                   2000               2
3                  24000               2
4                  50000               1

----- MERGED DATA -----
   Sale_ID  Customer_ID   Product  Quantity  Price  Total Customer    City
0      101            1    Laptop         1  50000  50000    Rahul    Pune
1      102            2     Mouse         2   1000   2000    Priya  Mumbai
2      103            1  Keyboard         1   1500   1500    Rahul    Pune
3      104            3   Monitor         2  12000  24000     Amit   Delhi
4      105            4    Laptop         1  50000  50000    Sneha    Pune

----- CITY SUMMARY -----
        Total_Sales  Total_Orders
City                             
Delhi         24000             1
Mumbai         2000             1
Pune         101500             3

----- PIVOT TABLE -----
Product  Keyboard  Laptop  Monitor  Mouse
City                                     
Delhi           0       0    24000      0
Mumbai          0       0        0   2000
Pune         1500  100000        0      0
"""
