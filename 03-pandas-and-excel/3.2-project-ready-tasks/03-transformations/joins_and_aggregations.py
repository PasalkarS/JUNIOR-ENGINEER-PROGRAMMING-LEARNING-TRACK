# Topic 03: Joins, GroupBy Aggregations, and Pivots
import pandas as pd
import io

ORDERS_CSV = """order_id,product_id,quantity,date
O1,P100,2,2026-09-01
O2,P200,1,2026-09-01
O3,P100,5,2026-09-02
O4,P300,3,2026-09-02
O5,P200,4,2026-09-03
"""

PRODUCTS_CSV = """product_id,category,unit_price,cost_price
P100,Electronics,120.00,80.00
P200,Office,45.00,20.00
P300,Furniture,250.00,150.00
"""

def transform_and_analyze():
    df_orders = pd.read_csv(io.StringIO(ORDERS_CSV.strip()))
    df_prods = pd.read_csv(io.StringIO(PRODUCTS_CSV.strip()))

    # 1. Relational Merge (equivalent to SQL INNER JOIN)
    merged = pd.merge(df_orders, df_prods, on='product_id', how='inner')

    # 2. Vectorized Calculated Columns
    merged['revenue'] = merged['quantity'] * merged['unit_price']
    merged['total_cost'] = merged['quantity'] * merged['cost_price']
    merged['profit'] = merged['revenue'] - merged['total_cost']

    print("--- 1. Enriched Orders Table ---")
    print(merged[['order_id', 'category', 'quantity', 'revenue', 'profit']])

    # 3. Multi-Metric GroupBy Aggregation
    cat_summary = merged.groupby('category').agg(
        total_revenue=('revenue', 'sum'),
        total_profit=('profit', 'sum'),
        units_sold=('quantity', 'sum')
    ).reset_index()

    # 4. Profit Margin Calculation
    cat_summary['margin_pct'] = round((cat_summary['total_profit'] / cat_summary['total_revenue']) * 100, 1)

    print("\n--- 2. Category Performance Summary ---")
    print(cat_summary)

if __name__ == "__main__":
    transform_and_analyze()
