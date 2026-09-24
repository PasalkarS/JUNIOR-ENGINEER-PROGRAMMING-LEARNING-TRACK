# API Contracts & Data Dictionaries

> **Module 13: Documentation | Topic 03**

## 1. Learning Outcomes
- **API Endpoint Contracts:** Document request parameters, headers, payload schemas, and response formats.
- **Data Dictionaries:** Define table names, column datatypes, primary keys, and business validation rules.
- **Error Dictionaries:** Document possible error codes and recovery actions.
- **Interchangeability:** Enable frontend or backend engineers to build integrations from docs alone.

## 2. Key Documentation Patterns

### Data Dictionary Table Standard
```markdown
### Orders Table (`orders`)

| Column | Type | Nullable? | Key | Business Description & Validation Rules |
|---|---|---|---|---|
| `order_id` | TEXT | No | PK | Alphanumeric unique identifier (e.g., `ORD-1001`) |
| `customer_id` | TEXT | No | FK | References `customers(customer_id)` |
| `order_date` | TEXT | No | - | ISO-8601 string (`YYYY-MM-DD`) |
| `total_amount`| REAL | No | - | Gross total; must be >= 0.00 |
| `status` | TEXT | No | - | Enum: `PENDING`, `PAID`, `SHIPPED`, `CANCELLED` |
```

### API Endpoint Contract Standard
```markdown
### `POST /api/v1/orders`

Creates a new customer order.

**Request Body (`application/json`):**
```json
{
  "customer_id": "C-100",
  "items": [
    {"sku": "LAP-01", "quantity": 1}
  ]
}
```

**Responses:**
- `201 Created`: Returns newly created order record.
- `400 Bad Request`: Validation failure (e.g., non-positive quantity).
- `404 Not Found`: Customer or SKU does not exist.
```

## 3. Common Mistakes & Gotchas
- **Undocumented Nullability:** Omitting whether a field is required or optional causes silent runtime crashes during integration.
- **Missing Example Payloads:** Providing JSON schema definitions without concrete example payloads slows down client integration.

## 4. Practice Tasks
- **Task 1:** Write a complete Data Dictionary table for an inventory tracking system with at least 5 attributes.

## 5. Self-Check Questions
- **Q1:** What are the essential columns in a database Data Dictionary table?
- **Q2:** Why should API contracts explicitly specify error responses in addition to success responses?
