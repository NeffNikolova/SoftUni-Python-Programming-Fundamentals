from math import ceil
number_of_people = int(input())
elevator_capacity = int(input())

courses_nr = ceil(number_of_people / elevator_capacity)
print(courses_nr)

