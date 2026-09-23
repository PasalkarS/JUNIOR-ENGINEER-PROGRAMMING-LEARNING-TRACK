# Pandas Series and DataFrames

> **Module 03: Pandas and Excel | Topic 01**



## 1. Learning Outcomes

- **Data Structures:** Differentiate 1D Series from 2D tabular DataFrames.
- **Loading Data:** Read CSV and Excel files into pandas DataFrames accurately.
- **Inspection:** Inspect tabular shapes, datatypes, and summary statistics.
- **Slicing & Subsets:** Select columns and filter rows using `.loc` and `.iloc`.

## 2. Key Syntax & Concepts


### Loading and Inspecting Data

```python
import pandas as pd

# Loading data
df = pd.read_csv('orders.csv')

# Essential inspection commands
print(df.shape)        # (rows, columns) tuple
print(df.columns)      # Index of column names
print(df.dtypes)       # Data types per column
print(df.head(5))      # First 5 records
print(df.info())       # Non-null counts and memory usage
print(df.describe())   # Numerical distribution summary
```


### Selecting Rows and Columns

```python
# 1. Selecting single or multiple columns
total_col = df['total_amount']             # Series
sub_df = df[['order_id', 'total_amount']]   # DataFrame

# 2. Filtering rows with boolean masks
high_value = df[df['total_amount'] > 100.0]

# 3. Label-based (.loc) vs Position-based (.iloc)
first_row = df.iloc[0]                     # By integer index
specific_cell = df.loc[0, 'order_id']      # By row label & column name
```


## 3. Common Mistakes & Gotchas

- **Single vs Double Brackets:** `df['col']` returns a 1D Series; `df[['col']]` returns a 2D DataFrame.
- **SettingWithCopyWarning:** Modifying a slice directly causes warnings. Always use `.copy()` when filtering subsets you intend to edit.

## 4. Practice Tasks & Self-Check

- **Task 1:** Load a 50-row sales CSV, filter orders where status is 'COMPLETED' and amount > $50, and display the top 5 highest amounts.
- **Q1:** What is the difference between df.iloc[0:3] and df.loc[0:3]?
