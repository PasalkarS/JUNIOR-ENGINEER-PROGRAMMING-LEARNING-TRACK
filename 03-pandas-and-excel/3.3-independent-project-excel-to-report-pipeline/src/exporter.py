import pandas as pd
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter


def export_report(
    output_file,
    sales_data,
    monthly_summary,
    category_summary,
    product_summary,
    errors
):

    error_data = pd.DataFrame({
        "Error": errors
    })

    with pd.ExcelWriter(
        output_file,
        engine="openpyxl"
    ) as writer:

        sales_data.to_excel(
            writer,
            sheet_name="Sales Data",
            index=False
        )

        monthly_summary.to_excel(
            writer,
            sheet_name="Monthly Summary",
            index=False
        )

        category_summary.to_excel(
            writer,
            sheet_name="Category Summary",
            index=False
        )

        product_summary.to_excel(
            writer,
            sheet_name="Product Summary",
            index=False
        )

        error_data.to_excel(
            writer,
            sheet_name="Error Summary",
            index=False
        )

        workbook = writer.book

        for sheet in workbook.worksheets:

            # Bold headers
            for cell in sheet[1]:
                cell.font = Font(bold=True)
                cell.alignment = Alignment(
                    horizontal="center"
                )

            # Adjust column widths
            for column in sheet.columns:

                column_letter = get_column_letter(
                    column[0].column
                )

                max_length = 0

                for cell in column:
                    if cell.value is not None:
                        max_length = max(
                            max_length,
                            len(str(cell.value))
                        )

                sheet.column_dimensions[
                    column_letter
                ].width = max_length + 2
                
