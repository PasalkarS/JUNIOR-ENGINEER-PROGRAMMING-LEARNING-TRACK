# Python Packaging Concepts & Deployment Artifacts

> **Module 12: Windows Packaging | Topic 01**

## 1. Learning Outcomes
- **The Packaging Problem:** Distribute Python applications to end-users without requiring manual Python installation.
- **Freezers vs Interpreters:** Understand how tools like PyInstaller bundle Python runtimes, C-extensions, and bytecode.
- **Standalone Executables:** Compare single-folder (`--onedir`) vs single-file (`--onefile`) builds.
- **External Dependencies:** Identify binary DLLs and assets that require explicit bundling.

## 2. Packaging Options Comparison

| Option | Architecture | Startup Speed | Best Use Case |
|---|---|---|---|
| `--onedir` (Directory) | Folder with `.exe` + DLLs + assets | Instant (No extraction) | Large desktop apps, complex packages (Pandas, Streamlit) |
| `--onefile` (Single EXE) | Compressed self-extracting archive | Slower (Unpacks to `%TEMP%` on run) | Small CLI utilities, portable tools |

## 3. Common Mistakes & Gotchas
- **Antivirus False Positives:** Heuristic antivirus scanners often flag newly compiled PyInstaller onefile binaries. Code signing mitigates this.
- **Assuming Hardcoded Paths Work:** Once packaged, `__file__` resolves inside temporary runtime directories (`sys._MEIPASS`).

## 4. Practice Tasks
- **Task 1:** Document the dependencies, external assets, and expected writable directories for an internal Python CLI tool.

## 5. Self-Check Questions
- **Q1:** What does PyInstaller bundle inside a frozen Windows executable?
- **Q2:** Why does `--onefile` have a slower startup time than `--onedir`?
