# Excel-to-Report Automation Pipeline

A production-style ETL (Extract, Transform, Load) data pipeline in Python using **Pandas** and **OpenPyXL** that audits raw sales data, remediates anomalies, computes profitability metrics, and generates styled executive Excel workbooks.

## Key Features

- **Robust Ingestion**: Supports `.csv` and `.xlsx` inputs.
- **Audit & Quarantine**: Detects schema defects, negative quantities, and duplicate keys into an audit log sheet.
- **Data Normalization**: Cleans whitespace, standardizes casing, and coerces datetime fields.
- **Relational Merges**: Vectorized product join computing revenue, COGS, and profit margin %.
- **Executive Styling**: Corporate Navy headers, frozen panes, and auto-adjusted column widths.

## Directory Structure

```text
3.3-independent-project-excel-to-report-pipeline/
├── README.md
├── src/
│   ├── loader.py        # Ingestion
│   ├── validator.py     # Data audit & quarantine
│   ├── cleaner.py       # Normalization
│   ├── transformer.py   # Joins & metrics
│   ├── exporter.py      # Styled OpenPyXL export
│   └── pipeline.py      # Pipeline runner
├── tests/
│   └── test_pipeline.py # Pytest test suite
├── data/
│   ├── sample_sales_raw.csv
│   └── sample_products.csv
└── docs/
    ├── architecture.md
    └── data_dictionary.md
```

## Running the Pipeline

Execute from this directory:

```bash
python src/pipeline.py
```

## Running Automated Tests

```bash
pytest tests/ -v
```
