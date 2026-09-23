# Topic 02: Data Cleaning & Normalization Pipeline
import pandas as pd
import numpy as np
import io

MESSY_DATA = """customer_id,name,email,signup_date,active
C01,  Alice Smith , alice@example.com , 2026-01-15 , TRUE
C02, Bob Jones,bob@test.com,2026/02/20,false
C03, Carlos G.,carlos@domain,INVALID_DATE,true
C01,  Alice Smith , alice@example.com , 2026-01-15 , TRUE
C04, Diane Vance,diane@corp.org,2026-03-01,
C05,,missing_name@corp.org,2026-03-05,false
"""

def clean_customers():
    df = pd.read_csv(io.StringIO(MESSY_DATA.strip()))
    print("Before Cleaning:")
    print(df)

    # 1. Deduplicate by customer_id
    df = df.drop_duplicates(subset=['customer_id'], keep='first')

    # 2. String trimming and case standardization
    df['name'] = df['name'].fillna('Unknown').astype(str).str.strip().str.title()
    df['email'] = df['email'].astype(str).str.strip().str.lower()

    # 3. Clean date parsing with coercion
    df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce', format='mixed')

    # 4. Fill missing active status
    df['active'] = df['active'].fillna('false').astype(str).str.strip().str.upper() == 'TRUE'

    print("\nAfter Cleaning:")
    print(df)
    return df

if __name__ == "__main__":
    clean_customers()
