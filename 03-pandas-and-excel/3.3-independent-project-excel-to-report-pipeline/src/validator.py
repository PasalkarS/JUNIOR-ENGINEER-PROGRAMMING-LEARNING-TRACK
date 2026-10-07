def validate_sales_data(df):
    errors = []

    required_columns = [
        "Sale_ID",
        "Customer",
        "Product_ID",
        "Quantity",
        "Price",
        "Sale_Date"
    ]

    for column in required_columns:
        if column not in df.columns:
            errors.append(
                "Missing required column: " + column
            )

    if "Sale_ID" in df.columns:
        duplicate_count = df["Sale_ID"].duplicated().sum()

        if duplicate_count > 0:
            errors.append(
                str(duplicate_count)
                + " duplicate Sale_ID values found"
            )

    if "Quantity" in df.columns:
        invalid_quantity = (df["Quantity"] <= 0).sum()

        if invalid_quantity > 0:
            errors.append(
                str(invalid_quantity)
                + " invalid quantity values found"
            )

    if "Price" in df.columns:
        invalid_price = (df["Price"] <= 0).sum()

        if invalid_price > 0:
            errors.append(
                str(invalid_price)
                + " invalid price values found"
            )

    return errors


def validate_product_data(df):
    errors = []

    required_columns = [
        "Product_ID",
        "Product_Name",
        "Category"
    ]

    for column in required_columns:
        if column not in df.columns:
            errors.append(
                "Missing required product column: "
                + column
            )

    return errors
    
