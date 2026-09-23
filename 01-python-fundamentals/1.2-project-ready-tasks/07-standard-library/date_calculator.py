# Date Calculator
# Demonstrates datetime and timedelta operations.

from datetime import datetime, timedelta

def calculate_deadline(start_iso: str, business_days: int) -> str:
    """Calculates target completion date adding business days (skipping weekends)."""
    current = datetime.fromisoformat(start_iso)
    added = 0
    while added < business_days:
        current += timedelta(days=1)
        if current.weekday() < 5:  # 0 to 4 are Monday to Friday
            added += 1
    return current.strftime("%Y-%m-%d")

def days_between(date1_iso: str, date2_iso: str) -> int:
    d1 = datetime.fromisoformat(date1_iso)
    d2 = datetime.fromisoformat(date2_iso)
    return abs((d2 - d1).days)

if __name__ == "__main__":
    start = "2026-09-01"
    deadline = calculate_deadline(start, 10)
    print(f"Start date: {start} | +10 business days deadline: {deadline}")
    print(f"Days between 2026-09-01 and 2026-09-25: {days_between('2026-09-01', '2026-09-25')}")
