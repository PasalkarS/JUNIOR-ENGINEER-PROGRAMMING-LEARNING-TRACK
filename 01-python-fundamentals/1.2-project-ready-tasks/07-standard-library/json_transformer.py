import json
from pathlib import Path

file = Path("data.json")

try:
    data = json.loads(file.read_text(encoding="utf-8"))

    for item in data:
        item["name"] = item["name"].upper()

    file.write_text(
        json.dumps(data, indent=4),
        encoding="utf-8"
    )

    print("JSON file updated successfully.")

except FileNotFoundError:
    print("JSON file not found.")

except json.JSONDecodeError:
    print("Invalid JSON file.")
