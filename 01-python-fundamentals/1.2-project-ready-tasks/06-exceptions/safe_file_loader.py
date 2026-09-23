# Safe File Loader
# Demonstrates try / except / else / finally when loading files.

from pathlib import Path

def safe_read_lines(file_path: str) -> list[str]:
    p = Path(file_path)
    try:
        print(f"Attempting to read: {p}")
        with open(p, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[WARN]: File '{file_path}' does not exist. Returning empty list.")
        return []
    except PermissionError:
        print(f"[ERROR]: Insufficient permissions to read '{file_path}'.")
        return []
    else:
        print(f"[SUCCESS]: Successfully loaded {len(lines)} non-empty lines.")
        return lines
    finally:
        print("[CLEANUP]: File operation block concluded.")

if __name__ == "__main__":
    # Test non-existent file handling
    result = safe_read_lines("non_existent_file_test.txt")
    print("Result:", result)
