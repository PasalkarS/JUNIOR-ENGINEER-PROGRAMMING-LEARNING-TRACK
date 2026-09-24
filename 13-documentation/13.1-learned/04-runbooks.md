# Operations Runbooks & Troubleshooting Guides

> **Module 13: Documentation | Topic 04**

## 1. Learning Outcomes
- **Operations Runbook:** Create step-by-step procedures for deployment, maintenance, and backup tasks.
- **Troubleshooting Protocols:** Provide quick diagnostic recipes for common production failure modes.
- **Escalation Pathways:** Document who to contact when automated recovery steps fail.
- **The Non-Author Standard:** Write runbooks so that a teammate with zero prior system knowledge can execute them.

## 2. Troubleshooting Recipe Pattern

```markdown
### Issue: Database File Locked (`sqlite3.OperationalError: database is locked`)

#### Symptoms
- Application UI hangs during order submission.
- Logs show `sqlite3.OperationalError: database is locked`.

#### Cause
Another process or zombie background task is holding a write lock on `app.db`.

#### Remediation Steps
1. Check for running application processes:
   ```powershell
   Get-Process -Name "*python*"
   ```
2. Identify process holding the file lock using Resource Monitor or Handle.
3. Terminate hung worker process.
4. Restart the service:
   ```powershell
   python src/main.py
   ```
5. If lock persists, verify database file integrity:
   ```bash
   sqlite3 app.db "PRAGMA integrity_check;"
   ```
```

## 3. Common Mistakes & Gotchas
- **Assuming Expert Knowledge:** Writing "restart the daemon" without giving the exact command line fails under stress.
- **Untested Recovery Steps:** Runbook steps that have never been tested during an actual drill frequently fail during incidents.

## 4. Practice Tasks
- **Task 1:** Write a 1-page operations runbook for database backup and restore using SQLite CLI commands.

## 5. Self-Check Questions
- **Q1:** What is the difference between a technical design document and an operations runbook?
- **Q2:** Why must runbook troubleshooting steps include concrete commands?
