# 04 — Excel Workbooks

## 1. Introduction to Excel Processing

### What it is

Python can be used to read, create, modify, and format Excel workbooks.

### Important Points

* Pandas is useful for working with tabular Excel data.
* OpenPyXL is useful for working with Excel workbook structure and formatting.
* Excel files can contain multiple worksheets.
* Python can automate repetitive Excel reporting tasks.

---

## 2. Pandas vs OpenPyXL

### What it is

Pandas and OpenPyXL can both work with Excel files, but they are used for different purposes.

### Important Points

* Pandas is mainly used for data processing and analysis.
* OpenPyXL is mainly used for workbook and cell-level operations.
* Pandas is useful for reading and writing DataFrames.
* OpenPyXL is useful for formatting and modifying workbook elements.
* Both libraries can be used together when needed.

---

## 3. Reading Excel Files

### What it is

Pandas can read an Excel workbook and load its data into a DataFrame.

### Important Points

* `read_excel()` is used to read Excel files.
* The result is normally a DataFrame.
* A specific worksheet can be selected.
* The file path must be correct.

### Basic Syntax

```python id="p8m2hx"
import pandas as pd

df = pd.read_excel("data.xlsx")
```

---

## 4. Reading Specific Sheets

### What it is

An Excel workbook can contain multiple sheets, and a specific sheet can be loaded when needed.

### Important Points

* Use `sheet_name` to select a worksheet.
* A sheet can be selected using its name.
* A sheet can also be selected using its position.
* Selecting the correct sheet is important when processing workbooks.

### Basic Syntax

```python id="gq1q4j"
df = pd.read_excel("data.xlsx", sheet_name="Sales")
```

---

## 5. Reading Multiple Sheets

### What it is

Multiple worksheets can be read from the same Excel workbook.

### Important Points

* Multiple sheet names can be provided.
* Reading multiple sheets is useful when data is stored across worksheets.
* Each sheet can be loaded into a separate DataFrame.
* The returned data should be checked before processing.

### Basic Syntax

```python id="j4f0kr"
data = pd.read_excel(
    "data.xlsx",
    sheet_name=["Sales", "Employees"]
)
```

---

## 6. Sheet Names

### What it is

Sheet names identify the individual worksheets inside an Excel workbook.

### Important Points

* Sheet names should be clear and meaningful.
* Existing sheet names can be inspected.
* Sheet names can be changed when creating or editing workbooks.
* Avoid unnecessary spaces and confusing names.

---

## 7. Creating Sheets

### What it is

New worksheets can be added to an Excel workbook to organize different types of information.

### Important Points

* A workbook can contain multiple sheets.
* Different sheets can contain raw data, cleaned data, summaries, or errors.
* Sheet names should describe their contents.
* A well-organized workbook is easier to use.

---

## 8. Renaming Sheets

### What it is

Renaming a worksheet changes its name to something more useful or descriptive.

### Important Points

* Clear names make reports easier to understand.
* Sheet names should be short and meaningful.
* Avoid duplicate sheet names.
* Renaming can be done using OpenPyXL.

### Basic Syntax

```python id="x6t2ks"
worksheet.title = "Summary"
```

---

## 9. Writing DataFrames to Excel

### What it is

Pandas can write DataFrame data into Excel worksheets.

### Important Points

* `to_excel()` is used to create Excel output.
* A worksheet name can be specified.
* Multiple DataFrames can be written to different sheets.
* Output files should be saved to the correct location.

### Basic Syntax

```python id="5db4nr"
df.to_excel("report.xlsx", sheet_name="Data", index=False)
```

---

## 10. Writing Cell Values

### What it is

OpenPyXL allows individual cells in a worksheet to be read and changed.

### Important Points

* A cell can contain text, numbers, dates, or formulas.
* Cells can be accessed using their position.
* Cell values can be updated directly.
* OpenPyXL is useful when individual cells need to be controlled.

### Basic Syntax

```python id="tvx0ag"
worksheet["A1"] = "Sales Report"
worksheet["B1"] = 1000
```

---

## 11. OpenPyXL Basics

### What it is

OpenPyXL is a Python library used to read and modify Excel `.xlsx` workbooks.

### Important Points

* `Workbook` represents an Excel workbook.
* `Worksheet` represents a sheet.
* `Cell` represents an individual cell.
* OpenPyXL can read, write, and format Excel files.
* It provides more control over workbook structure than Pandas.

### Basic Syntax

```python id="q7f4zv"
from openpyxl import Workbook

workbook = Workbook()
worksheet = workbook.active
```

---

## 12. Workbook

### What it is

A workbook is the complete Excel file containing one or more worksheets.

### Important Points

