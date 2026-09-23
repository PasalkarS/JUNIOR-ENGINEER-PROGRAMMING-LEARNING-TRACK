"""
Data ingestion module for CSV and Excel files.
"""
from pathlib import Path
import pandas as pd

def load_data(filepath: str | Path) -> pd.DataFrame:
    p = Path(filepath)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {p}")
    if p.suffix.lower() == ".csv":
        return pd.read_csv(p)
    elif p.suffix.lower() in [".xlsx", ".xls"]:
        return pd.read_excel(p)
    else:
        raise ValueError(f"Unsupported file format: {p.suffix}")
