# Employee Directory
# Demonstrates list of dicts, filtering, and set operations.

employees = [
    {"id": "E101", "name": "Sarah Connor", "dept": "Engineering", "salary": 85000},
    {"id": "E102", "name": "John Doe", "dept": "Marketing", "salary": 62000},
    {"id": "E103", "name": "Alice Wong", "dept": "Engineering", "salary": 92000},
    {"id": "E104", "name": "Bob Taylor", "dept": "Finance", "salary": 74000},
    {"id": "E105", "name": "Carlos Gomez", "dept": "Marketing", "salary": 58000},
]

# 1. Unique departments using a set comprehension
departments = {emp["dept"] for emp in employees}
print("Unique Departments:", sorted(departments))

# 2. Filter engineering employees
engineers = [emp["name"] for emp in employees if emp["dept"] == "Engineering"]
print("Engineering Team:", engineers)

# 3. Average salary calculation
total_salary = sum(emp["salary"] for emp in employees)
avg_salary = total_salary / len(employees)
print(f"Average Salary across company: ${avg_salary:,.2f}")
