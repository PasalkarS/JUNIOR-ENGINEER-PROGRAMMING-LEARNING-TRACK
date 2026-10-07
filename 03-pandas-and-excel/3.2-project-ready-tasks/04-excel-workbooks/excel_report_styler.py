import pandas as pd
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter

sales = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Quantity": [5, 20, 10, 8],
    "Price": [50000, 1000, 1500, 12000]
})

sales["Total"] = sales["Quantity"] * sales["Price"]

summary = pd.DataFrame({
    "Metric": [
        "Total Products",
        "Total Quantity",
        "Total Sales"
    ],
    "Value": [
        len(sales),
        sales["Quantity"].sum(),
        sales["Total"].sum()
    ]
})

output_file = "sales_report.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    sales.to_excel(writer, sheet_name="Sales", index=False)
    summary.to_excel(writer, sheet_name="Summary", index=False)

    workbook = writer.book

    for sheet in workbook.worksheets:
        # Make header bold
        for cell in sheet[1]:
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center")

        # Adjust column width
        for column in sheet.columns:
            column_letter = get_column_letter(column[0].column)

            max_length = 0

            for cell in column:
                if cell.value is not None:
                    max_length = max(
                        max_length,
                        len(str(cell.value))
                    )

            sheet.column_dimensions[column_letter].width = max_length + 2

print("Excel report created:", output_file)
