# Pandas Performance & Vectorization Best Practices

> **Module 03: Pandas and Excel | Topic 06**



## 1. Learning Outcomes

- **The Danger of Iteration:** Understand why `for row in df.iterrows()` is 100x-500x slower than vectorization.
- **Vectorized Operations:** Perform columnar calculations directly in C/NumPy memory speeds.
- **Memory Optimization:** Downcast integer/float types and use categorical types for low-cardinality strings.
- **Chunking:** Process multi-gigabyte files in batches using `chunksize`.

## 2. Performance Comparison


| Method | Speed Rank | When to Use |
| --- | --- | --- |
| Vectorized (df['a'] * df['b']) | Fastest (1x) | Always for mathematical / string operations |
| NumPy select / where | Very Fast (1.2x) | Conditional branching across columns |
| df.apply(lambda ...) | Moderate (10x slower) | Custom complex functions without vectorized alternatives |
| df.iterrows() / itertuples() | Extremely Slow (200x slower) | Last resort; avoid in production data pipelines |



## 3. Key Code Patterns

```python
import numpy as np
import pandas as pd

# Vectorized conditional tagging (instant speed!)
df['tier'] = np.where(df['amount'] > 500, 'Premium', 'Standard')

# Memory optimization using categories
df['status'] = df['status'].astype('category')  # 80% RAM reduction on repeated text

# Chunking large files
for chunk in pd.read_csv('huge_file.csv', chunksize=10000):
    # Process 10k rows at a time without running out of RAM
    summary = chunk.groupby('category')['amount'].sum()
```


## 4. Practice Tasks & Self-Check

- **Task 1:** Benchmark the runtime difference between calculating tax via `iterrows()` vs a vectorized operation on 50,000 rows.
- **Q1:** Why does `astype('category')` drastically reduce DataFrame memory consumption?
