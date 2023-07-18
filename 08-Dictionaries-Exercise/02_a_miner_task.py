command = input()
resources = {}

while command != 'stop':
    current_resource = command
    quantity = int(input())
    if current_resource not in resources.keys():
        resources[current_resource] = 0
    resources[current_resource] += quantity
    command = input()
else:
    for key,value in resources.items():
        print(f'{key} -> {value}')
