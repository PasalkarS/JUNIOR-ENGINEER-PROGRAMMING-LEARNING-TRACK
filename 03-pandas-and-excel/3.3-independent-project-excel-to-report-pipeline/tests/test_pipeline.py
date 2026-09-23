"""
Automated unit tests for Excel-to-Report Pipeline.
"""
import pytest
import pandas as pd
from pathlib import Path
import sys

src_path = str(Path(__file__).resolve().parent.parent / "src")
if src_path in sys.path:
    sys.path.remove(src_path)
sys.path.insert(0, src_path)

for mod in ["loader", "validator", "cleaner", "transformer", "exporter"]:
    sys.modules.pop(mod, None)

from loader import load_data
from validator import validate_sales_data
from cleaner import clean_data
from transformer import enrich_sales, generate_category_summary
from exporter import export_executive_report

@pytest.fixture
def sample_dfs():
    sales = pd.DataFrame({
        "order_id": ["O1", "O2", "O3", "O1"],  # O1 is duplicate
        "date": ["2026-09-01", "2026-09-02", "2026-09-03", "2026-09-01"],
        "customer": [" Acme ", "Globex", "Initech", "Acme"],
        "product_id": ["P1", "P2", "P1", "P1"],
        "quantity": [2, -1, 3, 2],  # O2 is negative quantity
        "region": ["north", "south", "north", "north"]
    })
    prods = pd.DataFrame({
        "product_id": ["P1", "P2"],
        "category": ["Electronics", "Furniture"],
        "unit_price": [100.0, 50.0],
        "cost_price": [60.0, 30.0]
    })
    return sales, prods

def test_validator_detects_errors(sample_dfs):
    sales, _ = sample_dfs
    valid, errors = validate_sales_data(sales)

    # O1 (duplicate) and O2 (negative qty) flagged
    assert len(valid) == 2  # O1 (first) and O3
    assert len(errors) == 2

def test_cleaner_normalizes_strings(sample_dfs):
    sales, _ = sample_dfs
    clean = clean_data(sales)
    assert clean.loc[0, "customer"] == "Acme"
    assert clean.loc[0, "region"] == "North"

def test_transformer_profit_calculation(sample_dfs):
    sales, prods = sample_dfs
    valid, _ = validate_sales_data(sales)
    enriched = enrich_sales(valid, prods)

    assert "revenue" in enriched.columns
    assert "profit" in enriched.columns

    # Order O1: qty=2, price=100 -> revenue=200, cost=120 -> profit=80
    o1 = enriched[enriched["order_id"] == "O1"].iloc[0]
    assert o1["revenue"] == 200.0
    assert o1["profit"] == 80.0

def test_excel_export_creates_file(tmp_path, sample_dfs):
    sales, prods = sample_dfs
    valid, errors = validate_sales_data(sales)
    clean = clean_data(valid)
    enriched = enrich_sales(clean, prods)
    cat_summary = generate_category_summary(enriched)
    reg_summary = enriched.groupby("region")["revenue"].sum().reset_index()

    out_file = tmp_path / "report.xlsx"
    export_executive_report(enriched, cat_summary, reg_summary, errors, out_file)

    assert out_file.exists()
    assert out_file.stat().st_size > 0
