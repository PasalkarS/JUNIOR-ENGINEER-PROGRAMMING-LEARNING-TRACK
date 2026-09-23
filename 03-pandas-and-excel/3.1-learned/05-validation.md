# Data Validation & Quality Assurance Pipelines

> **Module 03: Pandas and Excel | Topic 05**



## 1. Learning Outcomes

- **Schema Verification:** Validate required column presence and verify data types.
- **Domain Boundary Rules:** Detect negative amounts, future dates, and invalid category values.
- **Automated Audit Reports:** Log and export tabular validation error summaries for business review.
- **Quarantine Pipelines:** Separate valid records for processing while isolating rejected rows.

## 2. Key Validation Architecture

```python
def validate_dataset(df: pd.DataFrame) -> tuple[pd.DataFrame, list]:
    errors = []
    required_cols = {'order_id', 'amount', 'date', 'customer_id'}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f'Schema failure: missing columns {missing}')
        
    # Check negative or zero amounts
    bad_amounts = df[df['amount'] <= 0]
    for idx, row in bad_amounts.iterrows():
        errors.append({'row': idx, 'field': 'amount', 'error': 'Must be > 0', 'val': row['amount']})
        
    # Check duplicate IDs
    dup_ids = df[df.duplicated(subset=['order_id'], keep=False)]
    for idx, row in dup_ids.iterrows():
        errors.append({'row': idx, 'field': 'order_id', 'error': 'Duplicate ID', 'val': row['order_id']})
        
    valid_df = df[(df['amount'] > 0) & (~df.duplicated(subset=['order_id'], keep='first'))]
    return valid_df, errors
```


## 3. Common Mistakes & Gotchas

- **Crashing on First Error:** A robust data pipeline should log all data quality defects into an audit table rather than immediately crashing on row 1.
- **Silent Dropping:** Dropping invalid rows without logging why they were discarded makes reconciling financials impossible.

## 4. Practice Tasks & Self-Check

- **Task 1:** Create an automated validation class that audits an uploaded inventory sheet and writes `rejections.csv`.
- **Q1:** Why is quarantining invalid rows better than dropping them silently?
