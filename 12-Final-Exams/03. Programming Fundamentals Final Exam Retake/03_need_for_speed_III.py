def buy_cars(database, command):
    model, mileage, fuel = command.split('|')
    database[model] = [int(mileage), int(fuel)]
    return database


def drive_car(database, command):
    action, vehicle, distance, fuel = command.split(' : ')
    if int(fuel) > int(database[vehicle][1]):
        print("Not enough fuel to make that ride")
        return database
    else:
        if database[vehicle][0] + int(distance) >= 100000:
            database.pop(vehicle)
            print(f'{vehicle} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            print(f"Time to sell the {vehicle}!")
            return database
        else:
            database[vehicle][0] += int(distance)
            database[vehicle][1] -= int(fuel)
            print(f'{vehicle} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            return database


def refuel_car(database, command):
    action, vehicle, fuel = command.split(' : ')
    if int(database[vehicle][1]) + int(fuel) > 75:
        fuel = 75 - int(database[vehicle][1])
        database[vehicle][1] = 75
    else:
        database[vehicle][1] += int(fuel)
    print(f"{vehicle} refueled with {fuel} liters")
    return database


def revert_car(database, command):
    action, vehicle, kilometers = command.split(' : ')
    database[vehicle][0] -= int(kilometers)
    if int(database[vehicle][0]) < 10000:
        database[vehicle][0] = 10000
        return database
    else:
        print(f"{vehicle} mileage decreased by {kilometers} kilometers")
        return database


cars_number = int(input())
car_details = {}

for car in range(cars_number):
    current_car = input()
    car_details = buy_cars(car_details, current_car)

current_command = input()

while current_command != 'Stop':
    if current_command.startswith('Drive'):
        car_details = drive_car(car_details, current_command)
    elif current_command.startswith('Refuel'):
        car_details = refuel_car(car_details, current_command)
    elif current_command.startswith('Revert'):
        car_details = revert_car(car_details, current_command)
    current_command = input()

for car, details in car_details.items():
    print(f'{car} -> Mileage: {details[0]} kms, Fuel in the tank: {details[1]} lt.')
