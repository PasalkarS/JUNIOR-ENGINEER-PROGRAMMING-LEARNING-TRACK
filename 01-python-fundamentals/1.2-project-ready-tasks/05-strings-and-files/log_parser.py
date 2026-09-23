# Log Parser
# Parses simulated server log entries and extracts HTTP metrics.

import os
from pathlib import Path

SAMPLE_LOG = """2026-09-01 10:00:15 INFO [auth] User alice logged in 200
2026-09-01 10:01:22 ERROR [payment] Charge failed: card declined 402
2026-09-01 10:02:00 INFO [api] GET /items 200
2026-09-01 10:03:10 WARNING [api] Rate limit reached for ip 192.168.1.5 429
2026-09-01 10:04:45 ERROR [database] Connection timeout 500
2026-09-01 10:05:00 INFO [api] GET /orders 200
"""

def parse_logs(log_text: str) -> dict:
    level_counts = {}
    error_lines = []

    for line in log_text.strip().splitlines():
        parts = line.split()
        if len(parts) >= 3:
            level = parts[2]
            level_counts[level] = level_counts.get(level, 0) + 1
            if level == "ERROR":
                error_lines.append(line)

    return {"counts": level_counts, "errors": error_lines}

if __name__ == "__main__":
    result = parse_logs(SAMPLE_LOG)
    print("Log Level Counts:")
    for lvl, count in result["counts"].items():
        print(f" - {lvl}: {count}")

    print(f"\nFound {len(result['errors'])} Error(s):")
    for err in result["errors"]:
        print(f" [!] {err}")
