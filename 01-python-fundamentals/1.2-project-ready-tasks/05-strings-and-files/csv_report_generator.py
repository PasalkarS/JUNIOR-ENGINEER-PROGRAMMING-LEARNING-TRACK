# CSV Report Generator
# Reads sales CSV data and outputs an aggregated summary report.

import csv
import io

SAMPLE_CSV = """order_id,date,customer,region,amount
1001,2026-09-01,Acme Corp,North,450.00
1002,2026-09-01,Globex,South,1250.50
1003,2026-09-02,Initech,North,300.00
1004,2026-09-02,Umbrella Corp,East,890.25
1005,2026-09-03,Acme Corp,West,620.00
"""

def generate_region_summary(csv_data: str):
    f = io.StringIO(csv_data.strip())
    reader = csv.DictReader(f)

    region_totals = {}
    for row in reader:
        reg = row["region"]
        amt = float(row["amount"])
        region_totals[reg] = region_totals.get(reg, 0.0) + amt

    return region_totals

if __name__ == "__main__":
    summary = generate_region_summary(SAMPLE_CSV)
    print(f"{'Region':<12} {'Total Sales':>12}")
    print("-" * 25)
    for reg, total in summary.items():
        print(f"{reg:<12} ${total:>11.2f}")
