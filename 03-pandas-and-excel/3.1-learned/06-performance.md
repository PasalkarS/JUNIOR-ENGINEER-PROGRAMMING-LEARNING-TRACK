# 06 — Performance

## 1. Why Performance Matters

### What it is

Performance means how quickly and efficiently your Python and Pandas code processes data.

### Important Points

* Large datasets need efficient code.
* Some Pandas operations are much faster than normal Python loops.
* Unnecessary calculations can slow down a program.
* Good performance also reduces memory usage.
* Always try to write simple and efficient operations.

---

## 2. Loops in Pandas

### What it is

A loop processes data one row or item at a time.

### Important Points

* Loops are easy to understand but can be slow for large DataFrames.
* Pandas is designed to work with complete columns.
* Avoid loops when a Pandas operation can do the same job.
* Loops can still be useful for special cases.

### Basic Syntax

```python
for index, row in df.iterrows():
    print(row)
```

---

## 3. Vectorization

### What it is

Vectorization means performing an operation on an entire column or group of values at once.

### Important Points

* Vectorized operations are usually faster than loops.
* Pandas supports many vectorized operations.
* They make code shorter and easier to read.
* Use vectorization when possible.

### Basic Syntax

```python
df["total"] = df["price"] * df["quantity"]
```

---

## 4. Vectorized Calculations

### What it is

Vectorized calculations apply mathematical operations to a complete column.

### Important Points

* You do not need to process every row manually.
* Pandas applies the operation to all values.
* Common operations include `+`, `-`, `*`, and `/`.
* This is useful for calculated columns.

### Basic Syntax

```python
df["total"] = df["price"] * df["quantity"]
df["discount_price"] = df["price"] - df["discount"]
```

---

## 5. Vectorized Filtering

### What it is

Vectorized filtering selects rows using conditions without manually checking every row.

### Important Points

* Use conditions directly on columns.
* Pandas returns only matching rows.
* This is usually faster than looping through rows.
* Multiple conditions can be combined.

### Basic Syntax

```python
filtered_data = df[df["age"] > 18]
```

---

## 6. Avoiding Unnecessary Loops

### What it is

Avoiding unnecessary loops means using Pandas operations instead of manually processing each row.

### Important Points

* Prefer Pandas functions when available.
* Use vectorized operations for calculations.
* Use `groupby()` for grouped calculations.
* Use filtering instead of checking rows one by one.
* Use loops only when they are actually needed.

### Basic Syntax

```python
# Avoid
for index, row in df.iterrows():
    df.loc[index, "total"] = row["price"] * row["quantity"]

# Prefer
df["total"] = df["price"] * df["quantity"]
```

---

## 7. Selecting Only Required Columns

### What it is

Selecting only the columns you need can reduce memory usage and unnecessary processing.

### Important Points

* Do not load or process unused columns when possible.
* Smaller DataFrames require fewer resources.
* Selecting required columns can make code clearer.
* This is especially useful with large datasets.

### Basic Syntax

```python
df = df[["name", "price", "quantity"]]
```

---

## 8. Filtering Data Early

### What it is

Filtering data early means removing unnecessary rows before performing more operations.

### Important Points

* Process only the data you need.
* Filter before grouping or transforming when possible.
* This can reduce the amount of work Pandas performs.
* It is useful for large datasets.

### Basic Syntax

```python
df = df[df["status"] == "Active"]
```

---

## 9. Memory Usage

### What it is

Memory usage is the amount of computer memory required to store and process data.

### Important Points

* Large DataFrames can use a lot of memory.
* Unnecessary columns increase memory usage.
* Large text columns can use significant memory.
* Check memory usage when working with large datasets.

### Basic Syntax

```python
df.info(memory_usage="deep")
```

---

## 10. Data Types and Memory

### What it is

Choosing suitable data types can reduce the memory used by a DataFrame.

### Important Points

* Different data types use different amounts of memory.
* Numeric columns should use appropriate numeric types.
* Repeated text values can sometimes use the `category` type.
* Check `dtypes` before changing data types.
* Do not change types if it causes loss of important data.

### Basic Syntax

```python
print(df.dtypes)

df["category"] = df["category"].astype("category")
```

---

## 11. Processing Large Datasets

### What it is

Large datasets may not fit comfortably into memory when loaded all at once.

### Important Points

* Large files need careful memory management.
* Load only required columns when possible.
* Filter unnecessary data early.
* Process large files in smaller parts.
* Chunking can help process files without loading everything at once.

---

## 12. Chunking

### What it is

Chunking means dividing a large dataset into smaller parts and processing each part separately.

### Important Points

* It reduces memory usage.
* Each chunk contains only part of the dataset.
* Chunks can be processed one after another.
* It is commonly used with large CSV files.

---

## 13. Reading Files in Chunks

### What it is

Pandas can read a large CSV file in smaller groups of rows.

### Important Points

* Use the `chunksize` parameter.
* Each chunk is a DataFrame.
* Process each chunk separately.
* This is useful when the complete file is too large for memory.

### Basic Syntax

```python
for chunk in pd.read_csv("large_file.csv", chunksize=1000):
    print(chunk)
```

---

## 14. Measuring Execution Time

### What it is

Measuring execution time helps you understand how long a piece of code takes to run.

### Important Points

* Performance should be measured instead of guessed.
* Compare different approaches using the same data.
* Use timing when testing slow operations.
* Faster code is not always more important than readable code.

### Basic Syntax

```python
import time

start = time.time()

# Code to test

end = time.time()

print("Time:", end - start)
```

---

## 15. Comparing Slow vs Fast Approaches

### What it is

A performance comparison checks how different approaches perform on the same task.

### Important Points

* A loop may be slower than a vectorized operation.
* Use the same dataset for a fair comparison.
* Measure the execution time of both approaches.
* Also consider readability and memory usage.
* Prefer a simple approach that performs well.

### Basic Syntax

```python
start = time.time()

df["total"] = df["price"] * df["quantity"]

end = time.time()

print("Time:", end - start)
```

---

## 16. Common Pandas Performance Problems

### What it is

Performance problems happen when code does unnecessary work or uses inefficient operations.

### Important Points

* Using loops for simple column operations.
* Loading unnecessary columns.
* Processing unnecessary rows.
* Loading very large files completely into memory.
* Repeating the same calculation unnecessarily.
* Using inefficient data types.

---

## 17. Performance Best Practices

### What it is

Performance best practices are simple rules that help Pandas code run efficiently.

### Important Points

* Prefer vectorized operations over loops.
* Select only required columns.
* Filter unnecessary rows early.
* Use suitable data types.
* Process large files in chunks.
* Measure performance before optimizing.
* Keep the code simple and readable.
