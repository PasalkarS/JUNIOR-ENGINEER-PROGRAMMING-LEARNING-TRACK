# API Design Contracts, Pagination & Versioning

> **Module 07: REST API Integration | Topic 03**

## 1. Learning Outcomes
- **Resource Orientation:** Map domain nouns to plural endpoint paths (`/api/v1/orders`).
- **Pagination Patterns:** Consume and implement page/limit, offset/limit, and cursor-based pagination.
- **Query Filtering:** Pass structured search and filtering parameters safely.
- **API Versioning:** Understand URL versioning (`/v1/`) and header negotiation.

## 2. Key Syntax & Concepts

### Paginated Ingestion Loop
```python
def fetch_all_records(client, endpoint: str, page_size: int = 50) -> list[dict]:
    all_records = []
    page = 1
    
    while True:
        data = client.get(endpoint, params={"page": page, "limit": page_size})
        items = data.get("items", [])
        if not items:
            break
            
        all_records.extend(items)
        if len(items) < page_size:
            # Last page reached
            break
            
        page += 1
        
    return all_records
```

## 3. Common Mistakes & Gotchas
- **Unbounded Queries:** Attempting to retrieve all 100,000 records without pagination causes out-of-memory crashes on both client and server.
- **Infinite Pagination Loops:** If an API returns duplicate or circular next page tokens, pagination runs indefinitely. Always enforce a `max_pages` ceiling guard.

## 4. Practice Tasks
- **Task 1:** Write a generator function that yields items page by page from a mock paginated API response.

## 5. Self-Check Questions
- **Q1:** What is the advantage of cursor-based pagination over offset-based pagination on large, rapidly changing datasets?
- **Q2:** Why are plural nouns preferred for REST collection endpoints?
