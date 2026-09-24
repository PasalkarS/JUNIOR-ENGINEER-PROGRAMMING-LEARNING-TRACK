# Building Windows Executables with PyInstaller

> **Module 12: Windows Packaging | Topic 02**

## 1. Learning Outcomes
- **PyInstaller CLI:** Build standalone binaries with `--onefile`, `--windowed`, and `--add-data`.
- **The `.spec` File:** Maintain and customize reproducible build specifications.
- **Hidden Imports:** Explicitly bundle dynamically loaded modules with `--hidden-import`.
- **Resource Path Resolution:** Access bundled icons and data files safely using `sys._MEIPASS`.

## 2. Key Syntax & Concepts

### Resolving Bundled Assets at Runtime
```python
import sys
from pathlib import Path

def get_resource_path(relative_path: str) -> Path:
    """Get absolute path to resource, works for dev and PyInstaller."""
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent
    return base_path / relative_path
```

### Reproducible Build Command
```bash
pyinstaller --noconfirm --onedir --console \
    --name "AssetTracker" \
    --add-data "data/default_config.json;data" \
    --hidden-import "openpyxl" \
    src/main.py
```

## 3. Common Mistakes & Gotchas
- **Windows Semicolon Separator in `--add-data`:** On Windows, `--add-data` requires a semicolon delimiter: `"source_path;destination_folder"`, whereas Linux uses a colon `:`.
- **Missing Hidden Imports:** Packages using dynamic `importlib` (like database drivers) may not be detected by PyInstaller's static analyzer.

## 4. Practice Tasks
- **Task 1:** Build an executable for a simple CLI calculator and verify it runs from command prompt on a clean directory.

## 5. Self-Check Questions
- **Q1:** What special attribute does PyInstaller attach to `sys` to locate extracted runtime files?
- **Q2:** When is the `--windowed` (or `--noconsole`) flag appropriate?
