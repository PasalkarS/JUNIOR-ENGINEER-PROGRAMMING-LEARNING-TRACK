# Data Transformations, Merges, and Aggregations

> **Module 03: Pandas and Excel | Topic 03**



## 1. Learning Outcomes

- **Group By Aggregations:** Group rows by category and compute multi-metric summaries.
- **Calculated Columns:** Add derived columns efficiently using vectorized math.
- **Table Joins:** Join related datasets using inner, left, and outer merges.
- **Pivoting:** Reshape data matrices using `pivot_table` and `melt`.

## 2. Key Syntax & Concepts


### GroupBy & Multi-Aggregation

```python
# Grouping orders by department
dept_summary = df.groupby('department').agg(
    total_revenue=('amount', 'sum'),
    average_order=('amount', 'mean'),
    order_count=('order_id', 'count')
).reset_index()
```


### Merging Two DataFrames

```python
# Joining orders with customer details (equivalent to SQL LEFT JOIN)
full_df = pd.merge(
    df_orders,
    df_customers,
    on='customer_id',
    how='left'
)
```


### Pivot Tables

```python
# Reshaping: Monthly revenue by category
pivot = df.pivot_table(
    index='category',
    columns='month',
    values='amount',
    aggfunc='sum',
    fill_value=0.0
)
```


## 3. Common Mistakes & Gotchas

- **Cartesian Explosions in Merges:** If both DataFrames have duplicate keys in the `on` column, `merge()` multiplies rows unexpectedly. Check uniqueness before joining.
- **Index Trap after GroupBy:** GroupBy sets grouped columns as the index. Use `.reset_index()` to convert back to standard columnar DataFrame.

## 4. Practice Tasks & Self-Check

- **Task 1:** Given an orders dataset and items dataset, calculate the total profit per product category.
- **Q1:** What is the difference between pd.merge(how='inner') and pd.merge(how='left')?
