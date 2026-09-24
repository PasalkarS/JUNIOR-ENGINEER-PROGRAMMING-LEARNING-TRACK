# Building HTTP Clients with Requests & HTTPX

> **Module 07: REST API Integration | Topic 02**

## 1. Learning Outcomes
- **HTTP Client Libraries:** Use `requests` or `httpx` to send clean GET/POST requests.
- **Enforcing Timeouts:** NEVER send HTTP requests without explicit connection and read timeouts.
- **Session Pooling:** Reuse TCP connections with `requests.Session()` for performance.
- **Error Handling:** Check response health with `response.raise_for_status()`.

## 2. Key Syntax & Concepts

### Robust HTTP Client Pattern
```python
import requests
from typing import Any, Dict

class WeatherApiClient:
    def __init__(self, base_url: str, api_key: str, timeout: float = 5.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "User-Agent": "WeatherApp/1.0"
        })

    def get_forecast(self, city: str) -> Dict[str, Any]:
        url = f"{self.base_url}/v1/forecast"
        params = {"city": city, "units": "metric"}
        
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()  # Raises HTTPError on 4xx/5xx
            return response.json()
        except requests.Timeout as e:
            raise TimeoutError(f"Weather API request timed out after {self.timeout}s") from e
        except requests.HTTPError as e:
            raise RuntimeError(f"API Error {response.status_code}: {response.text}") from e
```

## 3. Common Mistakes & Gotchas
- **Missing Timeouts:** Omitting `timeout` means Python can hang indefinitely if the remote server drops the socket.
- **Parsing `.json()` on 500 Responses:** HTML error pages from web gateways crash `.json()` with `JSONDecodeError`. Always call `raise_for_status()` first.

## 4. Practice Tasks
- **Task 1:** Implement a client class with `create_post(title, body)` that sends JSON to `https://jsonplaceholder.typicode.com/posts`.

## 5. Self-Check Questions
- **Q1:** What does `response.raise_for_status()` do when receiving a 404 response?
- **Q2:** Why does `requests.Session()` improve performance for multiple consecutive API calls?
