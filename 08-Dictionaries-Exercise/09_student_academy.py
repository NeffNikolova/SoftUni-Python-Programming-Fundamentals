nr_of_entries = int(input())
students = {}

for entry in range(nr_of_entries):
    name = input()
    current_grade = float(input())

    if name not in students:
        students[name] = current_grade
    else:
        students[name] += current_grade
        students[name] /= 2

filtered_students = {name: grade for (name, grade) in students.items() if grade >= 4.50}

for name, grade in filtered_students.items():
    print(f'{name} -> {grade:.2f}')



