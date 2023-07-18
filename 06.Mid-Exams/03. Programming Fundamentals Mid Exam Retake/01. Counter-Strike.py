energy = int(input())
distance = input()

won_battles = 0
no_energy = False

while distance != 'End of battle':
    distance = int(distance)

    if distance <= energy:
        energy -= distance
        won_battles += 1
        if won_battles % 3 == 0:
            energy += won_battles
    else:
        no_energy = True
        break
    distance = input()

if no_energy:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
else:
    print(f"Won battles: {won_battles}. Energy left: {energy}")