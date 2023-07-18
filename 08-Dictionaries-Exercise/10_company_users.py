command = input()
users = {}

while command != 'End':
    company_name, employee_id = command.split(' -> ')
    if company_name not in users:
        users[company_name] = []
    if employee_id not in users[company_name]:
        users[company_name].append(employee_id)
    command = input()

for key, value in users.items():
    print(f'{key}')
    for entry in value:
        print(f'-- {entry}')
