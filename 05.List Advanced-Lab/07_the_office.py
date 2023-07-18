employee_happiness = input().split()
happiness_improvement_factor = int(input())

employee_happiness = [int(num) for num in employee_happiness]
employee_happiness = list(map(lambda x: x * happiness_improvement_factor, employee_happiness))
average_happiness = sum(employee_happiness) / len(employee_happiness)
happy_employees = [num for num in employee_happiness if int(num) >= average_happiness]

if len(happy_employees) < len(employee_happiness)/2:
    print(f"Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are not happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are happy!")