information = input().split(':')
students = {}
while len(information) > 1:
    name, id_n, course = information
    id_n = int(id_n)
    if course not in students:
        students[course] = {}
    students[course][id_n] = name
    information = input().split(':')
else:
    key_course = information[0].split('_')
    key_course = ' '.join(key_course)
    for key, value in students[key_course].items():
        print(f"{value} - {key}")