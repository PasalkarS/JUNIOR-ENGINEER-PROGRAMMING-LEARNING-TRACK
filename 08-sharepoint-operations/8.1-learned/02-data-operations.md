# SharePoint CRUD & REST Operations

> **Module 08: SharePoint Operations | Topic 02**

## 1. Learning Outcomes
- **REST / Graph APIs:** Query SharePoint lists using modern REST endpoints.
- **CRUD Lifecycle:** Create, Read, Update, and Delete list items programmatically.
- **OData Filtering:** Filter queries using `$select`, `$filter`, `$top`, and `$expand`.
- **Field Type Mapping:** Map Python types to SharePoint Choice, DateTime, and Lookup fields.

## 2. Key Syntax & Concepts

### Standard OData Query Patterns
```http
# Read top 50 active equipment records selecting specific columns
GET https://tenant.sharepoint.com/sites/ops/_api/web/lists/getbytitle('Assets')/items
    ?$select=ID,Title,AssetCode,PurchasePrice,Status
    &$filter=Status eq 'Active' and PurchasePrice gt 1000
    &$top=50
```

### Python CRUD Operations Pattern
```python
class SharePointListClient:
    def __init__(self, session, site_url: str, list_title: str):
        self.session = session
        self.endpoint = f"{site_url.rstrip('/')}/_api/web/lists/getbytitle('{list_title}')/items"

    def get_items(self, filter_query: str = "") -> list[dict]:
        params = {"$filter": filter_query} if filter_query else {}
        resp = self.session.get(self.endpoint, params=params)
        resp.raise_for_status()
        return resp.json()["value"]

    def create_item(self, item_data: dict) -> dict:
        resp = self.session.post(self.endpoint, json=item_data)
        resp.raise_for_status()
        return resp.json()
```

## 3. Common Mistakes & Gotchas
- **Missing X-HTTP-Method for Updates:** In SharePoint REST v1, updates often require `POST` with `X-HTTP-Method: MERGE` and `If-Match: *` headers.
- **Case Sensitivity in OData:** OData operators (`eq`, `ne`, `gt`, `lt`, `and`, `or`) must be lowercase.

## 4. Practice Tasks
- **Task 1:** Construct an OData query string that filters for tickets where `Priority` is `'High'` and `Created` is after `'2026-01-01'`.

## 5. Self-Check Questions
- **Q1:** What OData parameter limits the number of returned rows?
- **Q2:** Why is using `$select` critical when querying SharePoint lists with many columns?
