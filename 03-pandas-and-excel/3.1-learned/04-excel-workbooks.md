# Excel Automation with Pandas and OpenPyXL

> **Module 03: Pandas and Excel | Topic 04**



## 1. Learning Outcomes

- **Multi-Sheet Workbooks:** Export multiple DataFrames into named sheets via `pd.ExcelWriter`.
- **Styling & Formatting:** Apply professional font, fill color, and border styling to headers.
- **Auto-Fit Widths:** Calculate and adjust column widths automatically for readable reports.
- **Formulas & Panes:** Add Excel formulas (e.g. SUM) and freeze top rows with openpyxl.

## 2. Key Syntax: Professional Excel Export

```python
import pandas as pd
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

def export_styled_excel(df: pd.DataFrame, filename: str):
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Summary', index=False)
        
        # Access workbook and worksheet
        wb = writer.book
        ws = wb['Summary']
        
        # Freeze top header row
        ws.freeze_panes = 'A2'
        
        # Style header
        header_fill = PatternFill(start_color='1F4E79', end_color='1F4E79', fill_type='solid')
        header_font = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
        
        for cell in ws[1]:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal='center')
            
        # Auto-adjust column widths
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = max(max_len + 4, 12)
```


## 3. Common Mistakes & Gotchas

- **Corrupt Files on Write Crash:** Always use `with pd.ExcelWriter(...)` context manager to ensure the workbook file is properly closed and flushed.
- **1-Based Indexing in openpyxl:** openpyxl rows and columns start at 1 (Row 1, Column 1 = A1), unlike Python 0-based indexing.

## 4. Practice Tasks & Self-Check

- **Task 1:** Generate an Excel report containing two tabs: 'Raw Data' and 'Executive Summary', with styled navy blue headers.
- **Q1:** What openpyxl property freezes the top header row in place?
