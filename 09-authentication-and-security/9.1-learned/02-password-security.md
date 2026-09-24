# Password Hashing, Salting & Verification

> **Module 09: Authentication & Security | Topic 02**

## 1. Learning Outcomes
- **Hashing vs Encryption:** Understand one-way cryptographic hashes vs two-way reversible encryption.
- **Why Plaintext is Forbidden:** Never store raw passwords in databases, logs, or backups.
- **Salts & Work Factors:** Understand how unique cryptographic salts defeat precomputed rainbow tables.
- **Modern Hashing:** Implement password hashing using adaptive algorithms like bcrypt or Argon2.

## 2. Key Syntax & Concepts

### Password Hashing using Standard Python `hashlib` & Salt
```python
import hashlib
import os
import hmac

def hash_password(password: str) -> tuple[bytes, bytes]:
    # 1. Generate 16 bytes of cryptographically secure random salt
    salt = os.urandom(16)
    
    # 2. Derive 32-byte key using PBKDF2 with 100,000 iterations
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    return salt, key

def verify_password(password: str, salt: bytes, expected_key: bytes) -> bool:
    # Compute hash of incoming candidate password with the original salt
    candidate_key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    
    # Constant-time comparison to prevent timing attacks!
    return hmac.compare_digest(candidate_key, expected_key)
```

## 3. Common Mistakes & Gotchas
- **Using Fast Hashes (MD5 / SHA1):** MD5 and SHA-256 without key derivation are designed for speed, allowing attackers to test billions of guesses per second. Use slow, memory-hard algorithms (bcrypt/Argon2/PBKDF2).
- **Using `==` for Hash Comparison:** Regular `==` string equality leaks timing information. Always use `hmac.compare_digest()`.

## 4. Practice Tasks
- **Task 1:** Write a user registration and login verification class using PBKDF2-HMAC-SHA256 with unique per-user salts.

## 5. Self-Check Questions
- **Q1:** Why is a cryptographic salt added to passwords before hashing?
- **Q2:** Why should passwords be hashed rather than encrypted?
