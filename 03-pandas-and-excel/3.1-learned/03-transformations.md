# 03 — Transformations

## 1. Filtering Data

### What it is

Filtering means selecting only the rows that match a specific condition.

### Important Points

* Use conditions to find required records.
* Filtering does not need to change the original data.
* Multiple conditions can be combined.
* Filtering is commonly used before analysis.

### Basic Syntax

```python
filtered_df = df[df["Age"] > 25]
```

---

## 2. Conditional Filtering

### What it is

Conditional filtering selects rows based on one or more conditions.

### Important Points

* `>` means greater than.
* `<` means less than.
* `==` means equal to.
* `!=` means not equal to.
* Use `&` for AND conditions.
* Use `|` for OR conditions.

### Basic Syntax

```python
df[df["Age"] > 25]

df[(df["Age"] > 25) & (df["City"] == "Pune")]
```

---

## 3. Sorting Data

### What it is

Sorting arranges rows based on one or more columns.

### Important Points

* `sort_values()` is used for sorting.
* Data can be sorted in ascending or descending order.
* Multiple columns can be used for sorting.
* Sorting makes data easier to analyze.

### Basic Syntax

```python
df = df.sort_values("Age")

df = df.sort_values("Age", ascending=False)
```

---

## 4. Sorting by Multiple Columns

### What it is

Multiple columns can be used together when sorting a DataFrame.

### Important Points

* Pass column names as a list.
* Each column can have its own sort direction.
* The first column is used as the primary sort.

### Basic Syntax

```python
df = df.sort_values(
    ["City", "Age"],
    ascending=[True, False]
)
```

---

## 5. Calculated Columns

### What it is

A calculated column is a new column created using existing data.

### Important Points

* Calculations can be performed directly on columns.
* Useful for totals, differences, percentages, and other business calculations.
* Calculated columns can be used in further analysis.
* Vectorized calculations are generally preferred.

### Basic Syntax

```python
df["Total"] = df["Price"] * df["Quantity"]
```

---

## 6. `groupby()`

### What it is

`groupby()` groups rows based on one or more columns so that each group can be analyzed separately.

### Important Points

* Useful for summarizing data.
* Can group by one column.
* Can group by multiple columns.
* Usually combined with aggregation functions.

### Basic Syntax

```python
grouped = df.groupby("Department")
```

---

## 7. Grouping by One or Multiple Columns

### What it is

Data can be grouped using one column or a combination of columns.

### Important Points

* One column creates groups based on one category.
* Multiple columns create groups based on combinations.
* Grouping helps compare different categories.
* The selected columns should have meaningful values.

### Basic Syntax

```python
df.groupby("Department")["Salary"].sum()

df.groupby(["Department", "City"])["Salary"].sum()
```

---

## 8. Aggregation

### What it is

Aggregation combines multiple values into a summary value.

### Important Points

* `sum()` calculates a total.
* `mean()` calculates an average.
* `count()` counts values.
* `min()` finds the smallest value.
* `max()` finds the largest value.
* Aggregation is commonly used with `groupby()`.

### Basic Syntax

```python
df.groupby("Department")["Salary"].sum()

df.groupby("Department")["Salary"].mean()
```

---

## 9. Multiple Aggregations

### What it is

Multiple aggregation functions can be applied to the same grouped data.

### Important Points

* Several statistics can be calculated at once.
* Useful for creating summary reports.
* Common functions include `sum`, `mean`, `min`, and `max`.
* Multiple aggregations provide a broader view of the data.

### Basic Syntax

```python
df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "min", "max"]
)
```

---

## 10. Merging DataFrames

### What it is

Merging combines two DataFrames using one or more common columns called keys.

### Important Points

* Similar to joining tables in a database.
* The key connects related records.
* `merge()` is used to combine DataFrames.
* The key should contain matching values where records need to be connected.

### Basic Syntax

```python
result = pd.merge(
    employees,
    departments,
    on="Department"
)
```

---

## 11. Join Types

### What it is

Join types determine which records are included when two DataFrames are merged.

### Important Points

* **Inner join** keeps matching records from both tables.
* **Left join** keeps all records from the left table.
* **Right join** keeps all records from the right table.
* **Outer join** keeps records from both tables.
* The correct join type depends on the reporting requirement.

### Basic Syntax

```python
pd.merge(df1, df2, on="ID", how="inner")

pd.merge(df1, df2, on="ID", how="left")

pd.merge(df1, df2, on="ID", how="right")

pd.merge(df1, df2, on="ID", how="outer")
```

---

## 12. Join Keys

### What it is

A join key is a column used to match related records between DataFrames.

### Important Points

* Keys should represent the same type of information.
* Key values should use a consistent format.
* Duplicate keys can create multiple matching rows.
* Missing keys can result in unmatched records.
* Incorrect keys can produce incorrect reports.

---

## 13. Pivot Tables

### What it is

A pivot table summarizes data by organizing values into rows, columns, and calculated results.

### Important Points

* Useful for creating summary reports.
* Rows represent categories.
* Columns can represent another category.
* Values contain the data being summarized.
* Aggregation functions can be used to calculate results.

### Basic Syntax

```python
summary = pd.pivot_table(
    df,
    values="Sales",
    index="Month",
    columns="Category",
    aggfunc="sum"
)
```

---

## 14. Monthly Summaries

### What it is

A monthly summary groups data by month to show totals, averages, or other statistics for each month.

### Important Points

* Dates should first be converted to a datetime type.
* Month or month-year values can be extracted from dates.
* `groupby()` can be used to create monthly summaries.
* Monthly summaries are useful for tracking business activity over time.

### Basic Syntax

```python
df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.to_period("M")

monthly = df.groupby("Month")["Sales"].sum()
```

---

## 15. Cross-Table Reports

### What it is

A cross-table report combines information from multiple DataFrames to create a single useful summary.

### Important Points

* Data is usually merged using common keys.
* Different tables may contain different types of information.
* The merged data can then be filtered, grouped, and aggregated.
* Results should be checked to make sure records were matched correctly.
* Cross-table reports are useful for combining related business data.

### Basic Syntax

```python
merged = pd.merge(
    sales,
    employees,
    on="Employee_ID",
    how="left"
)

report = merged.groupby("Department")["Sales"].sum()
```
