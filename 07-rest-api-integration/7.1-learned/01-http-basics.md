# HTTP Protocols & REST Fundamentals

> **Module 07: REST API Integration | Topic 01**

## 1. Learning Outcomes
- **HTTP Anatomy:** Understand request verbs, headers, status codes, query params, and JSON payloads.
- **Standard Verbs:** Apply GET (read), POST (create), PUT/PATCH (update), and DELETE (remove).
- **HTTP Status Codes:** Differentiate 2xx (Success), 3xx (Redirect), 4xx (Client Error), and 5xx (Server Error).
- **Idempotency:** Understand which operations can be retried safely without unintended side effects.

## 2. Key Concepts & Status Code Cheat Sheet

| Code | Meaning | Typical Scenario |
|---|---|---|
| `200 OK` | Request Succeeded | Returned on successful GET, PUT |
| `201 Created` | Resource Created | Returned on successful POST with `Location` header |
| `204 No Content`| Succeeded with no response body | Returned on successful DELETE |
| `400 Bad Request` | Client Payload Invalid | Validation errors, malformed JSON |
| `401 Unauthorized` | Missing / Invalid Token | Bad API key or expired credentials |
| `403 Forbidden` | Authenticated but disallowed | User lacks necessary role / permissions |
| `404 Not Found` | Resource Does Not Exist | Invalid resource ID or URL |
| `429 Too Many Requests`| Rate Limited | Exceeded API quota; backoff required |
| `500 Internal Error` | Server Crashed | Backend bug or database failure |

## 3. Common Mistakes & Gotchas
- **Using GET for Mutations:** GET requests must be safe and idempotent. Never trigger deletions or database writes via GET.
- **Ignoring 429 Status:** Calling an API in a tight loop without honoring rate limits results in IP blocking.

## 4. Practice Tasks
- **Task 1:** Inspect the request and response headers of a public REST API (e.g. `https://httpbin.org/json`) using curl or Python.

## 5. Self-Check Questions
- **Q1:** Why is PUT considered idempotent while POST is not?
- **Q2:** What does a 401 status indicate compared to a 403 status?
