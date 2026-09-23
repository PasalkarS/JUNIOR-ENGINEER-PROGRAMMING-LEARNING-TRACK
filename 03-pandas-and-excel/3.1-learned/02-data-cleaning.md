# Data Cleaning, Type Casting, and Normalization

> **Module 03: Pandas and Excel | Topic 02**



## 1. Learning Outcomes

- **Missing Data:** Detect and remediate missing (NaN / null) values cleanly.
- **Deduplication:** Identify and drop duplicate records based on primary business keys.
- **Type Casting:** Convert strings to datetime and numeric types safely with error coercion.
- **Text Normalization:** Strip whitespace and standardize categorical strings.

## 2. Key Syntax & Operations

```python
import pandas as pd

# 1. Handling Missing Values
print(df.isna().sum())                 # Count nulls per column
df['notes'] = df['notes'].fillna('None')     # Fill missing values
df_clean = df.dropna(subset=['order_id'])    # Drop rows missing crucial key

# 2. Removing Duplicates
df = df.drop_duplicates(subset=['order_id'], keep='last')

# 3. Type Conversion
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0.0)

# 4. String Cleaning
df['customer_name'] = df['customer_name'].astype(str).str.strip().str.title()
df['category'] = df['category'].astype(str).str.strip().str.upper()
```


## 3. Common Mistakes & Gotchas

- **Silent NaN Creation with errors='coerce':** `pd.to_numeric('invalid', errors='coerce')` turns corrupted data into NaN. Always verify null count after coercion.
- **Forgetting In-Place Behavior:** In modern pandas, `inplace=True` is discouraged. Always assign back: `df = df.drop_duplicates()`.

## 4. Practice Tasks & Self-Check

- **Task 1:** Clean a messy customer contacts DataFrame: strip email spaces, lower-case emails, parse signup dates, and fill missing phones with 'N/A'.
- **Q1:** Why is `errors='coerce'` helpful when reading user-entered dates?
