# Topic 01: DataFrame Loading, Inspection, and Slicing
import pandas as pd
import io

CSV_DATA = """order_id,date,customer,region,amount,items_count
1001,2026-09-01,Acme Corp,North,450.00,3
1002,2026-09-01,Globex,South,1250.50,12
1003,2026-09-02,Initech,North,300.00,2
1004,2026-09-02,Umbrella,East,890.25,5
1005,2026-09-03,Acme Corp,West,620.00,4
1006,2026-09-03,Soylent,North,150.00,1
1007,2026-09-04,Globex,South,2100.00,18
"""

def analyze_orders():
    df = pd.read_csv(io.StringIO(CSV_DATA.strip()))
    
    print("--- 1. Dataset Overview ---")
    print(f"Shape (Rows, Columns): {df.shape}")
    print("\nColumns & Types:")
    print(df.dtypes)

    print("\n--- 2. High-Value Orders (Amount > $500) ---")
    high_value = df[df['amount'] > 500.0]
    print(high_value[['order_id', 'customer', 'region', 'amount']])

    print("\n--- 3. North Region Summary ---")
    north_orders = df[df['region'] == 'North']
    print(f"Total North Orders: {len(north_orders)}")
    print(f"Total North Revenue: ${north_orders['amount'].sum():,.2f}")

    print("\n--- 4. Summary Statistics ---")
    print(df[['amount', 'items_count']].describe())

if __name__ == "__main__":
    analyze_orders()
