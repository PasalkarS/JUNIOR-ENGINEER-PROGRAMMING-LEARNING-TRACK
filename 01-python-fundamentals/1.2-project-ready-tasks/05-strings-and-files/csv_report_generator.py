import csv

data = [
    ["Name", "Age", "Department"],
    ["Sam", 24, "QA"],
    ["John", 25, "Development"],
    ["Alex", 23, "Design"]
]

with open("report.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV report created successfully.")
