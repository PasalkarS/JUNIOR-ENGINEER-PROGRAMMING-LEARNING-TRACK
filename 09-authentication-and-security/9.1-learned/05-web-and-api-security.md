# Web Application Security (OWASP Top 10)

> **Module 09: Authentication & Security | Topic 05**

## 1. Learning Outcomes
- **OWASP Overview:** Understand the primary vulnerabilities affecting web apps and APIs.
- **SQL & Command Injection:** Prevent injection by separating code from data using parameterized queries.
- **Cross-Site Scripting (XSS):** Sanitize and escape user-supplied HTML text before rendering.
- **Secure Communication:** Enforce TLS/HTTPS and understand security headers (`Content-Security-Policy`).

## 2. Common Vulnerabilities & Countermeasures

| Vulnerability | Attack Vector | Countermeasure |
|---|---|---|
| **SQL Injection** | Attacker injects SQL fragments into query strings | Parameterized queries (`cursor.execute(..., (?))`) |
| **Command Injection** | Attacker executes arbitrary shell commands | Avoid `shell=True` in `subprocess`; pass argv arrays |
| **XSS** | Injected JavaScript executes in victim's browser | HTML entity escaping, modern templating engines |
| **CSRF** | Malicious sites forge requests on authenticated users | Anti-CSRF tokens, `SameSite=Lax/Strict` cookies |
| **Broken Object Level Auth (BOLA)** | User accesses records belonging to another tenant | Enforce user-ownership check on every query |

## 3. Common Mistakes & Gotchas
- **Using `os.system()` with User Input:** Passing un-sanitized strings into `os.system(cmd)` allows complete system takeover.
- **Overly Permissive CORS:** Setting `Access-Control-Allow-Origin: *` with credentials enabled exposes sensitive data cross-origin.

## 4. Practice Tasks
- **Task 1:** Audit a sample Python script for input validation vulnerabilities and rewrite dangerous string-concatenated SQL queries.

## 5. Self-Check Questions
- **Q1:** How does parameterization eliminate SQL injection?
- **Q2:** What does the `SameSite` attribute on HTTP cookies defend against?
