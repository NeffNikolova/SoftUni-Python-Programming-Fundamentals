health = 100
bitcoins = 0
rooms = input().split('|')
room_nr = 0
dead = False

for room in rooms:
    room_nr += 1
    command, value = room.split()
    if command == 'potion':
        if health + int(value) > 100:
            heal = 100 - health
            health = 100
            print(f"You healed for {heal} hp.")
        else:
            health += int(value)
            print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoins += int(value)
        print(f"You found {value} bitcoins.")
    else:
        if health <= int(value):
            print(f"You died! Killed by {command}.\nBest room: {room_nr}")
            dead = True
            break
        else:
            health -= int(value)
            print(f"You slayed {command}.")

if not dead:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")



