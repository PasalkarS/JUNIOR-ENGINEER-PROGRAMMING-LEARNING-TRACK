# Information Security Fundamentals & Threat Awareness

> **Module 09: Authentication & Security | Topic 01**

## 1. Learning Outcomes
- **The CIA Triad:** Master Confidentiality, Integrity, and Availability principles.
- **Least Privilege:** Ensure users and services possess only minimum required permissions.
- **Trust Boundaries:** Identify boundaries where untrusted external data crosses into the application.
- **Threat Awareness:** Recognize common attack vectors (injection, credential stuffing, brute force).

## 2. Key Security Principles

| Principle | Meaning | Concrete Software Example |
|---|---|---|
| **Confidentiality** | Only authorized parties see data | Hashing passwords, encrypting data in transit with TLS |
| **Integrity** | Data cannot be tampered with | HMAC signatures on session cookies, database constraints |
| **Availability** | Services remain responsive | Rate limiting, query timeouts, avoiding memory leaks |
| **Least Privilege** | Minimum necessary access granted | Read-only database user for analytics dashboards |
| **Defense in Depth** | Multiple independent security layers | Validating input on both client UI and server domain |

## 3. Common Mistakes & Gotchas
- **Security by Obscurity:** Hiding endpoint URLs or obfuscating variable names does not provide real security.
- **Trusting Client Input:** Never rely solely on front-end browser checks; always re-validate on the server.

## 4. Practice Tasks
- **Task 1:** Diagram trust boundaries for an e-commerce checkout flow receiving untrusted credit card input.

## 5. Self-Check Questions
- **Q1:** What is a trust boundary in software architecture?
- **Q2:** Why is the principle of least privilege essential for database user accounts?
