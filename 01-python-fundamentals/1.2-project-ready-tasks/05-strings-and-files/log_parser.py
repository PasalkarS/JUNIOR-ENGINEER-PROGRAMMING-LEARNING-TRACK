from pathlib import Path

log_file = Path("application.log")

try:
    text = log_file.read_text(encoding="utf-8")

    lines = text.splitlines()

    for line in lines:
        if "ERROR" in line:
            print(line)

except FileNotFoundError:
    print("Log file not found.")

except UnicodeDecodeError:
    print("Unable to read the file because of encoding.")

except Exception:
    print("Something went wrong while reading the file.")
