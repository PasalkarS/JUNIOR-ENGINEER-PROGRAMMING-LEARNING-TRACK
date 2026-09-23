"""
Data quality audit and quarantine engine.
"""
import pandas as pd

REQUIRED_COLUMNS = {"order_id", "date", "customer", "product_id", "quantity", "region"}

def validate_sales_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Audits incoming dataframe.
    Returns (valid_df, errors_df).
    """
    missing_cols = REQUIRED_COLUMNS - set(df.columns)
    if missing_cols:
        raise ValueError(f"Schema violation: missing required columns {missing_cols}")

    errors = []

    # 1. Invalid or Missing Order IDs
    for idx, row in df[df["order_id"].isna()].iterrows():
        errors.append({"row_index": idx, "field": "order_id", "reason": "Missing order ID"})

    # 2. Non-positive Quantity
    for idx, row in df[df["quantity"] <= 0].iterrows():
        errors.append({"row_index": idx, "field": "quantity", "reason": f"Quantity must be > 0 (got {row['quantity']})"})

    # 3. Duplicate Order IDs
    dupes = df[df.duplicated(subset=["order_id"], keep="first")]
    for idx, row in dupes.iterrows():
        errors.append({"row_index": idx, "field": "order_id", "reason": f"Duplicate order ID '{row['order_id']}'"})

    error_df = pd.DataFrame(errors)

    # Mask for clean valid records
    valid_mask = (
        df["order_id"].notna() &
        (df["quantity"] > 0) &
        (~df.duplicated(subset=["order_id"], keep="first"))
    )
    valid_df = df[valid_mask].copy()

    return valid_df, error_df
