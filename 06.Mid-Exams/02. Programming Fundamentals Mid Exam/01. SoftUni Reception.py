employee1_efficiency = int(input())
employee2_efficiency = int(input())
employee3_efficiency = int(input())
students_count = int(input())

all_employees_per_hour = employee1_efficiency + employee2_efficiency + \
                         employee3_efficiency
hours_passed = 0
hours_break = 0
iterations = 0
while students_count > 0:
    iterations += 1
    if iterations != 0 and iterations % 4 == 0:
        hours_break += 1
        students_count = students_count
    else:
        students_count -= all_employees_per_hour
        hours_passed += 1

print(f"Time needed: {hours_passed+hours_break}h.")

