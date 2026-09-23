# Topic 05: Data Quality Auditor & Quarantine Engine
import pandas as pd
import io

SAMPLE_BATCH = """row_id,sku,quantity,unit_price
1,SKU-A,10,25.00
2,SKU-B,-3,50.00
3,SKU-C,5,0.00
4,SKU-A,10,25.00
5,SKU-D,2,110.00
6,,4,40.00
"""

def audit_batch():
    df = pd.read_csv(io.StringIO(SAMPLE_BATCH.strip()))
    errors = []

    # Rule 1: Missing SKU
    missing_sku = df[df['sku'].isna()]
    for idx, row in missing_sku.iterrows():
        errors.append({"row": row['row_id'], "field": "sku", "reason": "Missing SKU code"})

    # Rule 2: Quantity must be > 0
    bad_qty = df[df['quantity'] <= 0]
    for idx, row in bad_qty.iterrows():
        errors.append({"row": row['row_id'], "field": "quantity", "reason": f"Invalid quantity: {row['quantity']}"})

    # Rule 3: Unit Price must be > 0
    bad_price = df[df['unit_price'] <= 0]
    for idx, row in bad_price.iterrows():
        errors.append({"row": row['row_id'], "field": "unit_price", "reason": f"Invalid unit price: {row['unit_price']}"})

    # Rule 4: Duplicate row entries
    dupes = df[df.duplicated(subset=['sku', 'quantity', 'unit_price'], keep='first')]
    for idx, row in dupes.iterrows():
        errors.append({"row": row['row_id'], "field": "row", "reason": "Duplicate transaction detected"})

    err_df = pd.DataFrame(errors)
    print("--- Data Quality Audit Report ---")
    print(err_df)

    # Valid rows
    valid_mask = (df['sku'].notna()) & (df['quantity'] > 0) & (df['unit_price'] > 0) & (~df.duplicated(subset=['sku'], keep='first'))
    clean_df = df[valid_mask]

    print(f"\nTotal Input: {len(df)} | Passed: {len(clean_df)} | Rejected: {len(errors)}")
    return clean_df, err_df

if __name__ == "__main__":
    audit_batch()
