# Diagnosing Runtime & Environment Failures

> **Module 11: Debugging & Logging | Topic 04**

## 1. Learning Outcomes
- **Separating Causes:** Differentiate code logic bugs, environment misconfigurations, and external dependency outages.
- **File System Failures:** Diagnose permissions, relative paths, and working directory discrepancies.
- **Network Failures:** Identify DNS resolution issues, socket timeouts, and TLS certificate errors.
- **Dependency Conflicts:** Inspect package versions with `pip list` and `python -m pip check`.

## 2. Common Runtime Failure Modes

| Symptom | Probable Cause | Diagnostic Command / Action |
|---|---|---|
| `FileNotFoundError` | Current working directory is different than expected | Print `Path.cwd()` and check absolute paths |
| `PermissionError` | File is locked by Excel or lack of write permissions | Close Excel or run as authorized user |
| `ModuleNotFoundError` | Script running in wrong virtualenv | Run `sys.executable` to verify active Python interpreter |
| `ConnectionRefusedError` | Database or API service is not running locally | Check `netstat` or verify service status |
| `MemoryError` | Ingesting massive file without streaming/chunking | Check DataFrame memory with `df.info(memory_usage='deep')` |

## 3. Common Mistakes & Gotchas
- **Hardcoding Windows Backslashes:** `C:\Users\name\file.txt` causes syntax errors with escape characters like `
` or `	`. Always use raw strings `r"..."` or `pathlib.Path`.
- **Assuming Working Directory is Script Directory:** If run from root, relative paths like `"data.csv"` look in root, NOT the subfolder containing the script.

## 4. Practice Tasks
- **Task 1:** Write a diagnostic script that prints `sys.executable`, `sys.version`, `Path.cwd()`, and verifies read/write access to a target directory.

## 5. Self-Check Questions
- **Q1:** How can you determine which Python interpreter is currently executing your script?
- **Q2:** Why should `Path(__file__).resolve().parent` be used to locate sibling assets?
