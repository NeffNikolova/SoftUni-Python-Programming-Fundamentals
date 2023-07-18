events = input().split('|')

energy = 100
coins = 100
success = True

for event in events:
    event_command, event_value = event.split('-')
    if event_command == 'rest':
        current_energy = energy
        if energy == 100:
            print(f'You gained 0 energy.')
        else:
            energy += int(event_value)
            if energy > 100:
                energy = 100
                print(f'You gained {abs(current_energy-energy)} energy.')
            else:
                print(f'You gained {event_value} energy.')
        print(f'Current energy: {energy}.')
    elif event_command == 'order':
        if energy >= 30:
            energy -= 30
            coins += int(event_value)
            print(f'You earned {event_value} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        if coins >= int(event_value):
            coins -= int(event_value)
            print(f'You bought {event_command}.')
        else:
            success = False
            break

if success:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')
else:
    print(f'Closed! Cannot afford {event_command}.')