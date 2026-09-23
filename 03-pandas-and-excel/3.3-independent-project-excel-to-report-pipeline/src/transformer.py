"""
Relational enrichment and multi-metric aggregation module.
"""
import pandas as pd

def enrich_sales(df_sales: pd.DataFrame, df_products: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(df_sales, df_products, on="product_id", how="left")
    merged["unit_price"] = merged["unit_price"].fillna(0.0)
    merged["cost_price"] = merged["cost_price"].fillna(0.0)
    merged["category"] = merged["category"].fillna("Unassigned")

    # Vectorized financial calculations
    merged["revenue"] = round(merged["quantity"] * merged["unit_price"], 2)
    merged["total_cost"] = round(merged["quantity"] * merged["cost_price"], 2)
    merged["profit"] = round(merged["revenue"] - merged["total_cost"], 2)

    return merged

def generate_category_summary(df_enriched: pd.DataFrame) -> pd.DataFrame:
    summary = df_enriched.groupby("category").agg(
        total_units_sold=("quantity", "sum"),
        total_revenue=("revenue", "sum"),
        total_profit=("profit", "sum")
    ).reset_index()

    summary["profit_margin_%"] = round(
        (summary["total_profit"] / summary["total_revenue"].replace(0, 1)) * 100, 1
    )
    return summary

def generate_regional_summary(df_enriched: pd.DataFrame) -> pd.DataFrame:
    summary = df_enriched.groupby("region").agg(
        total_orders=("order_id", "count"),
        total_revenue=("revenue", "sum"),
        total_profit=("profit", "sum")
    ).reset_index()
    return summary
