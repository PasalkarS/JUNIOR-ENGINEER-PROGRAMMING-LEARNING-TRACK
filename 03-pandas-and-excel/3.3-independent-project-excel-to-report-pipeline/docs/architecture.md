# Pipeline Architecture

The Excel-to-Report pipeline separates processing into 5 modular stages:

```
[Raw CSV / Excel]
       |
       v
  1. [loader.py] ----> Raw Ingestion
       |
       v
  2. [validator.py] -> Audits Schema & Quarantines Defective Rows
       |
       v
  3. [cleaner.py] ---> Trims Whitespace, Standardizes Dates & Casing
       |
       v
  4. [transformer.py]-> Relational Merge & Vectorized Profit Calculations
       |
       v
  5. [exporter.py] --> Multi-Tab Styled OpenPyXL Workbook
       |
       v
[Executive_Sales_Report.xlsx]
```
