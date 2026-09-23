# Data Dictionary

## Sales Dataset (`sample_sales_raw.csv`)

| Field | Type | Description |
|---|---|---|
| `order_id` | str / int | Unique alphanumeric transaction code (Primary Key) |
| `date` | str | Date of order in ISO format (`YYYY-MM-DD`) |
| `customer` | str | Customer organization name |
| `product_id` | str | Foreign key referencing product master |
| `quantity` | int | Purchased units (> 0) |
| `region` | str | Sales territory (North, South, East, West) |

## Product Catalog (`sample_products.csv`)

| Field | Type | Description |
|---|---|---|
| `product_id` | str | Unique product code |
| `product_name` | str | Item title |
| `category` | str | Department categorization |
| `unit_price` | float | Sales price per unit |
| `cost_price` | float | Cost of goods sold (COGS) |
