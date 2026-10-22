## Problem: Given employee records, return the second-highest distinct salary.
## Skills tested: Sets, sorting, edge cases, algorithmic reasoning.

def first_salary(employees):
    salaries = set()
    for employee in employees:
        salary = employee.get("salary")
        if salary is not None:
            salaries.add(salary)

    sorted_salaries = sorted(salaries)
    if len(sorted_salaries) < 2:
        return None

    return sorted_salaries[1]


employees = [
    {"name": "Amit", "salary": 50000},
    {"name": "Neha", "salary": 80000},
    {"name": "Raj", "salary": 80000},
    {"name": "Sara", "salary": 65000},
]

print(first_salary(employees)) # Output: 65000
        