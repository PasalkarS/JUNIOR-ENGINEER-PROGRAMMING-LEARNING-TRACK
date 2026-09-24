# Throttling, Permissions & Failure Modes

> **Module 08: SharePoint Operations | Topic 05**

## 1. Learning Outcomes
- **Principle of Least Privilege:** Scope application permissions to specific sites rather than tenant-wide admin rights.
- **Handling 429 Throttling:** Detect SharePoint rate limits and respect the `Retry-After` response header.
- **Authentication Separation:** Separate App Registration (Client ID & Client Secret) from source code.
- **Diagnosing Failures:** Differentiate credential expiry, network partition, and permission denial errors.

## 2. Key Concepts & Headers

### The Retry-After Protocol
When SharePoint experiences high tenant load, it returns status `429 Too Many Requests` or `503 Service Unavailable` with a `Retry-After` header specifying how many seconds to wait:

```python
def safe_sp_request(session, url: str) -> dict:
    resp = session.get(url)
    if resp.status_code == 429:
        wait_seconds = int(resp.headers.get("Retry-After", 10))
        print(f"[THROTTLED] Pausing for {wait_seconds} seconds...")
        time.sleep(wait_seconds)
        resp = session.get(url)
    resp.raise_for_status()
    return resp.json()
```

## 3. Common Mistakes & Gotchas
- **Hardcoding Client Secrets:** Storing Azure AD Client Secrets in Python files exposes corporate credentials to anyone reading the repository.
- **Ignoring Throttling Warnings:** Aggressive scripts that fail to back off will have their IP or service principal banned temporarily.

## 4. Practice Tasks
- **Task 1:** Write a middleware handler that parses the `Retry-After` header from a mocked 429 response.

## 5. Self-Check Questions
- **Q1:** What response header tells you how long to wait before retrying after a 429 error?
- **Q2:** Why should client secrets always be supplied via environment variables?
