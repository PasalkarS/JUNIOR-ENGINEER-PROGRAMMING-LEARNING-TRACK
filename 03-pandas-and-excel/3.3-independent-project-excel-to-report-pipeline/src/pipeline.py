from loader import (
    load_sales_data,
    load_product_data
)

from validator import (
    validate_sales_data,
    validate_product_data
)

from cleaner import (
    clean_sales_data,
    clean_product_data
)

from transformer import (
    transform_sales_data,
    create_monthly_summary,
    create_category_summary,
    create_product_summary
)

from exporter import export_report


def run_pipeline(
    sales_file,
    product_file,
    output_file
):

    # Load data
    sales = load_sales_data(sales_file)
    products = load_product_data(product_file)

    # Validate data
    sales_errors = validate_sales_data(sales)
    product_errors = validate_product_data(products)

    errors = sales_errors + product_errors

    # Clean data
    sales = clean_sales_data(sales)
    products = clean_product_data(products)

    # Transform data
    transformed_data = transform_sales_data(
        sales,
        products
    )

    monthly_summary = create_monthly_summary(
        transformed_data
    )

    category_summary = create_category_summary(
        transformed_data
    )

    product_summary = create_product_summary(
        transformed_data
    )

    # Export report
    export_report(
        output_file,
        transformed_data,
        monthly_summary,
        category_summary,
        product_summary,
        errors
    )

    print("Pipeline completed successfully.")
    print("Report created:", output_file)
