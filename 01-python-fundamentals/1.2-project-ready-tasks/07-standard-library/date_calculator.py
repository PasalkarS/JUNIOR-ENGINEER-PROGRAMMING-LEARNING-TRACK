from datetime import datetime, timedelta

date = input("Enter date (YYYY-MM-DD): ")

date = datetime.strptime(date, "%Y-%m-%d")

days = int(input("Enter number of days: "))

new_date = date + timedelta(days=days)

print("New date:", new_date.strftime("%Y-%m-%d"))
