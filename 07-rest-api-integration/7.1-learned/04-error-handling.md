# Resilient Error Handling, Retries & Backoff

> **Module 07: REST API Integration | Topic 04**

## 1. Learning Outcomes
- **Transient vs Permanent Errors:** Distinguish retryable failures (503, 429, timeouts) from client bugs (400, 401, 404).
- **Exponential Backoff:** Implement jittered delay intervals between retry attempts to prevent thundering herds.
- **User-Safe Error Messages:** Translate raw network tracebacks into clear, actionable error messages.
- **Circuit Breaker Basics:** Stop making calls when a downstream service is visibly offline.

## 2. Key Syntax & Concepts

### Exponential Backoff Retry Function
```python
import time
import requests

def request_with_retry(url: str, max_retries: int = 3, base_delay: float = 1.0) -> requests.Response:
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=5.0)
            # Only retry server errors (500, 502, 503, 504) or rate limits (429)
            if response.status_code in {429, 500, 502, 503, 504}:
                raise requests.HTTPError(f"Transient error {response.status_code}")
            return response
        except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as err:
            if attempt == max_retries:
                raise RuntimeError(f"Request failed after {max_retries} attempts: {err}") from err
            delay = base_delay * (2 ** (attempt - 1))
            print(f"[RETRY] Attempt {attempt} failed ({err}). Retrying in {delay:.1f}s...")
            time.sleep(delay)
```

## 3. Common Mistakes & Gotchas
- **Retrying Non-Idempotent POSTs:** Retrying a failed checkout POST request without an idempotency key risks charging customers multiple times.
- **Blind Instant Retries:** Retrying immediately without delay slams a recovering server and exacerbates outages.

## 4. Practice Tasks
- **Task 1:** Implement a simulated failure test where an endpoint fails twice with 503 before returning 200, verifying that your retry loop recovers.

## 5. Self-Check Questions
- **Q1:** Should a 400 Bad Request error be retried automatically? Why or why not?
- **Q2:** What purpose does exponential backoff serve during network congestion?
