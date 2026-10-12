# Schema Design — Inventory System

## 1. Tables

### Categories
Stores product categories.

- `category_id`: Primary key that uniquely identifies each category.
- `category_name`: Required and unique category name.

### Suppliers
Stores supplier details.

- `supplier_id`: Primary key that uniquely identifies each supplier.
- `supplier_name`: Required supplier name.
- `phone`: Optional contact number.
- `created_at`: Records when the supplier was created.

### Products
Stores inventory product details.

- `product_id`: Primary key that uniquely identifies each product.
- `product_name`: Required product name.
- `category_id`: Foreign key referencing the categories table.
- `supplier_id`: Foreign key referencing the suppliers table.
- `quantity`: Must not be negative.
- `price`: Must not be negative.
- `created_at`: Records when the product was created.

## 2. Relationships

- One category can contain many products.
- One supplier can supply many products.
- Each product must belong to a category.
- A product can have a supplier or no supplier.

## 3. Constraints

- `PRIMARY KEY` uniquely identifies every row.
- `FOREIGN KEY` connects related tables.
- `NOT NULL` prevents required fields from being empty.
- `UNIQUE` prevents duplicate category names.
- `CHECK` prevents negative quantities and prices.
- `DEFAULT CURRENT_TIMESTAMP` automatically records the creation time.

## 4. Indexes

Indexes are created on `category_id` and `product_name` to help searches using those columns.

Indexes can improve read performance but require additional storage and can slow down inserts and updates slightly.

## 5. Normalization

Category names are stored in the categories table instead of being repeated for every product.

Supplier details are stored separately in the suppliers table.

This reduces duplicate data and makes updates easier.

## 6. Design Decision

The products table uses foreign keys to reference categories and suppliers rather than storing category and supplier names directly.

This keeps the data organized and helps maintain consistent relationships.
