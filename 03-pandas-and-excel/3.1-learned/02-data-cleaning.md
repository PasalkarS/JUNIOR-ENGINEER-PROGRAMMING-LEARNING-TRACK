# 02 — Cleaning

## 1. What Data Cleaning Means

### What it is

Data cleaning is the process of finding and fixing incorrect, missing, duplicate, or inconsistent data.

### Important Points

* Makes data more accurate and consistent.
* Removes or fixes unwanted data.
* Helps prevent errors during analysis.
* Cleaning rules should be clear and repeatable.

---

## 2. Missing Values

### What it is

Missing values are records where a value is empty, unavailable, or not provided.

### Important Points

* Missing values can affect calculations and analysis.
* They can appear as `NaN`, `None`, or empty values.
* Missing values should be identified before processing data.
* The correct way to handle missing data depends on the dataset.

---

## 3. Detecting Missing Values

### What it is

Pandas provides functions to find missing values in a DataFrame.

### Important Points

* `isnull()` identifies missing values.
* `isna()` can also be used to identify missing values.
* `sum()` can count missing values.
* Checking missing values helps identify columns that need cleaning.

### Basic Syntax

```python
df.isnull()
df.isnull().sum()
```

---

## 4. Filling Missing Values

### What it is

Filling missing values means replacing empty values with a suitable value.

### Important Points

* `fillna()` is used to replace missing values.
* Missing numbers can sometimes be replaced with a default value.
* Missing text can sometimes be replaced with a label such as `"Unknown"`.
* The replacement value should make sense for the data.

### Basic Syntax

```python
df["Age"] = df["Age"].fillna(0)
```

---

## 5. Removing Missing Values

### What it is

Removing missing values means deleting rows or columns that contain empty values.

### Important Points

* `dropna()` is used to remove missing values.
* Rows can be removed when important data is missing.
* Columns can also be removed when necessary.
* Do not remove data without understanding its importance.

### Basic Syntax

```python
df = df.dropna()
```

---

## 6. Duplicate Rows

### What it is

Duplicate rows are repeated records containing the same or identical data.

### Important Points

* Duplicates can cause incorrect counts and calculations.
* `duplicated()` identifies duplicate rows.
* Duplicate records should be checked before removing them.
* Some repeated records may be valid, so duplicates should not always be removed automatically.

### Basic Syntax

```python
df.duplicated()
df.duplicated().sum()
```

---

## 7. Removing Duplicates

### What it is

Removing duplicates means deleting repeated records that are not required.

### Important Points

* `drop_duplicates()` removes duplicate rows.
* By default, the first occurrence is kept.
* Duplicates can also be checked using specific columns.
* The removal rule should match the purpose of the data.

### Basic Syntax

```python
df = df.drop_duplicates()
```

---

## 8. Type Conversion

### What it is

Type conversion means changing a column from one data type to another.

### Important Points

* Data types should match the meaning of the data.
* Numbers should be stored as numeric types.
* Dates should be stored as date/time values.
* Incorrect types can cause calculation and filtering problems.

---

## 9. Numeric Conversion

### What it is

Numeric conversion changes values into numbers so they can be used in calculations.

### Important Points

* `to_numeric()` is used for numeric conversion.
* Text values containing numbers may need to be converted.
* Invalid values can be handled during conversion.
* Numeric columns should be checked after conversion.

### Basic Syntax

```python
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
```

---

## 10. Date Conversion

### What it is

Date conversion changes text or other values into Pandas date/time values.

### Important Points

* `to_datetime()` is used for date conversion.
* Date columns can then be sorted and filtered by date.
* Invalid dates should be handled carefully.
* Consistent date types make date operations easier.

### Basic Syntax

```python
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
```

---

## 11. String Cleaning

### What it is

String cleaning removes unwanted characters and makes text values consistent.

### Important Points

* String methods can be applied to DataFrame columns.
* Extra spaces can be removed.
* Text case can be standardized.
* Incorrect or inconsistent values can be replaced.

---

## 12. Removing Extra Spaces

### What it is

Extra spaces can make identical values appear different.

### Important Points

* `str.strip()` removes spaces from the beginning and end.
* Extra spaces can cause problems when filtering or comparing values.
* Text columns should be checked for inconsistent spacing.

### Basic Syntax

```python
df["Name"] = df["Name"].str.strip()
```

---

## 13. Changing Text Case

### What it is

Changing text case makes values follow a consistent format.

### Important Points

* `str.lower()` converts text to lowercase.
* `str.upper()` converts text to uppercase.
* `str.title()` converts text to title case.
* A consistent case makes searching and comparison easier.

### Basic Syntax

```python
df["Name"] = df["Name"].str.title()
```

---

## 14. Replacing Values

### What it is

Replacing values means changing incorrect or inconsistent values to the required format.

### Important Points

* `replace()` can change specific values.
* Useful for correcting spelling differences.
* Useful for standardizing categories.
* Replacement rules should be based on known requirements.

### Basic Syntax

```python
df["Status"] = df["Status"].replace({
    "Y": "Yes",
    "N": "No"
})
```

---

## 15. Date Normalization

### What it is

Date normalization means converting different date formats into one consistent format.

### Important Points

* Dates may appear in different formats.
* Convert dates to a consistent datetime type.
* Standardized dates are easier to filter and compare.
* Invalid dates should be identified and handled.

### Basic Syntax

```python
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
```

---

## 16. Column-Name Normalization

### What it is

Column-name normalization means making column names consistent and easy to use.

### Important Points

* Remove unnecessary spaces.
* Use consistent capitalization.
* Avoid confusing or unclear names.
* Consistent names make code easier to read.

### Basic Syntax

```python
df.columns = df.columns.str.strip().str.lower()
```

---

## 17. Handling Invalid Data

### What it is

Invalid data contains values that do not follow the expected rules or format.

### Important Points

* Check values against expected rules.
* Identify incorrect numbers, dates, and categories.
* Invalid values can be corrected, replaced, or removed.
* Invalid records should be reported when necessary.
* Cleaning should not silently change important data.

---

## 18. Documenting Cleaning Assumptions

### What it is

Cleaning assumptions explain why specific cleaning decisions were made.

### Important Points

* Record how missing values were handled.
* Record which duplicates were removed.
* Explain type conversions.
* Document how invalid values were handled.
* Clear assumptions make the cleaning process easier to understand and review.

---

## 19. Repeatable Cleaning Logic

### What it is

Repeatable cleaning logic means using the same defined cleaning steps whenever similar data needs to be processed.

### Important Points

* Use functions to organize cleani
