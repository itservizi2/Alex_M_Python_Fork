# files/employee_list.json

import json
from datetime import datetime


def get_salary(employee):
    return employee["salary"]


def sort_by_salary(employee):
    return employee["salary"]


def sort_by_employee_from(employee):
    return datetime.strptime(employee["employee_from"], '%m/%d/%Y')


# scoatem date din fișierul JSON
with open("files/employee_list.json", "r") as f:
    data = json.load(f)

# vedem numele tuturor angajaților
print("Employee Names:")
for employee in data:
    print(employee["name"])

# vedem denumirea jobului
print("\nPosition Names:")
positions = set()
for employee in data:
    positions.add(employee["position"])
for position in positions:
    print(position)

# vedem salariul total lunar
salaries = map(get_salary, data)
total_salary = sum(salaries)
print("\nTotal monthly salary:", total_salary)

# vedem impozitele lunare
tax_percentage = float(input("\nEnter tax percentage: "))
tax_amount = total_salary * (tax_percentage / 100)
print("Monthly taxes:", tax_amount)

#  topul celor mai bine plătiți 10 angajați
print("\nTop 10 highest paid employees:")
sorted_data = sorted(data, key=sort_by_salary, reverse=True)
for i, employee in enumerate(sorted_data[:10], 1):
    print(
        f"{i}. Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, "
        f"Employment Start Date: {employee['employee_from']}")

#  primii 10 angajați cu cel mai lung timp lucrat
print("\nTop 10 employees with longest employment time:")
sorted_data = sorted(data, key=sort_by_employee_from, reverse=True)
for i, employee in enumerate(sorted_data[:10], 1):
    print(
        f"{i}. Name: {employee['name']}, Position: {employee['position']}, Salary: {employee['salary']}, "
        f"Employment Start Date: {employee['employee_from']}")
