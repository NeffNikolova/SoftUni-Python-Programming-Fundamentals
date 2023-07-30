def cast_spell(database, command):
    action, name, mp_needed, spell = command.split(' - ')
    if int(database[name][1]) >= int(mp_needed):
        database[name][1] = int(database[name][1]) - int(mp_needed)
        print(f"{name} has successfully cast {spell} and now has {database[name][1]} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell}!")
    return database


def take_damage(database, command):
    action, name, damage, attacker = command.split(' - ')
    if int(database[name][0]) > int(damage):
        database[name][0] = int(database[name][0]) - int(damage)
        print(f"{name} was hit for {damage} HP by {attacker} and now has {database[name][0]} HP left!")
    else:
        database[name][0] = int(database[name][0]) - int(damage)
        print(f"{name} has been killed by {attacker}!")
    return database


def recharge(database, command):
    action, name, mp_increase = command.split(' - ')
    if int(database[name][1]) + int(mp_increase) <= 200:
        database[name][1] = int(database[name][1]) + int(mp_increase)
        print(f"{name} recharged for {mp_increase} MP!")
    else:
        mp_increase = 200 - int(database[name][1])
        database[name][1] = 200
        print(f"{name} recharged for {mp_increase} MP!")
    return database


def heal(database, command):
    action, name, hp_increase = command.split(' - ')
    if int(database[name][0]) + int(hp_increase) <= 100:
        database[name][0] = int(database[name][0]) + int(hp_increase)
        print(f"{name} healed for {hp_increase} HP!")
    else:
        hp_increase = 100 - int(database[name][0])
        database[name][0] = 100
        print(f"{name} healed for {hp_increase} HP!")
    return database


available_heroes_spots = int(input())
heroes_in_party = {}

for hero in range(available_heroes_spots):
    hero_name, hero_hp, hero_mp = input().split()
    heroes_in_party[hero_name] = [hero_hp, hero_mp]

current_command = input()

while current_command != 'End':
    if current_command.startswith('CastSpell'):
        heroes_in_party = cast_spell(heroes_in_party, current_command)
    elif current_command.startswith('TakeDamage'):
        heroes_in_party = take_damage(heroes_in_party, current_command)
    elif current_command.startswith('Recharge'):
        heroes_in_party = recharge(heroes_in_party, current_command)
    elif current_command.startswith('Heal'):
        heroes_in_party = heal(heroes_in_party, current_command)
    current_command = input()


for name, stats in heroes_in_party.items():
    if int(heroes_in_party[name][0]) > 0:
        print(f'{name}\n  HP: {heroes_in_party[name][0]}\n  MP: {heroes_in_party[name][1]}')