* A workbook can contain multiple worksheets.
* It can be created, opened, modified, and saved.
* Worksheets are accessed through the workbook.
* Workbook structure should be kept organized.

---

## 13. Worksheet

### What it is

A worksheet is a single sheet inside an Excel workbook.

### Important Points

* Contains rows and columns of cells.
* Has a specific name.
* Can be created or removed.
* Can contain data, formulas, and formatting.

---

## 14. Cells

### What it is

A cell is an individual location in a worksheet where data can be stored.

### Important Points

* Cells are identified by row and column positions.
* A cell can contain text, numbers, dates, or formulas.
* Cell values can be read and modified.
* Cells can also be formatted.

### Basic Syntax

```python id="y1qf6d"
worksheet["A1"] = "Name"

value = worksheet["A1"].value
```

---

## 15. Formatting Cells

### What it is

Cell formatting changes the appearance and presentation of Excel data.

### Important Points

* Headers can be formatted differently from normal data.
* Fonts can be changed.
* Alignment can be adjusted.
* Number formats can be applied.
* Formatting should improve readability without making the report unnecessarily complex.

### Basic Syntax

```python id="f3p2zq"
from openpyxl.styles import Font

worksheet["A1"].font = Font(bold=True)
```

---

## 16. Headers

### What it is

Headers identify what each column contains.

### Important Points

* Headers should be clear and descriptive.
* Consistent formatting makes headers easier to identify.
* Headers are commonly placed in the first row.
* Avoid unclear or duplicate column names.

---

## 17. Font and Alignment

### What it is

Font and alignment control how text and values appear inside cells.

### Important Points

* Fonts can be bold, italic, or changed in size.
* Text can be aligned left, right, or center.
* Header alignment can improve readability.
* Formatting should be consistent across the report.

### Basic Syntax

```python id="8a5j2r"
from openpyxl.styles import Font, Alignment

worksheet["A1"].font = Font(bold=True)
worksheet["A1"].alignment = Alignment(horizontal="center")
```

---

## 18. Number Formats

### What it is

Number formats control how numbers, dates, percentages, and currency values are displayed.

### Important Points

* Numbers can be displayed with decimal places.
* Dates can use different date formats.
* Percentages can be displayed as percentages.
* Currency values can use appropriate currency formats.
* Formatting changes how values are displayed, not their underlying value.

### Basic Syntax

```python id="r8u1kq"
worksheet["B2"].number_format = "0.00"
```

---

## 19. Column Widths

### What it is

Column width controls how much horizontal space is available for data.

### Important Points

* Narrow columns can hide information.
* Wide columns can waste space.
* Column widths should fit the content.
* Proper widths make reports easier to read.

### Basic Syntax

```python id="6u5j9x"
worksheet.column_dimensions["A"].width = 20
```

---

## 20. Borders

### What it is

Borders are lines added around cells to visually separate and organize data.

### Important Points

* Borders can help separate headers and data.
* They can make tables easier to read.
* Use borders consistently.
* Avoid unnecessary formatting.

### Basic Syntax

```python id="6t2z6q"
from openpyxl.styles import Border, Side

side = Side(style="thin")
worksheet["A1"].border = Border(
    left=side,
    right=side,
    top=side,
    bottom=side
)
```

---

## 21. Formulas vs Values

### What it is

Excel cells can contain either calculated formulas or fixed values.

### Important Points

* A formula calculates a result using other cells.
* A value is the actual stored result.
* Formulas can update when source data changes.
* Calculated values are useful when the result does not need to change.
* Choose formulas or values based on the report requirement.

### Basic Syntax

```python id="l2t8wp"
worksheet["C2"] = "=A2+B2"
```

---

## 22. Multiple-Sheet Workbooks

### What it is

A multiple-sheet workbook stores different types of information in separate worksheets.

### Important Points

* Raw data can be kept in one sheet.
* Cleaned data can be kept in another sheet.
* Summary results can have their own sheet.
* Error information can be stored separately.
* Separate sheets make reports easier to navigate.

---

## 23. Workbook Structure

### What it is

Workbook structure is the way data and reports are organized across worksheets.

### Important Points

* Use clear sheet names.
* Keep related information together.
* Separate raw data from processed data when appropriate.
* Keep summary information easy to find.
* A consistent structure makes automated reports easier to maintain.

---

## 24. Saving Excel Files Safely

### What it is

Saving safely means creating the required output without accidentally losing or overwriting important data.

### Important Points

* Use a clear output file name.
* Save to the intended location.
* Avoid overwriting the original input file.
* Check that the workbook was created successfully.
* Open and inspect the output when necessary.

### Basic Syntax

```python id="c5w9hf"
workbook.save("report.xlsx")
```
