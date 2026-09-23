"""
Data normalization and type casting module.
"""
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()

    # Standardize string columns
    for col in ["customer", "region"]:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(str).str.strip().str.title()

    if "product_id" in df_clean.columns:
        df_clean["product_id"] = df_clean["product_id"].astype(str).str.strip().str.upper()

    # Convert dates
    df_clean["date"] = pd.to_datetime(df_clean["date"], errors="coerce").dt.strftime("%Y-%m-%d")

    # Cast numbers
    df_clean["quantity"] = pd.to_numeric(df_clean["quantity"], errors="coerce").fillna(1).astype(int)

    return df_clean
