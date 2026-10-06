# 06 — DataFrames

## 1. Introduction to Pandas

### What it is

Pandas is a Python library used to work with structured and tabular data.

### Important Points

* Used for working with rows and columns of data.
* Commonly used with CSV and Excel files.
* Provides tools for cleaning, filtering, and analyzing data.
* Import Pandas using `import pandas as pd`.

---

## 2. Series

### What it is

A Series is a one-dimensional data structure that usually represents a single column of data.

### Important Points

* Contains values and an index.
* Can contain numbers, strings, dates, or other data types.
* Each value has an index.
* A DataFrame can contain multiple Series.

### Basic Syntax

```python
import pandas as pd

ages = pd.Series([20, 25, 30])
```

---

## 3. DataFrames

### What it is

A DataFrame is a two-dimensional data structure that represents data in rows and columns.

### Important Points

* Similar to a table or spreadsheet.
* Each column can have a different data type.
* Each row has an index.
* DataFrames are the main structure used when working with tabular data in Pandas.

### Basic Syntax

```python
import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 28]
}

df = pd.DataFrame(data)
```

---

## 4. Creating DataFrames

### What it is

A DataFrame can be created directly from Python data such as dictionaries, lists, or other data structures.

### Important Points

* Dictionary keys normally become column names.
* Dictionary values become column data.
* Columns should normally have the same number of values.
* DataFrames can also be created by loading external files.

---

## 5. Loading CSV Files

### What it is

CSV files store tabular data in a simple text format where values are separated by commas.

### Important Points

* Use `read_csv()` to load a CSV file.
* The result is normally stored as a DataFrame.
* The file path must be correct.
* CSV data should be inspected after loading.

### Basic Syntax

```python
df = pd.read_csv("data.csv")
```

---

## 6. Loading Excel Files

### What it is

Pandas can read data from Excel workbooks and load it into a DataFrame.

### Important Points

* Use `read_excel()` to read Excel files.
* Excel workbooks can contain multiple sheets.
* A specific sheet can be selected when loading data.
* The loaded data can be inspected like any other DataFrame.

### Basic Syntax

```python
df = pd.read_excel("data.xlsx")
```

---

## 7. Inspecting Data

### What it is

Data inspection means checking the structure and contents of a DataFrame before working with it.

### Important Points

* Check the first and last rows.
* Check the number of rows and columns.
* Check column names and data types.
* Look for missing or unexpected data.
* Inspecting data helps understand an unfamiliar dataset quickly.

---

## 8. `head()` / `tail()`

### What it is

`head()` and `tail()` are used to view the beginning and end of a DataFrame.

### Important Points

* `head()` shows the first five rows by default.
* `tail()` shows the last five rows by default.
* A number can be provided to control how many rows are shown.
* Useful for quickly checking imported data.

### Basic Syntax

```python
df.head()
df.tail()

df.head(10)
df.tail(10)
```

---

## 9. `shape`, `columns`, `index`

### What it is

These properties provide basic information about the structure of a DataFrame.

### Important Points

* `shape` returns the number of rows and columns.
* `columns` returns the column names.
* `index` returns the row labels.
* These properties help understand the size and structure of the data.

### Basic Syntax

```python
df.shape
df.columns
df.index
```

---

## 10. `info()` / `describe()`

### What it is

`info()` provides structural information, while `describe()` provides summary statistics.

### Important Points

* `info()` shows columns, data types, and non-null values.
* `describe()` summarizes numerical columns.
* `describe()` can help identify unusual values.
* Both are useful during initial data inspection.

### Basic Syntax

```python
df.info()
df.describe()
```

---

## 11. Data Types (`dtypes`)

### What it is

Data types describe what kind of values are stored in each DataFrame column.

### Important Points

* Common types include integers, floats, strings, and dates.
* `dtypes` shows the type of each column.
* Incorrect data types can cause problems during calculations or filtering.
* Data types can be converted when necessary.

### Basic Syntax

```python
df.dtypes
```

---

## 12. Indexing

### What it is

Indexing means accessing specific rows, columns, or values from a DataFrame.

### Important Points

* DataFrames use an index to identify rows.
* Columns are accessed using their names.
* `loc` uses labels.
* `iloc` uses positions.
* Indexing is useful for accessing specific parts of a dataset.

---

## 13. `loc`

### What it is

`loc` is used to select data using row and column labels.

### Important Points

* Uses labels instead of numerical positions.
* Can select rows and columns together.
* Can be used with conditions.
* Useful when working with named indexes or column names.

### Basic Syntax

```python
df.loc[0]
df.loc[0, "Name"]
```

---

## 14. `iloc`

### What it is

`iloc` is used to select data using numerical positions.

### Important Points

* Uses zero-based positions.
* The first row has position `0`.
* Can select specific rows and columns.
* Useful when the position of the data is known.

### Basic Syntax

```python
df.iloc[0]
df.iloc[0, 1]
```

---

## 15. Selecting Columns

### What it is

Columns can be selected using their column names.

### Important Points

* Use the column name to select one column.
* Use a list of names to select multiple columns.
* Selected columns can be used for calculations and filtering.
* Column names must match the DataFrame column names.

### Basic Syntax

```python
df["Name"]

df[["Name", "Age"]]
```

---

## 16. Selecting Rows

### What it is

Rows can be selected using indexes, positions, or conditions.

### Important Points

* Rows can be selected using `loc` or `iloc`.
* Conditions can be used to filter rows.
* Multiple conditions can be combined.
* Row selection is commonly used when filtering data.

### Basic Syntax

```python
df.loc[0]

df.loc[df["Age"] > 25]
```

---

## 17. Basic DataFrame Operations

### What it is

DataFrame operations are used to view, modify, calculate, and work with tabular data.

### Important Points

* Columns can be added, removed, or renamed.
* Data can be filtered and sorted.
* Calculations can be performed using columns.
* DataFrame operations can create new results without changing the original data when needed.

---

## 18. Adding, Removing, and Renaming Columns

### What it is

Pandas provides simple operations for changing the columns of a DataFrame.

### Important Points

* A new column can be created by assigning values to a new column name.
* `drop()` can remove columns.
* `rename()` can change column names.
* Clear and consistent column names make data easier to work with.

### Basic Syntax

```python
df["Salary"] = [30000, 40000, 35000]

df = df.drop("Salary", axis=1)

df = df.rename(columns={"Name": "Employee Name"})
```

---

## 19. Basic Data-Quality Inspection

### What it is

Data-quality inspection means checking whether the dataset contains missing, duplicate, or incorrectly formatted data.

### Important Points

* Check for missing values.
* Check for duplicate rows.
* Check column data types.
* Check unexpected or invalid values.
* Data quality should be checked before performing important transformations or analysis.

### Basic Syntax

```python
df.isnull().sum()

df.duplicated().sum()

df.dtypes
```
