def plunder_city(database, current_command):
    action, town, people, money = current_command.split('=>')
    database[town][0] -= int(people)
    database[town][1] -= int(money)
    print(f"{town} plundered! {money} gold stolen, {people} citizens killed.")
    if database[town][0] == 0 or database[town][1] == 0:
        print(f'{town} has been wiped off the map!')
        database.pop(town)
    return database


def prosper_city(database, current_command):
    action, town, money = current_command.split('=>')
    if int(money) < 0:
        print("Gold added cannot be a negative number!")
    else:
        database[town][1] += int(money)
        print(f"{money} gold added to the city treasury. {town} now has {database[town][1]} gold.")
    return database


command = input()
targeted_cities = {}

while command != 'Sail':
    city, population, gold = command.split('||')
    if city not in targeted_cities:
        targeted_cities[city] = [int(population), int(gold)]
    else:
        targeted_cities[city][0] += int(population)
        targeted_cities[city][1] += int(gold)
    command = input()

command = input()
while command != 'End':
    if command.startswith('Plunder'):
        targeted_cities = plunder_city(targeted_cities, command)
    elif command.startswith('Prosper'):
        targeted_cities = prosper_city(targeted_cities, command)
    command = input()

if targeted_cities:
    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")
    for city in targeted_cities:
        print(f'{city} -> Population: {targeted_cities[city][0]} citizens, Gold: {targeted_cities[city][1]} kg')
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
