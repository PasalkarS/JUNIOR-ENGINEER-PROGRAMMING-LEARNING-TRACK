# 05 — Validation

## 1. What Data Validation Means

### What it is

Data validation is the process of checking whether data follows the expected rules before it is processed or used.

### Important Points

* Helps identify incorrect or unexpected data.
* Checks whether required information is present.
* Prevents invalid data from causing later problems.
* Validation rules should be clear and consistent.

---

## 2. Schema Validation

### What it is

Schema validation checks whether a dataset has the expected structure.

### Important Points

* Check that required columns exist.
* Check column names and data types.
* Identify unexpected columns when necessary.
* A valid schema allows the data to be processed safely.

---

## 3. Expected Columns

### What it is

Expected columns are the columns that a dataset must contain for processing to work correctly.

### Important Points

* Define the required column names.
* Check the dataset before processing it.
* Missing columns should produce a clear error.
* Column names should be consistent.

### Basic Syntax

```python id="n6k4vh"
required_columns = ["Name", "Age", "Salary"]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]
```

---

## 4. Missing Columns

### What it is

A missing column is a required column that does not exist in the input dataset.

### Important Points

* Missing columns can prevent processing.
* Check required columns before performing transformations.
* Report the names of missing columns.
* Do not continue processing when essential columns are missing.

---

## 5. Unexpected Columns

### What it is

Unexpected columns are columns that are not part of the expected dataset structure.

### Important Points

* They may be valid or may indicate incorrect input.
* Unexpected columns should be identified.
* They can be ignored, removed, or reported depending on requirements.
* Validation rules should clearly define how to handle them.

---

## 6. Required Columns

### What it is

Required columns contain information that is necessary for processing the dataset.

### Important Points

* Required columns should always be checked.
* They should exist before processing begins.
* Important fields should also be checked for missing values.
* A missing required column should produce an actionable error.

---

## 7. Required Values

### What it is

Required values are values that must be present for a record to be considered valid.

### Important Points

* Empty values can make a record invalid.
* Important fields should be checked for missing values.
* Different columns may have different requirements.
* Invalid records should be reported clearly.

### Basic Syntax

```python id="7s5h2a"
df["Name"].notna()
```

---

## 8. Null and Empty Values

### What it is

Null and empty values represent missing information in a dataset.

### Important Points

* `isnull()` and `isna()` can detect null values.
* Empty strings may need separate checking.
* Required fields should not contain missing values.
* Missing values should be reported or handled according to the rules.

---

## 9. Data-Type Validation

### What it is

Data-type validation checks whether columns contain the expected types of data.

### Important Points

* Numeric columns should contain valid numbers.
* Date columns should contain valid dates.
* Text columns should contain appropriate text values.
* Incorrect types can cause calculation and processing errors.

### Basic Syntax

```python id="d2u8jv"
print(df.dtypes)
```

---

## 10. Numeric Range Validation

### What it is

Range validation checks whether numeric values fall within an allowed minimum and maximum.

### Important Points

* Define valid minimum and maximum values.
* Values outside the allowed range are invalid.
* Useful for values such as age, quantity, price, and percentages.
* Invalid values should be reported with enough information to fix them.

### Basic Syntax

```python id="q5e7yn"
invalid = df[(df["Age"] < 18) | (df["Age"] > 60)]
```

---

## 11. Date-Range Validation

### What it is

Date-range validation checks whether dates fall within an expected period.

### Important Points

* Convert values to a date type before validation.
* Define the allowed date range.
* Identify dates outside the expected range.
* Invalid dates should be reported clearly.

### Basic Syntax

```python id="7v5x1p"
invalid = df[df["Date"] > "2026-12-31"]
```

---

## 12. Duplicate-Key Validation

### What it is

Duplicate-key validation checks whether a column that should uniquely identify records contains repeated values.

### Important Points

* A key should uniquely identify a record when required.
* Duplicate keys can cause incorrect merges and reports.
* `duplicated()` can be used to find repeated keys.
* Duplicate keys should be reported before processing.

### Basic Syntax

```python id="p7f4cx"
duplicates = df[df["Employee_ID"].duplicated()]
```

---

## 13. Validation Rules

### What it is

Validation rules define what makes data valid or invalid.

### Important Points

* Rules should be based on business requirements.
* Different columns can have different rules.
* Rules can check presence, type, range, uniqueness, or format.
* Validation should happen before important data transformations.

---

## 14. Collecting Validation Errors

### What it is

Collecting validation errors means storing all detected problems so they can be reviewed together.

### Important Points

* Avoid stopping after finding only one error when possible.
* Store useful information about each error.
* Include the row and column involved.
* Summarize errors for easier review.

---

## 15. Error Categories

### What it is

Error categories group validation problems based on their type.

### Important Points

* Missing column
* Missing value
* Invalid data type
* Invalid range
* Duplicate key
* Invalid date
* Invalid category
* Categories make error reports easier to understand.

---

## 16. Error Messages

### What it is

An error message explains what went wrong and helps identify how to fix it.

### Important Points

* Clearly describe the problem.
* Include the affected column.
* Include the affected value when useful.
* Avoid vague messages such as `"Invalid data"`.

---

## 17. Row and Column Information

### What it is

Row and column information identifies exactly where a validation error occurred.

### Important Points

* Include the row number or record identifier.
* Include the column name.
* Include the invalid value when appropriate.
* This makes errors easier to locate and fix.

---

## 18. Actionable Diagnostics

### What it is

Actionable diagnostics provide enough information for someone to understand and correct a validation error.

### Important Points

* Explain what failed.
* Identify where it failed.
* Show the invalid value when useful.
* Explain the expected value or rule.
* Good diagnostics reduce the time needed to fix data problems.

---

## 19. Reusable Validation Functions

### What it is

Reusable validation functions allow the same validation rules to be applied to different datasets.

### Important Points

* Keep each validation function focused on one type of check.
* Pass the DataFrame and required rules into functions.
* Return clear validation results.
* Reusable functions reduce repeated code.
* Centralized validation logic is easier to maintain and test.

### Basic Syntax

```python id="4d8j2k"
def check_required_columns(df, required_columns):
    missing = []

    for column in required_columns:
        if column not in df.columns:
            missing.append(column)

    return missing
```
