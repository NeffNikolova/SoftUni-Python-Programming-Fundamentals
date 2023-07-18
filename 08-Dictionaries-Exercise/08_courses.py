command = input().split(' : ')
courses = {}

while len(command) > 1:
    if command[0] not in courses:
        courses[command[0]] = []
    courses[command[0]].append(command[1])
    command = input().split(' : ')

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for name in value:
        print(f'-- {name}')