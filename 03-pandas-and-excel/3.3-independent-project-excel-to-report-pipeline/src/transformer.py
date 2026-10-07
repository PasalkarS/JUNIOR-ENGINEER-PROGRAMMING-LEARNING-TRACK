def transform_sales_data(sales, products):
    sales = sales.copy()
    products = products.copy()

    # Calculate total sale
    sales["Total"] = (
        sales["Quantity"] * sales["Price"]
    )

    # Create month column
    sales["Month"] = (
        sales["Sale_Date"]
        .dt.to_period("M")
        .astype(str)
    )

    # Join sales with products
    merged = sales.merge(
        products,
        on="Product_ID",
        how="left"
    )

    return merged


def create_monthly_summary(df):
    summary = (
        df.groupby("Month")
        .agg(
            Total_Sales=("Total", "sum"),
            Total_Quantity=("Quantity", "sum"),
            Number_of_Sales=("Sale_ID", "count")
        )
        .reset_index()
    )

    return summary


def create_category_summary(df):
    summary = (
        df.groupby("Category")
        .agg(
            Total_Sales=("Total", "sum"),
            Total_Quantity=("Quantity", "sum")
        )
        .reset_index()
    )

    return summary


def create_product_summary(df):
    summary = (
        df.groupby("Product_Name")
        .agg(
            Total_Sales=("Total", "sum"),
            Total_Quantity=("Quantity", "sum")
        )
        .reset_index()
        .sort_values(
            "Total_Sales",
            ascending=False
        )
    )

    return summary
    
