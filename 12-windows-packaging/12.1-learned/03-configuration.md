# Runtime Paths & External Configuration in Packaged Apps

> **Module 12: Windows Packaging | Topic 03**

## 1. Learning Outcomes
- **Read-Only App Directory:** Understand that `Program Files` or frozen directories are read-only for standard users.
- **Writable User Directories:** Store user data and logs in `%APPDATA%` or `%LOCALAPPDATA%`.
- **Configuration Precedence:** Layer default configs with external user overrides (`config.json`).
- **Path Portability:** Handle relative vs absolute paths reliably across different machines.

## 2. Key Syntax & Concepts

### Finding Standard Writable Paths on Windows
```python
import os
from pathlib import Path

def get_user_data_dir(app_name: str = "AssetTracker") -> Path:
    # Use Windows %LOCALAPPDATA% (typically C:\Users\<user>\AppData\Local)
    appdata = os.environ.get("LOCALAPPDATA")
    if appdata:
        data_dir = Path(appdata) / app_name
    else:
        data_dir = Path.home() / f".{app_name.lower()}"
        
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir

# Usage
db_file = get_user_data_dir() / "records.db"
log_file = get_user_data_dir() / "application.log"
```

## 3. Common Mistakes & Gotchas
- **Writing Files Inside the Frozen Executable Folder:** Attempting to write databases or logs next to `app.exe` in `C:\Program Files` crashes with `PermissionError`.
- **Relying on Hardcoded Drive Letters:** Never assume `C:\` drive exists or is writable. Always query environment variables.

## 4. Practice Tasks
- **Task 1:** Write a config manager that writes a default `settings.json` to `%LOCALAPPDATA%` on first run if missing.

## 5. Self-Check Questions
- **Q1:** Why is writing logs to `C:\Program Files\MyApp\` forbidden on Windows?
- **Q2:** What environment variable points to the local user's AppData directory?
