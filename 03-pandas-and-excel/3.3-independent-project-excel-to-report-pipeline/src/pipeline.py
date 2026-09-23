"""
End-to-end Pipeline Orchestrator.
"""
from pathlib import Path
from loader import load_data
from validator import validate_sales_data
from cleaner import clean_data
from transformer import enrich_sales, generate_category_summary, generate_regional_summary
from exporter import export_executive_report

def run_pipeline(sales_file: str, products_file: str, output_excel: str):
    print(f"[1/5] Ingesting source files...")
    df_raw_sales = load_data(sales_file)
    df_products = load_data(products_file)

    print(f"[2/5] Auditing sales schema and data quality...")
    valid_sales, audit_errors = validate_sales_data(df_raw_sales)
    print(f"      Passed rows: {len(valid_sales)} | Quarantined defects: {len(audit_errors)}")

    print(f"[3/5] Cleaning and standardizing data...")
    clean_sales = clean_data(valid_sales)

    print(f"[4/5] Enriching sales and computing analytical aggregations...")
    enriched = enrich_sales(clean_sales, df_products)
    cat_summary = generate_category_summary(enriched)
    reg_summary = generate_regional_summary(enriched)

    print(f"[5/5] Exporting styled executive report to: {output_excel}")
    export_executive_report(enriched, cat_summary, reg_summary, audit_errors, output_excel)
    print("[SUCCESS] Data pipeline execution completed successfully!")

if __name__ == "__main__":
    base_dir = Path(__file__).parent.parent
    sales_path = base_dir / "data" / "sample_sales_raw.csv"
    prods_path = base_dir / "data" / "sample_products.csv"
    report_path = base_dir / "data" / "Executive_Sales_Report.xlsx"

    run_pipeline(str(sales_path), str(prods_path), str(report_path))
