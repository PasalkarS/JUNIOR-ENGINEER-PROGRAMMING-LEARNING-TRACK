import pandas as pd

# Create a small DataFrame
data = {
    "Name": ["Rahul", "Amit", "Priya", "Sneha"],
    "Age": [25, 30, 28, 24],
    "Department": ["QA", "Development", "HR", "QA"],
    "Salary": [40000, 60000, 50000, 42000]
}

df = pd.DataFrame(data)

print("----- DATA -----")
print(df)

print("\n----- FIRST 3 ROWS -----")
print(df.head(3))

print("\n----- LAST 2 ROWS -----")
print(df.tail(2))

print("\n----- SHAPE -----")
print(df.shape)

print("\n----- COLUMNS -----")
print(df.columns)

print("\n----- INDEX -----")
print(df.index)

print("\n----- DATA TYPES -----")
print(df.dtypes)

print("\n----- INFORMATION -----")
df.info()

print("\n----- STATISTICS -----")
print(df.describe())

print("\n----- QA EMPLOYEES -----")
qa_employees = df[df["Department"] == "QA"]
print(qa_employees)

print("\n----- SALARY ABOVE 45000 -----")
high_salary = df[df["Salary"] > 45000]
print(high_salary)

"""
----- DATA -----
    Name  Age   Department  Salary
0  Rahul   25           QA   40000
1   Amit   30  Development   60000
2  Priya   28           HR   50000
3  Sneha   24           QA   42000

----- FIRST 3 ROWS -----
    Name  Age   Department  Salary
0  Rahul   25           QA   40000
1   Amit   30  Development   60000
2  Priya   28           HR   50000

----- LAST 2 ROWS -----
    Name  Age Department  Salary
2  Priya   28         HR   50000
3  Sneha   24         QA   42000

----- SHAPE -----
(4, 4)

----- COLUMNS -----
Index(['Name', 'Age', 'Department', 'Salary'], dtype='str')

----- INDEX -----
RangeIndex(start=0, stop=4, step=1)

----- DATA TYPES -----
Name            str
Age           int64
Department      str
Salary        int64
dtype: object

----- INFORMATION -----
<class 'pandas.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 4 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   Name        4 non-null      str  
 1   Age         4 non-null      int64
 2   Department  4 non-null      str  
 3   Salary      4 non-null      int64
dtypes: int64(2), str(2)
memory usage: 260.0 bytes

----- STATISTICS -----
             Age        Salary
count   4.000000      4.000000
mean   26.750000  48000.000000
std     2.753785   9092.121131
min    24.000000  40000.000000
25%    24.750000  41500.000000
50%    26.500000  46000.000000
75%    28.500000  52500.000000
max    30.000000  60000.000000

----- QA EMPLOYEES -----
    Name  Age Department  Salary
0  Rahul   25         QA   40000
3  Sneha   24         QA   42000

----- SALARY ABOVE 45000 -----
    Name  Age   Department  Salary
1   Amit   30  Development   60000
2  Priya   28           HR   50000
"""
