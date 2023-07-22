def rate_plant(database_rating, command):
    current_plant, rating = (command.split(': ')[1]).split(' - ')
    # if current_plant in database_rarity:
    #
    if current_plant not in database_rating:
        database_rating[current_plant] = []
    database_rating[current_plant].append(float(rating))
    return database_rating


def update_plant(database_rarity, command):
    current_plant, new_rarity = (command.split(': ')[1]).split(' - ')
    # if current_plant in database_rarity:
    #
    database_rarity[current_plant] = new_rarity
    return database_rarity


def reset_plant(database_rating, command):
    action, current_plant = command.split(': ')
    # if current_plant in database_rarity and current_plant in database_rating:
    # if current_plant not in database_rarity:
    database_rating[current_plant].clear()
    return database_rating


number_of_plants = int(input())
discovered_plants_rarity = {}
discovered_plants_rating = {}

for discovery in range(number_of_plants):
    plant, rarity = input().split('<->')
    discovered_plants_rarity[plant] = rarity

current_command = input()
error = False

while current_command != 'Exhibition':
    if 'Rate' in current_command:
        plant, current_rating = (current_command.split(': ')[1]).split(' - ')
        if plant in discovered_plants_rarity:
            discovered_plants_rating = rate_plant(discovered_plants_rating, current_command)
        else:
            error = True
    elif 'Update' in current_command:
        plant = (current_command.split(': ')[1]).split(' - ')[0]
        if plant in discovered_plants_rarity:
            discovered_plants_rarity = update_plant(discovered_plants_rarity, current_command)
        else:
            error = True
    elif 'Reset' in current_command:
        plant = current_command.split(': ')[1]
        if plant in discovered_plants_rarity and plant in discovered_plants_rating:
            discovered_plants_rating = reset_plant(discovered_plants_rating, current_command)
        else:
            error = True

    if error:
        print('error')
        error = False

    current_command = input()

print('Plants for the exhibition:')
for plant, rarity in discovered_plants_rarity.items():
    if plant not in discovered_plants_rating.keys():
        avg_score = 0
    elif len(discovered_plants_rating[plant]) == 0:
        avg_score = 0
    else:
        avg_score = sum(discovered_plants_rating[plant])/len(discovered_plants_rating[plant])
    print(f'- {plant}; Rarity: {rarity}; Rating: {avg_score:.2f}')
