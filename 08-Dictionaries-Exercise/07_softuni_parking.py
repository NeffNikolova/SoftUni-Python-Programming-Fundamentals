nr_of_cars = int(input())
parking_validations = {}

for visitor in range(nr_of_cars):
    command = input().split()
    if command[0] == 'register':
        if command[1] in parking_validations:
            print(f"ERROR: already registered with plate number {parking_validations[command[1]]}")
        else:
            parking_validations[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
    elif command[0] == 'unregister':
        if command[1] not in parking_validations:
            print(f"ERROR: user {command[1]} not found")
        else:
            parking_validations.pop(command[1])
            print(f"{command[1]} unregistered successfully")

for key, value in parking_validations.items():
    print(f"{key} => {value}")