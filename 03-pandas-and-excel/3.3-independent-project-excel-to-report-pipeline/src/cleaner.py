import pandas as pd


def clean_sales_data(df):
    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Clean text
    df["Customer"] = (
        df["Customer"]
        .fillna("Unknown")
        .str.strip()
        .str.title()
    )

    df["Product_ID"] = (
        df["Product_ID"]
        .fillna("Unknown")
        .str.strip()
    )

    # Convert quantity and price
    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        errors="coerce"
    )

    df["Price"] = pd.to_numeric(
        df["Price"],
        errors="coerce"
    )

    # Convert date
    df["Sale_Date"] = pd.to_datetime(
        df["Sale_Date"],
        errors="coerce"
    )

    # Remove rows with invalid important values
    df = df.dropna(
        subset=[
            "Sale_ID",
            "Quantity",
            "Price",
            "Sale_Date"
        ]
    )

    return df


def clean_product_data(df):
    df = df.copy()

    df = df.drop_duplicates()

    df["Product_ID"] = (
        df["Product_ID"]
        .fillna("Unknown")
        .str.strip()
    )

    df["Product_Name"] = (
        df["Product_Name"]
        .fillna("Unknown")
        .str.strip()
        .str.title()
    )

    df["Category"] = (
        df["Category"]
        .fillna("Unknown")
        .str.strip()
        .str.title()
    )

    return df
    
