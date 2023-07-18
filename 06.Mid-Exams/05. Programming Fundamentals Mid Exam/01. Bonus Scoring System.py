students_nr = int(input())
lectures_nr = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendance = 0

for student in range(students_nr):
    student_attendance = int(input())

    current_bonus = student_attendance/lectures_nr * (5 + additional_bonus)

    if current_bonus > max_bonus:
        max_bonus = current_bonus
        max_attendance = student_attendance

print(f"Max Bonus: {max_bonus:.0f}.\nThe student has attended {max_attendance} lectures.")