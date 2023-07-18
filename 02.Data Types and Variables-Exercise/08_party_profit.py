
group_size = int(input())
days_adventure = int(input())

coins_received = 0

for day in range(1, days_adventure+1):

    if day % 15 == 0:
        group_size += 5

    if day % 10 == 0:
        group_size -= 2

    if day % 5 == 0:
        coins_received += (20 * group_size)
        if day % 3 == 0:
            coins_received -= (2 * group_size)

    if day % 3 == 0:
        coins_received -= (3 * group_size)

    coins_received += 50
    coins_received -= (2 * group_size)

coins_per_companion = coins_received // group_size
print(f'{group_size} companions received {coins_per_companion} coins each.')