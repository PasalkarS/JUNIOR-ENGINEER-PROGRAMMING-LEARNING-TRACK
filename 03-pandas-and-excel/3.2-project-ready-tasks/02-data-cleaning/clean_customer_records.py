import pandas as pd

data = {
    "Customer_ID": [101, 102, 103, 103, 104, 105],
    "Name": [" Rahul ", "PRIYA", "amit", "amit", " Sneha ", None],
    "Email": [
        "rahul@example.com",
        "PRIYA@EXAMPLE.COM",
        "amit@example.com",
        "amit@example.com",
        "sneha@example.com",
        None
    ],
    "City": ["Pune", "mumbai", "PUNE", "PUNE", "Delhi", "Mumbai"],
    "Age": [25, 30, None, None, 28, 17]
}

df = pd.DataFrame(data)

print("----- ORIGINAL DATA -----")
print(df)

# Remove duplicate records
df = df.drop_duplicates()

# Clean names
df["Name"] = df["Name"].fillna("Unknown")
df["Name"] = df["Name"].str.strip().str.title()

# Clean email
df["Email"] = df["Email"].fillna("Not Provided")
df["Email"] = df["Email"].str.strip().str.lower()

# Clean city
df["City"] = df["City"].str.strip().str.title()

# Fill missing age
df["Age"] = df["Age"].fillna(0)

# Convert age to integer
df["Age"] = df["Age"].astype(int)

# Validate age
df["Age_Valid"] = (df["Age"] >= 18) & (df["Age"] <= 100)

print("\n----- CLEANED DATA -----")
print(df)

print("\n----- INVALID AGE RECORDS -----")
print(df[df["Age_Valid"] == False])


"""
----- ORIGINAL DATA -----
   Customer_ID     Name              Email    City   Age
0          101   Rahul   rahul@example.com    Pune  25.0
1          102    PRIYA  PRIYA@EXAMPLE.COM  mumbai  30.0
2          103     amit   amit@example.com    PUNE   NaN
3          103     amit   amit@example.com    PUNE   NaN
4          104   Sneha   sneha@example.com   Delhi  28.0
5          105      NaN                NaN  Mumbai  17.0

----- CLEANED DATA -----
   Customer_ID     Name              Email    City  Age  Age_Valid
0          101    Rahul  rahul@example.com    Pune   25       True
1          102    Priya  priya@example.com  Mumbai   30       True
2          103     Amit   amit@example.com    Pune    0      False
4          104    Sneha  sneha@example.com   Delhi   28       True
5          105  Unknown       not provided  Mumbai   17      False

----- INVALID AGE RECORDS -----
   Customer_ID     Name             Email    City  Age  Age_Valid
2          103     Amit  amit@example.com    Pune    0      False
5          105  Unknown      not provided  Mumbai   17      False
"""
